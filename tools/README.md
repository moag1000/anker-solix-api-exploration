> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Tools

Scripts that generate `data/*.json` and page skeletons from the Blutter asm of the app. Standard library only; run every script from the repo root as `python3 -I tools/<script>.py <args>`. The asm trees are untrusted data: the scripts only read them and never import from or chdir into them.

Not here: documentation of API facts; see [../docs/STRUCTURE.md](../docs/STRUCTURE.md). Output goes to [../data/README.md](../data/README.md). The Smi rule that `smi.py` implements is in [../METHODOLOGY.md](../METHODOLOGY.md).

## 1. Produce the asm with blutter

Blutter runs in the venv `ankerAPK/.venv-blutter` (sibling of this repo). Point it at the `lib/arm64-v8a` folder of the unpacked APK and an output folder:

```bash
source ankerAPK/.venv-blutter/bin/activate
python blutter.py <apk>/lib/arm64-v8a <out>      # writes <out>/asm, <out>/pp.txt
```

Used roots: 3.24.3 `ankerAPK/v3.24.3/blutter_output/asm`, 3.18.0 `ankerAPK/blutter_output/asm` (diff only). Upstream names come from `ankerAPK/anker-solix-api/api/apitypes.py` (parsed with `ast`, never imported).

## 2. Script order

`N` = 3.24.3 asm root, `O` = 3.18.0 asm root. About 30 s per script.

```bash
python3 -I tools/endpoint_inventory.py $N --version 3.24.3 --old-root $O   # data/endpoints.json
python3 -I tools/model_fields.py       $N --version 3.24.3 --old-root $O   # data/models.json
python3 -I tools/param_types.py        $N --version 3.24.3                 # data/param_types.json
python3 -I tools/diff_versions.py $O $N                                    # tools/out/diff_3.18.0_3.24.3.md
python3 -I tools/render_pages.py                                           # tools/out/pages/{api,models}/
python3 -I tools/service_index.py                                          # api/README.md + api/<service>/README.md
python3 -I tools/readme_stats.py [--check]                                 # README statistics block + migration-map statuses (docs/STRUCTURE.md)
python3 -I tools/smi.py <asm_file> <0xADDR> [--dump]                       # check one number by eye
```

`readme_stats.py` rewrites the block between the `readme_stats:begin/end` markers of `README.md` and the Status column of the migration map in `docs/STRUCTURE.md` from `data/*.json` and the files on disk (idempotent; `--check` exits 1 when a file is stale). `service_index.py` overwrites `api/charging_hes_installer_svc/README.md` with a generated version that loses its hand-written groups; after a run, `git checkout` that file.

