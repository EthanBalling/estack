---
name: agent-workspace
description: Initialize, audit, migrate, validate, or explicitly clean up a project's agent records and artifacts. Use for AGENTS.md routers, organizing .agents resources, bloated instructions, or whole-directory workspace restructuring with knowledge preservation. Audit and validate are read-only; migration requires a selected mutating scope.
---

# Agent workspace

1. **Resolve scope.** Identify the target and operation from the request. Inspect actual paths, ancestors, governing instructions, hidden resources, owners, symlinks, nested repositories, and privacy/export rules. If Git exists, inspect status and the index without changing either. Git is optional; never initialize it. A bare invocation with unclear intent authorizes inspection, not destructive work.
2. **Map ownership.** Read [layout](references/layout.md) for initialization or structural assessment. Read only relevant existing context, including applicable prerequisites. Assess the whole selected directory, including legacy containers and mixed artifacts, by purpose and audience. Preserve domain instructions. For audit/migration, follow the coverage procedure in [migration safeguards](references/migration.md): every candidate group needs a disposition or explicit boundary/unresolved choice, beyond the edited-file list.
3. **Perform the selected mode.** Use the table below. Explicit mutating requests authorize routine scoped edits, moves, and removal with recovery; ask only about consequential unresolved choices. Before substantial changes in any mode, read the [migration safeguards](references/migration.md). For meaningful setup uncertainty, consult an available `grill-with-docs` or `grilling` skill selectively. If unavailable, ask the smallest useful question about purpose, boundaries, or ownership directly. Clear requests need no interview.
4. **Verify and report.** Follow [validation](references/validation.md). Report changed paths or read-only findings, actual checks, recovery location, uncommitted changes, and unresolved limits. An already suitable workspace may require no writes.

| Mode | Procedure |
| --- | --- |
| Initialize | Create only justified missing resources from supplied purpose and actual content; use [layout](references/layout.md). Preserve an existing router. |
| Audit | Evaluate instructions, knowledge, ownership, duplication, stale claims, navigation, scope, loading cost, and compatibility using [validation](references/validation.md). Leave target content unchanged. |
| Migrate | Read and follow [migration](references/migration.md) before writes. Restructure agent records and artifacts by purpose; consolidate knowledge, preserve meaning, and repair dependencies and discovery routes. |
| Validate | Apply [validation](references/validation.md) read-only; separate errors, heuristic warnings, and semantic review. |
| Cleanup | Only when explicitly requested, consolidate superseded operational records using the full [migration](references/migration.md) safeguards. Age alone never justifies deletion. |

Keep actual source/product code, human documentation, and user deliverables in appropriate conventional locations; classify internal working code by purpose. Workspace organization is not authorization to execute backlogs, modify unrelated code/infrastructure, install skills/tools, or manage sessions. Never automatically stage, commit, push, change tracking/ignore rules, remotes, or global settings. Never modify existing skill installations as a workspace operation.
