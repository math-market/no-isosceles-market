# Task — No-Isosceles Sets in the Grid

*Complete, ready-to-post problem-market task. Package: `TASK.md` (this file) · `check.py` (validator) · `example_valid.json` / `example_bad.json` (fixtures).*

---

## The problem

Fix a grid size **n**. Find the **largest** set of distinct lattice points `S ⊆ {0,…,n−1}²` such that **no three points of S form an isosceles triangle**, where "isosceles" **includes the degenerate (collinear) case** — i.e. no point of S is equidistant from two others.

**Objective:** maximize `|S|`. **One leaderboard per n.**

## Precise definition (convention — LOCKED)

Three distinct points `A, B, C ∈ S` are **forbidden** iff two of their three pairwise **squared** Euclidean distances are equal:
`|AB|² = |AC|²` or `|AB|² = |BC|²` or `|AC|² = |BC|²`.
Squared distances are integers ⇒ the test is **exact**, no floating point. `S` is *valid* iff it contains no forbidden triple.

> ⚠️ **Convention lock.** We *include* degenerate/collinear isosceles (a point at the midpoint of two others counts). This matches the PatternBoost / AlphaEvolve record convention. A construction that is a "record" only under a *different* convention (e.g. non-degenerate only) does **not** count on this board.

## How to submit

Three tiers — a task carries a **separate escrowed bounty for each** (see below). Different solvers can claim different tiers.

- **Object** — a JSON file: `{"n": <int>, "points": [[x,y], …]}` (distinct, in `[0,n−1]²`).
- **Generator** — a program that, given `n`, prints the object JSON to stdout. Run in a sandbox (deterministic, budgeted, no network); scored on the constructions it produces **and its generality across n**.
- **Proof** — a Lean development proving the construction is **optimal** (a matching upper bound), or a general density/growth bound. Verified by Lean CI + faithfulness review.

## How verification works

1. **Client-side (run it yourself first):** `python3 check.py your_submission.json`. Prints `VALID n=… score=…` (exit 0) or `INVALID <witness>` (exit 1). Not a prerequisite to submit, but —
2. **Server-side first cut:** we run the **identical** `check.py` in a pinned container. If a submission fails this check (having skipped the free client-side run), the submitter forfeits the token cost. For **object** tier, passing this check is acceptance. For **generator**, we run the generator (sandboxed) then `check.py` on its output. For **proof**, CI runs the Lean build.
3. **Faithfulness / final acceptance (proof tier only):** the objective check ≠ "the theorem says what it should"; the task owner / faithfulness rubric confirms intent. (Object & generator tiers have no faithfulness gap — the checker is the whole story.)

`check.py` is the **canonical arbiter** — exact integer arithmetic, `O(|S|²)`, milliseconds for thousands of points. Reference algorithm: *apex scan* — every isosceles triple has an apex (the vertex where the two equal legs meet), so "no point is equidistant from two others" is equivalent to "no forbidden triple." (Tested: catches degenerate/collinear cases, out-of-range, duplicates.)

## Bounty tiers (per board / n)

| Tier | Submit | Check | Payout |
|---|---|---|---|
| **Object** | a record point set | `check.py` → beats current board best | base |
| **Generator** | code producing sets across many n | sandboxed run → `check.py`; score by generality | × |
| **Proof** | Lean proof of optimality / a bound | Lean CI + faithfulness | ×× |

A **static set is a degenerate generator** — accepted, but earns only the base tier and doesn't generalize. Award on **first *verified* record-beating** submission, not submission order; bounty stays in escrow until verified.

## Leaderboard & current records

One board per n (e.g. n = 16, 32, 64, 100, 128, …), ranked by `|S|` (ties → earliest submission). Show the standing board best **and** the published reference record:

| n | Reference record | Source |
|---|---|---|
| 64 | **112** points | AlphaEvolve (2026); PatternBoost had 110 |
| 100 | **160** points | PatternBoost (2024) |

*(Records to verify against this exact convention before treating as the bar — see the convention lock. Growth rate of `f(n)` is OPEN; even an `n^{1.99}` upper bound is open — hence the proof tier is a real, hard target.)*

## Acceptance criteria (summary)

- Object valid iff `check.py` returns VALID; it **wins** iff its score beats the current board best for that n.
- Generator valid iff every produced construction passes `check.py`; scored on best construction + generality.
- Proof valid iff it compiles axiom-clean and the faithfulness review passes.

## Sourcing

Problem stated in our own words. Studied/records-held by PatternBoost (Charton–Ellenberg–Wagner–Williamson, 2024) and AlphaEvolve (2026) — **credit both** when posting; for a public launch, a courtesy note to the authors is worthwhile (they're also beta-tester candidates). The *problem* is not copyrightable; do not copy their prose/figures or code except per license. (See `../../problems-to-solicit.md` → Sourcing & attribution.)
