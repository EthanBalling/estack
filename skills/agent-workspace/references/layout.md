# Layout and context

## Minimal router

Keep `AGENTS.md` at the actual governing project/subworkspace scope. Include essential purpose, safety, conventions, and conditional pointers. Generally aim for 150–300 words or fewer; preserve necessary governing meaning even if longer. Keep essential constraints visible before optional retrieval.

Supporting agent context belongs in project-local `.agents/`. Create `.agents/INDEX.md` when multiple resources warrant navigation: each entry states when to read, the relative path (optionally a stable heading), and what it owns. An empty project may need only `AGENTS.md`. Create no empty resources, invented profile, task history, or universal checklist.

Each concept may be a file, a directory, a combined record, an existing authoritative document, or absent:

| Concept | Owns |
| --- | --- |
| GOAL / REQUIREMENTS | Intended outcome, constraints, acceptance |
| PLAN / TASKS | Approach, dependencies, status, blockers, next action |
| STATE | Resumable state not owned elsewhere |
| MEMORY | Durable preferences, corrections, cross-task lessons |
| NOTES | Topic knowledge and evidence |
| DECISIONS | Accepted choices, reasons, trade-offs |
| WORKFLOWS / SYSTEM | Reusable procedures / system context |
| SUB-AGENTS | Project delegation constraints and ownership |
| HANDOFF | Continuation context and owner pointers |
| LOGS / README | Useful dated evidence / human navigation |

Retain useful existing names and file/directory forms. During migration move agent operational records into `.agents/`, splitting mixed documents by purpose; human/source/output documents remain conventional. Preserve genuine nested ownership and governing scope. Do not collapse domain workspaces into one root ledger.

## Generic continuity instructions

Adapt this example to actual purpose and resources; omit nonexistent pointers:

> Read supporting context only when relevant to the current task, including applicable safety constraints and prerequisites. Persist consequential discoveries, accepted decisions and reasons, corrections, and task state in their authoritative records during work. Freshly read before narrow edits; preserve intervening changes. Keep source/date and uncertainty when consequential. Maintain a concise continuation handoff when useful, pointing to detailed owners. Leave governing and safety meaning unchanged without approval. Keep secrets and information the user declined to save out of records.

Generated instructions describe responsibilities without naming skills or harnesses. Give each fact one owner; indexes and handoffs point there. Split large documents only when independent retrieval earns the navigation. A Markdown fragment is a locator, not proof that a reader bounded its output; include introductions, applicable constraints, descendants, and prerequisites, then expand if needed.

## Adaptive context hierarchy

Continue while current context helps; persist consequential knowledge/state; record continuation at meaningful transitions; compact through supported native mechanisms when useful; start fresh when task/history changes warrant it. Below roughly 50% utilization is an aspiration only when measurable and practical. Never fabricate utilization, force resets, or prescribe unsupported commands.

Discovery, instruction loading, inheritance, and live reload are distinct. Supporting resources do not automatically load. Verify the selected harness's actual behavior before offering a minimal optional adapter; retain one canonical source. When worker inheritance is uncertain, pass essential applicable constraints in bounded briefs. Separate checkouts and conversations do not synchronize through shared files.
