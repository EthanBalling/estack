# Portability, distribution and validation

## Packaging and compatibility

Deliver independent `agent-workspace` and `update-memory` Agent Skills, each with a focused `SKILL.md` and relative bundled references where needed. A suitable repository layout is `skills/<name>/SKILL.md`; implementation may refine supporting files without changing the skill contracts. Support normal `npx skills` installation using existing authentication/configuration. Installation, remote creation/publication and global-library cleanup are separate actions.

Generated project documentation uses ordinary Markdown and tool-agnostic responsibilities. No machine-specific paths, accounts, orchestration interfaces, models, provider commands or external skills are required for ordinary use. Preserve genuinely relevant project-specific tool instructions and disclose detail conditionally.

Instruction loading, skill discovery, context inheritance and live reload are separate capabilities. Do not assume supporting `.agents/` files load automatically, every harness reads the router, workers inherit it, running sessions reread edits, or separate checkouts share state. Confirm actual scope/loading when relevant; pass essential applicable constraints in bounded worker briefs when inheritance is uncertain.

Offer minimal optional adapters only for a demonstrated gap and selected harness, preserving a canonical source. No mandatory adapter layer. Recheck current authoritative documentation and relevant installed behavior before compatibility changes; documentation support alone is not a live-session guarantee. Native compaction/reset remains the active interface's responsibility.

## Validation approach

The implementation agent chooses suitable tools, language and focused test framework. No particular runtime, helper, parser, background service, hook or paid-model benchmark is prescribed.

Prefer a high-level seam: run a workspace operation or memory update against sanitized fixture content and inspect resulting files, preserved originals, references and reported outcomes. Test observable contracts rather than reproducing internal implementation. Use deterministic checks where possible; distinguish mechanical failures from semantic review findings and heuristic warnings.

Checks cover discoverable references, file/directory collisions, applicable containment, scope boundaries, ownership consistency, preserved required content, read-only behavior and useful reruns. Word counts can flag router bulk but cannot invalidate necessary instructions. Do not claim automatic checks prove secret absence, complete history recovery, actual native loading or race-free writes.

## Required acceptance coverage

- Empty initialization creates useful grounded instructions without empty scaffolding or invented history.
- Existing/cloned/Git/non-Git/learning/persistent projects are recognized without automatic Git setup.
- Audit and validation leave target content unchanged; mutating operations stay within authorization.
- Mixed documents and nested agent resources migrate into appropriate owners; nested repositories/external symlink destinations remain excluded unless explicitly included.
- Useful content, domain safety and provenance survive consolidation; references resolve; destructive changes have verified recovery, including uncommitted originals.
- Dirty/unrelated work, tracking/privacy conflicts and ambiguous owners are preserved or reported rather than silently overwritten.
- Repeating an operation on suitable content produces no unnecessary changes.
- Memory capture updates the correct owners, can create a warranted supporting record, and updates handoffs/indexes only when useful.
- Trivial or already captured context produces a no-op; contested writes preserve intervening content and report unsaved proposals.
- Neither skill depends on a particular harness, third-party skill or hard-coded implementation runtime. `update-memory` performs no Git publication, workspace migration or session lifecycle action.

Use synthetic fixtures instead of private workspaces. Purely semantic judgments can be exercised with focused documented scenarios; do not replace them with claims of deterministic proof or extensive model evaluation.
