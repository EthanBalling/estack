# Migration and safety

## Scope and authorization

Apply this procedure to requested initialization, migration and cleanup. Routine operations within an explicitly selected mutating scope carry implied authorization. Audit/validation remain read-only. Substantive changes to safety or standing behavior require user grounding/approval rather than being hidden inside restructuring.

Move all relevant agent operational resources to the [chosen architecture](ARCHITECTURE.md), including nested resources within scope. Keep human documentation, sources, code and deliverables in appropriate conventional locations. Preserve genuine domain workflows and governing instruction scope.

Inspect the whole selected directory for agent resources, including legacy `files/`, `scratch/`, hidden locations and nested operational artifacts. Folder labels do not exempt their contents from assessment. Inspect structure and sufficient content to classify each candidate group; expand around mixed ownership, uncertainty and dependencies without indiscriminately reading source libraries, generated dependencies or sensitive recovery payloads. Account for each candidate group as moved, split, consolidated, retained with justification, excluded by an explicit boundary, or unresolved. Preservation checks on edited files alone do not establish migration completeness.

An explicit migration permits disruptive organizational restructuring within scope, including replacement of obsolete placement/record-routing conventions and repair of affected local references. Do not preserve an indiscriminate legacy output location merely because old instructions prescribe it. This organizational authority does not weaken safety, privacy or substantive domain behavior, or extend to external owners.

Assess contents for consolidation and knowledge extraction as well as relocation. Put durable lessons in their authoritative owners, reconcile demonstrably superseded summaries against evidence, and separate useful historical execution evidence from current task state. Retain useful history; do not create an archive merely to keep every redundant version. Removal remains subject to the preservation and recovery checks below.

Repair routine in-scope path dependencies in agent scripts and their consumers as part of restructuring. Before moving working environments or recovery bundles, check path assumptions, permissions, symlinks and restoration references. If safe relocation requires unrelated infrastructure changes, tool installation or uncertain reconstruction, report the affected group as blocked or explicitly retained with its reason. Do not silently omit it or claim that portion complete. Git-specific scope remains a separate boundary.

Repair old paths and local routing instructions instead of automatically retaining legacy aliases. Keep an alias only for a demonstrated consumer that cannot yet be updated; record the dependency and the condition for removing the alias. Dependencies on shared tooling outside the selected scope require reporting, not unrequested edits to that tooling.

Treat nested Git repository contents, external symlink destinations and sibling projects as separate boundaries requiring explicit inclusion before internal modification. A nested checkout may be relocated intact to an appropriate location within the selected workspace as part of restructuring; that does not authorize migration of its internal files. Classify its purpose rather than automatically placing every repository under `.agents/`. Preserve its complete internal structure, tracked/untracked/ignored content, dirty work and Git state. Check location dependencies before and after, including Git metadata pointers, worktree/submodule relationships and relevant external consumers. If intact relocation cannot preserve operation without internal or out-of-scope changes, report the blocker rather than altering Git administration or leaving a broken checkout. Git administrative data may travel as part of an intact directory; never reorganize it independently. An explicitly selected repository root can have its own agent resources migrated under the ordinary Git safeguards.

Resolve paths and affected ancestors before writes; discovering a pointer is not authorization to modify its destination. Preserve relevant external references and report machine-specific dependencies that cannot be resolved within scope. A skill's source/distribution repository is a separate owner, not an implicit migration target or a place for private workspace records.

## Procedure

1. **Inspect:** Identify actual owners, mixed documents, competing instructions, privacy/export rules, symlink targets and unrelated or uncommitted changes. Historical tasks and approvals are evidence, not a backlog to execute.
2. **Map:** Assign affected content to authoritative destinations. Resolve meaningful contradictions from evidence or ask when a decision is necessary. Separate useful knowledge from superseded wording and source material.
3. **Protect recovery:** Before destructive rewriting or removal, verify that the affected original content is recoverable. An exact existing version or protected private copy can suffice; Git does not recover arbitrary uncommitted content. Keep protection proportional to affected changes rather than duplicating the whole workspace automatically. Choose protected storage and define temporary recovery's exit condition before creating it; no directory name or permanent target-local recovery area is required. Record recovery location/method without exposing private data. Keep recovery artifacts outside auto-loaded or published paths. If recovery is unavailable, do not perform the destructive portion.
4. **Transform:** Move, split and consolidate operational resources. Preserve meaningful knowledge, required instructions, provenance and domain procedures. Repair paths, anchors and conditional pointers. Preserve unique sources, deliverables, native history and unrelated data.
5. **Remove superseded records:** Delete duplicates or obsolete operational files only after useful content has a verified owner, references are repaired and recovery exists. Age, scratch placement and similarity alone are insufficient evidence for deletion.
6. **Verify and report:** Check intended ownership, applicable instruction meaning, reference integrity, boundaries and privacy. Report changed paths, checks, recovery details, unresolved issues and any needed follow-up. Do not claim full semantic or secret-safety certification.

## Temporary recovery and closeout

Recovery protects the transformation; it is not an indefinite-retention requirement. Distinguish operation-created temporary rollback copies, restore-test trees and intermediates from operational backups, useful evidence, original sources/history and unrelated user data. Existing exact versions and safe intact moves may avoid unnecessary copies.

After the selected scope passes coverage, semantic-preservation and mechanical validation, repair obsolete pointers and remove operation-created temporary material and empty containers once they hold no unique information, unresolved work or live dependency. Retain useful concise verification evidence at its private owner. Retain temporary recovery only for an explicit user/project rule or concrete unresolved rollback need, with a stated purpose, protected location and removal event/condition. Do not move or re-archive disposable material merely to keep it indefinitely.

This is ordinary closeout within the authorized mutating operation, not a separate cleanup approval gate. It does not authorize deleting recovery/evidence from earlier operations or operational backups. Failed/incomplete validation preserves necessary recovery and prevents claiming that portion complete. Read-only modes do not clean up. Preserving current meaning and operation differs from retaining the exact pre-migration layout for rollback.

## Git and private content

Support non-Git directories without initializing Git. Preserve existing system configuration. Migration invocation alone does not authorize changing the Git index, ignore/tracking rules, remotes or global settings, or committing/pushing.

Filesystem moves may produce unstaged deletions/new paths. Inspect and report them. If a move risks exposing private content through tracking or export behavior, resolve it within existing authorization or stop that portion and surface the conflict. Apply necessary exclusion changes only when separately authorized; otherwise preserve the privacy boundary rather than silently changing tracking. Do not stage files as part of migration.

Honor project export/submission rules and explicit do-not-save instructions. Recovery copies are private too. Never copy raw private audits, personal context or secrets into distributable templates or sanitized design examples.
