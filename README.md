# estack

Two independent [Agent Skills](https://agentskills.io/specification) for portable
project context:

| Skill | Use |
| --- | --- |
| [agent-workspace](skills/agent-workspace/SKILL.md) | Familiarize with, initialize, audit, migrate, validate, or explicitly clean up an agent workspace. |
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

Select compatible agents interactively, or append `-y` to accept the installer's
default targets; add `-a <agent>` only to narrow them. Omit `-g` for a
project-local installation. Select just one name after `--skill` for an
independent install. Inspect existing same-name installations before
replacement; never remove other skills as part of an update.

In skills CLI 1.7.4, a global install writes one shared copy to
`~/.agents/skills` for every agent that uses `.agents/skills`, and links agents
with their own directory, such as Claude Code at `~/.claude/skills`. Some
harnesses do not scan that shared global location; see
[compatibility](#compatibility-and-delivery).

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
command to refresh only these skills. For remote-backed installations, name the
skills explicitly:

```sh
npx skills update agent-workspace update-memory -g
```

Avoid unscoped `npx skills update` and `npx skills check`: in skills CLI 1.7.4,
`check` runs the same code path as `update`, so either form refreshes every
tracked skill in scope. Use `npx skills list -g` to inspect installations, and
confirm behavior for other installer versions before relying on a read-only
check. For manual installation without Node, copy one
complete `skills/<name>/` directory to the selected harness's documented skill
directory, preserving bundled resources. Recopy on update.

## Use

Invoke by name using the active agent's skill mechanism, or ask for the operation:

- “Use agent-workspace to initialize this project as a local plant catalog.”
- “Use agent-workspace to familiarize yourself with this workspace and report
  readiness without starting its backlog.”
- “Use agent-workspace to audit this repository without changing it.”
- “Use agent-workspace to migrate the agent records in this selected directory;
  preserve the knowledge, domain rules, and uncommitted work.”
- “Use agent-workspace to validate these instructions and references.”
- “Use agent-workspace to clean up these explicitly selected superseded notes.”
- “Use update-memory to save the accepted decision and unfinished next action.”

The [approved contracts](docs/design/README.md) own behavior; this summary is
orientation only:

- **Familiarize, audit and validate** leave the target unchanged. Familiarize
  follows the workspace's own startup rules and reports file-backed
  understanding, readiness and gaps, not verified integration access.
- **Initialize** creates only grounded resources around a minimal `AGENTS.md`
  router, preserving existing roles, unexpected content and intervening writers.
- **Migrate and cleanup** assess the whole selected directory, organize agent
  records and artifacts by purpose under `.agents/`, and keep verified recovery
  through validation before closing out only the operation's own temporary
  material. See [migration and safety](docs/design/MIGRATION.md).
- **update-memory** updates existing authoritative owners, including projects
  without `.agents/`, refreshes a handoff only when useful, and writes nothing
  when the context is already recorded or trivial.

Neither skill stages, commits, pushes, settles a thread or executes a discovered
backlog. `agent-workspace` bundles an optional exact-heading
[section reader](skills/agent-workspace/references/retrieval.md); ordinary file
tools remain sufficient, and `update-memory` depends on neither the helper nor
the other skill.

## Validate

Run the deterministic checks from the repository:

```sh
python3 -B -m unittest discover -s tests -v
python3 -B skills/agent-workspace/scripts/validate_workspace.py .
git diff --check
```

The unit tests cover the bundled checker and section reader, standalone package
copies run outside the checkout, repository documentation links/anchors, and a
static Python 3.9 grammar guard for the helpers. For a workspace outside the
checkout, run the installed helper with an explicit target. It is read-only and
optional; ordinary skill operation uses available file tools and requires no
particular runtime. See its
[coverage and limits](skills/agent-workspace/references/validation.md).

[Behavioral walkthroughs](tests/scenarios.md) are authored scenarios for
familiarization, initialization and destination collisions, existing Git and
`.agents/` conventions, whole-directory migration with mixed artifacts and
dependency blockers, recovery closeout, cleanup, intact checkout relocation,
incomplete coverage, optional grilling absence, and meaningful, independent,
no-change and contested memory capture. Each was exercised against synthetic
fixtures when introduced. Assess coverage, semantic preservation and mechanics
separately, and keep raw inputs/results under ignored `.local/`.

Unit tests are mechanical. Authored walkthroughs do not prove future model
behavior, complete semantic preservation, secret absence, history recovery,
native loading or race-free writes. Real persistent-workspace migration is
separate work, and the optional checker cannot certify coverage or artifact
purpose.

## Compatibility and delivery

Runtime skills need Markdown file access and a compatible agent capable of
following instructions. Git, GitHub CLI, Node, Python, and third-party grilling
skills are not runtime dependencies. The optional checker, section reader and
tests use Python 3.9+ standard library; 3.9 is guarded statically, while
exercised runs used newer CPython. The Git fixture skips if Git is unavailable.

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
