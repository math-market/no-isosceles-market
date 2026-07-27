# No-Isosceles — a problem-market task (CI-as-verifier PoC)

A single **problem-market board**: find the largest no-isosceles set in the n×n grid.
Submissions are **verified automatically by GitHub Actions** — this repo is a proof of
concept for "the task is a repo; the checker is CI."

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
   (branch-protected) — submitters cannot make uncontrolled changes.

Run it yourself first: `python3 check.py submissions/your-handle.json`.

## Access model
- Hosted in an org so access is controlled.
- **`main` is branch-protected** — every change goes through a reviewed PR; no direct pushes.
- Submitters contribute via **forks + PRs** — read-only to the source of truth.
- **Object tier only** in this repo (JSON point sets, verified as data — safe to run on untrusted PRs).
  Generator/proof tiers run in the platform's sandbox, not here (running untrusted *code* in CI needs isolation).
