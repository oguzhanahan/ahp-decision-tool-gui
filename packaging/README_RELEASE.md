# AHP Decision Tool v1.0 - Release Package

**Modern, accurate, single-file GUI application for the Analytic Hierarchy Process (AHP) decision making method.**

Built following strict MISRA-inspired coding standards for Python:
- Every functional unit ≤ 250 lines of code
- Full type hints + mypy strict
- Layered architecture (pure core + thin GUI)
- Peer-reviewed process ready
- Comprehensive tests + classic reference examples

## What's Included in This Release

- `ahp-gui.spec` — PyInstaller specification for building the **single-file executable**
- `src/` — Complete, production source code (all modules < 250 LOC)
- `docs/` — Implementation plan, task plan, agent commitments, test strategy
- `pyproject.toml` — Modern Python packaging (v1.0.0)
- `README.md` — Full user & developer documentation

## Quick Start (from source)

```bash
git clone https://github.com/oguzhanahan/ahp-decision-tool-gui.git
cd ahp-decision-tool-gui
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -e ".[gui]"
ahp-gui
```

Or run directly:
```bash
python -m src.ahp_tool.gui.app
```

## Building the Single-File Executable (Recommended)

On **Windows**, **macOS**, or **Linux** desktop with Python 3.10+ and Tkinter:

1. Install build dependencies:
   ```bash
   pip install pyinstaller numpy scipy pandas matplotlib customtkinter fpdf2
   ```

2. Build:
   ```bash
   pyinstaller ahp-gui.spec
   ```

3. The executable will be in `dist/ahp-gui` (Linux/macOS) or `dist/ahp-gui.exe` (Windows).

**One-file advantages**:
- Single executable, no installation needed
- Includes all dependencies (NumPy, SciPy, Matplotlib, CustomTkinter, etc.)
- Runs on machines without Python installed

**Note on Tkinter**: The app gracefully falls back to standard Tkinter if `customtkinter` is not installed. Your system Python must have Tkinter support (included by default on Windows and macOS; on Linux install `python3-tk`).

## Features (v1.0 Complete)

- Interactive hierarchy definition (goal, criteria, alternatives)
- Saaty-scale pairwise comparison matrices with **live consistency ratio (CR)** feedback (color coded)
- Real AHP engine: geometric mean + power iteration, consistency index/ratio
- Global priority synthesis
- Results: sortable table + bar chart / radar chart toggle
- **Interactive sensitivity analysis** — drag weight sliders and see instant ranking updates
- Save / Load projects (JSON, lossless)
- Export results to CSV, Excel (multi-sheet), JSON, PDF
- Classic car-purchase example pre-loaded
- Modern dark theme (CustomTkinter) with graceful Tk fallback

## Verification & Quality

All phases executed per original plans:
- Phase 0: Foundation, MISRA rules, CI, PR process
- Phase 1: Core AHP engine (priority, consistency, synthesis)
- Phase 2: GUI data entry + live CR
- Phase 3: Results visualization + sensitivity
- Phase 4: Persistence, multi-format export, v1.0 packaging

Tested with classic Saaty examples — priorities and CR match reference values.

## License

MIT License (see original repo for full text).

## Support & Contributing

See `CONTRIBUTING.md` and the detailed plans in `docs/`.

For issues: https://github.com/oguzhanahan/ahp-decision-tool-gui/issues

---

**Ready for real-world multi-criteria decisions.**  
Enjoy the tool!
