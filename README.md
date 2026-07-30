# No-Isosceles — a problem-market task (CI-as-verifier PoC)

A single **problem-market board**: find the largest no-isosceles set in the n×n grid.
Submissions are **verified automatically by GitHub Actions** — this repo is a proof of
concept for "the task is a repo; the checker is CI."

## Leaderboard

### Market board — n = 64 (OPEN RECORD — main bounty)

| Rank | Score | Submitter | Date | Notes |
|---|---|---|---|---|
| — | *no submissions yet* | | | |

**Bounty bar (n=64): ≥ 111 points** — beat the published record of 110. The n=64 optimum is
genuinely open (112 was speculated by PatternBoost but never found).

### Market board — n = 16 (practice board, small bounty)

| Rank | Score | Submitter | Date | Notes |
|---|---|---|---|---|
| 1 | **27** | md (platform solver org) | 2026-07-30 | Seed entry — SLS + fixed-size annealing; verified VALID |
| 2 | 22 | Relativity Research Circle | 2026-07-28 | Exhibition entry (format demo; verified VALID) |

**Bounty bar (n=16): beat 27.** Practice/format board — n ≤ 32 optima are SAT-proven in the
literature, so this board demonstrates search and submission flow, not open records.

Full living board: [`LEADERBOARD.md`](LEADERBOARD.md).

### Published records — the numbers to beat

Best published constructions, per grid size `n` (`f(n)` = max points in `{0,…,n−1}²` with
no three forming an isosceles triangle, degenerate/collinear triangles **included**):

| n | Record | How | Source |
|---|--------|-----|--------|
| ≤ 32 | optimal known | SAT solvers find + prove optimal | PatternBoost 2024 [1] |
| 64 | **110** | 108 by classical search → 110 with one transformer loop (112 speculated, never found) | PatternBoost 2024 [1] |
| 100 | **160** | 154 by classical search → 160 with a transformer loop (optimum est. ~176) | PatternBoost 2024 [1] |

Beat a record for a given `n` and your construction — not the citation — wins the bounty.
The growth rate of `f(n)` is **open**: even an `n^{1.99}` upper bound is unproven, which is
why the proof tier is a genuinely hard target.

**Citations**

- **[1]** M. Charton, J. Ellenberg, A. Z. Wagner, G. Williamson. *PatternBoost: Constructions
  in Mathematics with a Little Help from AI.* 2024. arXiv:2411.00566.
  The problem was asked independently by **Chai Wah Wu**, by **Ellenberg–Jain**, and possibly
  by **Erdős**; PatternBoost holds the current records above and fixes the convention this
  board uses (`a,b,c ∈ S distinct ⟹ d(a,b) ≠ d(b,c)`, flat triangles included).

> **Note.** AlphaEvolve (arXiv:2506.13131) did **not** work this problem — its combinatorics
> results are Erdős's minimum-overlap and sum/difference sets. Do not attribute any record here
> to it. The mathematical problem itself is not owned by anyone (a fact, not an expression).

## What's here

- **The task:** [`TASK.md`](TASK.md) — statement, convention (locked), bounty tiers, leaderboard, records.
- **The canonical checker:** [`check.py`](check.py) — exact integer apex-scan; the arbiter.
- **Reference baseline:** [`generator_example.py`](generator_example.py) — a valid (non-record) construction, per n.

## How to submit (object tier)
1. **Fork** this repo (you do **not** get write access — that's the point).
2. Add your set as `submissions/<your-handle>.json`:
   ```json
   {"n": 64, "points": [[x, y], ...]}
   ```
3. Open a **pull request**. GitHub Actions runs `check.py` on your file and reports
   **VALID (with score)** or **INVALID (with a witness)** as a PR check.
4. A maintainer merges valid, record-beating submissions. **Only maintainers can change `main`**
   — submitters cannot make uncontrolled changes.

Run it yourself first: `python3 check.py submissions/your-handle.json`.

## Access model
- Hosted in an org so access is controlled.
- Submitters contribute via **forks + PRs** — read-only to the source of truth; forks cannot push to `main`.
- **Object tier only** in this repo (JSON point sets, verified as data — safe to run on untrusted PRs).
  Generator/proof tiers run in the platform's sandbox, not here (running untrusted *code* in CI needs isolation).
