# Legacy Experimental Contracts

These files preserve the pre-v0.1 Authority Composition Experiment test
contracts.

They are retained as experimental lineage and are intentionally not collected
as active pytest contracts.

The experimental inspector used:

- `CompositionAuthorityFinding`
- `AuthorityGrantEvidence`
- grant coverage
- `AuthorityDeltaState.UNEXPLAINED`
- `explanation_grant_ids`

The frozen Authority Composition Inspector v0.1 architecture supersedes those
inspector semantics.

The v0.1 inspector requires independently supplied:

- `AuthorityBasisFinding`
- `AuthorityCompetenceFinding`
- `AuthorityScopeFinding`

The frozen terminal dispositions are:

- `EXPLAINED`
- `NO_MATERIAL_DELTA`
- `HOLD`

`UNEXPLAINED` is not a terminal disposition in v0.1.
`UNEXPLAINED_AUTHORITY_DELTA` is an epistemic diagnostic beneath `HOLD`.

These legacy files MUST NOT be treated as normative v0.1 behavior.

Their preservation records the experimental path that preceded the frozen
architecture.
