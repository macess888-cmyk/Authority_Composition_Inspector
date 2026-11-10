from dataclasses import dataclass
from enum import Enum
from typing import Mapping, Sequence


class AuthorityMutationState(str, Enum):
    NO_MUTATION = "NO_MUTATION"
    TRACEABLE = "TRACEABLE"
    HOLD = "HOLD"


class AuthorityMutationDiagnostic(str, Enum):
    MUTATION_AUTHORITY_MISSING = "MUTATION_AUTHORITY_MISSING"
    MUTATION_AUTHORITY_STALE = "MUTATION_AUTHORITY_STALE"
    UNEXPLAINED_AUTHORITY_DELTA = "UNEXPLAINED_AUTHORITY_DELTA"


@dataclass(frozen=True)
class AuthorityMutationFinding:
    state: AuthorityMutationState
    diagnostics: tuple[AuthorityMutationDiagnostic, ...]


def _scope(values: object) -> set[str]:
    if not isinstance(values, Sequence) or isinstance(
        values,
        (str, bytes),
    ):
        return set()

    return {
        value
        for value in values
        if isinstance(value, str)
    }


def inspect_authority_mutation(
    *,
    prior_authority_state: Mapping[str, object],
    mutation: Mapping[str, object],
    resulting_authority_state: Mapping[str, object],
) -> AuthorityMutationFinding:
    mutation_present = mutation.get("present") is True

    if not mutation_present:
        if prior_authority_state == resulting_authority_state:
            return AuthorityMutationFinding(
                state=AuthorityMutationState.NO_MUTATION,
                diagnostics=(),
            )

        return AuthorityMutationFinding(
            state=AuthorityMutationState.HOLD,
            diagnostics=(
                AuthorityMutationDiagnostic.UNEXPLAINED_AUTHORITY_DELTA,
            ),
        )

    basis_id = mutation.get("basis_id")

    if not isinstance(basis_id, str) or not basis_id.strip():
        return AuthorityMutationFinding(
            state=AuthorityMutationState.HOLD,
            diagnostics=(
                AuthorityMutationDiagnostic.MUTATION_AUTHORITY_MISSING,
            ),
        )

    basis_status = mutation.get("basis_status")

    if basis_status == "STALE":
        return AuthorityMutationFinding(
            state=AuthorityMutationState.HOLD,
            diagnostics=(
                AuthorityMutationDiagnostic.MUTATION_AUTHORITY_STALE,
            ),
        )

    if basis_status != "CURRENT":
        return AuthorityMutationFinding(
            state=AuthorityMutationState.HOLD,
            diagnostics=(
                AuthorityMutationDiagnostic.UNEXPLAINED_AUTHORITY_DELTA,
            ),
        )

    requested_scope = _scope(
        mutation.get("requested_scope_change")
    )
    basis_scope = _scope(
        mutation.get("basis_scope")
    )

    if not requested_scope.issubset(basis_scope):
        return AuthorityMutationFinding(
            state=AuthorityMutationState.HOLD,
            diagnostics=(
                AuthorityMutationDiagnostic.UNEXPLAINED_AUTHORITY_DELTA,
            ),
        )

    return AuthorityMutationFinding(
        state=AuthorityMutationState.TRACEABLE,
        diagnostics=(),
    )