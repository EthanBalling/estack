# Architecture and file taxonomy

## Problem and solution

Conversation history alone cannot provide durable, portable project understanding. Excessive startup documents also consume context without helping the current task. Use a small governing router and selectively retrieved project resources with explicit ownership.

## Layout

Keep `AGENTS.md` at its governing project or subworkspace scope. It primarily routes context and contains only essential identity, rules, safety boundaries, conventions, conditional pointers and brief continuity responsibilities. Aim for approximately 150–300 words or fewer in ordinary projects; preserve necessary instructions even when longer. Describe context preservation generically without requiring either named skill.

Agent operational resources belong under project-local `.agents/`. An empty project may need only `AGENTS.md`; create supporting resources when they have useful content. Prefer `.agents/INDEX.md` when multiple resources warrant navigation. Its entries identify when to read a resource, its location and its ownership. No separate registry, mandatory record-maintenance file or machine-readable manifest is required.

Human-facing documentation, source material, code and deliverables retain conventional locations. An agent index can reference their authoritative content without copying it. During migration, agent-specific operational records move into `.agents/`; existing mixed-purpose documents are split by purpose.

Classify by purpose and audience, not authorship, extension or existing folder name. Agent resources include operational records and artifacts: internal reports, execution evidence, supporting scripts, intermediate data and working environments require assessment alongside instructions and memory. An actual user deliverable can be AI-created; agent working code is not automatically conventional project/product code. Mixed-purpose bundles require content-level ownership decisions rather than blanket preservation of their current directory.

Appropriate internal working material, execution evidence and recovery artifacts belong within the selected `.agents/` architecture, subject to privacy, restoration and dependency constraints. Distinguish temporary work, retained evidence and protected recovery material without imposing a mandatory directory checklist. Keep them out of default context loads, but preserve a concise route through an established index, task, topic or other owner so another agent/thread can locate and use them when needed. Route useful groups or entry points rather than requiring a registry entry for every intermediate file; a route does not imply permission to read secret payloads or execute retained scripts.

## Optional concepts

Each concept may be a Markdown file, a directory of Markdown files, an appropriate authoritative existing document, or omitted. Combine concepts when separate records add no value. These are meanings, not a mandatory filename checklist.

Migration is active restructuring, not a mechanical mapping of existing files to `[TYPE].md`. Select a file or topic/type directory according to the actual content and retrieval needs; directories may contain appropriate non-Markdown agent artifacts. Preserve useful meaning rather than obsolete organizational conventions.

| Concept | Owns |
| --- | --- |
| GOAL | Intended outcome and success conditions |
| REQUIREMENTS | Accepted constraints and acceptance criteria |
| PLAN | Approach, dependencies and sequence |
| TASKS | Execution status, blockers and next action |
| STATE | Resumable operational state not already owned elsewhere |
| MEMORY | Durable preferences, corrections and cross-task lessons |
| NOTES | Topic knowledge and supporting evidence |
| DECISIONS | Accepted choices, reasons and consequential trade-offs |
| WORKFLOWS | Reusable project procedures |
| SYSTEM | Project-specific system context or architecture |
| SUB-AGENTS | Project-specific delegation constraints and ownership |
| HANDOFF | Concise continuation context and owner pointers |
| LOGS | Useful dated evidence or history, when needed |
| README | Human navigation of agent resources, when useful |

Default persistent handoff: `.agents/HANDOFF.md`. Task-specific handoffs are optional.

## Ownership and scope

Give each fact, decision and state item one authoritative owner. Indexes and handoffs point to that owner. Avoid empty templates and duplicate ledgers. Split large resources only when independent retrieval earns the extra navigation.

Use nested `.agents/` where a genuine course, topic or subworkspace owns context. Preserve applicable governing instruction scope. Nested repository contents and external symlink destinations are separate boundaries; an intact nested checkout may be relocated without migrating its internals under [migration policy](MIGRATION.md).
