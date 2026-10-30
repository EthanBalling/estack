# Validation

Audit and validate are read-only. Put any requested report outside target content or return it in conversation. Evaluate only the selected scope, without following symlinks or entering nested repositories unless separately included.

## Mechanical checks

- Check file/directory collisions, actual path containment and excluded boundaries.
- Check local links, anchors, and conditional pointers in affected instructions, indexes, and resources; report external references without claiming they were verified.
- Count router words as a bulk warning, preserving necessary instructions.
- For migration/cleanup, compare exact originals with recovery copies, inspect Git index/dirty-work preservation, and resolve every item in the preservation map.
- Repeat a suitable operation: unchanged content needs no new timestamps, summaries, backups, or scaffolding.

An optional read-only helper checks ordinary inline Markdown links and ATX heading anchors in `AGENTS.md` and `.agents/**/*.md`:

```sh
python3 <installed-skill-directory>/scripts/validate_workspace.py <project-target>
```

Resolve the script relative to this skill, not the current working directory. Python 3.9+ is needed only for this helper. With no Python, perform equivalent focused file checks using available tools; skill operation has no prescribed runtime. The helper reports boundary references without reading their destinations, skips nested repositories/symlinks, and warns about unsupported reference-style links. It does not parse arbitrary Markdown, check prose/backtick paths, fetch URLs, or inspect the entire source tree. Check those manually when affected. Exit 1 means errors, 0 means no mechanical errors; warnings still require judgment.

## Semantic review

Check that essential purpose, safety, approval rules, source/date, meaningful knowledge, workflows, and genuine nested ownership survived. Ensure each fact/state item has one owner; handoffs and indexes route rather than duplicate. Check evidence labels: observation, user report, source claim, proposal, inference, accepted decision. Old tests are dated evidence, not current health. Record accessible-history gaps without claiming full recovery.

Check that startup stays selective, resources have useful content, and generated documentation is tool-agnostic. Read only material needed for the task and applicable prerequisites. Confirm no unnecessary adapters, hooks, background services, automatic audits, or mandatory skill dependencies were introduced.

Mechanical success does not prove semantic preservation, secret absence, exhaustive history recovery, native auto-loading, live reload, or concurrent-write safety. Report actual evidence and limits separately.
