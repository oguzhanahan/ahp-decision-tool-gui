# Changelog

All notable changes to the AHP Decision Tool will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-07-06

### Added
- Complete AHP decision support application with modern GUI (CustomTkinter + Tk fallback)
- Full core engine: priority vectors (geometric mean + power iteration), consistency ratio (Saaty), global synthesis
- Interactive hierarchy editor (add/edit/remove criteria & alternatives)
- Pairwise comparison matrices with live Saaty 1-9 scale widgets and real-time CR color feedback
- Results view with sortable ranking table, bar chart, and radar/spider chart
- Interactive sensitivity analysis with live weight sliders and instant re-ranking preview
- Persistence: Save/Load full projects as JSON (lossless roundtrip)
- Multi-format export: CSV, Excel (multi-sheet), JSON, PDF reports
- Classic family car selection example pre-loaded in GUI
- Strict MISRA-adapted Python coding standards enforced (≤250 LOC per file, type hints, frozen dataclasses, etc.)
- Comprehensive test suite + CI configuration
- Professional packaging: `pyproject.toml`, console script `ahp-gui`, PyInstaller single-file spec
- Full documentation: Implementation Plan, Task Execution Plan, Agent Skill Commitments, Test & Verification Structure

### Changed
- All functional units kept under 250 lines of code
- Layered architecture: pure `core/` + thin `gui/` + `utils/`

### Fixed
- Proper reciprocal matrix validation and defensive error handling throughout

## [0.1.0] - 2026-07-05

### Added
- Initial project structure and planning documents
- Core AHP engine skeleton
- Basic GUI scaffolding
