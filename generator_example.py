#!/usr/bin/env python3
"""
Reference generator — No-Isosceles Sets in the Grid.

Given n, greedily builds a VALID (no-isosceles, degenerate case included) subset
of {0,...,n-1}^2 and prints it as the task's object JSON to stdout:
    {"n": n, "points": [[x, y], ...]}

This is a BASELINE — a legitimate but non-record construction — to demonstrate
the generator tier end to end:

    python3 generator_example.py 32 | python3 check.py /dev/stdin

It generalizes across n (a deterministic greedy), which is the whole point of the
generator tier. A real generator-tier submission would beat this baseline and/or
the published records (n=64 -> 112, n=100 -> 160); this one just shows the shape.

Invariant maintained while building: no chosen point is equidistant from two
others (⇔ no isosceles triple, incl. collinear).  O(n^2 * |S|) time.
"""
import json
import sys


def generate(n):
    S = []          # chosen points, in scan order
    dsets = []      # dsets[i] = { squared distances from S[i] to the other chosen points }
    for x in range(n):
        for y in range(n):
            dP = [(qx - x) ** 2 + (qy - y) ** 2 for (qx, qy) in S]

            # Condition A: the new point P is not equidistant from two chosen points.
            if len(set(dP)) != len(dP):
                continue

            # Condition B: adding P does not make any chosen point equidistant from
            # P and one of its existing neighbours.
            if any(dP[i] in dsets[i] for i in range(len(S))):
                continue

            for i in range(len(S)):
                dsets[i].add(dP[i])
            dsets.append(set(dP))
            S.append((x, y))
    return S


def main(argv):
    if len(argv) != 2:
        print("usage: python3 generator_example.py <n>", file=sys.stderr)
        return 2
    try:
        n = int(argv[1])
        if n <= 0:
            raise ValueError
    except ValueError:
        print("n must be a positive integer", file=sys.stderr)
        return 2
    S = generate(n)
    print(json.dumps({"n": n, "points": [[x, y] for (x, y) in S]}))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
