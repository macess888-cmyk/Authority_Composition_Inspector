from dataclasses import FrozenInstanceError

import pytest

from authority_composition_experiment.models import (
    AuthorityDeltaFinding,
    AuthorityDeltaState,
    AuthorityGrantEvidence,
    CapabilityFinding,
    CapabilityIdentity,
    ComponentAuthorityFinding,
    CompositionAuthorityFinding,
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


def test_authority_grant_keeps_component_and_composition_coverage_separate() -> None:
    grant = AuthorityGrantEvidence(
        grant_id="GRANT-001",
        issuer="synthetic_competent_authority",
        covered_capability_ids=("READ_RECORD", "WRITE_SUMMARY"),
        covered_composition_ids=("COMP-A-001",),
        covered_resulting_capabilities=("DERIVE_AND_PERSIST_SUMMARY",),
    )

    assert grant.covered_capability_ids == ("READ_RECORD", "WRITE_SUMMARY")
    assert grant.covered_composition_ids == ("COMP-A-001",)
    assert grant.covered_resulting_capabilities == (
        "DERIVE_AND_PERSIST_SUMMARY",
    )


def test_component_authority_finding_does_not_contain_composition_authority() -> None:
    finding = ComponentAuthorityFinding(
        capability_id="READ_RECORD",
        state=EvidenceState.PASS,
        grant_ids=("GRANT-READ",),
    )

    assert not hasattr(finding, "composition_authority")


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


def test_composition_finding_and_authority_finding_are_distinct() -> None:
    composition = CompositionFinding(
        composition_id="COMP-B-001",
        state=EvidenceState.PASS,
        resulting_capability_id="CLASSIFY_AND_ISSUE_NOTICE",
    )

    authority = CompositionAuthorityFinding(
        composition_id="COMP-B-001",
        state=EvidenceState.HOLD,
        grant_ids=(),
    )

    assert composition.state is EvidenceState.PASS
    assert authority.state is EvidenceState.HOLD


def test_material_delta_can_pass_while_composition_authority_holds() -> None:
    delta = MaterialDeltaFinding(
        composition_id="COMP-B-001",
        state=EvidenceState.PASS,
        dimensions=("new consequential notice",),
    )

    authority = CompositionAuthorityFinding(
        composition_id="COMP-B-001",
        state=EvidenceState.HOLD,
        grant_ids=(),
    )

    assert delta.state is EvidenceState.PASS
    assert authority.state is EvidenceState.HOLD


def test_unexplained_authority_delta_does_not_mean_unauthorized() -> None:
    finding = AuthorityDeltaFinding(
        composition_id="COMP-B-001",
        state=AuthorityDeltaState.UNEXPLAINED,
        explanation_grant_ids=(),
    )

    assert finding.state is AuthorityDeltaState.UNEXPLAINED
    assert not hasattr(finding, "unauthorized")
    assert not hasattr(finding, "illegal")
    assert not hasattr(finding, "unsafe")


def test_no_material_delta_is_distinct_from_explained_delta() -> None:
    no_delta = AuthorityDeltaFinding(
        composition_id="COMP-C-001",
        state=AuthorityDeltaState.NO_MATERIAL_DELTA,
        explanation_grant_ids=(),
    )

    explained = AuthorityDeltaFinding(
        composition_id="COMP-A-001",
        state=AuthorityDeltaState.EXPLAINED,
        explanation_grant_ids=("GRANT-A-001",),
    )

    assert no_delta.state is AuthorityDeltaState.NO_MATERIAL_DELTA
    assert explained.state is AuthorityDeltaState.EXPLAINED


def test_capability_pass_does_not_promote_component_authority() -> None:
    capability = CapabilityFinding(
        capability_id="READ_RECORD",
        state=EvidenceState.PASS,
    )

    authority = ComponentAuthorityFinding(
        capability_id="READ_RECORD",
        state=EvidenceState.HOLD,
        grant_ids=(),
    )

    assert capability.state is EvidenceState.PASS
    assert authority.state is EvidenceState.HOLD
