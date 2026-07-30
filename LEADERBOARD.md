# No-Isosceles Sets in the Grid — Leaderboard

All **checker-valid** submissions to the market tasks are recorded here, record-breaking or
not. Ranked by score `|S|` per board (ties → earliest submission). Convention:
degenerate/collinear isosceles triples **count** (PatternBoost convention — see TASK).

## Market board — n = 64 (OPEN RECORD — main bounty)

| Rank | Score | Submitter | Date | Notes |
|---|---|---|---|---|
| — | *no submissions yet* | | | |

**Bounty bar (n=64): ≥ 111 points** — beat the published record of 110 (PatternBoost,
arXiv:2411.00566; n=64 optimum is open). First checker-valid submission over the bar wins.

## Market board — n = 16 (practice board, small bounty)

| Rank | Score | Submitter | Date | Notes |
|---|---|---|---|---|
| 1 | **27** | md (platform solver org) | 2026-07-30 | Seed entry — SLS + fixed-size annealing; verified VALID |
| 2 | 22 | Relativity Research Circle | 2026-07-28 | Exhibition entry (format demo; verified VALID) |

**Bounty bar (n=16): beat 27.** Practice/format board: the n ≤ 32 optima are SAT-proven in
the literature (PatternBoost), so this board demonstrates search and the submission flow
rather than open records — hence the small bounty. The serious bounty is the n=64 board.

## Published records (not market submissions)

| n | Record | Status | Source |
|---|---|---|---|
| ≤ 32 | optimal known | SAT-proven | PatternBoost 2024, arXiv:2411.00566 |
| 64 | 110 | open (112 speculated, never found) | PatternBoost 2024 |
| 100 | 160 | open (optimum est. ~176) | PatternBoost 2024 |

---

*Maintained by the task owner; updated as submissions are adjudicated. The verification
script (`check.py`) referenced from the live tasks is pinned to a specific commit; this
leaderboard is informational and deliberately lives at `main`.*
