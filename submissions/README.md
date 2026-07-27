# Submissions

Add your submission here as `submissions/<your-handle>.json`, via a **pull request from your fork**:

```json
{"n": 64, "points": [[x, y], ...]}
```

- `n` — grid size (points must lie in `{0,…,n−1}²`, distinct).
- `points` — your no-isosceles set.

On your PR, GitHub Actions runs `../check.py` and reports **VALID (score)** or **INVALID (witness)**.
Run it locally first: `python3 check.py submissions/<your-handle>.json`.

Object tier only in this repo. Generator and proof submissions go through the platform (sandboxed).
