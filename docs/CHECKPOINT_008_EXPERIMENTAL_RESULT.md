# CHECKPOINT 008 — EXPERIMENTAL RESULT AND CLAIM BOUNDARY

Status: BOUNDED EXPERIMENTAL RESULT

Architecture: NOT FROZEN
Inspector: NOT YET ESTABLISHED
Real-World Authority Validation: NONE
Promotion: NONE

UNKNOWN -> HOLD

## 1. Research Question

When individually authorized capabilities compose into a capability with new reach, what competent authority, if any, explains the authority standing of that composed reach?

The experiment tested whether authority standing for materially expanded composed reach can be distinguished from:

- component capability authority;
- composition existence;
- technical executability;
- material capability expansion.

It did not test legality, legitimacy, safety, policy compliance, or real-world authorization.

---

## 2. Experimental Boundary

The experiment used synthetic specimens only.

The implemented inspection surface receives independently represented findings concerning:

- composition;
- material delta;
- composition authority;
- supporting grant evidence.

The inspection surface does not create authority.

The experiment does not contain a real-world authority verifier.

Synthetic specimen formation is not equivalent to independent real-world verification.

---

## 3. Control Outcomes

### Specimen A — Explicit Composition Coverage

Observed experimental result:

Component capability standing:
PASS

Composition:
PASS

Material delta:
PASS

Composition authority:
PASS

Authority delta:
EXPLAINED

Interpretation:

A materially expanded composition can retain or receive explained authority standing when competent authority evidence explicitly covers the composition and resulting capability.

This falsifies the overly strong claim:

"Every composed capability requires a new authority grant."

An existing competent grant may already cover the composition.

---

### Specimen B — Unexplained Material Delta

Observed experimental result:

Component capability standing:
PASS

Component authority:
PASS

Composition:
PASS

Material delta:
PASS

Composition authority:
HOLD

Authority delta:
UNEXPLAINED

Interpretation:

Authority attached to independently authorized components did not automatically establish authority for materially expanded composed reach.

The experiment did not classify the composition as:

UNAUTHORIZED
ILLEGAL
INVALID
UNSAFE
PROHIBITED

The bounded finding remained:

AUTHORITY FOR MATERIAL DELTA -> HOLD

---

### Specimen C — Technical Composition Without Material Delta

Observed experimental result:

Component capability standing:
PASS

Composition:
PASS

Material delta:
NOT_ESTABLISHED

Authority delta:
NO_MATERIAL_DELTA

Interpretation:

Technical composition alone did not create an authority-delta finding.

Composition existence is therefore insufficient to establish material authority expansion.

---

## 4. Strong Negative Control

The experiment represented a condition in which:

Capability A was individually authorized.

Capability B was individually authorized.

A composed with B was executable.

The composition introduced material consequential reach.

Competent authority covering that additional reach was not established.

The system did not silently promote:

COMPONENT AUTHORITY PASS

into:

COMPOSITION AUTHORITY PASS

Observed result:

COMPOSITION AUTHORITY -> HOLD

AUTHORITY DELTA -> UNEXPLAINED

This supports the bounded reduction:

Component Authority != Composition Authority

---

## 5. Positive Control

The experiment also represented explicit competent authority coverage for:

Capability A

Capability B

and

the defined composition and resulting capability.

Observed result:

COMPOSITION AUTHORITY -> PASS

AUTHORITY DELTA -> EXPLAINED

Therefore:

Composition Novelty != Automatic Reauthorization Requirement

The experiment is not intended to reject legitimate authority persistence.

---

## 6. Binding Integrity Results

The experiment additionally established that the following are insufficient by themselves:

matching grant identifier;

authority evidence presence;

composition identifier match;

composition authority PASS declaration;

material delta PASS declaration.

The inspection requires relevant evidence to remain bound across:

grant identity;

composition identity;

resulting capability identity;

material-delta formation.

Observed hardening reductions:

Evidence Present != Evidence Bound

Matching Identifier != Matching Scope

Claimed Material Delta != Formed Material Delta

Authority Finding PASS != Supporting Grant Evidence Present

Evidence About Composition X != Evidence About Composition Y

---

## 7. Oracle Independence

The control specimens contain expected outcomes for experimental comparison.

A tampering control altered a specimen's declared control expectation without altering the underlying inspection evidence.

The inspection result remained derived from the bound evidence rather than from the declared expected result.

Supported reduction:

Test Oracle != Inspection Input

Expected Result != Earned Result

Specimen Declaration != Verified Finding

Important limitation:

Within this experiment, specimen declarations are transformed into synthetic findings.

This does not establish independent real-world verification.

---

## 8. Candidate Failure Class Result

Candidate failure class:

UNEXPLAINED AUTHORITY DELTA

Bounded definition:

A materially expanded composed capability is established, while competent authority explaining the additional reach has not been established.

Experimental status:

SUPPORTED WITHIN THE BOUNDED SYNTHETIC EXPERIMENT

The result does not independently establish:

absence of authority;

unauthorized operation;

