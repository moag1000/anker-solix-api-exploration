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

`readme_stats.py` rewrites the block between the `readme_stats:begin/end` markers of `README.md` and the Status column of the migration map in `docs/STRUCTURE.md` from `data/*.json` and the files on disk (idempotent; `--check` exits 1 when a file is stale). `service_index.py` refuses (exit 1, names the file, writes nothing) to overwrite a service README that carries prose the generator does not emit unless the file contains the `<!-- hand-written below: kept by tools/service_index.py -->` marker. Every service README row has one of four statuses: `owner` (purpose without TODO), `skeleton`, `pool-only` and `removed` (the last two from the inventory); `api/README.md` counts them.

`data/*.json` is committed (envelope: `generated_by`, `app_version`, `snapshot`, `rows`; keys sorted). `tools/out/` is scratch and git-ignored. `render_pages.py` never writes into `api/` or `models/`: render into `tools/out/pages/`, then copy into `api/` with a no-clobber copy (`cp -n`, or a loop that skips existing files) so hand-written pages are never overwritten. After copying, run `tools/service_index.py` (reads `data/endpoints.json` and the pages on disk, rewrites `api/README.md` and every `api/<service>/README.md`; idempotent, purpose column comes from each page's "Purpose" line). Page paths: `v1` is dropped, other version segments are kept ([../docs/STRUCTURE.md](../docs/STRUCTURE.md#naming-conventions)). `render_pages.py` renders one page per distinct URL (all senders listed under "Callers in app"), including URLs removed in 3.24.3.

## 3. Reading the output

- Everything is heuristic string-level evidence: a header of `Confidence: string-only` on rendered pages is deliberate. Promote a fact to `asm-traced` only after a human has read the cited asm site (and checked integers with `smi.py --dump`).
- URL literals are found with and without the leading slash (`"/power_service/..."` and `"power_service/v1/..."`); the stored `url` always has the slash. A slashless literal counts only when its first segment is a known service prefix (`asmparse.SERVICE_PREFIXES`) or it matches `<name>/v<N>/`; Dart package paths such as `charging_platform/...` are not URLs. A literal with no `*Http*` call in the same function stays `role: url_provider` with `encrypted: false`. The caller walk (`resolve_senders`) looks for the nearest sender. A function sends when it calls an HTTP/SDK primitive (`*requestHttp*`, `*encryptionRequestHttp*`, `AKIoTKitManagerImpl::handle[WithProgress]`, ...) or a wrapper (a function of an `http_helper.dart`, `http_manager.dart` or `*_http_*` module that calls a primitive, e.g. `HttpHelper::getDataFromService`). At the function that holds the URL literal and then at each caller (at most 3 levels, over `bl` call sites and static-field loads such as `Api.getPrice`): (a) the function itself sends after the URL load (address order), (b) else a non-generic callee called after the URL load sends (a callee holding another endpoint's literal, a callee called from more than 30 functions, and `dart:`/flutter/get callees are skipped), (c) else go to the callers. Sibling closures of the same function count as the function. Fields added to the row: `sender`, `sender_file`, `sender_kind` (`self` = the function holds the primitive call, `wrapper` = the sender is the helper function it calls, `callee`), `sender_wrapper` (the primitive or wrapper symbol called), `sender_via`/`sender_via_files` (callers walked up from the provider, excluding it; `[]` = the provider itself), optionally `sender_via_also` (other chains to the same sender) and `sender_also` (other senders at the same depth, at most 5); or `resolution`: `generic-path-check` (the literal sits in the generic HTTP manager and is a path check, not a request), `mixin-gap` (the walk reaches a mixin application whose body is absent from the dump, deduplicated or not; UNCONFIRMED) or `unresolved`. `role` stays `url_provider`. All of it is string-only evidence: a caller that sends may send something else than this URL.
- A literal such as `app/foo` passes the literal regex (known prefix) but the inventory filter `url_ok` rejects two-segment shapes for rows without a sender, so generic words do not become endpoints; a real two-segment URL that no `*Http*` function sends would be missed (none exists in 3.24.3). Limitation: a slashless literal with a known prefix and at least three segments is accepted even if it is not an endpoint.
- `reference: "pool-only"` marks a URL that has a 3.18.0 row, whose string is still in the 3.24.3 object pool (`pp.txt`, next to the asm root) but is loaded by no asm code. `removed_in` is set only when the string is absent from the 3.24.3 pool altogether (2 URLs). Pages say "string present in the object pool, no code reference found" for pool-only rows. `diff_versions.py` still lists both kinds as removed (it only sees code references).
- `service_index.py` keeps a row for every page on disk that has no inventory row (hand-added pages such as `passport/external_login`), with status "owner, not in `data/endpoints.json`" (or "skeleton, ...") (for example `passport/external_login` and `passport/terminal_id`: hand-written pages with no inventory row). Orphan rows are listed in the service README but excluded from the page and skeleton counts.
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

`lint_docs.py` checks every Markdown page of the repo (not `.superpowers/` nor `tools/out/`; an old page listed in the migration map of [../docs/STRUCTURE.md](../docs/STRUCTURE.md) that still has no status header is checked for the `links` rule only, so a broken link in CHANGELOG.md or a root page is reported). Output lines are `path:line: ERROR|WARN rule: message`. Rules:

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

## 6. Error-code catalog

```bash
python3 -I tools/error_codes.py [--asm <asm_root>] [--upstream <errors.py>] [--pool <pp.txt>] [--check]   # data/errors.json
python3 -I -m unittest discover -s tools/tests -t . -p 'test_error_codes.py'          # own tests, about 1 s
python3 -m unittest tools.tests.test_error_codes                                       # same tests; without -I, because -I drops the cwd from sys.path
```

`error_codes.py` writes `data/errors.json` and nothing else (the path is fixed; there is no `--out`). Rows have a `source`: `upstream` (every `ERRORS` entry of the upstream `api/errors.py`, read with `ast`), `asm` (compares of an error code in the handler functions listed in `SITES` inside the script, by file and function address, valid for 3.24.3 only) and `issue` (codes reported in a GitHub issue, hard-coded with the issue link). Every row also has `kind`: `api` (an error code, the rows the catalog page is about) or `message-type-excluded` (a compare of 10000 to 10007 in an `onMessageDispatch` function or MQTT closure listed in `MSG_SITES`: a device message type that shares numbers with API codes; recorded with file, function address and compare address so the exclusion is data, never counted as a catalog code and not needing a page row). The asm rows obey the Smi rule by compare width: `cmp wN` (or `r17 = N; cmp wN, w17`) is a tagged int and the value is raw / 2, `cmp xN` is an unboxed int and the value is raw; `width`, `raw` and `branch` stay in the row so the step can be redone. The handler list is curated on purpose: a sweep of every compare against a 4 to 6 digit constant mostly finds class ids, MQTT message types in `onMessageDispatch` and UI limits, so the tool reads only the listed functions and aborts with exit 2 (writing nothing) when a listed function is missing. `--check` writes nothing and exits 1 when `data/errors.json` is stale or missing, or when `api/errors.md` lacks a table row (`| <code> |`) for a code in the JSON. Asm rows also get `message_keys` (every localisation key in the equal-path block after the compare that exists in the `en_US` block of the translation table in the pool dump; `--pool`, default `pp.txt` beside the asm root, exit 2 without it), `message_key` (the first), `message_en` (its text) and `message_tag` `asm-traced (proximity)` (only when a key exists). Rule: the first localisation key loaded in the equal-path block after the compare; may be a dialog title, not the body. The block is the fall-through of `b.ne` or the target of `b.eq`, up to an unconditional branch, `ret`, the `b.ne` target or the next compare; range splits have none, so no key. `--check` also fails when, for any code row of the table under `## User-visible message` in `api/errors.md`, the keys listed there are not exactly the union of `message_keys` over that code's JSON rows (order-insensitive), or a code with keys has no row. The catalog page is hand-written; the JSON holds the extracted facts it cites.

## 7. Data export schema check and models.json filter

```bash
python3 -I tools/schema_check.py [--repo .] [--check]                                  # validate data/*.json, writes nothing
python3 -I -m unittest discover -s tools/tests -t . -p 'test_schema_check.py'          # own tests, under 1 s
python3 -I tools/model_fields.py $N --version 3.24.3 --old-root $O [--include-noise]   # data/models.json
python3 -I -m unittest discover -s tools/tests -t . -p 'test_model_fields_dedupe.py'   # own tests, under 1 s
```

`schema_check.py` validates the four exports against the inline schemas that [../data/README.md](../data/README.md) documents: envelope keys, required and optional row fields with their types, unknown fields, unique `models.json` keys and equal `app_version`/`snapshot` across the files. It prints one line per violation; `--check` makes any violation exit 1. When a generator gains a field, extend the schema and `data/README.md` in the same change. `model_fields.py` keys every row `package::Class` (extended to a unique directory or file path where the package key collides; `class` keeps the short name) and by default drops the `sentry` package only; `--include-noise` keeps it. Field-less app classes stay with an empty `fields` list.

## 8. Known-unknowns triage

```bash
python3 -I tools/unknowns_triage.py . --out docs/audit/KNOWN_UNKNOWNS_TRIAGE.md --json tools/out/unknowns.json --override docs/audit/unknowns_overrides.json
python3 -I -m unittest discover -s tools/tests -t . -p 'test_unknowns_triage.py'      # own tests, under 1 s
```

`unknowns_triage.py` reads every `*.md` under the root except `docs/archive/`, `docs/superpowers/`, `docs/templates/`, `.superpowers/`, `tools/out/` and hidden directories. Every bullet (`- `, with its indented continuation lines) under a Known-unknowns heading is one row: `## Known unknowns`, `## Known unknowns on this page` or the `#### Known unknowns` of a command section; the section ends at the next heading of the same or a higher level, fenced code is skipped, and the skeleton placeholders `<!-- TODO -->` and `<open question>` are not rows. The class comes from ordered keyword rules (`RULES` in the script; the first match wins and its name goes to `hint`): `server` (server, accepts, rejects, enforces, returns, cloud side, backend), then `device` (firmware, device test, on a real, capture, which devices, hardware), then `asm` (polarity, closure, register, not traced, not decoded, not re-derived, which function, caller, builder, `@0x`), else `unclear`. Words match at a word start, case-insensitive.

`--override` reads a hand-maintained JSON file, `{"<page>:<hash>": {"class": "asm|server|device|unclear", "note": "..."}}` (`docs/audit/unknowns_overrides.json`). `<hash>` is the first 10 hex characters of the sha1 of the bullet text (stripped, whitespace collapsed; the row field `key` holds `page:hash`), so an override survives a line shift and any edit that leaves the bullet text alone; identical bullets on one page share a key. A missing key keeps the heuristic class; an override sets `class`, sets `hint` to `override` and keeps the heuristic result in `heuristic_class`. A key with no matching bullet (the text was edited or the bullet removed) is printed on stderr with its page and the exit code stays 0; `--strict` makes it exit 1. An invalid class exits 2 and writes nothing. `--rekey-overrides` rewrites the override file from the current pages: old `<page>:<line>` keys become hash keys (looked up by the bullet at that line, so run it on the tree the lines belong to), hash keys stay, and keys that match nothing are kept and reported; the run prints how many line keys it rekeyed, how many hash keys it kept and how many matched no bullet. A hash key cannot be mapped to an edited bullet text, so `--rekey-overrides` alone never repairs a stale key: either move the entry by hand to the new text's hash (the `key` field of `tools/out/unknowns.json`) after checking that its class still holds, or add `--prune-stale` to drop every key that matches no bullet (the bullet then falls back to the heuristic class until it is classified again). `--date YYYY-MM-DD` sets the date printed in the generated page header (default: today), so a regeneration of an unchanged tree can be made byte-identical. The "Manual pass" section of the audit page is generated from the override file, so a regeneration keeps it.

**The count rose after promotion.** The first run counted 913 bullets, the run after Task 5 of the depth pass 1578, although several hundred bullets were resolved: the 329 skeleton `<!-- TODO -->` placeholders are not rows, and promotion replaced them by real bullets. Compare a class count only between runs on the same set of pages; resolved bullets are counted in the SDD results files of the tasks, not by this page.

`tools/out/unknowns.json` (git-ignored scratch) holds one row per bullet: `page`, `line`, `text`, `class`, `hint` (plus `heuristic_class`, `heuristic_hint` and `note` on overridden rows). `line` is for display only and goes stale as soon as a page is edited: re-run the tool before every use of the JSON.

## 9. Request-field extractor

```bash
python3 -I tools/request_fields.py $N --service power_service --out tools/out/request_fields_power_service.json
python3 -I tools/request_fields.py $N --all [--out tools/out/request_fields_all.json]
python3 -I tools/request_fields.py $N --service power_service --check --out tools/out/request_fields_power_service.json   # extract, then exit 1 on a response_key missing from data/models.json
python3 -I tools/request_fields.py --check --out tools/out/request_fields_power_service.json    # check an existing file only (exit 2 when it is missing)
python3 -I -m unittest discover -s tools/tests -t . -p 'test_request_fields.py'                  # own tests, under 1 s
```

`request_fields.py` reads `data/endpoints.json` and `data/models.json` (override with `--endpoints`, `--models`) and writes one record per endpoint row to `tools/out/` (git-ignored worksheet, never committed). `--service` keeps the rows whose URL starts with that service segment; `--all` takes every row. A run over `power_service` takes a few seconds.

The builder is the function that holds the URL literal (for `role: sender` rows that is the sender itself; for `url_provider` rows the provider function, not the wrapper it hands the request to). Its instructions are replayed with a small register and stack-slot tracker: a stored value is classified from the instruction that produced the stored register (`mov` immediate, `ldur` of a parameter slot, `lsl x,x,#1` Smi tag of its source, `LoadField`); every other write, every call result and every `AllocateArray` size invalidates the register, so a stale `r2 = N` can never become a value. The array handed to `Map._fromLiteral` is found among the registers spilled to `[SP...]` (`stp`/`str`, including `lr`). When the builder holds no map literal, the maps of the functions in the row's `callers` are searched: the last top-level literal before the first call to the builder gives the fields (`source: caller`, `caller`, `call_addr`); only direct callers are read, an interface caller needs a second hop that is not done. A map literal is an `AllocateArray` that ends in `Map._fromLiteral`; an even slot with a string literal is a key, the next slot holds the value (slot index from the store offset: `(offset - 0xf) / 4`). Keys added after the literal by `Map.[]=` (a `GDT[cid_x0 + 0x6a9]()` call with the map in `r1`, a string literal in `r2` and the value in `r3`; the selector is not named by Blutter, but 0x6a9 is the only one seen) are listed with `source: map_set`; this includes keys set on an empty `Map._fromLiteral(THR::empty_array)` literal. A store from the zero register (`stur wzr`) is `const_smi` raw 0, value 0, width w. Value kinds: `const_smi` (32-bit store of an immediate, `value` = raw / 2, `width: w`), `const_int64` (immediate through `BoxInt64Instr`, `value` = raw, `width: x`), `const_string`, `const_bool`, `param` (loaded from a parameter slot), `field` (`LoadField`/`ArrayLoad`), `list`, `map` (nested; `children` names its keys) and `unknown` wherever the tracker cannot decide (`raw` then holds the defining instruction text). Every field carries `addr` (the key load) and `evidence` (raw text of the value store with its address). `required` is `false` when a `cmp .., NULL` plus conditional branch spans the key and stays inside the builder (`guard_addr` names the compare), else `true`. A nested map or list is a value, not a top-level body.

Other columns: `method` (`Method.post` or `Method.get` when the pool entry `pp+0xa7e0` or `pp+0x340e8` is loaded in the builder, else `null`), `response_class` (class of a `<Class>.fromJson` or `.fromMap` call that consumes the response: its input is the awaited result of the send call, a field of it, the parameter of a success closure, or a value derived from those after the response was read, incl. the `?? {}` default; a `fromJson` fed by a map literal built in the same function, by a captured closure context value or by another call's result is request-side or unrelated and is not attributed. Failing that the single class found by the same rule in the functions named in the row's `callers` when they await the call to the builder, `response_source: caller`; several distinct caller classes stay `null`, `response_source: caller-ambiguous`, `response_classes` lists them; `response_evidence` names for each attributed class the input register and the instruction it came from) and `response_key` (the `data/models.json` key of that class; with several packages the one in the same directory as the function that holds the call, else `response_key: null` and `response_candidates` lists the keys). A row with no field carries a `note` (no map literal in the builder or its direct callers, only empty or non-string-keyed literals, or the builder is absent from the asm). All of it is string-level and instruction-level evidence for a human to verify before a page is promoted; it does not replace reading the cited site.

**Known gaps.** The typing is heuristic: `value_kind` is decided from the defining instruction of the stored register, so a value that arrives through a second hop, a mixin-deduplicated sender that is absent from the dump, or an untyped parameter or field stays `param`, `field` or `unknown`; a page was promoted to `asm-traced` only after the builder was read from the asm, never from the worksheet alone. The extractor starts from `data/endpoints.json`, and that inventory misses senders that load the URL as `r1 = "/..."` and go through `getDataFromService` (found for `quit_disaster_prepare` and `set_site_device_disaster`). Follow-up for the next plan: extend `tools/endpoint_inventory.py` to recognise that form.
