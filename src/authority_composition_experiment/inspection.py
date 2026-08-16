from __future__ import annotations

from .models import (
    AuthorityDeltaFinding,
    AuthorityDeltaState,
    AuthorityGrantEvidence,
    CompositionAuthorityFinding,
    CompositionFinding,
    EvidenceState,
    MaterialDeltaFinding,
)


def inspect_authority_delta(
    *,
    composition: CompositionFinding,
    material_delta: MaterialDeltaFinding,
    composition_authority: CompositionAuthorityFinding,
    grants: tuple[AuthorityGrantEvidence, ...],
) -> AuthorityDeltaFinding:
    """Inspect whether a material composed reach has explained authority standing."""

    if composition.state is not EvidenceState.PASS:
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.HOLD,
            explanation_grant_ids=(),
        )

    if material_delta.state is EvidenceState.NOT_ESTABLISHED:
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.NO_MATERIAL_DELTA,
            explanation_grant_ids=(),
        )

    if material_delta.state is not EvidenceState.PASS:
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.HOLD,
            explanation_grant_ids=(),
        )

    if composition_authority.state is not EvidenceState.PASS:
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.UNEXPLAINED,
            explanation_grant_ids=(),
        )

    matching_grant_ids = tuple(
        grant.grant_id
        for grant in grants
        if grant.grant_id in composition_authority.grant_ids
        and composition.composition_id in grant.covered_composition_ids
        and composition.resulting_capability_id
        in grant.covered_resulting_capabilities
    )

    if not matching_grant_ids:
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.HOLD,
            explanation_grant_ids=(),
        )

    return AuthorityDeltaFinding(
        composition_id=composition.composition_id,
        state=AuthorityDeltaState.EXPLAINED,
        explanation_grant_ids=matching_grant_ids,
    )