illegality;

invalidity;

unsafety;

prohibition;

illegitimacy.

UNEXPLAINED remains an epistemic finding.

---

## 9. Strong Claim Review

Original strong formulation:

Capability may compose.
Authority must be re-established.

Result:

TOO STRONG AS A GENERAL STATEMENT.

Reason:

Specimen A demonstrates that an existing competent authority grant may explicitly cover the composition and resulting reach.

The experiment therefore does not support a universal requirement for a new authority grant at every composition.

---

## 10. Narrower Supported Formulation

The bounded experiment supports:

Capability may compose.

Authority does not arise merely because capability composed.

Authority standing for materially expanded composed reach must be independently traceable to an authority basis whose competence and scope are established for that reach.

A further bounded reduction is:

Authority is not automatically closed under capability composition.

This is narrower than:

Authority is not closed under composition.

The universal statement has NOT been established.

---

## 11. New Failure Surface

The experiment demonstrates a condition in which:

Component A standing -> PASS

Component B standing -> PASS

Composition existence -> PASS

Material composed reach -> PASS

while:

Authority for the materially expanded composed reach -> HOLD

This supports the distinction:

Component Standing != Composed Standing

The failure occurs at the composition boundary without requiring either component authority to fail.

---

## 12. Relationship To Existing Architectures

### Bell-Pair Domain Transfer Inspector

Bell-Pair work established that validity in one verification domain cannot repair failure in another inspection domain.

This experiment is different.

The present failure surface concerns authority standing created or exposed by capability composition.

---

### Relational Comparison Protocol

RCP established separation between comparison, integration, transition authority, and standing architecture scope.

This experiment extends a different question:

What happens when separately standing capabilities compose into materially expanded reach?

The relevant failure is not merely transition without authority.

It is composition whose components retain standing while the emergent reach lacks independently established authority coverage.

---

### PRRGE

PRRGE established bounded evidence, admission, witness, variant, lineage, and aggregation separations.

This experiment does not duplicate those source-admission boundaries.

Its relevant question is authority standing across capability composition.

---

## 13. What Has Been Falsified

The following strong statement does not survive the controls:

"Every composed capability requires a new authority grant."

Existing competent authority may explicitly cover composition.

The experiment also rejects:

Technical Composition -> Automatic Authority Delta

and:

Component Authority PASS -> Automatic Composition Authority PASS

---

## 14. What Remains Unknown

The experiment has not established:

how competent authority is determined in real systems;

how conflicting grants should be resolved;

how revocation affects composition;

how temporal authority changes affect composed capability;

how jurisdiction affects composition;

how delegated authority behaves under composition;

whether authority deltas can be quantified;

whether all material-delta dimensions require the same authority treatment;

whether the bounded result generalizes across domains;

whether authority composition obeys a universal formal law.

UNKNOWN -> HOLD

---

## 15. Non-Claims

This experiment does NOT establish that:

authority is universally non-compositional;

all compositions require reauthorization;

novel capability is unauthorized;

missing authority evidence proves authority absence;

authority can be determined from capability structure alone;

authority competence can be inferred from issuer naming;

synthetic grant evidence represents real legal or institutional authority;

execution implies legitimacy;

authority implies safety;

authority implies correctness;

authority implies permission in every external context.

---

## 16. Experimental Result

The experiment has earned the bounded result:

Capability composition can produce materially expanded reach for which component authority alone is insufficient to establish composition authority.

When competent authority covering that expanded reach is not established, the appropriate experimental result is:

COMPOSITION AUTHORITY -> HOLD

AUTHORITY DELTA -> UNEXPLAINED

When competent authority explicitly covers that expanded reach:

COMPOSITION AUTHORITY -> PASS

AUTHORITY DELTA -> EXPLAINED

When no material expansion is established:

AUTHORITY DELTA -> NO_MATERIAL_DELTA

---

## 17. Inspector Justification Review

A distinct inspection surface is justified if the following failure condition cannot be reduced to existing component, transition, or validity inspection:

Component authorities remain standing.

Composition exists.

Material reach expands.

Authority for that expanded reach is not independently established.

The current experiment demonstrates that this condition can be represented and distinguished from:

component authority failure;

absence of composition;

absence of material delta;

explicitly explained composition authority.

Therefore:

DEDICATED INSPECTION SURFACE -> JUSTIFIED

However:

FORMAL INSPECTOR ARCHITECTURE -> NOT YET FROZEN

The experiment should not be renamed or promoted solely from this result document.

---

## 18. Current Candidate Principle

Capability may compose.

Authority does not arise merely because capability composed.

Authority standing for materially expanded composed reach must be independently traceable to an authority basis whose competence and scope are established for that reach.

Status:

SUPPORTED WITHIN BOUNDED SYNTHETIC EXPERIMENT

NOT UNIVERSAL

NOT REAL-WORLD VALIDATED

NOT A LEGAL DETERMINATION

NOT AN AUTHORITY DECISION PROCEDURE

UNKNOWN -> HOLD
