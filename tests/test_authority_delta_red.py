from authority_composition_experiment.inspection import (
    inspect_authority_delta,
)
from authority_composition_experiment.models import (
    AuthorityDeltaState,
    AuthorityGrantEvidence,
    CompositionAuthorityFinding,
    CompositionFinding,
    EvidenceState,
    MaterialDeltaFinding,
)


def test_explicit_composition_coverage_explains_material_delta() -> None:
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

    assert result.state is AuthorityDeltaState.EXPLAINED
    assert result.explanation_grant_ids == ("GRANT-A-001",)


def test_material_delta_without_established_composition_authority_holds() -> None:
    composition = CompositionFinding(
        composition_id="COMP-B-001",
        state=EvidenceState.PASS,
        resulting_capability_id="CLASSIFY_AND_ISSUE_NOTICE",
    )

    material_delta = MaterialDeltaFinding(
        composition_id="COMP-B-001",
        state=EvidenceState.PASS,
        dimensions=(
            "new derived classification",
            "new consequential notice based on classification",
        ),
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

    assert result.state is AuthorityDeltaState.UNEXPLAINED
    assert result.explanation_grant_ids == ()


def test_technical_composition_without_material_delta_does_not_trigger_authority_delta() -> None:
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

    authority = CompositionAuthorityFinding(
        composition_id="COMP-C-001",
        state=EvidenceState.PASS,
        grant_ids=("GRANT-C-001",),
    )

    result = inspect_authority_delta(
        composition=composition,
        material_delta=material_delta,
        composition_authority=authority,
        grants=(),
    )

    assert result.state is AuthorityDeltaState.NO_MATERIAL_DELTA
    assert result.explanation_grant_ids == ()


def test_component_success_cannot_silently_create_composition_authority() -> None:
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

    assert authority.state is EvidenceState.HOLD
    assert result.state is AuthorityDeltaState.UNEXPLAINED


def test_missing_composition_evidence_cannot_produce_explained_authority_delta() -> None:
    composition = CompositionFinding(
        composition_id="COMP-UNKNOWN",
        state=EvidenceState.HOLD,
        resulting_capability_id="UNKNOWN",
    )

    material_delta = MaterialDeltaFinding(
        composition_id="COMP-UNKNOWN",
        state=EvidenceState.HOLD,
        dimensions=(),
    )

    authority = CompositionAuthorityFinding(
        composition_id="COMP-UNKNOWN",
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


def test_mismatched_material_delta_composition_id_holds() -> None:
    composition = CompositionFinding(
        composition_id="COMP-A-001",
        state=EvidenceState.PASS,
        resulting_capability_id="DERIVE_AND_PERSIST_SUMMARY",
    )

    material_delta = MaterialDeltaFinding(
        composition_id="COMP-B-001",
        state=EvidenceState.PASS,
        dimensions=("derived consequential write",),
    )

    authority = CompositionAuthorityFinding(
        composition_id="COMP-A-001",
        state=EvidenceState.PASS,
        grant_ids=("GRANT-A-001",),
    )

    result = inspect_authority_delta(
        composition=composition,
        material_delta=material_delta,
        composition_authority=authority,
        grants=(),
    )

    assert result.state is AuthorityDeltaState.HOLD


def test_mismatched_composition_authority_id_holds() -> None:
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
        composition_id="COMP-B-001",
        state=EvidenceState.PASS,
        grant_ids=("GRANT-A-001",),
    )

    result = inspect_authority_delta(
        composition=composition,
        material_delta=material_delta,
        composition_authority=authority,
        grants=(),
    )

    assert result.state is AuthorityDeltaState.HOLD
