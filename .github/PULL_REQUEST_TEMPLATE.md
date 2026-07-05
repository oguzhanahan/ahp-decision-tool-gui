# Pull Request Checklist (MISRA-Adapted + LOC Enforcement)

## Required for ALL PRs

- [ ] **All changed/added `.py` files are ≤ 250 lines of code** (run `python scripts/check_loc.py` locally before pushing)
- [ ] Type hints added on all public functions/classes; `mypy` passes
- [ ] New or changed functionality has corresponding tests (or explicit justification in description)
- [ ] Numerical results verified against at least one reference AHP example (car purchase, house selection, etc.)
- [ ] Ruff lint + format passed (`ruff check . && ruff format --check .`)
- [ ] No new runtime dependencies added without DevOpsDocs approval
- [ ] Documentation / tooltips / README updated if user-facing change
- [ ] PR title follows Conventional Commits (e.g. `feat(core): implement geometric mean priority`)

## Additional for Core Changes (`src/ahp_tool/core/`)
- [ ] CoreDev reviewed and approved
- [ ] At least 3 reference examples produce expected priorities/CR within 1e-6 tolerance
- [ ] Cyclomatic complexity ≤ 8 and function bodies ≤ 40 LOC (where practical)

## Additional for GUI Changes
- [ ] GUIDev reviewed
- [ ] Widget reusability considered; no business logic in view files
- [ ] Live feedback (CR color coding, etc.) works as expected

## Review Requirements
This PR requires **at least 2 approvals**:
- One from the primary code owner (see CODEOWNERS)
- QAAgent is mandatory reviewer on every PR

**Description of changes** (why, what, how it was tested):