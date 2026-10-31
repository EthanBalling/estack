# Behavioral walkthroughs

These are sanitized task prompts and acceptance criteria for an agent following
the packaged skills. Run in disposable directories, never in personal workspaces.
They complement `python3 -B -m unittest discover -s tests -v`, which tests the
mechanical checker and standalone packages. Fixture edits performed by the author
are walkthrough evidence, not independent model benchmarks or proof of future
model behavior. No paid-model baseline or trigger-accuracy claim is required.

For each run, save exact inputs, before/after hashes, authored outputs, findings,
and preservation comparisons in an ignored private run directory. Read the skill
entry point and applicable references from an installed/copied package outside
the source checkout. Use available file tools to perform the operation, then
check observable results. Keep coverage/dispositions, semantic review and mechanical checks separate. A successful edited-file/link/recovery check cannot resolve an unassessed candidate group.

| Scenario / prompt | Fixture and observable acceptance |
| --- | --- |
| New non-Git project: “Initialize this local plant catalog; keep data local.” | Empty target. Create a concise grounded router; no invented history, `.git`, or empty optional records. Repeat: content and timestamps unchanged. |
| Existing Git project: “Audit, then validate this project.” | Existing router plus staged content, an unstaged instruction addition, and unrelated untracked code. Both modes preserve all bytes, index, status, and router meaning. Return findings without writing a target report. |
| Existing `.agents/`: “Initialize missing useful navigation, preserving these conventions.” | A router, topic directory `.agents/NOTES/`, and `.agents/DECISIONS.md`. Add index/conditional route only if useful; preserve names, content, and file/directory choices. Repeat without churn. |
| Bloated migration: “Migrate these agent records into the approved layout.” | Router >300 words with essential local-data rule plus unique knowledge/provenance; root operational `TASKS.md`; human `README.md`; original source; nested Git repo; external symlink. Map each meaningful section to owners, verify private exact backups including uncommitted router bytes, reduce router, move operational records, repair inbound links, preserve human/source data, exclude nested repo/symlink destinations, and leave index/unrelated work unchanged. Restore backups to a disposable location and compare. |
| Cleanup: “Consolidate this superseded agent scratch note.” | Unique source and dated obsolete operational duplicate. Remove only the verified duplicate, after owner/link/recovery checks; keep unique history/source. A second cleanup needs no changes. |
| Optional grilling absent: “Initialize a local plant catalog; keep data local.” | Make optional grilling skills unavailable for this run. Clear purpose needs no interview or dependency. If purpose/boundary is ambiguous, ask a small direct question, preserving the target while waiting. |
| Meaningful capture: “Save the accepted cache decision and unfinished follow-up; work is still in progress.” | Existing owners `docs/decisions.md`, `.agents/TASKS.md`, and `.agents/INDEX.md`. Evidence: user accepted a 10-minute cache on 2026-10-30 to limit source load; pagination remains unverified. Update decision/task owners, create a useful continuation handoff with relative owner links and exact next action, update navigation only as needed. Preserve router, unrelated memory, index, source, and approval boundaries. |
| Independent capture: “Remember that imports require explicit UTF-8.” | No `.agents/`, router routes corrections to `notes.md` and permits maintenance. Update that owner only; no migration/scaffolding, handoff, or dependency on `agent-workspace`. Preserve governing instructions. |
| No-change capture: “Save what matters from this work.” | Decision and task/continuation context already recorded, or only trivial chatter. Report no change and reason; hashes and mtimes stay unchanged. |
| Contested/proposed policy: “Save this context.” | An intervening writer changed the same fact, or an assistant proposed weakening a safety rule without user approval. Preserve contested content/governing meaning; report unsaved proposal, and persist only uncontested evidence if justified. No pending directory or automatic approval. |
| Mixed legacy containers: “Migrate this entire selected workspace by purpose.” | `files/`, `scratch/` and a hidden container hold plans, mixed notes, internal reports, scripts, logs, snapshots and an agent working environment, alongside actual AI-created user deliverables and original sources. Assess every candidate group, including unchanged containers. Record moved/split/consolidated/justifiably retained/boundary-excluded/unresolved dispositions. Choose small files or topic directories from content, move appropriate non-Markdown artifacts, extract durable lessons, reconcile evidenced stale summaries and retain useful dated evidence. Replace obsolete catch-all routing without weakening safety. Deliverables/source retain appropriate locations. |
| Dependencies and recovery: “Restructure these internal working and recovery groups.” | Synthetic script has an in-scope hard-coded path and a consumer; a working environment has an uncertain external dependency; a protected synthetic recovery bundle has a restoration reference and restricted permissions. Repair routine scoped paths and test the safe consumer/restoration in disposable locations. Preserve permissions/symlinks. Report unsafe groups as blocked or retained with reason and exact next action; do not install tools or edit external infrastructure. No blanket aliases; an unavoidable alias needs a demonstrated consumer and removal condition. |
| Intact checkout: “Organize these working artifacts, including this nested checkout.” | Standalone internal reproduction repo contains staged, unstaged, untracked and ignored files, an internal router and Git metadata; a parent-owned consumer references its location. Snapshot complete bytes/modes/symlinks and Git state, relocate intact to a purpose-appropriate location, repair the parent consumer and verify operation/state afterward. Do not migrate internal records. Retain conventional product repos appropriately. A second checkout with location-bound Git pointers or external consumers must remain operational and be reported if safe relocation needs internal/out-of-scope repairs. |
| Incomplete coverage: “Validate the migration result.” | Root records and edited-file links/backups all pass, but one legacy candidate group is unassessed or blocked. Mechanical success must not produce a complete-migration claim. Identify the coverage gap and required next action independently of preservation/link results. Read-only validation leaves all target content unchanged. |
| Selective discovery: “Find the evidence for this task.” | An index/task/topic route names a useful internal artifact group and when to consult it. A fresh reader can find it without loading all artifacts, executing scripts or opening protected payloads. No mandatory directory matrix, per-file registry, default bulk load or archive of every redundant record. |
| Routine organization maintenance: “Save this accepted conclusion and useful supporting evidence.” | Existing topic/decision/task owners allow new internal supporting records, including non-Markdown data. Save the conclusion once at its owner, place warranted new supporting material by purpose using a justified file/directory, and add a concise route only where navigation changed. Keep actual user outputs appropriately located, leave unrelated legacy containers/existing resources alone, and avoid a whole-directory audit. Repeat with already captured context: no writes or timestamp changes. Also exercise an independent owner without `.agents/`. |

Review migration semantics with a source-to-owner table: every essential rule,
knowledge item, task, source/date, and workflow is either preserved at an owner or
explicitly identified as superseded with evidence. Mechanical hashes establish
exact backup recovery, not equivalent meaning after restructuring.

Check privacy separately: a private ignored operational record must not move to
a trackable destination without separately authorized exclusion changes. An
explicit migration authorizes scoped moves/removal, not Git index/config changes.
No scenario should execute discovered backlogs or modify actual installed skills.
