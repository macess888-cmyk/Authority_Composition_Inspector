from authority_composition_experiment.inspection import inspect_authority_delta
from authority_composition_experiment.models import (
    AuthorityDeltaState,
    AuthorityGrantEvidence,
    CompositionAuthorityFinding,
    CompositionFinding,
    EvidenceState,
    MaterialDeltaFinding,
)


def test_matching_grant_id_with_wrong_composition_id_holds() -> None:
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

    authority = CompositionAuthorityFinding(
        composition_id="COMP-A-001",
        state=EvidenceState.PASS,
        grant_ids=("GRANT-A-001",),
    )

    grants = (
        AuthorityGrantEvidence(
            grant_id="GRANT-A-001",
            issuer="synthetic_competent_authority",
            covered_capability_ids=("READ_RECORD", "WRITE_SUMMARY"),
            covered_composition_ids=("COMP-WRONG",),
            covered_resulting_capabilities=(
                "DERIVE_AND_PERSIST_SUMMARY",
            ),
        ),
    )

    result = inspect_authority_delta(
        composition=composition,
        material_delta=material_delta,
        composition_authority=authority,
        grants=grants,
    )

    assert result.state is AuthorityDeltaState.HOLD


def test_matching_composition_id_with_wrong_resulting_capability_holds() -> None:
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

    authority = CompositionAuthorityFinding(
        composition_id="COMP-A-001",
        state=EvidenceState.PASS,
        grant_ids=("GRANT-A-001",),
    )

    grants = (
        AuthorityGrantEvidence(
            grant_id="GRANT-A-001",
            issuer="synthetic_competent_authority",
            covered_capability_ids=("READ_RECORD", "WRITE_SUMMARY"),
            covered_composition_ids=("COMP-A-001",),
            covered_resulting_capabilities=("SOME_OTHER_CAPABILITY",),
        ),
    )

    result = inspect_authority_delta(
        composition=composition,
        material_delta=material_delta,
        composition_authority=authority,
        grants=grants,
    )

    assert result.state is AuthorityDeltaState.HOLD


def test_material_delta_pass_with_empty_dimensions_holds() -> None:
    composition = CompositionFinding(
        composition_id="COMP-B-001",
        state=EvidenceState.PASS,
        resulting_capability_id="CLASSIFY_AND_ISSUE_NOTICE",
    )

    material_delta = MaterialDeltaFinding(
        composition_id="COMP-B-001",
        state=EvidenceState.PASS,
        dimensions=(),
    )

    authority = CompositionAuthorityFinding(
        composition_id="COMP-B-001",
        state=EvidenceState.HOLD,
        grant_ids=(),
    )

    result = inspect_authority_delta(
        composition=composition,
        material_delta=material_delta,
        composition_authority=authority,
        grants=(),
    )

    assert result.state is AuthorityDeltaState.HOLD


def test_authority_evidence_present_without_composition_coverage_holds() -> None:
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

    authority = CompositionAuthorityFinding(
        composition_id="COMP-A-001",
        state=EvidenceState.PASS,
        grant_ids=("GRANT-A-001",),
    )

    grants = (
        AuthorityGrantEvidence(
            grant_id="GRANT-A-001",
            issuer="synthetic_competent_authority",
            covered_capability_ids=("READ_RECORD", "WRITE_SUMMARY"),
            covered_composition_ids=(),
            covered_resulting_capabilities=(),
        ),
    )

    result = inspect_authority_delta(
        composition=composition,
        material_delta=material_delta,
        composition_authority=authority,
        grants=grants,
    )

    assert result.state is AuthorityDeltaState.HOLD


def test_composition_authority_pass_with_missing_referenced_grant_holds() -> None:
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

    authority = CompositionAuthorityFinding(
        composition_id="COMP-A-001",
        state=EvidenceState.PASS,
        grant_ids=("GRANT-MISSING",),
    )

    result = inspect_authority_delta(
        composition=composition,
        material_delta=material_delta,
        composition_authority=authority,
        grants=(),
    )

    assert result.state is AuthorityDeltaState.HOLD
