# Modern AHP Decision Making Tool (PyAHP-GUI)

A Python-based desktop application implementing the Analytic Hierarchy Process (AHP) for structured decision making, featuring a modern graphical user interface.

## Features (Planned)
- Intuitive hierarchy definition (Goal, Criteria, Alternatives)
- Interactive pairwise comparison matrices with Saaty 1-9 scale + verbal descriptions
- Automatic consistency ratio (CR) calculation and warnings
- Priority vector computation using reliable methods (geometric mean / power iteration)
- Global priority synthesis and alternative ranking
- Interactive sensitivity analysis
- Modern dark-themed GUI with embedded visualizations (bar, radar charts)
- Project save/load (JSON), export to Excel/CSV/PDF report
- Example templates and comprehensive help

## Tech Stack
- **Core Computation**: Python 3.10+, NumPy, SciPy (eigen), Pandas
- **GUI**: Tkinter + CustomTkinter (modern widgets, themes)
- **Visualization**: Matplotlib (embedded in Tk)
- **Persistence/Export**: JSON, openpyxl/pandas for Excel, optional fpdf2 for PDF
- **Quality**: Type hints (mypy), Ruff/Black linting, Pytest, pre-commit

## Project Structure (Optimized for MISRA-like compliance & small units)
All functional units (source files) are designed to be **≤ 250 lines of code** (target <180 for most). 
See `docs/implementation_plan.md` for detailed module breakdown, architecture, and adapted MISRA Python coding standards.

```
ahp_decision_tool/
├── src/ahp_tool/
│   ├── core/               # Pure AHP engine (no GUI deps)
│   │   ├── constants.py
│   │   ├── exceptions.py
│   │   ├── datamodels.py
│   │   ├── matrix_operations.py
│   │   ├── priority_vector.py
│   │   ├── consistency.py
│   │   ├── synthesis.py
│   │   └── ahp_engine.py
│   ├── gui/                # Modern GUI layer (depends on core)
│   │   ├── app.py
│   │   ├── hierarchy_editor.py
│   │   ├── matrix_input.py
│   │   ├── results_view.py
│   │   └── ...
│   ├── utils/
│   │   ├── persistence.py
│   │   ├── exporters.py
│   │   └── validators.py
│   └── __init__.py
├── tests/
├── docs/
│   ├── implementation_plan.md
│   ├── task_execution_plan.md
│   ├── agent_skill_commitments.md
│   └── test_verification_structure.md
├── .github/
│   └── workflows/ (CI)
├── pyproject.toml
├── requirements.txt
└── README.md
```

## Getting Started (After Implementation)
```bash
git clone https://github.com/<your-org>/ahp-decision-tool-gui.git
cd ahp-decision-tool-gui
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m src.ahp_tool.gui.app
```

## Status
This repository is initialized with **detailed implementation, task, agent commitment, and verification plans** following best practices for safety-critical inspired development (MISRA-adapted).

Implementation will proceed via structured tasks with peer review. See docs/ for full plans.

**License**: MIT (or Apache 2.0)
**Author**: Grok-assisted structured project bootstrap

## Contributing
See `docs/agent_skill_commitments.md` for roles and peer-review process.
All contributions via Pull Requests with checklist enforcement.