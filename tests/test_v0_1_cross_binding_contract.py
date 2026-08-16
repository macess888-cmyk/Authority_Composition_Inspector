from authority_composition_experiment.inspection import inspect_authority_delta
from authority_composition_experiment.models import (
    AuthorityBasisFinding,
    AuthorityCompetenceFinding,
    AuthorityDeltaDiagnostic,
    AuthorityDeltaState,
    AuthorityScopeFinding,
    CompositionFinding,
    EvidenceState,
    MaterialDeltaFinding,
)


def _composition() -> CompositionFinding:
    return CompositionFinding(
        composition_id="COMP-A-001",
        state=EvidenceState.PASS,
        resulting_capability_id="CAP-A",
    )


def _delta() -> MaterialDeltaFinding:
    return MaterialDeltaFinding(
        composition_id="COMP-A-001",
        state=EvidenceState.PASS,
        dimensions=("new consequence",),
    )


def test_competence_bound_to_different_authority_basis_holds() -> None:
    result = inspect_authority_delta(
        composition=_composition(),
        material_delta=_delta(),
        authority_basis=AuthorityBasisFinding(
            authority_basis_id="BASIS-001",
            composition_id="COMP-A-001",
            resulting_capability_id="CAP-A",
            state=EvidenceState.PASS,
        ),
        authority_competence=AuthorityCompetenceFinding(
            authority_basis_id="BASIS-002",
            state=EvidenceState.PASS,
        ),
        authority_scope=AuthorityScopeFinding(
            authority_basis_id="BASIS-001",
            composition_id="COMP-A-001",
            resulting_capability_id="CAP-A",
            state=EvidenceState.PASS,
        ),
    )

    assert result.state is AuthorityDeltaState.HOLD
    assert result.explanation_authority_basis_ids == ()


def test_scope_bound_to_different_composition_holds() -> None:
    result = inspect_authority_delta(
        composition=_composition(),
        material_delta=_delta(),
        authority_basis=AuthorityBasisFinding(
            authority_basis_id="BASIS-001",
            composition_id="COMP-A-001",
            resulting_capability_id="CAP-A",
            state=EvidenceState.PASS,
        ),
        authority_competence=AuthorityCompetenceFinding(
            authority_basis_id="BASIS-001",
            state=EvidenceState.PASS,
        ),
        authority_scope=AuthorityScopeFinding(
            authority_basis_id="BASIS-001",
            composition_id="COMP-B-001",
            resulting_capability_id="CAP-A",
            state=EvidenceState.PASS,
        ),
    )

    assert result.state is AuthorityDeltaState.HOLD


def test_scope_bound_to_different_resulting_capability_holds() -> None:
    result = inspect_authority_delta(
        composition=_composition(),
        material_delta=_delta(),
        authority_basis=AuthorityBasisFinding(
            authority_basis_id="BASIS-001",
            composition_id="COMP-A-001",
            resulting_capability_id="CAP-A",
            state=EvidenceState.PASS,
        ),
        authority_competence=AuthorityCompetenceFinding(
            authority_basis_id="BASIS-001",
            state=EvidenceState.PASS,
        ),
        authority_scope=AuthorityScopeFinding(
            authority_basis_id="BASIS-001",
            composition_id="COMP-A-001",
            resulting_capability_id="CAP-B",
            state=EvidenceState.PASS,
        ),
    )

    assert result.state is AuthorityDeltaState.HOLD


def test_basis_bound_to_different_resulting_capability_holds() -> None:
    result = inspect_authority_delta(
        composition=_composition(),
        material_delta=_delta(),
        authority_basis=AuthorityBasisFinding(
            authority_basis_id="BASIS-001",
            composition_id="COMP-A-001",
            resulting_capability_id="CAP-B",
            state=EvidenceState.PASS,
        ),
        authority_competence=AuthorityCompetenceFinding(
            authority_basis_id="BASIS-001",
            state=EvidenceState.PASS,
        ),
        authority_scope=AuthorityScopeFinding(
            authority_basis_id="BASIS-001",
            composition_id="COMP-A-001",
            resulting_capability_id="CAP-A",
            state=EvidenceState.PASS,
        ),
    )

    assert result.state is AuthorityDeltaState.HOLD


def test_fully_bound_authority_findings_explain() -> None:
    result = inspect_authority_delta(
        composition=_composition(),
        material_delta=_delta(),
        authority_basis=AuthorityBasisFinding(
            authority_basis_id="BASIS-001",
            composition_id="COMP-A-001",
            resulting_capability_id="CAP-A",
            state=EvidenceState.PASS,
        ),
        authority_competence=AuthorityCompetenceFinding(
            authority_basis_id="BASIS-001",
            state=EvidenceState.PASS,
        ),
        authority_scope=AuthorityScopeFinding(
            authority_basis_id="BASIS-001",
            composition_id="COMP-A-001",
            resulting_capability_id="CAP-A",
            state=EvidenceState.PASS,
        ),
    )

    assert result.state is AuthorityDeltaState.EXPLAINED
    assert result.diagnostics == ()
    assert result.explanation_authority_basis_ids == ("BASIS-001",)


def test_missing_authority_standing_uses_unexplained_diagnostic_only_under_hold() -> None:
    result = inspect_authority_delta(
        composition=_composition(),
        material_delta=_delta(),
        authority_basis=AuthorityBasisFinding(
            authority_basis_id="BASIS-001",
            composition_id="COMP-A-001",
            resulting_capability_id="CAP-A",
            state=EvidenceState.HOLD,
        ),
        authority_competence=AuthorityCompetenceFinding(
            authority_basis_id="BASIS-001",
            state=EvidenceState.PASS,
        ),
        authority_scope=AuthorityScopeFinding(
            authority_basis_id="BASIS-001",
            composition_id="COMP-A-001",
            resulting_capability_id="CAP-A",
            state=EvidenceState.PASS,
        ),
    )

    assert result.state is AuthorityDeltaState.HOLD
    assert result.diagnostics == (
        AuthorityDeltaDiagnostic.UNEXPLAINED_AUTHORITY_DELTA,
    )
