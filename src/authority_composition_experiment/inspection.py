from __future__ import annotations

from .models import (
    AuthorityBasisFinding,
    AuthorityCompetenceFinding,
    AuthorityDeltaDiagnostic,
    AuthorityDeltaFinding,
    AuthorityDeltaState,
    AuthorityScopeFinding,
    CompositionFinding,
    EvidenceState,
    MaterialDeltaFinding,
)


def inspect_authority_delta(
    *,
    composition: CompositionFinding,
    material_delta: MaterialDeltaFinding,
    authority_basis: AuthorityBasisFinding,
    authority_competence: AuthorityCompetenceFinding,
    authority_scope: AuthorityScopeFinding,
) -> AuthorityDeltaFinding:
    """Inspect whether verified authority findings explain composed material reach."""

    if material_delta.composition_id != composition.composition_id:
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.HOLD,
            diagnostics=(),
            explanation_authority_basis_ids=(),
        )

    if authority_basis.composition_id != composition.composition_id:
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.HOLD,
            diagnostics=(),
            explanation_authority_basis_ids=(),
        )

    if authority_scope.composition_id != composition.composition_id:
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.HOLD,
            diagnostics=(),
            explanation_authority_basis_ids=(),
        )

    if (
        authority_basis.resulting_capability_id
        != composition.resulting_capability_id
    ):
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.HOLD,
            diagnostics=(),
            explanation_authority_basis_ids=(),
        )

    if (
        authority_scope.resulting_capability_id
        != composition.resulting_capability_id
    ):
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.HOLD,
            diagnostics=(),
            explanation_authority_basis_ids=(),
        )

    if (
        authority_basis.authority_basis_id
        != authority_competence.authority_basis_id
        or authority_basis.authority_basis_id
        != authority_scope.authority_basis_id
    ):
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.HOLD,
            diagnostics=(),
            explanation_authority_basis_ids=(),
        )

    if composition.state is not EvidenceState.PASS:
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.HOLD,
            diagnostics=(),
            explanation_authority_basis_ids=(),
        )

    if material_delta.state is EvidenceState.NOT_ESTABLISHED:
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.NO_MATERIAL_DELTA,
            diagnostics=(),
            explanation_authority_basis_ids=(),
        )

    if material_delta.state is not EvidenceState.PASS:
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.HOLD,
            diagnostics=(),
            explanation_authority_basis_ids=(),
        )

    if not material_delta.dimensions:
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.HOLD,
            diagnostics=(),
            explanation_authority_basis_ids=(),
        )

    if authority_basis.state is not EvidenceState.PASS:
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.HOLD,
            diagnostics=(
                AuthorityDeltaDiagnostic.UNEXPLAINED_AUTHORITY_DELTA,
            ),
            explanation_authority_basis_ids=(),
        )

    if authority_competence.state is not EvidenceState.PASS:
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.HOLD,
            diagnostics=(
                AuthorityDeltaDiagnostic.UNEXPLAINED_AUTHORITY_DELTA,
            ),
            explanation_authority_basis_ids=(),
        )

    if authority_scope.state is not EvidenceState.PASS:
        return AuthorityDeltaFinding(
            composition_id=composition.composition_id,
            state=AuthorityDeltaState.HOLD,
            diagnostics=(
                AuthorityDeltaDiagnostic.UNEXPLAINED_AUTHORITY_DELTA,
            ),
            explanation_authority_basis_ids=(),
        )

    return AuthorityDeltaFinding(
        composition_id=composition.composition_id,
        state=AuthorityDeltaState.EXPLAINED,
        diagnostics=(),
        explanation_authority_basis_ids=(
            authority_basis.authority_basis_id,
        ),
    )
