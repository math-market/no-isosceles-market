# No-Isosceles Sets in the Grid — Leaderboard

All **checker-valid** submissions to the market task are recorded here, record-breaking or
not. Ranked by score `|S|` per board (ties → earliest submission). Convention:
degenerate/collinear isosceles triples **count** (PatternBoost convention — see TASK).

## Market board — n = 16

| Rank | Score | Submitter | Date | Notes |
|---|---|---|---|---|
| 1 | **27** | md (platform solver org) | 2026-07-30 | Seed entry — SLS + fixed-size annealing, ~20 min CPU; verified VALID |
| 2 | 22 | Relativity Research Circle | 2026-07-28 | Exhibition entry (format demo; verified VALID) |

**Bounty bar (n=16): beat 27.**
⚠️ *Caveat:* PatternBoost (arXiv:2411.00566) reports **SAT-proven optima for all n ≤ 32**, so
the true `f(16)` is known in the literature. A submission that matches or beats 27 by
reproducing the published optimum is checker-valid and wins under the current rule — the task
owner may prefer to re-scope the bounty to a board with open records (n = 64, 100, 128) or
set the n=16 bar at the published optimum. Pending that decision, this bar stands.

## Published records (not market submissions)

| n | Record | Status | Source |
|---|---|---|---|
| ≤ 32 | optimal known | SAT-proven | PatternBoost 2024, arXiv:2411.00566 |
| 64 | 110 | open (112 speculated, never found) | PatternBoost 2024 |
| 100 | 160 | open (optimum est. ~176) | PatternBoost 2024 |

---

*Maintained by the task owner; updated as submissions are adjudicated. The verification
script (`check.py`) referenced from the live task is pinned to a specific commit; this
leaderboard is informational and deliberately lives at `main`.*
