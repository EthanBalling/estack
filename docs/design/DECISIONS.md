# Approved decisions

Approved 2026-10-30. This records rationale; linked specifications own detailed behavior.

- **Two independent skills:** Workspace setup/migration and routine memory capture have different scopes. Keep them separate; memory capture never invokes migration. See [skill contracts](README.md).
- **Minimal router and lazy resources:** Reduce automatic context overhead without hiding essential safety. Optional concepts replace a mandatory record set. See [architecture](ARCHITECTURE.md).
- **Normalize during migration:** Move agent operational resources into the established architecture rather than preserve fragmented legacy placement. Keep conventional human/source/output locations and genuine nested ownership. See [migration](MIGRATION.md).
- **Implied mutation authority:** Explicit mutating operations authorize routine restructuring/deletion within scope. Preserve governing meaning and a recovery path instead of adding repeated approval gates. See [migration](MIGRATION.md).
- **Selective, evidence-based continuity:** Preserve meaningful context, allow warranted new records and no-ops, and keep handoffs small. Context utilization is advisory, not a reset rule. See [context policy](CONTEXT.md).
- **Minimal conflict handling:** Fresh reads, narrow edits and reporting unresolved conflicts provide useful protection without mandatory queues, locks or extra directories. See [context policy](CONTEXT.md).
- **Harness-agnostic core:** Use portable project files; optional discovery adapters address demonstrated gaps. Do not guarantee universal auto-loading. See [portability](PORTABILITY-VALIDATION.md).
- **Implementation tools remain open:** Specify deterministic outcomes and focused scenarios, without prescribing Python or another toolchain. See [validation](PORTABILITY-VALIDATION.md).
- **Preserve Git and privacy boundaries:** No automatic Git setup, tracking changes or publication. Keep raw audits/session material outside distributable content. See [migration](MIGRATION.md).

Global skill curation is separate from workspace migration and memory capture.

## Pilot follow-up alignment — 2026-10-30

Approved clarifications to migration scope and routine memory maintenance. These define the target behavior; implementation status is described in the [design overview](README.md).

- **Whole-directory assessment:** Migration covers all appropriate agent records and artifacts throughout the selected directory, not only root instructions and memory. Explicit dispositions prevent a narrow edited-file preservation check from being mistaken for complete restructuring. See [migration scope](MIGRATION.md).
- **Purpose-based ownership:** Classify internal reports, evidence, scripts and working resources by purpose/audience, not AI authorship, filename or their presence in `files/` or `scratch/`. Preserve conventional locations for actual user deliverables and project/source material. See [architecture](ARCHITECTURE.md).
- **Disruptive organization, adaptive forms:** Replace obsolete local organizational conventions when needed to normalize agent resources under `.agents/`, while preserving substantive safety/domain meaning and external boundaries. Choose files versus directories from actual content rather than flattening everything into `[TYPE].md`; appropriate non-Markdown artifacts remain supported. See [architecture](ARCHITECTURE.md) and [migration authority](MIGRATION.md).
- **Discoverable internal artifacts:** Keep appropriate agent working material and evidence within the selected architecture, with meaningful routes for other agents/threads but without default bulk loading. Preserve recovery protections; hidden placement is not deletion authority or access control. See [architecture](ARCHITECTURE.md).
- **Consolidation beyond moves:** Extract durable knowledge, reconcile demonstrably stale summaries and consolidate duplicated state while preserving useful history and recovery. An archive of every redundant version is not the goal. See [migration](MIGRATION.md).
- **Dependency-aware relocation:** Routine in-scope path repairs belong to migration; unsafe relocation requiring unrelated changes is a reported blocker or justified exception, not an invisible omission. See [migration](MIGRATION.md).
- **Aliases by demonstrated need:** Update in-scope references and routing rather than preserving every old path. An unavoidable compatibility alias needs a known consumer and removal condition; external shared tooling remains outside scope. See [migration](MIGRATION.md).
- **Git contents exempt; intact relocation allowed:** A nested checkout may move as a whole to an appropriate location without internal restructuring or changes to Git state. Verify that relocation preserves its operation and location relationships; report blockers requiring internal or out-of-scope repairs. Selecting a repository root for its own agent-resource migration remains supported. See [migration](MIGRATION.md).
- **Routine memory maintains the organization:** Preserve purpose-based placement and concise discovery routes for useful new records without adding a migration or whole-directory audit to routine capture. Existing independent owners and no-op behavior remain supported. See [update-memory](UPDATE-MEMORY.md).

## Resource discovery alignment — 2026-10-30

- **Discovery stays in existing routes:** User selected keeping discovery information in `AGENTS.md`, `.agents/INDEX.md` and established task/topic routes. These pointers carry the read trigger, destination and ownership under the existing [architecture](ARCHITECTURE.md) and [context policy](CONTEXT.md). Do not introduce a new resource-header convention. Clear routes support selective retrieval without additional per-file metadata upkeep. This retains the current skill behavior; no header implementation is planned.
