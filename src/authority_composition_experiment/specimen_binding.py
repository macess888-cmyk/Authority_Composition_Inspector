from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .models import (
    AuthorityGrantEvidence,
    CompositionAuthorityFinding,
    CompositionFinding,
    EvidenceState,
    MaterialDeltaFinding,
)


@dataclass(frozen=True)
class BoundSpecimen:
    specimen_id: str
    composition: CompositionFinding
    material_delta: MaterialDeltaFinding
    composition_authority: CompositionAuthorityFinding
    grants: tuple[AuthorityGrantEvidence, ...]


def _load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict):
        raise TypeError("specimen root must be a JSON object")

    return data


def _grant_from_mapping(data: dict[str, Any]) -> AuthorityGrantEvidence:
    covers = tuple(str(value) for value in data.get("covers", ()))

    return AuthorityGrantEvidence(
        grant_id=str(data["grant_id"]),
        issuer=str(data["issuer"]),
        covered_capability_ids=covers,
        covered_composition_ids=(),
        covered_resulting_capabilities=(),
    )


def bind_specimen(path: Path) -> BoundSpecimen:
    data = _load_json(path)

    specimen_id = str(data["specimen_id"])
    composition_data = data["composition"]
    delta_data = data["candidate_material_delta"]

    composition_id = str(composition_data["composition_id"])
    resulting_capability = str(composition_data["resulting_capability"])

    composition = CompositionFinding(
        composition_id=composition_id,
        state=EvidenceState.PASS,
        resulting_capability_id=resulting_capability,
    )

    delta_present = bool(delta_data["present"])
    dimensions_raw = delta_data.get("dimensions")
    dimensions: tuple[str, ...]

    if dimensions_raw is None:
        dimension = delta_data.get("dimension")
        dimensions = () if dimension is None else (str(dimension),)
    else:
        dimensions = tuple(str(value) for value in dimensions_raw)

    material_delta = MaterialDeltaFinding(
        composition_id=composition_id,
        state=(
            EvidenceState.PASS
            if delta_present
            else EvidenceState.NOT_ESTABLISHED
        ),
        dimensions=dimensions,
    )

    authority_raw = data["authority_evidence"]

    grants: tuple[AuthorityGrantEvidence, ...]

    if isinstance(authority_raw, list):
        grants = tuple(
            _grant_from_mapping(grant)
            for grant in authority_raw
        )
    else:
        grant = _grant_from_mapping(authority_raw)

        explicit_composition_coverage = (
            composition_id
            if any("->" in item for item in grant.covered_capability_ids)
            else None
        )

        grants = (
            AuthorityGrantEvidence(
                grant_id=grant.grant_id,
                issuer=grant.issuer,
                covered_capability_ids=grant.covered_capability_ids,
                covered_composition_ids=(
                    ()
                    if explicit_composition_coverage is None
                    else (composition_id,)
                ),
                covered_resulting_capabilities=(
                    ()
                    if explicit_composition_coverage is None
                    else (resulting_capability,)
                ),
            ),
        )

    matching_grant_ids: tuple[str, ...] = tuple(
        grant.grant_id
        for grant in grants
        if composition_id in grant.covered_composition_ids
        and resulting_capability in grant.covered_resulting_capabilities
    )

    composition_authority = CompositionAuthorityFinding(
        composition_id=composition_id,
        state=(
            EvidenceState.PASS
            if matching_grant_ids
            else EvidenceState.HOLD
        ),
        grant_ids=matching_grant_ids,
    )

    return BoundSpecimen(
        specimen_id=specimen_id,
        composition=composition,
        material_delta=material_delta,
        composition_authority=composition_authority,
        grants=grants,
    )


