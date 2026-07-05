"""High-level AHPModel facade.

Orchestrates the full AHP workflow using smaller functional units.
All heavy lifting delegated to dedicated modules (priority_vector, consistency, synthesis).
This file kept < 180 LOC by design.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

import numpy as np

from .constants import CR_THRESHOLD, TOLERANCE
from .datamodels import (
    AHPStructure,
    Alternative,
    ComparisonMatrix,
    Criterion,
    PriorityVector,
)
from .exceptions import ComputationError, InvalidHierarchyError
from .consistency import (
    calculate_consistency_ratio_from_matrix,
    is_consistent,
)
from .priority_vector import calculate_priority_vector
from .synthesis import synthesize_global_priorities


@dataclass
class AHPModel:
    """Main facade for AHP computations. Maintains hierarchy and matrices."""

    goal: str = "Goal"
    criteria: list[Criterion] = field(default_factory=list)
    alternatives: list[Alternative] = field(default_factory=list)
    criteria_matrix: ComparisonMatrix | None = None
    alt_matrices: dict[str, ComparisonMatrix] = field(default_factory=dict)  # criterion.name -> matrix

    def add_criterion(self, name: str, description: str = "") -> None:
        if any(c.name == name for c in self.criteria):
            raise ValueError(f"Criterion '{name}' already exists")
        self.criteria.append(Criterion(name=name, description=description))

    def add_alternative(self, name: str, description: str = "") -> None:
        if any(a.name == name for a in self.alternatives):
            raise ValueError(f"Alternative '{name}' already exists")
        self.alternatives.append(Alternative(name=name, description=description))

    def set_criteria_matrix(self, matrix: list[list[float]]) -> None:
        self.criteria_matrix = ComparisonMatrix(values=matrix)

    def set_alt_matrix(self, criterion_name: str, matrix: list[list[float]]) -> None:
        self.alt_matrices[criterion_name] = ComparisonMatrix(values=matrix)

    def compute(self) -> dict[str, Any]:
        """Run full AHP pipeline and return results dict."""
        if not self.criteria or not self.alternatives:
            raise InvalidHierarchyError("Hierarchy must have at least one criterion and one alternative")
        if self.criteria_matrix is None:
            raise ComputationError("Criteria comparison matrix not set")

        # Criteria priorities
        crit_pv, crit_cr = calculate_priority_vector(self.criteria_matrix.values), calculate_consistency_ratio_from_matrix(self.criteria_matrix.values)
        crit_priorities = {c.name: float(p) for c, p in zip(self.criteria, crit_pv)}

        # Per-criterion alt priorities
        alt_local: dict[str, dict[str, float]] = {}
        alt_crs: dict[str, float] = {}
        for crit in self.criteria:
            mat = self.alt_matrices.get(crit.name)
            if mat is None:
                raise ComputationError(f"Alternative matrix for '{crit.name}' not set")
            pv, cr = calculate_priority_vector(mat.values), calculate_consistency_ratio_from_matrix(mat.values)
            alt_local[crit.name] = {a.name: float(p) for a, p in zip(self.alternatives, pv)}
            alt_crs[crit.name] = cr

        # Global synthesis
        global_prios = synthesize_global_priorities(crit_priorities, alt_local)

        return {
            "global_priorities": global_prios,
            "criteria_priorities": crit_priorities,
            "criteria_cr": crit_cr,
            "alt_local_priorities": alt_local,
            "alt_crs": alt_crs,
            "overall_consistency_ratio": max([crit_cr] + list(alt_crs.values())),
            "message": "Computation successful" if max([crit_cr] + list(alt_crs.values())) < CR_THRESHOLD else "Some matrices have high inconsistency (CR >= 0.1)"
        }

    def to_dict(self) -> dict[str, Any]:
        return {
            "goal": self.goal,
            "criteria": [c.__dict__ for c in self.criteria],
            "alternatives": [a.__dict__ for a in self.alternatives],
            "criteria_matrix": self.criteria_matrix.values if self.criteria_matrix else None,
            "alt_matrices": {k: v.values for k, v in self.alt_matrices.items()},
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "AHPModel":
        model = cls(goal=data.get("goal", "Goal"))
        for c in data.get("criteria", []):
            model.add_criterion(c["name"], c.get("description", ""))
        for a in data.get("alternatives", []):
            model.add_alternative(a["name"], a.get("description", ""))
        if data.get("criteria_matrix"):
            model.set_criteria_matrix(data["criteria_matrix"])
        for k, v in data.get("alt_matrices", {}).items():
            model.set_alt_matrix(k, v)
        return model
