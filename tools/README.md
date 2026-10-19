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
python3 -I tools/smi.py <asm_file> <0xADDR> [--dump]                       # check one number by eye
```

`data/*.json` is committed (envelope: `generated_by`, `app_version`, `snapshot`, `rows`; keys sorted). `tools/out/` is scratch and git-ignored. `render_pages.py` never writes into `api/` or `models/`: render into `tools/out/pages/`, then copy into `api/` with a no-clobber copy (`cp -n`, or a loop that skips existing files) so hand-written pages are never overwritten. After copying, run `tools/service_index.py` (reads `data/endpoints.json` and the pages on disk, rewrites `api/README.md` and every `api/<service>/README.md`; idempotent, purpose column comes from each page's "Purpose" line). Page paths: `v1` is dropped, other version segments are kept ([../docs/STRUCTURE.md](../docs/STRUCTURE.md#naming-conventions)). `render_pages.py` renders one page per distinct URL (all senders listed under "Callers in app"), including URLs removed in 3.24.3.

## 3. Reading the output

- Everything is heuristic string-level evidence: a header of `Confidence: string-only` on rendered pages is deliberate. Promote a fact to `asm-traced` only after a human has read the cited asm site (and checked integers with `smi.py --dump`).
- URL literals are found with and without the leading slash (`"/power_service/..."` and `"power_service/v1/..."`); the stored `url` always has the slash. A slashless literal counts only when its first segment is a known service prefix (`asmparse.SERVICE_PREFIXES`) or it matches `<name>/v<N>/`; Dart package paths such as `charging_platform/...` are not URLs. A literal with no `*Http*` call in the same function stays `role: url_provider` with `encrypted: false`.
- `service_index.py` keeps a row for every page on disk that has no inventory row (hand-added pages such as `passport/external_login`), with status "hand-written, not in `data/endpoints.json`".
- `encrypted` follows the callee name (`*encryptionRequestHttp*`). Plain `requestHttp` callees default to `needEncryption = true`; rows carry `encryption_note` for those.
- `nullable: null` means the extractor could not tell. `param_type: "variable"` means the key is stored from a register (see `unresolved` in `param_types.json`).

## 4. Tests

```bash
python3 -I -m unittest discover -s tools/tests -t .
```

The tests read the real asm trees (about 2 minutes) and skip with a message when a root is missing.
