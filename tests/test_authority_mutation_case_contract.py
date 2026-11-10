import json
from pathlib import Path

CASES = (
    Path(__file__).parent.parent
    / "specimens"
    / "authority_mutation"
)

EXPECTED = {
    "AM-00_CONTROL.json": "NO_MUTATION",
    "AM-01_AUTHORIZED_POLICY_CHANGE.json": "TRACEABLE",
    "AM-02_UNAUTHORIZED_PERMISSION_EXPANSION.json": (
        "MUTATION_AUTHORITY_MISSING"
    ),
    "AM-03_STALE_DELEGATION.json": "MUTATION_AUTHORITY_STALE",
    "AM-04_AUTHORITY_TO_CHANGE_AUTHORITY_FAILURE.json": (
        "UNEXPLAINED_AUTHORITY_DELTA"
    ),
}


def load_case(filename: str) -> dict:
    return json.loads(
        (CASES / filename).read_text(encoding="utf-8")
    )


def test_all_authority_mutation_cases_are_present() -> None:
    present = {path.name for path in CASES.glob("AM-*.json")}
    assert present == set(EXPECTED)


def test_case_ids_match_filenames() -> None:
    for filename in EXPECTED:
        data = load_case(filename)
        assert filename.startswith(data["case_id"])


def test_expected_standings_are_explicit() -> None:
    for filename, expected in EXPECTED.items():
        data = load_case(filename)
        assert data["expected_standing"] == expected


def test_control_has_no_mutation() -> None:
    data = load_case("AM-00_CONTROL.json")

    assert data["mutation"]["present"] is False
    assert (
        data["prior_authority_state"]
        == data["resulting_authority_state"]
    )


def test_authorized_change_has_current_basis() -> None:
    data = load_case(
        "AM-01_AUTHORIZED_POLICY_CHANGE.json"
    )

    assert data["mutation"]["present"] is True
    assert data["mutation"]["basis_status"] == "CURRENT"
    assert data["mutation"]["basis_id"]


def test_missing_basis_case_has_no_basis() -> None:
    data = load_case(
        "AM-02_UNAUTHORIZED_PERMISSION_EXPANSION.json"
    )

    assert data["mutation"]["basis_id"] is None


def test_stale_delegation_is_explicitly_stale() -> None:
    data = load_case("AM-03_STALE_DELEGATION.json")

    assert data["mutation"]["basis_status"] == "STALE"


def test_operational_scope_does_not_cover_mutation_target() -> None:
    data = load_case(
        "AM-04_AUTHORITY_TO_CHANGE_AUTHORITY_FAILURE.json"
    )

    mutation_scope = set(
        data["mutation"]["requested_scope_change"]
    )
    basis_scope = set(data["mutation"]["basis_scope"])

    assert not mutation_scope.issubset(basis_scope)