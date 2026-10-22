> Verified against: App 3.24.3 · Date: 2026-10-23 · Page type: guidance (no API facts) · Owner page: this page

# Lessons learned

One row per error pattern this repository made, with the guard that now catches the whole pattern, not only the instance. The rule texts live on [../METHODOLOGY.md](../METHODOLOGY.md) and [../CONTRIBUTING.md](../CONTRIBUTING.md); the lint rules are in `tools/lint_docs.py`. When a new error turns up: add a row, then build a guard for the pattern, or say in the row why none can be built.

| pattern | how it showed | guard | kind |
|---|---|---|---|
| Blutter immediates read without Smi decoding | integers 2× too large in the 3.18.0 docs, e.g. `cmd` 246 for 123 (CHANGELOG, "Errata 2026-10") | lint `uncited-int` (every decoded integer cites its asm site), lint `owner-cmd` (cmd values only on `api/param_types.md`), `tools/smi.py`, METHODOLOGY "Smi rule" | lint, tool |
| hedged statement under an `asm-traced` header | inferred facts presented as traced | lint `tag-overclaim`, lint `inferred-as-traced-sequence` | lint |
| one value kept at two places | copies drift once one of them is corrected | lint `dup-payload`, lint `owner-cmd`, ownership map [STRUCTURE.md](STRUCTURE.md) | lint |
| key material in a page | risk of publishing the preset key | lint `secret` | lint |
| BLE offered as a live cloud fallback | old pages; BLE is unavailable while the device is on WiFi ([../ble/protocol.md](../ble/protocol.md#connection-routing-and-the-wifi-exclusion-rule)) | lint `ble-fallback` (fact pages), CONTRIBUTING "What not to contribute" | lint |
| asm root of another build | regenerating `data/endpoints.json` from the older tree gave a different file stamped with the 3.24.3 snapshot label (2026-10-21) | `check_root` landmark in `tools/asmparse.py`, called by `endpoint_inventory.py`, `model_fields.py`, `param_types.py` (tests: `RootGuardTests`); `error_codes.py` already stops on missing sites | tool, test |
| conclusion from truncated output | `head -1` hid the matching site of a function address (2026-10-21); `sort -u` merged strings of unrelated enums into an apparent `sourceType` list (2026-10-22) | METHODOLOGY "Verification discipline"; not mechanisable, a habit (count instead of cut) | rule |
| delegated finding taken as fact | a subagent's usage-mode values nearly replaced the correct `EmsModeType` table in [../models/hes.md](../models/hes.md) (2026-10-22) | METHODOLOGY "Verification discipline"; the controller re-reads the source before an edit | rule |
| case mismatch in a coverage scan | URL `getMiStatus` against page `getmistatus.md`: six endpoints reported as undocumented that had pages (2026-10-23) | METHODOLOGY "Verification discipline" | rule |

Rows of kind `rule` have no mechanical guard; they rely on the working rule being followed.
