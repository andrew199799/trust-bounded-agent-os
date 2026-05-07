# AGENTS.md

Operational baseline for Codex collaboration in this public TBAO repository.

## Default Reading Scope

- Do not scan the full repository by default.
- Read `docs/development-log/current-task-context.md` first for task continuity.
- Then read only the files named by the current human request.
- Do not read archive, evidence, artifact, historical log, or unrelated material unless explicitly required for the task.

## PR Budget

- Each phase has a maximum budget of 4 PRs.
- Keep each PR narrow and reviewable.
- Use PR body notes for intermediate work status.
- Create final evidence only at the end of a phase, not for every PR.

## Side-Effect Boundary

- Side-effectful or execution-capable changes require explicit human confirmation before implementation.
- Do not add production plugin activation, live APIs, live keys, schedulers, workers, or runtime execution frameworks unless explicitly requested and confirmed.
- Preserve the TBAO v0.1 safety boundary:

```text
local-only
mock-only
non-executing
no real credentials
no real funds
no real external side effects
```

## Project Boundary

- Do not claim TBAO is production-ready.
- Do not expand a narrow task into PET/KET, education product, OKX, trading, health, legal, personal-data runtime, or other scenario work unless the human explicitly asks for it.
- Prefer concise operational docs over retrospective, evidence, or governance essays during active implementation phases.
