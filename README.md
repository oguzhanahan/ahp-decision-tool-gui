# Modern AHP Decision Making Tool (PyAHP-GUI)

A Python-based desktop application implementing the Analytic Hierarchy Process (AHP) for structured decision making, featuring a modern graphical user interface.

## Features (v1.0 - Complete)
- Full AHP workflow: Define hierarchy → Interactive Saaty matrices with **live CR feedback** (color-coded)
- Real computation engine (geom. mean + power iteration, synthesis, consistency)
- Results: Sorted global ranking table + embedded Bar / Radar charts
- Interactive sensitivity analysis (live weight sliders → instant re-ranking)
- **Persistence**: Save/Load full projects as .ahp.json (lossless roundtrip)
- **Export**: CSV, Excel (multi-sheet), PDF report, JSON (via menu buttons)
- Modern dark GUI (CustomTkinter) with graceful Tk fallback
- Classic car selection example pre-loaded with realistic consistent judgments
- Comprehensive inline help + settings dialog

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
│   │   ├── ahp_engine.py
│   ├── gui/                # Modern GUI layer (depends on core)
│   │   ├── app.py
│   │   ├── hierarchy_editor.py
│   │   ├── matrix_input.py
│   │   ├── results_view.py
│   │   ├── sensitivity_panel.py
│   │   ├── theme.py
│   │   ├── widgets/saaty_scale.py
│   ├── utils/
│   │   ├── persistence.py
│   │   ├── exporters.py
│   ├── __init__.py
├── tests/
├── docs/
├── .github/
├── pyproject.toml
├── requirements.txt
├── README.md
```

## Getting Started
```bash
git clone https://github.com/oguzhanahan/ahp-decision-tool-gui.git
cd ahp-decision-tool-gui
python -m venv .venv && source .venv/bin/activate
pip install -e ".[gui]"
ahp-gui
```

## Status
**v1.0.0 Complete** - All phases (0-4) executed. Full working application with accurate AHP math, modern GUI, sensitivity, persistence, and multi-format export.

**License**: MIT
**Author**: Grok xAI structured project