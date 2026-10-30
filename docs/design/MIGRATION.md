# Migration and safety

## Scope and authorization

Apply this procedure to requested initialization, migration and cleanup. Routine operations within an explicitly selected mutating scope carry implied authorization. Audit/validation remain read-only. Substantive changes to safety or standing behavior require user grounding/approval rather than being hidden inside restructuring.

Move all relevant agent operational resources to the [chosen architecture](ARCHITECTURE.md), including nested resources within scope. Keep human documentation, sources, code and deliverables in appropriate conventional locations. Preserve genuine domain workflows and governing instruction scope.

Treat nested Git repositories, external symlink destinations and sibling projects as separate boundaries requiring explicit inclusion. Resolve paths and affected ancestors before writes; discovering a pointer is not authorization to modify its destination. Preserve relevant external references and report machine-specific dependencies when they cannot be made local within scope. The estack distribution repository is excluded from the separately audited workspaces' migration targets.

## Procedure

1. **Inspect:** Identify actual owners, mixed documents, competing instructions, privacy/export rules, symlink targets and unrelated or uncommitted changes. Historical tasks and approvals are evidence, not a backlog to execute.
2. **Map:** Assign affected content to authoritative destinations. Resolve meaningful contradictions from evidence or ask when a decision is necessary. Separate useful knowledge from superseded wording and source material.
3. **Protect recovery:** Before destructive rewriting or removal, verify that the affected original content is recoverable. An exact existing version or protected private copy can suffice; Git does not recover arbitrary uncommitted content. Record recovery location/method without exposing private data. Keep recovery artifacts outside auto-loaded or published paths. If recovery is unavailable, do not perform the destructive portion.
4. **Transform:** Move, split and consolidate operational resources. Preserve meaningful knowledge, required instructions, provenance and domain procedures. Repair paths, anchors and conditional pointers. Preserve unique sources, deliverables, native history and unrelated data.
5. **Remove superseded records:** Delete duplicates or obsolete operational files only after useful content has a verified owner, references are repaired and recovery exists. Age, scratch placement and similarity alone are insufficient evidence for deletion.
6. **Verify and report:** Check intended ownership, applicable instruction meaning, reference integrity, boundaries and privacy. Report changed paths, checks, recovery details, unresolved issues and any needed follow-up. Do not claim full semantic or secret-safety certification.

## Git and private content

Support non-Git directories without initializing Git. Preserve existing system configuration. Migration invocation alone does not authorize changing the Git index, ignore/tracking rules, remotes or global settings, or committing/pushing.

Filesystem moves may produce unstaged deletions/new paths. Inspect and report them. If a move risks exposing private content through tracking or export behavior, resolve it within existing authorization or stop that portion and surface the conflict. Apply necessary exclusion changes only when separately authorized; otherwise preserve the privacy boundary rather than silently changing tracking. Do not stage files as part of migration.

Honor project export/submission rules and explicit do-not-save instructions. Recovery copies are private too. Never copy raw private audits, personal context or secrets into distributable templates or sanitized design examples.
