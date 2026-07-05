#!/usr/bin/env python3
"""Simple LOC checker for MISRA rule enforcement.

Fails if any .py file in src/ exceeds 250 lines.
Run before committing or in CI.
"""

import os
import sys

MAX_LOC = 250
SRC_DIR = "src"


def count_lines(filepath: str) -> int:
    with open(filepath, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def main() -> None:
    violations = []
    for root, _, files in os.walk(SRC_DIR):
        for filename in files:
            if filename.endswith(".py"):
                path = os.path.join(root, filename)
                loc = count_lines(path)
                if loc > MAX_LOC:
                    violations.append((path, loc))

    if violations:
        print("MISRA VIOLATION: The following files exceed 250 LOC:")
        for path, loc in violations:
            print(f"  {path}: {loc} lines")
        print(f"\nPlease refactor to keep all functional units ≤ {MAX_LOC} LOC.")
        sys.exit(1)
    else:
        print(f"All source files in {SRC_DIR}/ are ≤ {MAX_LOC} LOC ✓")
        sys.exit(0)


if __name__ == "__main__":
    main()