`data/*.json` is committed (envelope: `generated_by`, `app_version`, `snapshot`, `rows`; keys sorted). `tools/out/` is scratch and git-ignored. `render_pages.py` never writes into `api/` or `models/`: render into `tools/out/pages/`, then copy into `api/` with a no-clobber copy (`cp -n`, or a loop that skips existing files) so hand-written pages are never overwritten. After copying, run `tools/service_index.py` (reads `data/endpoints.json` and the pages on disk, rewrites `api/README.md` and every `api/<service>/README.md`; idempotent, purpose column comes from each page's "Purpose" line). Page paths: `v1` is dropped, other version segments are kept ([../docs/STRUCTURE.md](../docs/STRUCTURE.md#naming-conventions)). `render_pages.py` renders one page per distinct URL (all senders listed under "Callers in app"), including URLs removed in 3.24.3.

## 3. Reading the output

- Everything is heuristic string-level evidence: a header of `Confidence: string-only` on rendered pages is deliberate. Promote a fact to `asm-traced` only after a human has read the cited asm site (and checked integers with `smi.py --dump`).
- URL literals are found with and without the leading slash (`"/power_service/..."` and `"power_service/v1/..."`); the stored `url` always has the slash. A slashless literal counts only when its first segment is a known service prefix (`asmparse.SERVICE_PREFIXES`) or it matches `<name>/v<N>/`; Dart package paths such as `charging_platform/...` are not URLs. A literal with no `*Http*` call in the same function stays `role: url_provider` with `encrypted: false`.
- A literal such as `app/foo` passes the literal regex (known prefix) but the inventory filter `url_ok` rejects two-segment shapes for rows without a sender, so generic words do not become endpoints; a real two-segment URL that no `*Http*` function sends would be missed (none exists in 3.24.3). Limitation: a slashless literal with a known prefix and at least three segments is accepted even if it is not an endpoint.
- `reference: "pool-only"` marks a URL that has a 3.18.0 row, whose string is still in the 3.24.3 object pool (`pp.txt`, next to the asm root) but is loaded by no asm code. `removed_in` is set only when the string is absent from the 3.24.3 pool altogether (2 URLs). Pages say "string present in the object pool, no code reference found" for pool-only rows. `diff_versions.py` still lists both kinds as removed (it only sees code references).
- `service_index.py` keeps a row for every page on disk that has no inventory row (hand-added pages such as `passport/external_login`), with status "hand-written, not in `data/endpoints.json`" (for example `passport/external_login` and `passport/terminal_id`: hand-written pages with no inventory row). Orphan rows are listed in the service README but excluded from the page and skeleton counts.
- `service_index.py` keeps the hand-written tail of a service README: everything from the line `<!-- hand-written below: kept by tools/service_index.py -->` to the end of the file survives a regeneration (used by `api/smart_service/README.md`). The READMEs of `charging_hes_installer_svc` have hand-written groups and sections without that marker, so do not run the generator over them without copying them back.
- `encrypted` follows the callee name (`*encryptionRequestHttp*`). Plain `requestHttp` callees default to `needEncryption = true`; rows carry `encryption_note` for those.
- `nullable: null` means the extractor could not tell. `param_type: "variable"` means the key is stored from a register (see `unresolved` in `param_types.json`).

Page checks:

```bash
python3 -I tools/cmp_since.py <old_asm> <new_asm> <relpath.dart> [function ...]   # literal sequences per function, 3.18.0 vs 3.24.3 (branch logic is NOT compared)
python3 -I tools/check_citations.py <asm_root> <page.md> ...                      # every @0xADDR exists; table-row JSON keys match the decoded instruction
```

`check_citations.py` MISSING lines can be false positives when the file name comes later in the sentence; read each one.

## 4. Documentation lint

```bash
python3 -I tools/lint_docs.py --summary            # counts per rule; exit 1 when any error
python3 -I tools/lint_docs.py [--rule header,links] [--json] [--warn-only] [--strict]
```

`lint_docs.py` checks every Markdown page of the repo (not `.superpowers/`, `tools/out/`, `patches/`, nor an old root doc listed in the migration map of [../docs/STRUCTURE.md](../docs/STRUCTURE.md) that still has no status header). Output lines are `path:line: ERROR|WARN rule: message`. Rules:

| Rule | Checks |
|---|---|
| `header` | first non-blank line is the status header (App 3.24.3, date, `Confidence:` one of the 4 tags or `Page type:`, `Owner page:`) on api/, models/, flows/, devices/, mqtt/, ble/, reference/, docs/ top level and docs/audit/, METHODOLOGY, GLOSSARY |
| `sections` | H2 order of endpoint/model/flow/device pages (extras allowed, template sections required and ordered) or H4 order under each H3 of mqtt/ble command pages (`envelope`, `protocol`, `handshake`, README excluded); the lists are read from `docs/templates/` |
| `uncited-int` | integer >= 2 in a table row of a fact page (header has `Confidence:`, or a `Page type:` other than guidance) with no `@0x` citation and no row tag. Not checked: audit tables, Known unknowns and Device-tested by sections, sections with the line `Tag: untagged by design`, cells of a count column (header has count, rows, calls or total; never the first column) and of a `param_type` id column, ISO dates (`2026-10-19`), versions, hex, line numbers, `step N`, `N sends/calls/functions/endpoints/pages/files/rows`. A section tagged `string-only`, `upstream-confirmed` or `device-tested` still needs a citation or a row tag per row |
| `tag-overclaim` | scope: the same sentence (cells of a table row are split into sentences), or a section headed or opened by `Tag: asm-traced`; the sentence carries `asm-traced` and one of the hedge words in `OVERCLAIM` in the script. `is not traced` and `(..., not traced)` state a limit of the evidence and pass. It does not look across sentences or at page-header tags; `--strict` additionally reports the hedge words on table rows that cite `@0x` under an `asm-traced` page header, as warnings |
| `inferred-as-traced-sequence` | a line carrying a traced-step marker (the letter T in square brackets) and the same hedge words |
| `todo-purpose` | warning: `## Purpose` is `<!-- TODO -->`, printed as one count per service |
| `links` | every relative link resolves, and every `#anchor` matches a GitHub slug of the target page; code spans and fences are not links |
| `length` | error above 600 lines; warning above 150 lines without a Contents section (docs/audit tables are exempt from the limit) |
| `dup-payload` | identical ```json block on more than one page. Not checked: docs/templates, docs/audit, the empty success envelope, and identical shapes that each sit in their own endpoint page's `Example request/response` section |
| `secret` | 32+ hex run outside docs/audit. A run of exactly 32, 40 or 64 characters directly after `sha256`, `sha1`, `md5`, `snapshot` or `checksum` is a build identifier, not a secret |
| `owner-cmd` | `"cmd": N`, `cmd = N`, `cmd N` (also with the backticked word) on a fact page other than `api/param_types.md`. Exempt: docs/audit, and a line carrying the marker `<!-- lint: owner-cmd example -->` (the worked Smi example in METHODOLOGY) |

## 5. Tests

```bash
python3 -I -m unittest discover -s tools/tests -t .
```

The tests read the real asm trees (about 2 minutes) and skip with a message when a root is missing.
