# Optional retrieval mechanics

Read when using the section reader for the first time or when exact-section mechanics/measurement are needed. This is not another mandatory startup read. Follow the selected workspace's own required reads and relevant owner routes; no fixed core record set is imposed.

## Selective reading

Locate the relevant exact heading and include descendants through the next peer/ancestor. Include applicable document/ancestor introductions, evidence/current-state limits and linked prerequisites. A Markdown fragment locates content; it saves no context if the tool returns the full file. Expand when needed, and read the complete relevant file when no safe section boundary exists. Required procedures still need complete reading.

Ordinary file tools and verified line ranges are sufficient. An optional [standard-library helper](../scripts/read_section.py) provides exact ATX heading reads. Resolve it from this installed skill, not a source checkout or the current working directory. With no suitable Python or supported heading structure, use file tools.

## Section reader

Replace the example script path with this skill's actual installed path; pass the explicitly selected local file as `FILE`:

```sh
python3 /path/to/agent-workspace/scripts/read_section.py FILE --list
python3 /path/to/agent-workspace/scripts/read_section.py FILE '## Exact heading'
python3 /path/to/agent-workspace/scripts/read_section.py FILE '### Exact child' --preamble
```

Python 3.9+ standard library is sufficient. Listing prints real ATX headings with 1-based line numbers. The target must exactly match the listed heading line, including `#` markers, indentation and optional closing hashes. Selected output includes descendants through the next peer/ancestor boundary. `--preamble` adds document lead and applicable ancestor headings/introductions, excluding unrelated siblings. Linked prerequisites remain separate reads.

Matching backtick/tilde fences suppress apparent headings until a valid same-character closing fence of at least the opening length. This is an ATX reader, not a general Markdown renderer: setext headings and headings in blockquotes/lists are unsupported. Duplicate/missing exact targets, unreadable files and invalid UTF-8 return nonzero with stderr and no content. Usage errors return 2, read/selection errors 1, success 0. Never silently select a duplicate or truncate required context to meet a token target.

The helper reads only the requested file; it does not enforce workspace ownership, resolve permission to read protected content or discover prerequisites. Apply the selected scope/privacy rules before choosing a file. It writes no target content and requires no external package.

## Optional footprint comparisons

Compare equal before/after startup or task read sets, including added routers, introductions and first-use helper prerequisites. Label UTF-8 bytes/whitespace words as proxies; name any tokenizer/encoding used. Static text counts are not runtime-injected context, model billing, latency or task totals. Preserve behavior and coverage even when text grows. No tokenizer installation, benchmark or size target is required.
