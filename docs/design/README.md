# estack design

Approved 2026-10-30. This specification defines two independent Agent Skills for portable, lightweight project continuity.

The approved [migration scope expansion](DECISIONS.md#pilot-follow-up-alignment--2026-10-30) covers whole-directory restructuring, purpose-based artifact ownership, adaptive files/directories, discoverable internal working resources, dependency-aware moves and routine memory maintenance. The skill packages implement this expansion; see the repository [validation guidance](../../README.md#validate) for exercised checks and limits. Persistent-workspace migration remains a separate operation; synthetic validation does not certify a future migration.

The approved [legacy workflow replacement choices](DECISIONS.md#legacy-workflow-replacement-alignment--2026-10-30) add read-only familiarization, safe initialization detail and an optional section reader. The packages implement these choices and have synthetic validation. Installation and local workflow retirement are separate authorized operations requiring replacement delivery, consumer repairs and recovery verification; private delivery records own host-specific status.

Read the document relevant to the work:

- [Architecture](ARCHITECTURE.md): project layout, resource taxonomy and ownership.
- [Context policy](CONTEXT.md): selective loading, memory, handoffs and concurrent edits.
- [agent-workspace](AGENT-WORKSPACE.md): familiarization, initialization, audit, migration, validation and cleanup contract.
- [update-memory](UPDATE-MEMORY.md): selective session capture contract.
- [Migration and safety](MIGRATION.md): scope, recovery, restructuring and deletion.
- [Portability and validation](PORTABILITY-VALIDATION.md): packaging, compatibility and acceptance scenarios.
- [Approved decisions](DECISIONS.md) and [glossary](GLOSSARY.md).

Shared policy is authoritative in these documents; individual skill specifications reference it rather than repeat it. Raw audits, temporary handoffs and scratch material are private local artifacts, excluded from distribution.

Implementation tools remain open. These specifications are distinct from executing a migration, installing skills, publishing a repository or managing native sessions; each operation requires its own applicable authorization.
