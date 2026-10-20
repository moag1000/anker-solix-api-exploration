> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# cancel_pop

## Purpose

Tells the cloud that the OTA upgrade popup of a station was cancelled (`A5101MqttLogic::cancelOtaUpdate`, called from the cancel closure of `A5101MqttLogic::checkOtaVersion`, which logs `弹窗取消升级`, "popup cancel upgrade", my translation) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/cancel_pop` (asm-traced): URL string at `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479e300`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x479e2f8`, in `A5101MqttLogic::cancelOtaUpdate` (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479e240`), sent through `requestHttp` (`@0x479e31c`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `A5101MqttLogic::cancelOtaUpdate` (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart`, call `@0x479e31c`, argument list `@0x479e314`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `A5101MqttLogic::cancelOtaUpdate` (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479e2c8`, 2 keys). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `stationId` | string | yes | `"<stationId>"` | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479e26c` |
| `version` | string | yes | `"<version>"` | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479e288` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479e338`) only interpolates the response object into a log text (`@0x479e35c`..`@0x479e374`, `exeInfo` `@0x479e380`); it reads no key and builds no model. The worksheet entry `A5101OtaCheckUpdateModel` for this URL comes from the caller, not from a parse in this sender.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "stationId": "<stationId>",
  "version": "<version>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart`: `cancelOtaUpdate` @0x479e240 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart::checkOtaVersion`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- `version` is stored as the empty string when the source value is null (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479e2c0`); which version string the caller normally passes was not decoded.
- What the server does with the cancel report: the app ignores the answer.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
