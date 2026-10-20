> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# update_device_info_by_app

## Purpose

Uploads the firmware versions of an A5101 station after a Bluetooth OTA (`A5101MqttLogic::_handleNewOtaVersion` and `A5101MqttLogic::_updateVersionInfo`, called from `_handleOTAVersion` and `_listenEvenBus`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/update_device_info_by_app` (asm-traced): URL string at `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b07e4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x23b07dc`, in `A5101MqttLogic::_handleNewOtaVersion` (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b06a0`), sent through `requestHttp` (`@0x23b080c`).

Same URL and method object in the other sender(s) read:

- `A5101MqttLogic::_updateVersionInfo` (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b895c`): URL string `@0x23b8ec8`, method object `Method.post` (`pp+0xa7e0`) at `@0x23b8ec0`, sent through `requestHttp` (`@0x23b8ef0`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `A5101MqttLogic::_handleNewOtaVersion` (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart`, call `@0x23b080c`, argument list `@0x23b0804`), `A5101MqttLogic::_updateVersionInfo` (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart`, call `@0x23b8ef0`, argument list `@0x23b8ee8`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

Two senders. `_handleNewOtaVersion` (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b06a0`) sends the map returned by `_getMergeVersion` (`@0x23b0770`) after adding `main_sn` with `[]=` (`@0x23b07a8`); the keys of that map were not read. `_updateVersionInfo` (`@0x23b895c`) fills a `<String, dynamic>` literal (`@0x23b897c`), which does not type the values, with `time`, `main_sn` and `source` and then with one key per component (`ems`, `pcs`, `pcs2`, `bms`, `dcdc`, `mcu`, `esp32`); each component key is always stored, its value is `Null` when the source list field is null (guard column) and otherwise the result of `map<Map<String, dynamic>>` with a `toJson` closure followed by an unnamed call (`GDT[cid_x0 + 0x3506a]`).

| field | type | required | example | source |
|---|---|---|---|---|
| `main_sn` | ? | yes | ? | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b07a0`; `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b89dc` |
| `time` | ? | yes | ? | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b89ac` |
| `source` | ? | yes | ? | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8a0c` |
| `ems` | ? | yes | `null` or a list built by `map<Map<String, dynamic>>` (guard on the source list `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8a2c`) | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8aac` |
| `pcs` | ? | yes | same shape (guard `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8ad0`) | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8b50` |
| `pcs2` | ? | yes | same shape (guard `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8b74`) | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8bf4` |
| `bms` | ? | yes | same shape (guard `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8c18`) | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8c98` |
| `dcdc` | ? | yes | same shape (guard `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8cbc`) | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8d3c` |
| `mcu` | ? | yes | same shape (guard `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8d60`) | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8de0` |
| `esp32` | ? | yes | same shape (guard `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8e04`) | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8e7c` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the senders (asm-traced): the success closures (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b452c` and `@0x23b8f48`) only log `A5101OtaLogic==new==蓝牙OTA更新成功，上传版本号成功` ("Bluetooth OTA update succeeded, version upload succeeded", my translation); the failure closures (`@0x23b44f0`, `@0x23b8f0c`) log the matching failure text.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "main_sn": "<main_sn>",
  "time": "<time>",
  "source": "<source>",
  "ems": "<ems>",
  "pcs": "<pcs>",
  "pcs2": "<pcs2>",
  "bms": "<bms>",
  "dcdc": "<dcdc>",
  "mcu": "<mcu>",
  "esp32": "<esp32>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart`: `_handleNewOtaVersion` @0x23b06a0 (requestHttp; encrypted: default-true (requestHttp) — verify); `_updateVersionInfo` @0x23b895c (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart::_handleOTAVersion`
- `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart::_listenEvenBus`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The keys and types of the map returned by `_getMergeVersion`, and the types of `time`, `main_sn`, `source` and the component lists.
- The meaning of `source`: the value is stored as received (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b8a0c` region). — traced 2026-10-20: `source` is passed as received by `A5101MqttLogic::_handleNewOtaVersion` and `_updateVersionInfo` (`charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b080c`, `@0x23b8a0c` region); the constant behind it was not decoded
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
