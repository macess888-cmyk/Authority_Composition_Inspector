import json
from pathlib import Path

import pytest

from authority_composition_experiment.authority_mutation import (
    AuthorityMutationDiagnostic,
    AuthorityMutationState,
    inspect_authority_mutation,
)

CASES = (
    Path(__file__).parent.parent
    / "specimens"
    / "authority_mutation"
)


def load_case(filename: str) -> dict:
    return json.loads(
        (CASES / filename).read_text(encoding="utf-8")
    )


def inspect_case(filename: str):
    data = load_case(filename)

    return inspect_authority_mutation(
        prior_authority_state=data["prior_authority_state"],
        mutation=data["mutation"],
        resulting_authority_state=data["resulting_authority_state"],
    )


def test_control_returns_no_mutation() -> None:
    result = inspect_case("AM-00_CONTROL.json")

    assert result.state is AuthorityMutationState.NO_MUTATION
    assert result.diagnostics == ()


def test_authorized_policy_change_is_traceable() -> None:
    result = inspect_case(
        "AM-01_AUTHORIZED_POLICY_CHANGE.json"
    )

    assert result.state is AuthorityMutationState.TRACEABLE
    assert result.diagnostics == ()


def test_missing_mutation_basis_holds() -> None:
    result = inspect_case(
        "AM-02_UNAUTHORIZED_PERMISSION_EXPANSION.json"
    )

    assert result.state is AuthorityMutationState.HOLD
    assert result.diagnostics == (
        AuthorityMutationDiagnostic.MUTATION_AUTHORITY_MISSING,
    )


def test_stale_mutation_basis_holds() -> None:
    result = inspect_case("AM-03_STALE_DELEGATION.json")

    assert result.state is AuthorityMutationState.HOLD
    assert result.diagnostics == (
        AuthorityMutationDiagnostic.MUTATION_AUTHORITY_STALE,
    )


def test_operational_authority_does_not_explain_policy_mutation() -> None:
    result = inspect_case(
        "AM-04_AUTHORITY_TO_CHANGE_AUTHORITY_FAILURE.json"
    )

    assert result.state is AuthorityMutationState.HOLD
    assert result.diagnostics == (
        AuthorityMutationDiagnostic.UNEXPLAINED_AUTHORITY_DELTA,
    )


def test_result_does_not_claim_illegality_or_real_world_authority() -> None:
    result = inspect_case(
        "AM-02_UNAUTHORIZED_PERMISSION_EXPANSION.json"
    )

    assert not hasattr(result, "illegal")
    assert not hasattr(result, "authorized_execution")
    assert not hasattr(result, "legal_authority")


def test_expected_standing_is_not_inspection_input(
    tmp_path: Path,
) -> None:
    source = CASES / "AM-02_UNAUTHORIZED_PERMISSION_EXPANSION.json"
    data = json.loads(source.read_text(encoding="utf-8"))

    data["expected_standing"] = "TRACEABLE"

    tampered = tmp_path / "tampered.json"
    tampered.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8",
    )

    loaded = json.loads(tampered.read_text(encoding="utf-8"))

    result = inspect_authority_mutation(
        prior_authority_state=loaded["prior_authority_state"],
        mutation=loaded["mutation"],
        resulting_authority_state=loaded["resulting_authority_state"],
    )

    assert result.state is AuthorityMutationState.HOLD
    assert result.diagnostics == (
        AuthorityMutationDiagnostic.MUTATION_AUTHORITY_MISSING,
    )


@pytest.mark.parametrize(
    ("filename", "expected_state"),
    [
        (
            "AM-00_CONTROL.json",
            AuthorityMutationState.NO_MUTATION,
        ),
        (
            "AM-01_AUTHORIZED_POLICY_CHANGE.json",
            AuthorityMutationState.TRACEABLE,
        ),
        (
            "AM-02_UNAUTHORIZED_PERMISSION_EXPANSION.json",
            AuthorityMutationState.HOLD,
        ),
        (
            "AM-03_STALE_DELEGATION.json",
            AuthorityMutationState.HOLD,
        ),
        (
            "AM-04_AUTHORITY_TO_CHANGE_AUTHORITY_FAILURE.json",
            AuthorityMutationState.HOLD,
        ),
    ],
)
def test_case_state_matrix(
    filename: str,
    expected_state: AuthorityMutationState,
) -> None:
    result = inspect_case(filename)

    assert result.state is expected_state