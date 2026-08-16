from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .models import (
    AuthorityBasisFinding,
    AuthorityCompetenceFinding,
    AuthorityScopeFinding,
    CompositionFinding,
    EvidenceState,
    MaterialDeltaFinding,
)


@dataclass(frozen=True)
class BoundSpecimen:
    specimen_id: str
    composition: CompositionFinding
    material_delta: MaterialDeltaFinding
    authority_basis: AuthorityBasisFinding
    authority_competence: AuthorityCompetenceFinding
    authority_scope: AuthorityScopeFinding


def _load_json(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as handle:
        data = json.load(handle)

    if not isinstance(data, dict):
        raise TypeError("specimen root must be a JSON object")

    return data


def bind_specimen(path: Path) -> BoundSpecimen:
    """
    Form synthetic v0.1 findings from a bounded control specimen.

    This adapter is test infrastructure only.

    Synthetic finding formation is not real-world authority verification.
    """
    data = _load_json(path)

    specimen_id = str(data["specimen_id"])
    composition_data = data["composition"]
    delta_data = data["candidate_material_delta"]

    composition_id = str(composition_data["composition_id"])
    resulting_capability_id = str(
        composition_data["resulting_capability"]
    )

    composition = CompositionFinding(
        composition_id=composition_id,
        state=EvidenceState.PASS,
        resulting_capability_id=resulting_capability_id,
    )

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
            if bool(delta_data["present"])
            else EvidenceState.NOT_ESTABLISHED
        ),
        dimensions=dimensions,
    )

    authority_raw = data["authority_evidence"]

    basis_id = f"SYNTHETIC-BASIS-{specimen_id}"

    composition_covered = False
    resulting_capability_covered = False

    def _apply_synthetic_coverage(
        covers: tuple[str, ...],
    ) -> tuple[bool, bool]:
        explicit_composition_coverage = any(
            composition_id in value or "->" in value
            for value in covers
        )

        explicit_resulting_coverage = (
            resulting_capability_id in covers
            or explicit_composition_coverage
        )

        return (
            explicit_composition_coverage,
            explicit_resulting_coverage,
        )

    if isinstance(authority_raw, list):
        for grant in authority_raw:
            covers = tuple(
                str(value)
                for value in grant.get("covers", ())
            )

            (
                grant_composition_covered,
                grant_resulting_covered,
            ) = _apply_synthetic_coverage(covers)

            composition_covered = (
                composition_covered
                or grant_composition_covered
            )

            resulting_capability_covered = (
                resulting_capability_covered
                or grant_resulting_covered
            )
    else:
        covers = tuple(
            str(value)
            for value in authority_raw.get("covers", ())
        )

        (
            composition_covered,
            resulting_capability_covered,
        ) = _apply_synthetic_coverage(covers)

    authority_explained = (
        composition_covered
        and resulting_capability_covered
    )

    authority_basis = AuthorityBasisFinding(
        authority_basis_id=basis_id,
        composition_id=composition_id,
        resulting_capability_id=resulting_capability_id,
        state=(
            EvidenceState.PASS
            if authority_explained
            else EvidenceState.HOLD
        ),
    )

    authority_competence = AuthorityCompetenceFinding(
        authority_basis_id=basis_id,
        state=(
            EvidenceState.PASS
            if authority_explained
            else EvidenceState.HOLD
        ),
    )

    authority_scope = AuthorityScopeFinding(
        authority_basis_id=basis_id,
        composition_id=composition_id,
        resulting_capability_id=resulting_capability_id,
        state=(
            EvidenceState.PASS
            if authority_explained
            else EvidenceState.HOLD
        ),
    )

    return BoundSpecimen(
        specimen_id=specimen_id,
        composition=composition,
        material_delta=material_delta,
        authority_basis=authority_basis,
        authority_competence=authority_competence,
        authority_scope=authority_scope,
    )
