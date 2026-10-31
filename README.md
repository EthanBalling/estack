# estack

Two independent [Agent Skills](https://agentskills.io/specification) for portable
project context:

| Skill | Use |
| --- | --- |
| [agent-workspace](skills/agent-workspace/SKILL.md) | Initialize, audit, migrate, validate, or explicitly clean up agent records and artifacts. |
| [update-memory](skills/update-memory/SKILL.md) | Save consequential context during work; maintain useful continuation pointers or report no change. |

The [approved design](docs/design/README.md) owns behavior and safety policy.
Each skill carries its own relative references and works without the other.
There are no hooks, background services, recurring audits, or mandatory external
skills. Existing custom skills are left intact.

The repository keeps `skills/` as the installable packages, `docs/design/` as
sanitized specifications and maintenance decisions, and `tests/` as reusable
validation. `AGENTS.md` guides contributions. Private audits, raw planning
material, migration backups and temporary handoffs belong under ignored
`.local/`; local environment files, dependency folders and generated artifacts
are also excluded by `.gitignore`. Each skill is self-contained and does not
require the repository's design documents or tests at runtime.

## Install

Use the [skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md)
with its supported Node.js version and existing Git/authentication configuration.
Consult the CLI documentation for installation prerequisites; installation
tooling is separate from runtime skill requirements.

From an absolute path to this checkout, install either or both skills globally:

```sh
npx skills add /path/to/estack --skill agent-workspace update-memory -g
```

Select the desired compatible agents interactively. For a noninteractive
installation targeting Codex, append `-a codex -y`. Omit `-g` for a project-local
installation. Select just one name after `--skill` for an independent install.
Inspect existing same-name installations before replacement; never remove other
skills as part of an update.

List installed skills and check source discovery:

```sh
npx skills list -g
npx skills add /path/to/estack --list
```

Additional machines can install directly from the existing remote:

```sh
npx skills add EthanBalling/estack --skill agent-workspace update-memory -g
```

For offline or local-source installation, transfer/clone the implemented source
to the other machine and use its absolute checkout path. Use existing
authentication; installation never requires changing repository visibility or
credentials.

## Update

Local-path installs are installed copies, not live source-checkout links.
After updating the checkout and reviewing changes, rerun the same local install
command to refresh only these skills. For remote-backed installations, use:

```sh
npx skills check
npx skills update agent-workspace update-memory -g
```

Confirm installer/version behavior with `npx skills --help`; avoid a blanket
update of unrelated skills. For manual installation without Node, copy one
complete `skills/<name>/` directory to the selected harness's documented skill
directory, preserving bundled resources. Recopy on update.

## Use

Invoke by name using the active agent's skill mechanism, or ask for the operation:

- “Use agent-workspace to initialize this project as a local plant catalog.”
- “Use agent-workspace to audit this repository without changing it.”
- “Use agent-workspace to migrate the agent records in this selected directory;
  preserve the knowledge, domain rules, and uncommitted work.”
- “Use agent-workspace to validate these instructions and references.”
- “Use agent-workspace to clean up these explicitly selected superseded notes.”
- “Use update-memory to save the accepted decision and unfinished next action.”

`AGENTS.md` remains a minimal context router, generally 150–300 words or fewer.
Useful supporting resources live under `.agents/`, with `INDEX.md` for nontrivial
navigation. Optional concepts can be files, directories, existing owners, or
absent. Initialization creates only grounded resources. Migration assesses the
whole selected directory, including hidden and mixed legacy containers. It restructures agent records and non-Markdown artifacts by purpose,
consolidates knowledge, repairs scoped dependencies and provides selective
routes to working material, evidence and protected recovery. Each candidate group
needs a disposition; unresolved portions remain incomplete. Actual deliverables
and source/product material retain appropriate locations. Nested checkouts may
relocate intact only when content, Git state and location relationships survive;
internal restructuring and Git repairs remain separately scoped.

Memory capture follows existing conventions, including projects without
`.agents/`. It updates authoritative owners, can create a warranted record, and
keeps handoffs separate from durable knowledge. Warranted new internal supporting
records follow established purpose-based placement and discovery, using files or
directories as needed. Routine capture does not relocate existing resources or
assess the whole directory. Already recorded or trivial context produces no writes. Neither skill automatically stages, commits, pushes,
merges, settles a thread, or executes a discovered backlog.

## Validate

Run the deterministic checks from the repository:

```sh
python3 -B -m unittest discover -s tests -v
python3 -B skills/agent-workspace/scripts/validate_workspace.py .
git diff --check
```

For a workspace outside the checkout, run the installed helper with an explicit
target. It is read-only and optional; ordinary skill operation uses available
file tools and requires no particular runtime. See its
[coverage and limits](skills/agent-workspace/references/validation.md).

[Behavioral walkthroughs](tests/scenarios.md) cover initialization, existing Git
and `.agents/` conventions, migration/recovery, cleanup, optional grilling
absence, meaningful and no-change capture, independent memory owners, privacy,
and contested updates. Expansion scenarios cover mixed artifacts, consolidation,
discovery, dependency blockers, intact checkout relocation and incomplete coverage.
Assess coverage, semantic preservation and mechanics separately. Keep raw
inputs/results under ignored `.local/`.

Validation on 2026-10-30 passed 11 mechanical/package tests, both skill-package
validators, repository link checks and synthetic behavioral walkthroughs. The
expansion walkthroughs checked coverage/dispositions separately from semantic
preservation and mechanics: mixed artifact consolidation, exact recovery,
scoped path repairs, protected modes, intact dirty checkout relocation, an
explicitly unresolved linked-worktree move, selective discovery and routine
memory maintenance. Source/deliverables and unrelated work survived; no-op
capture and read-only reruns preserved bytes and timestamps.

These authored walkthroughs do not prove future model behavior, complete
semantic preservation, secret absence, history recovery, native loading or
race-free writes. Linux was exercised; real persistent-workspace migration is
separate work. The optional checker cannot certify coverage or artifact purpose.

## Compatibility and delivery

Runtime skills need Markdown file access and a compatible agent capable of
following instructions. Git, GitHub CLI, Node, Python, and third-party grilling
skills are not runtime dependencies. The optional checker/tests use Python 3.9+
standard library; the Git fixture skips if Git is unavailable.

Linux was exercised. macOS should support the portable Markdown and Python
tooling but was not exercised. Windows file operations can work with suitable
tools; shell examples, symlink permissions, path/case behavior, and native skill
discovery need platform-specific verification. Use installer copy mode when
symlinks are unavailable. The boundary test needs symlink support.

Discovery, automatic instruction loading, inheritance, and live reload are
different capabilities. Installed files do not guarantee a running session will
reload them. Check the selected harness's current documentation and observed
behavior; start a fresh session when necessary. No adapter is required by estack.

After installation, check that each selected harness discovers the skill and
that its bundled resources are accessible outside the source checkout. File
discovery does not establish successful native invocation or live reload.
Preserve unrelated installed skills when refreshing these packages.
