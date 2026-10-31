# Validation

Familiarize, audit and validate are read-only. Familiarize uses its [bounded readiness verification](familiarize.md#verify-and-report-readiness), not a whole-directory structural check. Put any requested report outside target content or return it in conversation. Evaluate only the selected scope, without following symlinks or entering nested repositories unless separately included.

## Coverage and completeness

For audit/migration, reconcile the whole-directory assessment with the disposition map: include legacy/hidden containers, mixed bundles, internal non-Markdown artifacts and unmodified candidate groups. Each group needs a destination, justified retention, explicit boundary exclusion or unresolved status. Inspect enough content to support classifications without opening protected payloads unnecessarily. Check that actual deliverables/source remain appropriately placed and internal working/evidence/recovery groups have concise discovery routes.

Report coverage separately from the list of edited files. A preserved root router and passing links cannot establish completeness; unresolved or blocked groups remain incomplete with an exact next action or needed decision. Do not silently convert a blocker into a boundary exclusion.

## Mechanical checks

- Check file/directory collisions, actual path containment and excluded boundaries.
- Check local links, anchors, and conditional pointers in affected instructions, indexes, and resources; report external references without claiming they were verified.
- Count router words as a bulk warning, preserving necessary instructions.
- For migration/cleanup, compare exact originals with recovery copies, inspect Git index/dirty-work preservation, and resolve every item in the preservation map.
- Verify moved script consumers, environment paths, permissions, symlinks and restoration references. For intact checkouts compare complete content and Git state/operation before and after; check metadata pointers and location relationships without internal repairs.
- Repeat a suitable operation: unchanged content needs no new timestamps, summaries, backups, or scaffolding.

An optional read-only helper checks ordinary inline Markdown links and ATX heading anchors in `AGENTS.md` and `.agents/**/*.md`:

```sh
python3 <installed-skill-directory>/scripts/validate_workspace.py <project-target>
```

The helper reads all Markdown in those locations, including internal artifact groups. Use focused file checks instead when protected or irrelevant Markdown should remain unread.

Resolve the script relative to this skill, not the current working directory. Python 3.9+ is needed only for this helper. With no Python, perform equivalent focused file checks using available tools; skill operation has no prescribed runtime. The helper reports boundary references without reading their destinations, skips nested repositories/symlinks, and warns about unsupported reference-style links. It does not parse arbitrary Markdown, check prose/backtick paths, fetch URLs, or assess whole-directory coverage, artifact purpose, dependency safety or semantic preservation. A clean result does not certify a migration. Check those manually when affected. Exit 1 means errors, 0 means no mechanical errors; warnings still require judgment.

## Semantic review

Check that essential purpose, safety, approval rules, source/date, meaningful knowledge, workflows, and genuine nested ownership survived. Ensure each fact/state item has one owner; handoffs and indexes route rather than duplicate. Check evidence labels: observation, user report, source claim, proposal, inference, accepted decision. Old tests are dated evidence, not current health. Record accessible-history gaps without claiming full recovery.

Review extracted knowledge and reconciled summaries against source evidence, including useful historical context and source/date. Confirm obsolete organization was replaced where warranted without weakening domain/safety meaning. Verify file/directory choices fit retrieval, and artifact routes find useful groups without a mandatory matrix, redundant archives or blanket aliases.

Check that startup stays selective, resources have useful content, and generated documentation is tool-agnostic. Read only material needed for the task and applicable prerequisites. Confirm no unnecessary adapters, hooks, background services, automatic audits, or mandatory skill dependencies were introduced.

Mechanical success does not prove semantic preservation, secret absence, exhaustive history recovery, native auto-loading, live reload, or concurrent-write safety. Report actual evidence and limits separately.
