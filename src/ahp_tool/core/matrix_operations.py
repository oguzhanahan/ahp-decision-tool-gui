'''Matrix operations for AHP pairwise comparisons.

MISRA-adapted: pure functions, type hints, explicit validation,
small focused functions, no magic numbers.
'''

from __future__ import annotations

import numpy as np

from .constants import TOLERANCE
from .exceptions import InvalidInputError, NonReciprocalMatrixError


def is_reciprocal(matrix: np.ndarray, tol: float = TOLERANCE) -> bool:
    """Check if matrix M satisfies M[i,j] * M[j,i] ≈ 1 for all i != j."""
    if matrix.ndim != 2 or matrix.shape[0] != matrix.shape[1]:
        raise InvalidInputError("Matrix must be square 2D array")
    n = matrix.shape[0]
    for i in range(n):
        for j in range(i + 1, n):
            product = matrix[i, j] * matrix[j, i]
            if not np.isclose(product, 1.0, atol=tol):
                return False
    return True


def validate_reciprocal_matrix(matrix: np.ndarray, tol: float = TOLERANCE) -> None:
    """Raise if not positive reciprocal matrix."""
    mat = np.asarray(matrix, dtype=np.float64)
    if mat.ndim != 2 or mat.shape[0] != mat.shape[1]:
        raise InvalidInputError("Comparison matrix must be square")
    if not np.all(mat > 0):
        raise InvalidInputError("All entries in comparison matrix must be positive")
    if not is_reciprocal(mat, tol):
        raise NonReciprocalMatrixError("Matrix is not reciprocal (M[i,j] * M[j,i] != 1)")


def normalize_columns(matrix: np.ndarray) -> np.ndarray:
    """Column-normalize a matrix (each column sums to 1)."""
    mat = np.asarray(matrix, dtype=np.float64)
    col_sums = mat.sum(axis=0)
    if np.any(col_sums == 0):
        raise InvalidInputError("Cannot normalize matrix with zero column sum")
    return mat / col_sums


def row_geometric_means(matrix: np.ndarray) -> np.ndarray:
    """Compute row geometric means and normalize to priority vector."""
    mat = np.asarray(matrix, dtype=np.float64)
    n = mat.shape[0]
    if n == 0:
        return np.array([])
    # Geometric mean per row: (prod over columns)^{1/n}
    with np.errstate(divide="ignore", invalid="ignore"):
        geo_means = np.exp(np.log(mat).sum(axis=1) / n)
    # Handle any zero or negative (should not happen after validation)
    geo_means = np.where(geo_means > 0, geo_means, 1e-12)
    return geo_means / geo_means.sum()


def build_matrix_from_upper_triangle(
    upper_triangle: dict[tuple[int, int], float],
    n: int,
    default_diagonal: float = 1.0,
) -> np.ndarray:
    """Build full reciprocal matrix from upper triangle comparisons (i < j)."""
    mat = np.full((n, n), default_diagonal, dtype=np.float64)
    for (i, j), value in upper_triangle.items():
        if i >= j or i < 0 or j >= n:
            raise InvalidInputError(f"Invalid index pair {(i, j)} for n={n}")
        mat[i, j] = float(value)
        mat[j, i] = 1.0 / float(value)
    return mat
