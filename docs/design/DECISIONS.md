# Approved decisions

Approved by the user on 2026-10-30 after audit and two alignment rounds. This records rationale; linked specifications own detailed behavior.

- **Two independent skills:** Workspace setup/migration and routine memory capture have different scopes. Keep them separate; memory capture never invokes migration. See [skill contracts](README.md).
- **Minimal router and lazy resources:** Reduce automatic context overhead without hiding essential safety. Optional concepts replace a mandatory record set. See [architecture](ARCHITECTURE.md).
- **Normalize during migration:** Move agent operational resources into the established architecture rather than preserve fragmented legacy placement. Keep conventional human/source/output locations and genuine nested ownership. See [migration](MIGRATION.md).
- **Implied mutation authority:** Explicit mutating operations authorize routine restructuring/deletion within scope. Preserve governing meaning and a recovery path instead of adding repeated approval gates. See [migration](MIGRATION.md).
- **Selective, evidence-based continuity:** Preserve meaningful context, allow warranted new records and no-ops, and keep handoffs small. Context utilization is advisory, not a reset rule. See [context policy](CONTEXT.md).
- **Minimal conflict handling:** Fresh reads, narrow edits and reporting unresolved conflicts provide useful protection without mandatory queues, locks or extra directories. See [context policy](CONTEXT.md).
- **Harness-agnostic core:** Use portable project files; optional discovery adapters address demonstrated gaps. Do not guarantee universal auto-loading. See [portability](PORTABILITY-VALIDATION.md).
- **Implementation tools remain open:** Specify deterministic outcomes and focused scenarios, without prescribing Python or another toolchain. See [validation](PORTABILITY-VALIDATION.md).
- **Preserve Git and privacy boundaries:** No automatic Git setup, tracking changes or publication. Keep raw audits/session material outside distributable content. See [migration](MIGRATION.md).

The design-only session stops after these specifications and a private implementation handoff. Existing custom skills and workspaces remain unchanged; global skill curation is separate.
