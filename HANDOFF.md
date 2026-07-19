# Handoff — StAnify

**Last updated:** 2026-07-19

## State

Rebuilt 2026-07-19 (commit `1670fcf`) with `docs/thesis.md` as the source of truth:

- **README.md**: research-grade — blinded-study results (64.4% preference, 270 evaluations, statistical tests), eight-agent architecture table + Mermaid orchestration diagram, cost/time analysis (~$0.15/concept, 17–25x), citation block. Deliberately states that this repo holds scaffold + documentation + thesis, with the experimental system described in the thesis — do not add claims of runnable production code.
- **docs/thesis.md**: the complete MSc thesis (committed verbatim; keep it byte-faithful — corrections belong in the README, not the thesis).
- Numbers convention: README matches the thesis exactly (64.4%, not the rounded 65% used in resume/portfolio copy).

## Pending

1. Thesis figures (`figure_5_1.png` etc.) are referenced in docs/thesis.md but the image files were never provided — add them to `docs/` if/when exported, or leave as-is (tables carry the data).
2. Optional: replace the toy `main.py` demo with the real agents.yaml/tasks.yaml configuration if the experimental code is ever cleaned for release — until then the README's honest framing stands.
