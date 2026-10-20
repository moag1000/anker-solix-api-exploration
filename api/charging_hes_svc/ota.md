> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# ota

## Purpose

Starts the OTA firmware upgrade of a station now (`A5101FirmwareUpdateLogic::sendStartOtaUpdate`) or schedules it with a delay (`A5101FirmwareUpdateLogic::sendSetTimeOta`); callers `_parseMinSoc`, `onInit` and `showChooseTimerView` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/ota` (asm-traced): URL string at `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x42ea7bc`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x42ea7b4`, in `A5101FirmwareUpdateLogic::sendSetTimeOta` (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x42ea618`), sent through `requestHttp` (`@0x42ea7e4`).

Same URL and method object in the other sender(s) read:

- `A5101FirmwareUpdateLogic::sendStartOtaUpdate` (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x347bee8`): URL string `@0x347c124`, method object `Method.post` (`pp+0xa7e0`) at `@0x347c11c`, sent through `requestHttp` (`@0x347c14c`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `A5101FirmwareUpdateLogic::sendSetTimeOta` (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart`, call `@0x42ea7e4`, argument list `@0x42ea7dc`), `A5101FirmwareUpdateLogic::sendStartOtaUpdate` (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart`, call `@0x347c14c`, argument list `@0x347c144`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

Both senders store keys in a map literal with type arguments `<String, Object>` (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x42ea770`; `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x347c0d8`), which do not type the values. `stationId` is `field_97` of `A5101MqttLogic` (`@0x42ea6ec`); its declaration was not read. In `sendSetTimeOta`, `delay` is boxed from an unboxed 64-bit integer (`BoxInt64Instr` `@0x42ea734`): the first field of the parameter object (`@0x42ea658`) times 3600 (`mul` `@0x42ea66c`), or -1 when that field is 0 (`cbnz x3` `@0x42ea65c`, `r3 = -1` `@0x42ea660`).

| field | type | required | example | source |
|---|---|---|---|---|
| `stationId` | ? | yes | ? | `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x42ea6bc`; `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x347c060` |
| `delay` | int (unboxed, x) | yes (`sendSetTimeOta` only) | a number of seconds, or -1 | `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x42ea724` |

## `param_type`/`cmd`

n/a

## Response model (link)

read key by key, no `fromJson`, both senders: the success closure (`charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart @0x42ea868` for `sendSetTimeOta`, `@0x3481860` for `sendStartOtaUpdate`) reads the key `messageId` (`@0x42ea894`, cast `String?` `@0x42ea8ec`; `@0x348188c`, cast `@0x34818e4`), stores it in a controller field when it is non-empty (`cbz w1` `@0x42ea908`; `@0x3481900`) and calls `timeOut` (`@0x42ea948`; `@0x3481944`).

## Response

(asm-traced) One key is read by the app: `messageId` (String?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "stationId": "<stationId>",
  "delay": "<delay>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

The failure closure of `sendSetTimeOta` (`a5101_firmware_update_logic.dart @0x42ea800`) compares the code with a tagged 32-bit immediate (`r17 = 400000` `@0x42ea818`, `cmp w0, w17` `@0x42ea820`, so code 200000): the equal path shows `deviceIsOffline` (`@0x42ea828`), every other code shows the message (`show` `@0x42ea844`). The failure closure of `sendStartOtaUpdate` is the folded closure `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart @0x238c8d0`, which shows the message (`show` `@0x238c8ec`). Code meanings are owned by `api/errors.md` (200000 is listed there).

## Callers in app

- `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart`: `sendSetTimeOta` @0x42ea618 (requestHttp; encrypted: default-true (requestHttp) — verify); `sendStartOtaUpdate` @0x347bee8 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart::_parseMinSoc`
- `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart::onInit`
- `charging/ui/page/device/a5101/setting/firmware_update/a5101_firmware_update_logic.dart::showChooseTimerView`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The type of `stationId`: `field_97` of `A5101MqttLogic` was not resolved to a declaration.
- The unit and meaning of the first field of the delay parameter (times 3600, so probably hours): only the arithmetic was read.
- How `messageId` is matched with the MQTT progress messages: `timeOut` was not read.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
