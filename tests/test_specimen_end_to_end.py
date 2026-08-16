import json
from pathlib import Path

from authority_composition_experiment.inspection import inspect_authority_delta
from authority_composition_experiment.models import AuthorityDeltaState
from authority_composition_experiment.specimen_binding import bind_specimen

SPECIMENS = Path(__file__).parent.parent / "specimens"


def inspect_specimen(filename: str) -> AuthorityDeltaState:
    bound = bind_specimen(SPECIMENS / filename)

    result = inspect_authority_delta(
        composition=bound.composition,
        material_delta=bound.material_delta,
        composition_authority=bound.composition_authority,
        grants=bound.grants,
    )

    return result.state


def test_specimen_a_is_explained() -> None:
    assert (
        inspect_specimen("specimen_a_explicit_coverage.json")
        is AuthorityDeltaState.EXPLAINED
    )


def test_specimen_b_is_unexplained() -> None:
    assert (
        inspect_specimen("specimen_b_unexplained_delta.json")
        is AuthorityDeltaState.UNEXPLAINED
    )


def test_specimen_c_has_no_material_delta() -> None:
    assert (
        inspect_specimen("specimen_c_no_material_delta.json")
        is AuthorityDeltaState.NO_MATERIAL_DELTA
    )


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
        composition_authority=bound.composition_authority,
        grants=bound.grants,
    )

    assert result.state is AuthorityDeltaState.UNEXPLAINED


def test_binding_does_not_expose_control_expectation() -> None:
    bound = bind_specimen(
        SPECIMENS / "specimen_a_explicit_coverage.json"
    )

    assert not hasattr(bound, "control_expectation")
    assert not hasattr(bound, "expected_result")
