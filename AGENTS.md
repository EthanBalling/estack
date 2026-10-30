# estack

This repository owns two independent portable Agent Skills under `skills/`.
For behavior or safety changes, read the relevant contract in
[docs/design/README.md](docs/design/README.md) and its linked shared policies.
Approved architecture governs implementation; surface material contradictions.

Keep entry points small and resource links relative to each installed skill.
Each skill must work without the other or any third-party skill. Runtime use
requires file tools, not Git or an installer. Python is optional validation tooling.
Use synthetic disposable projects for verification; never migrate real persistent
workspaces as an implementation test. Preserve other installed skills.

For checks, installation, compatibility limits, and usage, read
[README.md](README.md). Keep it accurate when behavior changes. Keep private
audits, scratch files, recovery copies, and session handoffs under ignored
`.local/`; never stage them. Review staged content before committing. Existing
remote/visibility changes and publication need explicit authorization.

Persist consequential decisions in their authoritative design or project document,
with evidence and uncertainty where useful. Keep continuation context concise in
the local handoff, pointing to owners and exact next actions. Freshly read before
narrow edits and preserve intervening work. Do not change governing meaning
without user grounding or approval.
