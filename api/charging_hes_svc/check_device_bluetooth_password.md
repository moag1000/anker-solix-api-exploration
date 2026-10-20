> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# check_device_bluetooth_password

## Purpose

Checks the Bluetooth password of an Italy-market device during the Italy self-check (`ItalySelfCheckRequestController::checkDeviceBluetoothPassword`), sending station id, product number, serial number, an encoded secret and a salt (string-only: no caller chain in `data/endpoints.json`, inferred from the builder name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/check_device_bluetooth_password` (asm-traced): URL string at `charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea1bdc`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3ea1bd4`, in `ItalySelfCheckRequestController::checkDeviceBluetoothPassword` (`charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea18d4`), sent through `requestHttp` (`@0x3ea1c04`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `ItalySelfCheckRequestController::checkDeviceBluetoothPassword` (`charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart`, call `@0x3ea1c04`, argument list `@0x3ea1bfc`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `ItalySelfCheckRequestController::checkDeviceBluetoothPassword` (`charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea1b90`, 5 keys). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes | `"<station_id>"` | `charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea1b2c` |
| `pn` | string | yes | `"<pn>"` | `charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea1b40` |
| `sn` | string | yes | `"<sn>"` | `charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea1b54` |
| `p_secret` | string | yes | `"<p_secret>"` | `charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea1b68` |
| `salt` | string | yes | `"<salt>"` | `charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea1b7c` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure is the folded closure `settings/src/common/page/timing_setting/timing_setting_controller.dart @0x351515c` (pool entry of this builder); it completes the pending completer with `true` (`@0x3515188`, `complete` `@0x3515198`) and reads no response key. The failure closure `@0x351546c` of the same file completes it with `false` (`@0x3515498`, `@0x35154a8`).

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "pn": "<pn>",
  "sn": "<sn>",
  "p_secret": "<p_secret>",
  "salt": "<salt>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure completes with `false` without reading the code.

## Callers in app

- `charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart`: `checkDeviceBluetoothPassword` @0x3ea18d4 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- How `p_secret` and `salt` are derived: the builder calls `getUserId` (`charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea1ab8`), interpolates a string (`@0x3ea1af4`), runs `convert` (`@0x3ea1b0c`) and `encode` (`@0x3ea1b18`) and formats a `DateFormat` pattern `yyyyMMdd HH:mm:ss` (`@0x3ea1a50`) before the map is built; the data flow into the two keys and the classes behind `convert` and `encode` were not followed.
- `sn` is stored from a local that defaults to the empty string (`charging/ui/page/device/a5101/setting/italy_selfcheck/italy_selfcheck_request.dart @0x3ea1a04`, `@0x3ea1a30`); which serial the caller supplies was not decoded.
- No caller of `checkDeviceBluetoothPassword` is recorded in `data/endpoints.json`.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
