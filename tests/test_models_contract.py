from dataclasses import FrozenInstanceError

import pytest

from authority_composition_experiment.models import (
    AuthorityBasisFinding,
    AuthorityCompetenceFinding,
    AuthorityDeltaDiagnostic,
    AuthorityDeltaFinding,
    AuthorityDeltaState,
    AuthorityScopeFinding,
    CapabilityFinding,
    CapabilityIdentity,
    CompositionEvidence,
    CompositionFinding,
    EvidenceState,
    MaterialDeltaEvidence,
    MaterialDeltaFinding,
)


def test_capability_identity_is_immutable() -> None:
    capability = CapabilityIdentity(
        capability_id="READ_RECORD",
        action="read",
        resource="record_alpha",
    )

    with pytest.raises(FrozenInstanceError):
        capability.action = "write"  # type: ignore[misc]


def test_composition_evidence_does_not_assert_authority() -> None:
    composition = CompositionEvidence(
        composition_id="COMP-B-001",
        component_capability_ids=("READ_RECORD", "WRITE_NOTICE"),
        resulting_capability_id="CLASSIFY_AND_ISSUE_NOTICE",
    )

    assert not hasattr(composition, "authority")
    assert not hasattr(composition, "authorized")


def test_material_delta_evidence_does_not_assert_authority() -> None:
    delta = MaterialDeltaEvidence(
        present=True,
        dimensions=("new consequential notice",),
    )

    assert delta.present is True
    assert not hasattr(delta, "authority")
    assert not hasattr(delta, "authorized")


def test_composition_and_authority_basis_findings_are_distinct() -> None:
    composition = CompositionFinding(
        composition_id="COMP-B-001",
        state=EvidenceState.PASS,
        resulting_capability_id="CLASSIFY_AND_ISSUE_NOTICE",
    )

    basis = AuthorityBasisFinding(
        authority_basis_id="BASIS-B-001",
        composition_id="COMP-B-001",
        resulting_capability_id="CLASSIFY_AND_ISSUE_NOTICE",
        state=EvidenceState.HOLD,
    )

    assert composition.state is EvidenceState.PASS
    assert basis.state is EvidenceState.HOLD


def test_material_delta_can_pass_while_authority_basis_holds() -> None:
    delta = MaterialDeltaFinding(
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

    assert delta.state is EvidenceState.PASS
    assert basis.state is EvidenceState.HOLD


def test_authority_basis_does_not_contain_competence_or_scope() -> None:
    basis = AuthorityBasisFinding(
        authority_basis_id="BASIS-A-001",
        composition_id="COMP-A-001",
        resulting_capability_id="DERIVE_AND_PERSIST_SUMMARY",
        state=EvidenceState.PASS,
    )

    assert not hasattr(basis, "competence")
    assert not hasattr(basis, "scope")


def test_authority_competence_and_scope_are_distinct() -> None:
    competence = AuthorityCompetenceFinding(
        authority_basis_id="BASIS-A-001",
        state=EvidenceState.PASS,
    )

    scope = AuthorityScopeFinding(
        authority_basis_id="BASIS-A-001",
        composition_id="COMP-A-001",
        resulting_capability_id="DERIVE_AND_PERSIST_SUMMARY",
        state=EvidenceState.HOLD,
    )

    assert competence.state is EvidenceState.PASS
    assert scope.state is EvidenceState.HOLD


def test_unexplained_authority_delta_diagnostic_does_not_mean_unauthorized() -> None:
    finding = AuthorityDeltaFinding(
        composition_id="COMP-B-001",
        state=AuthorityDeltaState.HOLD,
        diagnostics=(
            AuthorityDeltaDiagnostic.UNEXPLAINED_AUTHORITY_DELTA,
        ),
        explanation_authority_basis_ids=(),
    )

    assert finding.state is AuthorityDeltaState.HOLD
    assert finding.diagnostics == (
        AuthorityDeltaDiagnostic.UNEXPLAINED_AUTHORITY_DELTA,
    )
    assert not hasattr(finding, "unauthorized")
    assert not hasattr(finding, "illegal")
    assert not hasattr(finding, "unsafe")


def test_no_material_delta_is_distinct_from_explained_delta() -> None:
    no_delta = AuthorityDeltaFinding(
        composition_id="COMP-C-001",
        state=AuthorityDeltaState.NO_MATERIAL_DELTA,
        diagnostics=(),
        explanation_authority_basis_ids=(),
    )

    explained = AuthorityDeltaFinding(
        composition_id="COMP-A-001",
        state=AuthorityDeltaState.EXPLAINED,
        diagnostics=(),
        explanation_authority_basis_ids=("BASIS-A-001",),
    )

    assert no_delta.state is AuthorityDeltaState.NO_MATERIAL_DELTA
    assert explained.state is AuthorityDeltaState.EXPLAINED


def test_capability_pass_does_not_promote_authority_basis() -> None:
    capability = CapabilityFinding(
        capability_id="READ_RECORD",
        state=EvidenceState.PASS,
    )

    basis = AuthorityBasisFinding(
        authority_basis_id="BASIS-READ",
        composition_id="COMP-READ",
        resulting_capability_id="READ_RECORD",
        state=EvidenceState.HOLD,
    )

    assert capability.state is EvidenceState.PASS
    assert basis.state is EvidenceState.HOLD
