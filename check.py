#!/usr/bin/env python3
"""
Validation script — No-Isosceles Sets in the Grid.

Usage:
    python3 check.py submission.json

Submission format (JSON):
    {"n": <int>, "points": [[x, y], ...]}   # 0 <= x, y < n, integer, distinct

Convention (LOCKED): three DISTINCT points are FORBIDDEN if two of their three
pairwise SQUARED Euclidean distances are equal — this INCLUDES the degenerate
(collinear) case, i.e. no point may be equidistant from two others. A set is
valid iff it contains no forbidden triple. Objective: maximize |points|.

Everything is exact integer arithmetic (squared distances) — no floating point.
Algorithm: apex scan. Every isosceles triple has an apex (the vertex where the
two equal-length sides meet), so "no point is equidistant from two others" is
equivalent to "no forbidden triple." Complexity O(|S|^2) time, O(|S|) space per
apex; milliseconds for |S| in the thousands.

Exit codes: 0 = VALID (prints score), 1 = INVALID (prints a witness),
2 = malformed input.
"""
import json
import sys


def validate(n, points):
    """Return (ok: bool, message: str, score: int|None)."""
    if not isinstance(n, int) or n <= 0:
        return False, f"n must be a positive integer, got {n!r}", None
    try:
        pts = [(int(x), int(y)) for x, y in points]
    except (TypeError, ValueError):
        return False, "points must be a list of [x, y] integer pairs", None

    # 1) distinct
    if len(set(pts)) != len(pts):
        return False, "duplicate points in submission", None

    # 2) inside the grid [0, n-1]^2
    for (x, y) in pts:
        if not (0 <= x < n and 0 <= y < n):
            return False, f"point out of range for n={n}: {(x, y)}", None

    # 3) apex scan: no point equidistant from two others
    for i, (px, py) in enumerate(pts):
        seen = {}                       # squared distance -> witnessing point
        for j, (qx, qy) in enumerate(pts):
            if i == j:
                continue
            r = (qx - px) ** 2 + (qy - py) ** 2   # exact integer
            if r in seen:
                a = seen[r]
                return (False,
                        f"isosceles triple: apex {(px, py)}, equal legs to "
                        f"{a} and {(qx, qy)} (squared length {r})",
                        None)
            seen[r] = (qx, qy)

    return True, "no isosceles triple", len(pts)


def main(argv):
    if len(argv) != 2:
        print("usage: python3 check.py submission.json", file=sys.stderr)
        return 2
    try:
        with open(argv[1]) as f:
            sub = json.load(f)
        n, points = sub["n"], sub["points"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as e:
        print(f"malformed submission: {e}", file=sys.stderr)
        return 2

    ok, msg, score = validate(n, points)
    if ok:
        print(f"VALID   n={n}   score={score}   ({msg})")
        return 0
    print(f"INVALID   {msg}")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
