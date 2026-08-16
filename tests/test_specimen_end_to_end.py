import json
from pathlib import Path

from authority_composition_experiment.inspection import inspect_authority_delta
from authority_composition_experiment.models import (
    AuthorityDeltaDiagnostic,
    AuthorityDeltaState,
)
from authority_composition_experiment.specimen_binding import bind_specimen

SPECIMENS = Path(__file__).parent.parent / "specimens"


def inspect_specimen(filename: str):
    bound = bind_specimen(SPECIMENS / filename)

    return inspect_authority_delta(
        composition=bound.composition,
        material_delta=bound.material_delta,
        authority_basis=bound.authority_basis,
        authority_competence=bound.authority_competence,
        authority_scope=bound.authority_scope,
    )


def test_specimen_a_is_explained() -> None:
    result = inspect_specimen("specimen_a_explicit_coverage.json")

    assert result.state is AuthorityDeltaState.EXPLAINED
    assert result.diagnostics == ()


def test_specimen_b_holds_with_unexplained_authority_delta() -> None:
    result = inspect_specimen("specimen_b_unexplained_delta.json")

    assert result.state is AuthorityDeltaState.HOLD
    assert result.diagnostics == (
        AuthorityDeltaDiagnostic.UNEXPLAINED_AUTHORITY_DELTA,
    )


def test_specimen_c_has_no_material_delta() -> None:
    result = inspect_specimen("specimen_c_no_material_delta.json")

    assert result.state is AuthorityDeltaState.NO_MATERIAL_DELTA
    assert result.diagnostics == ()


def test_control_expectation_is_not_used_as_inspection_input(
    tmp_path: Path,
) -> None:
    source = SPECIMENS / "specimen_b_unexplained_delta.json"

    data = json.loads(source.read_text(encoding="utf-8"))

    data["control_expectation"] = {
        "composition_authority": "PASS",
        "authority_delta": "EXPLAINED",
    }

    tampered = tmp_path / "tampered_specimen.json"
    tampered.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8",
    )

    bound = bind_specimen(tampered)

    result = inspect_authority_delta(
        composition=bound.composition,
        material_delta=bound.material_delta,
        authority_basis=bound.authority_basis,
        authority_competence=bound.authority_competence,
        authority_scope=bound.authority_scope,
    )

    assert result.state is AuthorityDeltaState.HOLD
    assert result.diagnostics == (
        AuthorityDeltaDiagnostic.UNEXPLAINED_AUTHORITY_DELTA,
    )


def test_binding_does_not_expose_control_expectation() -> None:
    bound = bind_specimen(
        SPECIMENS / "specimen_a_explicit_coverage.json"
    )

    assert not hasattr(bound, "control_expectation")
    assert not hasattr(bound, "expected_result")


def test_synthetic_binding_does_not_expose_real_world_authority_claims() -> None:
    bound = bind_specimen(
        SPECIMENS / "specimen_a_explicit_coverage.json"
    )

    assert not hasattr(bound, "legal")
    assert not hasattr(bound, "jurisdiction")
    assert not hasattr(bound, "authorized_execution")
