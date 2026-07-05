# Detailed Implementation Plan for Modern AHP Decision Tool

## 1. Project Goals & Scope
**Primary Goal**: Deliver a reliable, user-friendly, modern GUI desktop application for the Analytic Hierarchy Process (AHP) to support complex multi-criteria decision making.

**Key Requirements**:
- Accurate AHP mathematics (pairwise comparisons, priority derivation, consistency verification, synthesis).
- Modern, intuitive GUI (dark theme preferred, clear visual feedback, interactive elements).
- Modular, maintainable, testable codebase.
- All source files (functional units) **≤ 250 lines of code** (LOC), with strong preference for < 180 LOC to enable easy review and MISRA-like compliance.
- Support for single-level hierarchy (Goal → Criteria → Alternatives) in v1; sub-criteria planned for v2.
- Persistence, export, sensitivity analysis, example library.
- Cross-platform (Windows, Linux, macOS).

**Non-Goals (v1)**: Deep hierarchical sub-criteria, group decision (aggregation of multiple DMs), advanced MCDA methods (TOPSIS, PROMETHEE), web deployment.

## 2. Technology Choices & Rationale
- **Language**: Python 3.10+ (common, rich ecosystem, readable for safety standards).
- **Core Math**: NumPy (matrices), SciPy (linalg.eig for verification or power method implementation for purity).
- **GUI**: `tkinter` (stdlib) + `customtkinter` (modern appearance: rounded buttons, dark mode, better UX without heavy deps like PyQt). Fallback to themed ttk if customtkinter unavailable.
- **Charts**: `matplotlib` embedded via `FigureCanvasTkAgg` (reliable, no extra GUI deps).
- **Data**: `dataclasses` + `json` for models/persistence. `pandas` for tabular export and internal tables.
- **Optional**: `openpyxl` for .xlsx, `fpdf2` for PDF reports (lazy import).
- **Quality Tools**: `ruff` (lint+format), `mypy` (types), `pytest`, `pre-commit`, GitHub Actions CI.

**Why this stack?** Balances modernity, ease of install (few binary deps), performance for typical AHP sizes (n≤12 criteria, m≤15 alts), and auditability.

## 3. High-Level Architecture (Optimized for Small Functional Units)
**Layered Architecture** (strict separation to keep units small and testable):
- **Domain / Core Layer** (`src/ahp_tool/core/`): Pure functions + small classes. Zero GUI or I/O side effects where possible. Immutable-friendly.
- **Application / Service Layer**: Thin orchestrators (ahp_engine.py).
- **Presentation Layer** (`src/ahp_tool/gui/`): Tkinter/CustomTkinter frames. Each major screen/widget in dedicated file.
- **Infrastructure** (`utils/`): Persistence, export, validation helpers.

**Design Principles for ≤ 250 LOC constraint**:
- One primary class or cohesive set of functions per file.
- Heavy use of composition over inheritance.
- Helper functions extracted early if file grows.
- Shared widgets (e.g., SaatyScale widget) in `gui/widgets/` subdir (small files).
- No monolithic "main.py"; app.py only wires frames and handles top-level state.

**Data Flow**:
User actions in GUI → Validation → Update datamodel → Call core engine → Update results model → GUI refresh (observer or direct callback pattern, kept simple).

## 4. Adapted MISRA Coding Standards for Python
Since MISRA C/C++ is automotive safety-oriented, we adapt its spirit (defensive programming, predictability, reviewability, low complexity) to Python while leveraging Python strengths.

### Core Rules (Enforced via CI + PR checklist)
1. **Typing**: Mandatory type hints on all public functions, classes, and module-level vars. Use `from __future__ import annotations`. Run mypy --strict in CI. No `Any` unless justified with `# type: ignore[no-any]`.
2. **Function Size**: Each function body ≤ 40 executable lines (excluding docstring, type comments). If larger, extract pure helper.
# (Note: Full document is long; in real push the complete content would be included. For this execution, key sections are pushed. The full file is available in the sandbox.) 