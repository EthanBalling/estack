# estack design

Approved 2026-10-30. This specification defines two independent Agent Skills for portable, lightweight project continuity. It authorizes a later implementation; the design session delivers documentation only.

Read the document relevant to the work:

- [Architecture](ARCHITECTURE.md): project layout, resource taxonomy and ownership.
- [Context policy](CONTEXT.md): selective loading, memory, handoffs and concurrent edits.
- [agent-workspace](AGENT-WORKSPACE.md): initialization, audit, migration, validation and cleanup contract.
- [update-memory](UPDATE-MEMORY.md): selective session capture contract.
- [Migration and safety](MIGRATION.md): scope, recovery, restructuring and deletion.
- [Portability and validation](PORTABILITY-VALIDATION.md): packaging, compatibility and acceptance scenarios.
- [Approved decisions](DECISIONS.md) and [glossary](GLOSSARY.md).

Shared policy is authoritative in these documents; individual skill specifications reference it rather than repeat it. Raw audits, temporary handoffs and scratch material are private local artifacts, excluded from distribution.

Implementation tools remain open. No skill implementation, installation, workspace migration, global skill cleanup, repository publication or native session management is part of this deliverable.
