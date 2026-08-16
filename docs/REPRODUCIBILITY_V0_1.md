# Authority Composition Inspector v0.1.0 — Reproducibility

## Environment

Python: >= 3.12

Package: authority-composition-experiment

## Validation Commands

python -m pytest -q
python -m ruff check .
python -m mypy src
git diff --check
git status

## Expected Validation

35 passed
Ruff: PASS
Mypy: PASS across 4 source files
git diff --check: no output
git status: clean after release commit

## Frozen Active Test Surface

- test_models_contract.py
- test_specimen_end_to_end.py
- test_v0_1_conformance_red.py
- test_v0_1_cross_binding_contract.py
- test_v0_1_inspector_semantics_red.py

## Legacy Experimental Lineage

Preserved under:

tests/legacy/

These files are not normative v0.1 behavior.

## Release Boundary

Reproducing this validation establishes only conformance with the frozen v0.1
software architecture and tests.

It does not establish real-world authority validity or external institutional
competence.
