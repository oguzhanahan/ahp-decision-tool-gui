"""Custom exceptions for AHP errors (defensive, specific)."""

class AHPError(Exception):
    """Base exception for all AHP-related errors."""
    pass

class InvalidMatrixError(AHPError):
    """Raised when a comparison matrix is not reciprocal, not positive, or malformed."""
    pass

class ComputationError(AHPError):
    """Raised when AHP computation fails (e.g., no hierarchy, missing matrices)."""
    pass

class InvalidHierarchyError(AHPError):
    """Raised when the hierarchy (criteria/alternatives) is invalid or empty."""
    pass
