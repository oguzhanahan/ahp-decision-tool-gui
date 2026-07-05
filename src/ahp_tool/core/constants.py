"""Project-wide constants for AHP calculations (Saaty scale, thresholds)."""

CR_THRESHOLD: float = 0.10
TOLERANCE: float = 1e-10
SAATY_SCALE: tuple[int, ...] = tuple(range(1, 10))

# Verbal labels for Saaty scale (for GUI)
SAATY_LABELS: dict[int, str] = {
    1: "Equal importance",
    2: "Weak",
    3: "Moderate importance",
    4: "Moderate plus",
    5: "Strong importance",
    6: "Strong plus",
    7: "Very strong",
    8: "Very, very strong",
    9: "Extreme importance",
}
