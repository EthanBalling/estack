# agent-workspace specification

## Problem and user outcomes

Projects need portable context structures without a fixed collection of boilerplate records. Existing agent resources need normalization without losing knowledge, domain instructions or unrelated work.

Users can initialize an empty directory, organize an existing or cloned project, migrate a learning/persistent workspace, inspect problems without changes, validate a result, and occasionally remove superseded operational records. Git is optional.

## Inputs and authorization

Resolve the selected directory and requested operation from the request and environment. Infer routine choices from actual content; ask only for consequential unresolved decisions. Use optional `grill-with-docs` or `grilling` when helpful and available, with a built-in interview fallback.

Supported operations:

| Operation | Observable behavior |
| --- | --- |
| Initialize | Create only useful missing router/resources grounded in supplied purpose |
| Audit | Inspect structure, instructions, ownership, duplication, staleness, compatibility and risks without editing target content |
| Migrate | Normalize relevant agent resources into the selected architecture |
| Validate | Check the selected structure and report findings without editing target content |
| Cleanup | Consolidate or remove superseded operational records under migration safeguards |

Explicit mutating requests imply authorization for routine creation, restructuring, edits and deletion within scope. Do not require repeated approval of normal steps. Substantive unresolved policy choices and out-of-scope actions remain subject to clarification. A bare invocation with unclear intent does not establish destructive scope.

## Procedure and completion

1. Discover the actual root, governing instructions, hidden resources, owners, Git/non-Git state, nested scopes, symlinks and privacy/export boundaries. Inspect targeted content rather than bulk-loading histories. Finish when scope and material constraints are known.
2. Map content to the [architecture](ARCHITECTURE.md). Identify conflicts, duplicates, stale summaries and relevant existing procedures. Assess the whole selected directory, including legacy operational containers and mixed artifact bundles, under the [migration scope rules](MIGRATION.md). Finish when each candidate resource group has an owner and disposition, an explicit boundary exclusion, or a reported unresolved choice; an edited-file-only map is insufficient.
3. For mutating operations, follow [migration and safety](MIGRATION.md). For read-only operations, report changes that would be needed without applying them.
4. Validate the result using [the acceptance contract](PORTABILITY-VALIDATION.md). Report changed paths, findings, actual checks, recovery information and unresolved limitations. An already suitable workspace may require no changes.

Do not execute discovered backlogs, install tools/skills, provision native sessions or impose a provider. Apply [context policy](CONTEXT.md) to generated instructions and resources. Global skill-library cleanup is separate work.

## Acceptance

Use observable filesystem/content outcomes and the scenarios in the shared validation contract. Initialization is useful without invented profile/history; read-only operations preserve target content; migration preserves required meaning and repairs references; cleanup has recovery evidence; reruns avoid gratuitous churn.
