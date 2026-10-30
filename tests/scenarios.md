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
check observable results. Keep semantic review separate from mechanical checks.

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

Review migration semantics with a source-to-owner table: every essential rule,
knowledge item, task, source/date, and workflow is either preserved at an owner or
explicitly identified as superseded with evidence. Mechanical hashes establish
exact backup recovery, not equivalent meaning after restructuring.

Check privacy separately: a private ignored operational record must not move to
a trackable destination without separately authorized exclusion changes. An
explicit migration authorizes scoped moves/removal, not Git index/config changes.
No scenario should execute discovered backlogs or modify actual installed skills.
