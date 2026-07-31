# Deterministic checker for the no-isosceles boards — sandboxed runner image.
# Build context needs only check.py. No network, no writes at runtime (enforced
# by the run flags in run-checker.sh; the image itself has no extra packages).
FROM python:3.12-slim
WORKDIR /task
COPY check.py /task/check.py
USER 65534:65534
ENTRYPOINT ["python3", "/task/check.py"]
