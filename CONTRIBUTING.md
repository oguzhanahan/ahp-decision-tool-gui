# Contributing to Modern AHP Decision Tool

Thank you for your interest in contributing! This project follows a high-assurance, MISRA-adapted development process to ensure reliability for decision-support software.

## Development Process

1. **Read the Plans First**
   - `docs/implementation_plan.md` — Architecture, MISRA Python rules, module breakdown
   - `docs/task_execution_plan.md` — Phased tasks with DoD
   - `docs/agent_skill_commitments.md` — Roles (CoreDev, GUIDev, QAAgent, DevOpsDocs) and peer-review rules
   - `docs/test_verification_structure.md` — How we verify correctness

2. **Branching & PRs**
   - Create feature branch from `main`
   - All changes via Pull Request
   - **Mandatory**: ≥ 2 approvals (including primary owner + QAAgent)
   - Use the PR template checklist (includes LOC ≤ 250 rule)

3. **Coding Standards (Enforced)**
   - Every file ≤ 250 LOC (target <180)
   - Full type hints + mypy --strict
   - Ruff + Black formatting
   - Pre-commit hooks recommended
   - See `implementation_plan.md` Section 4 for full adapted MISRA rules

4. **Testing**
   - Add/update tests for every public API
   - Verify against reference AHP examples
   - Run `pytest` and the LOC checker before PR

## Local Development Setup

```bash
git clone https://github.com/oguzhanahan/ahp-decision-tool-gui.git
cd ahp-decision-tool-gui
python -m venv .venv
source .venv/bin/activate
pip install -e "[dev,gui]"
pre-commit install   # optional but recommended
```

## Commit Messages
Use Conventional Commits:
- `feat(core): add geometric mean priority calculation`
- `fix(gui): correct live CR color feedback`
- `docs: update task plan for Phase 1`

## Questions?
Open an issue or discuss in the relevant task issue.

We appreciate high-quality, well-tested contributions that keep the codebase maintainable and trustworthy!