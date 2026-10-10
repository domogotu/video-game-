# Design Workflow: Step Completion, Dependency Gates, and Loop Prevention

**Project:** Lethal Absorption  
**Status:** Project workflow rule; applies to design work and future implementation planning.  
**Purpose:** Prevent circular rework, incomplete steps, premature expansion, and repeated verification of already-closed work.

## 1. Governing Rule

Work advances through a finite sequence of named steps. A step is not complete because a document was started, an idea was discussed, or a partial change was made. It is complete only when its defined deliverables and exit criteria are satisfied and recorded.

Once a step is marked **DONE**, do not reopen it casually. Reopen only when new evidence shows a defect, a dependency has changed, a contradiction is discovered, or the user explicitly requests a revision. Record the reason and impact before changing the status.

## 2. Required Status Values

Use exactly these statuses in plans and trackers:

- **NOT STARTED** — no work has begun.
- **IN PROGRESS** — work is actively being completed.
- **BLOCKED** — progress requires a specific missing decision, dependency, permission, or resource.
- **READY FOR REVIEW** — deliverables exist and the exit checklist has been run; a decision or review remains.
- **DONE** — all exit criteria are satisfied and the result is recorded.
- **DEFERRED** — intentionally postponed with a reason and a stated dependency or return condition.
- **REOPENED** — a previously completed step is being revisited for a documented reason.

Never use ambiguous statuses such as “mostly done,” “almost finished,” or “verified” without identifying exactly what was verified.

## 3. The Step-Completion Contract

Before starting a step, write down:
1. **Objective:** one sentence describing the result this step must produce.
2. **Inputs/dependencies:** the decisions, files, or prior steps it relies on.
3. **Deliverables:** the specific artifacts or decisions to produce.
4. **Exit criteria:** observable checks that determine completion.
5. **Out of scope:** work that must not be added to this step.
6. **Next step:** one named step that follows if this step passes.

At the end, report:
- What changed or was decided.
- The exact artifact(s) created or updated.
- Which exit criteria passed and which did not.
- Remaining blockers, if any.
- The next step, or the explicit reason work cannot proceed.

If any required exit criterion fails, keep the step IN PROGRESS or BLOCKED. Do not label it DONE.

## 4. Anti-Loop Rules

1. **One active step:** maintain one primary active step at a time. Related work can be noted as future tasks, but should not silently replace the active objective.
2. **No circular restarts:** do not restart at an earlier step merely because a later step exposes a new idea. Log the idea in the backlog and continue unless the new information invalidates a requirement.
3. **No repeated checking without cause:** once an artifact is verified, reuse the recorded result. Recheck only after a change, a relevant dependency change, a failure, or an explicit request.
4. **No endless “continue” expansion:** “Continue” means finish the currently active step against its exit criteria before inventing more scope.
5. **No scope creep during closure:** new ideas discovered during a step go into a labeled backlog, unless essential to pass that step's exit criteria.
6. **No silent substitutions:** if the planned deliverable cannot be produced, mark the step BLOCKED and explain the specific reason; do not replace it with a different artifact and claim completion.
7. **No false completion:** creating a specification does not mean gameplay is implemented; committing a file does not mean its contents are consistent with every other document; reading code does not mean it was executed or tested.
8. **Limit review passes:** perform one planned completeness pass, then one correction pass for issues found. If major unresolved issues remain, record them as blockers or create a targeted follow-up step rather than repeating the same broad review.
9. **Carry-forward ledger:** each response must preserve the current step, status, completed criteria, open blockers, deferred ideas, and next action in a durable project document or concise session summary.
10. **Close the loop explicitly:** every active step ends with DONE, BLOCKED, DEFERRED, or a clearly stated reason it remains IN PROGRESS. Do not leave the user guessing.

## 5. Change Control and Reopening a Step

A completed step may be reopened only if at least one condition applies:
- A contradiction with an accepted project rule is demonstrated.
- A deliverable is missing, incorrect, or fails its stated acceptance criterion.
- A dependency or platform constraint changes.
- A new decision makes the prior output invalid.
- The user explicitly asks for a change.

When reopening, record:
- Previous completion date/commit or artifact.
- Evidence or request that justifies reopening.
- Exact portion being changed.
- Whether downstream steps need revalidation.

Preserve valid prior work. Do not rewrite an entire system to correct a localized defect.

## 6. Project-Level Sequence

For gameplay/design work, use this order unless a documented dependency requires a change:

1. **Core loop** — establish the repeatable player experience and feedback.
2. **Vertical-slice boundaries** — choose the smallest representative area and systems that can validate the loop.
3. **Slice content and rules** — define the setting, species, player capabilities, resources, threats, and win/failure outcomes.
4. **System interactions** — specify ability combinations, absorption, evolution, and world-state effects used by the slice.
5. **UI and feedback** — define how players read risks, discoveries, costs, and progression.
6. **Edge cases and safeguards** — cover failure, exploit loops, persistent-state limits, multiplayer authority, and accessibility.
7. **Consistency review** — check the slice against existing design rules and log only actionable conflicts.
8. **Scope freeze** — record the accepted slice and move new ideas to backlog.
9. **Implementation handoff** — only after design gates pass, produce implementation tasks with explicit acceptance criteria.
10. **Verification** — after implementation, test the defined behaviors and record actual results separately from design approval.

Do not expand into a full catalogue, cosmic endgame, or every character-specific route while the core slice still has unresolved mandatory decisions.

## 7. Current Work Ledger

The following is the initial ledger based on the repository state reviewed for this workflow. Update it only when evidence supports a status change.

| Step | Status | Completion rule / next action |
|---|---|---|
| Core gameplay loop and player feedback | DONE — document created and fetched back from GitHub | Use as the baseline for the slice; reopen only for a documented conflict or explicit change request. |
| Define the first gameplay vertical slice | DESIGN SCOPE FROZEN | Scope includes the cellular teaching sequence, first evolution, compact animal habitat, one bounded predator-prey relationship, one diet-driven growth/condition change and adaptation clue, and explicit acceptance criteria. Numeric tuning remains for implementation evidence. |
| Specify slice systems and edge cases | NEXT — NOT STARTED | Convert the frozen slice rules into bounded system requirements and edge-case outcomes; do not add unrelated endgame systems. |
| UI/feedback for the slice | NOT STARTED | Define only the information needed to play and understand the slice. |
| Slice consistency and scope freeze | REVIEWED — DESIGN BASELINE FROZEN | One documentation consistency pass and correction pass recorded in MASTER_DOCUMENTATION_CONSISTENCY_AUDIT.md; runtime acceptance remains untested. |
| Implementation handoff | DEFERRED | This project is currently being focused on gameplay/design. Do not claim implementation or runtime verification. |

## 8. Definition of “Done” for a Design Step

A design step is DONE only if:
- Its objective and scope are explicit.
- All required decisions for this step are made or explicitly marked as approved open questions that do not block the next step.
- Deliverables exist in the repository when a durable artifact is required.
- Exit criteria have been checked against the actual artifact.
- Conflicts with governing design rules are resolved or recorded as blockers.
- The next step is identified.
- Status and evidence are recorded in the work ledger.

## 9. Required End-of-Step Report Format

Use this concise report:

**Step:** [name]  
**Status:** [one allowed status]  
**Completed:** [deliverables and criteria passed]  
**Not completed / blockers:** [specific items, or “None”]  
**Deferred ideas:** [backlog items, or “None”]  
**Next step:** [one named action]

Do not claim the overall project is finished when only one step or one document is complete.
