# CHECKPOINT 001 — FALSIFICATION CONTRACT

Status: EXPERIMENTAL

Architecture: NOT FROZEN
Implementation: NONE
Promotion: NONE

UNKNOWN -> HOLD

## 1. Research Question

When individually authorized capabilities compose into a capability with new reach, what competent authority, if any, explains the authority standing of that composed reach?

The experiment does not assume that composition:

- creates authority;
- destroys authority;
- always requires a new grant;
- is unauthorized when no grant has yet been found.

The experiment asks only whether authority for the composed reach is independently traceable.

---

## 2. Candidate Failure Class

UNEXPLAINED AUTHORITY DELTA

Definition:

A materially expanded capability is observed after composition, but competent authority covering that expanded reach has not been established.

This finding is epistemic.

It does not independently mean:

UNAUTHORIZED
ILLEGAL
INVALID
UNSAFE
PROHIBITED

The bounded result is:

AUTHORITY FOR MATERIAL DELTA -> HOLD

---

## 3. Properties Kept Independent

The experiment MUST NOT collapse:

Capability Existence

Component Capability Authority

Composition Existence

Material Reach

Material Consequence

Authority Coverage

Authority Source

Authority Competence

Authority Scope

Authority Delta Explanation

Execution Availability

Execution Permission

Execution Legitimacy

A PASS in one property does not silently promote another.

---

## 4. Independent Authorities

### Capability Verifier

Question:

What capability actually exists?

May establish:

- Capability A exists.
- Capability B exists.
- Composed capability exists.
- Observable reach of the composition.

May NOT establish:

- permission;
- authority;
- legitimacy;
- safety.

---

### Authority Verifier

Question:

What authority was actually granted?

May establish:

- grant identity;
- grant source;
- grant scope;
- grant subject;
- grant object;
- grant temporal standing;
- explicit composition coverage where present.

May NOT infer authority merely from executable capability.

---

### Composition Verifier

Question:

What changes when A and B compose?

May establish:

- whether composition occurs;
- whether the composition creates new reach;
- whether persistence changes;
- whether scope changes;
- whether binding force changes;
- whether consequence changes.

May NOT decide whether that new reach is authorized.

---

### Authority Delta Inspector

Question:

Does competent authority independently explain any material increase introduced by composition?

Inputs:

- verified capability findings;
- verified composition findings;
- verified authority evidence.

May return:

EXPLAINED
NO_MATERIAL_DELTA
HOLD

It MUST NOT create authority.

---

## 5. Material Delta

A composition has a candidate material delta when it introduces at least one property not already established for the relevant component grants.

Candidate dimensions:

- new target;
- new recipient;
- new resource;
- new scope;
- new persistence;
- new binding force;
- new consequence;
- new execution pathway;
- new ability to affect an external state.

Technical composition alone is insufficient.

A -> B existing in sequence does not automatically mean a material authority delta exists.

---

## 6. Specimen A — Explicit Coverage

Given:

Capability A is authorized.

Capability B is authorized.

A competent grant explicitly covers the defined A -> B composition and resulting reach.

Expected:

CAPABILITY A                     PASS
CAPABILITY B                     PASS
COMPONENT AUTHORITY              PASS
COMPOSITION EXISTS               PASS
MATERIAL DELTA                   PASS or NO_MATERIAL_DELTA
COMPOSITION AUTHORITY            PASS
AUTHORITY DELTA                  EXPLAINED

Purpose:

Falsify the overly strong claim that every composition requires a new grant.

---

## 7. Specimen B — Unexplained Material Delta

Given:

Capability A is authorized.

Capability B is authorized.

A and B compose.

The composition creates new consequential reach.

No competent grant covering that new reach has been established.

Expected:

CAPABILITY A                     PASS
CAPABILITY B                     PASS
COMPONENT AUTHORITY              PASS
COMPOSITION EXISTS               PASS
MATERIAL DELTA                   PASS
COMPOSITION AUTHORITY            HOLD
AUTHORITY DELTA                  UNEXPLAINED

Important:

UNEXPLAINED does not mean authority is proven absent.

---

## 8. Specimen C — Technical Composition Without Material Delta

Given:

Capability A is authorized.

Capability B is authorized.

A and B technically compose.

No new material reach, persistence, binding force, scope, or consequence is established.

Expected:

CAPABILITY A                     PASS
CAPABILITY B                     PASS
COMPONENT AUTHORITY              PASS
COMPOSITION EXISTS               PASS
MATERIAL DELTA                   NOT_ESTABLISHED
AUTHORITY DELTA                  NO_MATERIAL_DELTA

Purpose:

Prevent the experiment from treating every composition as authority expansion.

---

## 9. Strong Negative Control

Construct a specimen in which:

A is individually authorized.

B is individually authorized.

A composed with B is demonstrably executable.

The composition demonstrably gains a material consequential capability.

No independently traceable competent grant covering that added consequence is provided.

Required result:

COMPONENT CAPABILITY             PASS
COMPONENT AUTHORITY              PASS
COMPOSITION                      PASS
MATERIAL DELTA                   PASS
COMPOSITION AUTHORITY            HOLD
AUTHORITY DELTA                  UNEXPLAINED

If the experiment instead automatically returns:

COMPOSITION AUTHORITY PASS

then the experiment has silently inherited authority and fails its own boundary.

---

## 10. Positive Control

Provide explicit competent authority covering:

A

B

and

A composed with B for the specified consequence.

Required result:

COMPOSITION AUTHORITY            PASS
AUTHORITY DELTA                  EXPLAINED

If the experiment returns HOLD merely because composition occurred, it is over-restrictive and fails its own boundary.

---

## 11. Falsification Conditions

The candidate principle:

"Authority for composed reach must be independently traceable."

is weakened or falsified if a valid specimen demonstrates that authority standing can be established without any independently identifiable authority basis.

The stronger statement:

"Every composed capability requires a new authority grant."

is already treated as falsifiable and is expected to fail under Specimen A.

No experiment outcome may redefine this after execution.

---

## 12. Primary Reductions Under Test

Capability != Authority

Component Authority != Composition Authority

Executable != Authorized

Individually Authorized != Collectively Authorized

Technical Composition != Material Authority Delta

New Capability != New Authority

Missing Authority Evidence != Proven Authority Absence

Existing Grant != Automatically Insufficient

Composition Novelty != Automatic Reauthorization Requirement

---

## 13. Candidate Principle

Capability may compose.

Authority does not arise merely because capability composed.

Authority standing for materially expanded composed reach must be independently traceable to competent authority.

Status:

CANDIDATE ONLY
NOT ESTABLISHED

UNKNOWN -> HOLD
