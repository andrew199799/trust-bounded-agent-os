# Current Task Context

## Project

Trust-Bounded Agent OS (TBAO)

## Current Stage

v0.1 public draft.

The repository currently defines TBAO as a conceptual framework, governance spine, and mock-only MVP design. It is not production-ready and must not be treated as a runtime for real systems.

## Current Objective

Prepare a lightweight three-party collaboration baseline before Action Spine MVP work begins.

This PR creates only the operational collaboration-control files needed to keep future work scoped, reviewable, and context-light. It does not implement the Action Spine MVP.

## Responsibilities

Human:

- Owns final meaning, priorities, approvals, and scope boundaries.
- Confirms when a task may create side effects or move beyond documentation.
- Decides when a phase is complete and when final evidence should be created.

ChatGPT:

- Helps shape task intent, phase structure, review expectations, and collaboration language.
- Keeps project framing aligned with TBAO doctrine and non-goals.
- Should avoid turning narrow implementation tasks into broad governance essays.

Codex:

- Reads `current-task-context.md` first for continuity.
- Avoids full-repository scans by default.
- Reads only the files needed for the current task.
- Makes narrow, reviewable changes.
- Uses PR body notes for intermediate status.
- Does not create evidence reports except at phase end.
- Does not add runtime, scheduler, worker, API, key, plugin activation, or execution-capable behavior without explicit human confirmation.

## Current PR Budget

Maximum 4 PRs for this phase.

PR 1 is limited to the lightweight collaboration baseline. Later PRs may prepare mock-only Action Spine MVP work only after this PR is reviewed or merged.

## Current Non-Goals

- No Action Spine MVP implementation in this PR.
- No runtime execution framework.
- No production plugin activation.
- No live API integration.
- No live keys or credential handling.
- No scheduler.
- No worker.
- No tests, scripts, package files, or build tooling.
- No evidence report, retrospective, or long governance essay.
- No production-readiness claim.
- No expansion into PET/KET, education product, OKX, trading, health, legal, or personal-data runtime scenarios.

## Files Allowed In This PR

```text
AGENTS.md
docs/development-log/current-task-context.md
docs/development-log/current-task-status.md
```

## Files Forbidden In This PR

All existing public-facing doctrine docs and all implementation surfaces are forbidden in this PR, including:

```text
README.md
docs/non-goals.zh-en.md
docs/action-spine-mvp.zh-en.md
docs/one-page-summary.zh-en.md
docs/position-paper.zh-en.md
docs/principles.zh-en.md
docs/glossary.zh-en.md
examples/
scripts/
src/
package files
tests
runtime files
artifact, evidence, or archive materials
```

## Validation Commands

Run:

```sh
git status --short
find . -maxdepth 3 -type f | sort
grep -R "production-ready" -n README.md docs AGENTS.md || true
grep -R "real credentials\|real funds\|external side effects" -n README.md docs AGENTS.md || true
```

Expected result:

- Only the three allowed files are added.
- No existing files are modified.
- Safety boundaries remain consistent with the current README.
- No implementation files are introduced.

## Stop Condition

Stop after PR 1 is created with the collaboration baseline only. Do not implement the Action Spine MVP in this PR.
