from authority_composition_experiment.models import (
    AuthorityBasisFinding,
    AuthorityCompetenceFinding,
    AuthorityDeltaDiagnostic,
    AuthorityDeltaFinding,
    AuthorityDeltaState,
    AuthorityScopeFinding,
    EvidenceState,
)


def test_authority_delta_terminal_states_are_frozen_v0_1_set() -> None:
    assert set(AuthorityDeltaState) == {
        AuthorityDeltaState.EXPLAINED,
        AuthorityDeltaState.NO_MATERIAL_DELTA,
        AuthorityDeltaState.HOLD,
    }


def test_unexplained_is_not_a_terminal_authority_delta_state() -> None:
    assert not hasattr(AuthorityDeltaState, "UNEXPLAINED")


def test_unexplained_authority_delta_exists_as_diagnostic() -> None:
    assert (
        AuthorityDeltaDiagnostic.UNEXPLAINED_AUTHORITY_DELTA.value
        == "UNEXPLAINED_AUTHORITY_DELTA"
    )


def test_authority_basis_finding_is_independent() -> None:
    finding = AuthorityBasisFinding(
        authority_basis_id="BASIS-001",
        composition_id="COMP-A-001",
        resulting_capability_id="DERIVE_AND_PERSIST_SUMMARY",
        state=EvidenceState.PASS,
    )

    assert finding.state is EvidenceState.PASS
    assert not hasattr(finding, "competence")
    assert not hasattr(finding, "scope")


def test_authority_competence_finding_is_independent() -> None:
    finding = AuthorityCompetenceFinding(
        authority_basis_id="BASIS-001",
        state=EvidenceState.PASS,
    )

    assert finding.state is EvidenceState.PASS
    assert not hasattr(finding, "scope")


def test_authority_scope_finding_is_independent() -> None:
    finding = AuthorityScopeFinding(
        authority_basis_id="BASIS-001",
        composition_id="COMP-A-001",
        resulting_capability_id="DERIVE_AND_PERSIST_SUMMARY",
        state=EvidenceState.PASS,
    )

    assert finding.state is EvidenceState.PASS
    assert not hasattr(finding, "competence")


def test_hold_can_carry_unexplained_authority_delta_diagnostic() -> None:
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


def test_explained_finding_has_no_unexplained_diagnostic() -> None:
    finding = AuthorityDeltaFinding(
        composition_id="COMP-A-001",
        state=AuthorityDeltaState.EXPLAINED,
        diagnostics=(),
        explanation_authority_basis_ids=("BASIS-001",),
    )

    assert finding.diagnostics == ()
