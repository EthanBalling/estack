---
name: agent-workspace
description: Initialize, audit, migrate, validate, or explicitly clean up a project's agent instructions and memory. Use for AGENTS.md routers, organizing .agents resources, bloated instructions, or preserving knowledge during workspace restructuring. Audit and validate are read-only; migration requires a selected mutating scope.
---

# Agent workspace

1. **Resolve scope.** Identify the target and operation from the request. Inspect actual paths, ancestors, governing instructions, hidden resources, owners, symlinks, nested repositories, and privacy/export rules. If Git exists, inspect status and the index without changing either. Git is optional; never initialize it. A bare invocation with unclear intent authorizes inspection, not destructive work.
2. **Map ownership.** Read [layout](references/layout.md) for initialization or structural assessment. Read only relevant existing context, including applicable prerequisites. Preserve useful conventions and domain instructions. Finish with an intended owner for every affected item, or a reported unresolved decision.
3. **Perform the selected mode.** Use the table below. Explicit mutating requests authorize routine scoped edits, moves, and removal with recovery; ask only about consequential unresolved choices. Before substantial changes in any mode, read the [migration safeguards](references/migration.md). For meaningful setup uncertainty, consult an available `grill-with-docs` or `grilling` skill selectively. If unavailable, ask the smallest useful question about purpose, boundaries, or ownership directly. Clear requests need no interview.
4. **Verify and report.** Follow [validation](references/validation.md). Report changed paths or read-only findings, actual checks, recovery location, uncommitted changes, and unresolved limits. An already suitable workspace may require no writes.

| Mode | Procedure |
| --- | --- |
| Initialize | Create only justified missing resources from supplied purpose and actual content; use [layout](references/layout.md). Preserve an existing router. |
| Audit | Evaluate instructions, knowledge, ownership, duplication, stale claims, navigation, scope, loading cost, and compatibility using [validation](references/validation.md). Leave target content unchanged. |
| Migrate | Read and follow [migration](references/migration.md) before writes. Normalize relevant operational resources, preserving meaning and repairing references. |
| Validate | Apply [validation](references/validation.md) read-only; separate errors, heuristic warnings, and semantic review. |
| Cleanup | Only when explicitly requested, consolidate superseded operational records using the full [migration](references/migration.md) safeguards. Age alone never justifies deletion. |

Keep source material, human documentation, code, and deliverables in their conventional locations. Workspace organization is not authorization to execute backlogs, modify unrelated code/infrastructure, install skills/tools, or manage sessions. Never automatically stage, commit, push, change tracking/ignore rules, remotes, or global settings. Never modify existing skill installations as a workspace operation.
