# Authority Composition Inspector v0.1.0 — Release Notes

Status:
RELEASE CANDIDATE

Architecture:
FROZEN

Implementation:
CONFORMANT

UNKNOWN -> HOLD

## Purpose

Authority Composition Inspector v0.1.0 inspects whether materially expanded
composed capability is supported by independently established and correctly
bound authority findings.

It does not create authority.

It does not authorize execution.

## Frozen Principle

Capability may compose.

Authority does not arise merely because capability composed.

Authority standing for materially expanded composed reach must be independently
traceable to an authority basis whose competence and scope are established for
that reach.

## Terminal Dispositions

EXPLAINED

NO_MATERIAL_DELTA

HOLD

UNEXPLAINED is not a terminal disposition.

Diagnostic beneath HOLD:

UNEXPLAINED_AUTHORITY_DELTA

## Independent Authority Findings

v0.1 keeps separate:

AuthorityBasisFinding

AuthorityCompetenceFinding

AuthorityScopeFinding

Authority Basis != Authority Competence

Authority Basis != Authority Scope

Authority Competence != Authority Scope

## Cross-Binding

EXPLAINED requires consistent binding across:

- composition;
- material delta;
- authority basis;
- authority competence;
- authority scope;
- resulting capability.

Misbinding results in HOLD.

## Core Reductions

Capability != Authority

Component Authority != Composition Authority

Executable != Authorized

Technical Composition != Material Delta

Material Delta != Authority Delta

Authority Evidence != Authority Standing

Authority Basis != Authority Competence

Authority Basis != Authority Scope

Missing Authority Evidence != Proven Authority Absence

UNEXPLAINED_AUTHORITY_DELTA != UNAUTHORIZED

## Synthetic Specimens

The release includes bounded synthetic control specimens.

Synthetic specimen binding is test infrastructure only.

It is not real-world authority verification.

## Legacy Lineage

Pre-v0.1 experimental contracts and models are preserved under:

tests/legacy/

They are non-normative and excluded from active pytest collection.

## Explicit Non-Claims

v0.1.0 does not establish:

- jurisdiction;
- legality;
- safety;
- legitimacy;
- delegation;
- revocation;
- execution rights;
- execution control;
- policy compliance;
- authority scoring;
- universal authority semantics.

## Validation Baseline

Active pytest suite:

35 passed

Ruff:

PASS

Mypy:

PASS across 4 source files

git diff --check:

PASS

## Release Standing

Architecture:
FROZEN

Implementation:
CONFORMANT

Release:
PENDING FINAL VALIDATION AND TAG

UNKNOWN -> HOLD outside the frozen inspected surface.
