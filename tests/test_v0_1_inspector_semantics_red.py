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


def test_explained_requires_independent_basis_competence_and_scope() -> None:
    composition = CompositionFinding(
        composition_id="COMP-A-001",
        state=EvidenceState.PASS,
        resulting_capability_id="DERIVE_AND_PERSIST_SUMMARY",
    )

    material_delta = MaterialDeltaFinding(
        composition_id="COMP-A-001",
        state=EvidenceState.PASS,
        dimensions=("derived consequential write",),
    )

    basis = AuthorityBasisFinding(
        authority_basis_id="BASIS-001",
        composition_id="COMP-A-001",
        resulting_capability_id="DERIVE_AND_PERSIST_SUMMARY",
        state=EvidenceState.PASS,
    )

    competence = AuthorityCompetenceFinding(
        authority_basis_id="BASIS-001",
        state=EvidenceState.PASS,
    )

    scope = AuthorityScopeFinding(
        authority_basis_id="BASIS-001",
        composition_id="COMP-A-001",
        resulting_capability_id="DERIVE_AND_PERSIST_SUMMARY",
        state=EvidenceState.PASS,
    )

    result = inspect_authority_delta(
        composition=composition,
        material_delta=material_delta,
        authority_basis=basis,
        authority_competence=competence,
        authority_scope=scope,
    )

    assert result.state is AuthorityDeltaState.EXPLAINED
    assert result.diagnostics == ()
    assert result.explanation_authority_basis_ids == ("BASIS-001",)


def test_missing_authority_basis_holds_with_unexplained_diagnostic() -> None:
    composition = CompositionFinding(
        composition_id="COMP-B-001",
        state=EvidenceState.PASS,
        resulting_capability_id="CLASSIFY_AND_ISSUE_NOTICE",
    )

    material_delta = MaterialDeltaFinding(
        composition_id="COMP-B-001",
        state=EvidenceState.PASS,
        dimensions=("new consequential notice",),
    )

    basis = AuthorityBasisFinding(
        authority_basis_id="BASIS-B-001",
        composition_id="COMP-B-001",
        resulting_capability_id="CLASSIFY_AND_ISSUE_NOTICE",
        state=EvidenceState.HOLD,
    )

    competence = AuthorityCompetenceFinding(
        authority_basis_id="BASIS-B-001",
        state=EvidenceState.PASS,
    )

    scope = AuthorityScopeFinding(
        authority_basis_id="BASIS-B-001",
        composition_id="COMP-B-001",
        resulting_capability_id="CLASSIFY_AND_ISSUE_NOTICE",
        state=EvidenceState.PASS,
    )

    result = inspect_authority_delta(
        composition=composition,
        material_delta=material_delta,
        authority_basis=basis,
        authority_competence=competence,
        authority_scope=scope,
    )

    assert result.state is AuthorityDeltaState.HOLD
    assert result.diagnostics == (
        AuthorityDeltaDiagnostic.UNEXPLAINED_AUTHORITY_DELTA,
    )


def test_missing_competence_holds() -> None:
    composition = CompositionFinding(
        composition_id="COMP-A-001",
        state=EvidenceState.PASS,
        resulting_capability_id="DERIVE_AND_PERSIST_SUMMARY",
    )

    material_delta = MaterialDeltaFinding(
        composition_id="COMP-A-001",
        state=EvidenceState.PASS,
        dimensions=("derived consequential write",),
    )

    basis = AuthorityBasisFinding(
        authority_basis_id="BASIS-001",
        composition_id="COMP-A-001",
        resulting_capability_id="DERIVE_AND_PERSIST_SUMMARY",
        state=EvidenceState.PASS,
    )

    competence = AuthorityCompetenceFinding(
        authority_basis_id="BASIS-001",
        state=EvidenceState.HOLD,
    )

    scope = AuthorityScopeFinding(
        authority_basis_id="BASIS-001",
        composition_id="COMP-A-001",
        resulting_capability_id="DERIVE_AND_PERSIST_SUMMARY",
        state=EvidenceState.PASS,
    )

    result = inspect_authority_delta(
        composition=composition,
        material_delta=material_delta,
        authority_basis=basis,
        authority_competence=competence,
        authority_scope=scope,
    )

    assert result.state is AuthorityDeltaState.HOLD


def test_missing_scope_holds() -> None:
    composition = CompositionFinding(
        composition_id="COMP-A-001",
        state=EvidenceState.PASS,
        resulting_capability_id="DERIVE_AND_PERSIST_SUMMARY",
    )

    material_delta = MaterialDeltaFinding(
        composition_id="COMP-A-001",
        state=EvidenceState.PASS,
        dimensions=("derived consequential write",),
    )

    basis = AuthorityBasisFinding(
        authority_basis_id="BASIS-001",
        composition_id="COMP-A-001",
        resulting_capability_id="DERIVE_AND_PERSIST_SUMMARY",
        state=EvidenceState.PASS,
    )

    competence = AuthorityCompetenceFinding(
        authority_basis_id="BASIS-001",
        state=EvidenceState.PASS,
    )

    scope = AuthorityScopeFinding(
        authority_basis_id="BASIS-001",
        composition_id="COMP-A-001",
        resulting_capability_id="DERIVE_AND_PERSIST_SUMMARY",
        state=EvidenceState.HOLD,
    )

    result = inspect_authority_delta(
        composition=composition,
        material_delta=material_delta,
        authority_basis=basis,
        authority_competence=competence,
        authority_scope=scope,
    )

    assert result.state is AuthorityDeltaState.HOLD


def test_no_material_delta_does_not_require_authority_explanation() -> None:
    composition = CompositionFinding(
        composition_id="COMP-C-001",
        state=EvidenceState.PASS,
        resulting_capability_id="READ_AND_FORMAT_RECORD",
    )

    material_delta = MaterialDeltaFinding(
        composition_id="COMP-C-001",
        state=EvidenceState.NOT_ESTABLISHED,
        dimensions=(),
    )

    basis = AuthorityBasisFinding(
        authority_basis_id="BASIS-C-001",
        composition_id="COMP-C-001",
        resulting_capability_id="READ_AND_FORMAT_RECORD",
        state=EvidenceState.HOLD,
    )

    competence = AuthorityCompetenceFinding(
        authority_basis_id="BASIS-C-001",
        state=EvidenceState.HOLD,
    )

    scope = AuthorityScopeFinding(
        authority_basis_id="BASIS-C-001",
        composition_id="COMP-C-001",
        resulting_capability_id="READ_AND_FORMAT_RECORD",
        state=EvidenceState.HOLD,
    )

    result = inspect_authority_delta(
        composition=composition,
        material_delta=material_delta,
        authority_basis=basis,
        authority_competence=competence,
        authority_scope=scope,
    )

    assert result.state is AuthorityDeltaState.NO_MATERIAL_DELTA
    assert result.diagnostics == ()
