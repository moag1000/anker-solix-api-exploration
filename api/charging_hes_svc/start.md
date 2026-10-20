> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# start

## Purpose

Switches a station on or off remotely from the remote-switch page (`RemoteSwitchLogic::remoteRequestDeviceStart`, called from `chooseEvent`); the failure closure logs `开关机失败：` ("power on/off failed", my translation) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/start` (asm-traced): URL string at `charging/ui/page/device/a5101/setting/remote_switch/remote_switch_logic.dart @0x3ea96b4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3ea96ac`, in `RemoteSwitchLogic::remoteRequestDeviceStart` (`charging/ui/page/device/a5101/setting/remote_switch/remote_switch_logic.dart @0x3ea956c`), sent through `requestHttp` (`@0x3ea96dc`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `RemoteSwitchLogic::remoteRequestDeviceStart` (`charging/ui/page/device/a5101/setting/remote_switch/remote_switch_logic.dart`, call `@0x3ea96dc`, argument list `@0x3ea96d4`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`RemoteSwitchLogic::remoteRequestDeviceStart` (`charging/ui/page/device/a5101/setting/remote_switch/remote_switch_logic.dart @0x3ea956c`) stores 2 keys in a map literal with type arguments `<String, Object>` (`@0x3ea9668`), which do not type the values. `start` is an integer built from the boolean parameter: `tst x3, #0x10` (`@0x3ea9658`, Dart true has bit 4 clear), `cset x0, eq` (`@0x3ea965c`), `lsl x0, x0, #1` (`@0x3ea9660`) gives the Smi 1 for true and 0 for false. `station_id` is `field_7` of the value of `StationMainPageLogic` (load `@0x3ea9604`, fallback `""` `@0x3ea9614`). `StationMainPageLogic` holds an `Rx<StationModel>` (`charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart @0x22597b0`, stored `@0x22597cc`); `StationModel.field_7` is declared `String?` (cast `r8 = String?` `@0x238e858`, store `@0x238e870` in `base_service/ak_iot_kit/business/basic/model/station_model.dart`, key `site_id` `@0x238e808`), so the value is a String with the empty string as fallback.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes | `"<station_id>"` | `charging/ui/page/device/a5101/setting/remote_switch/remote_switch_logic.dart @0x3ea95d8` |
| `start` | int (Smi, w) | yes | `1` for true, `0` for false (the boolean parameter) | `charging/ui/page/device/a5101/setting/remote_switch/remote_switch_logic.dart @0x3ea9650` |

## `param_type`/`cmd`

n/a

## Response model (link)

read key by key, no `fromJson`: the success closure (`charging/ui/page/device/a5101/setting/remote_switch/remote_switch_logic.dart @0x3ea975c`) reads the key `messageId` (`@0x3ea9788`, lookup `@0x3ea97a8`, cast to `String?` `@0x3ea97e0`), and when it is non-empty (`cbz w1` `@0x3ea97f4`) stores it in a controller field (`@0x3ea9804`) and calls `timeOut` (`@0x3ea9824`).

## Response

(asm-traced) One key is read by the app: `messageId` (String?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "start": 1
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure (`charging/ui/page/device/a5101/setting/remote_switch/remote_switch_logic.dart @0x3ea96f8`) logs `开关机失败：` and the message and calls `exeError` (`@0x3ea9740`) without comparing the code.

## Callers in app

- `charging/ui/page/device/a5101/setting/remote_switch/remote_switch_logic.dart`: `remoteRequestDeviceStart` @0x3ea956c (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a5101/setting/remote_switch/remote_switch_logic.dart::chooseEvent`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What `messageId` is used for: the app stores it and starts `timeOut`; the matching MQTT message was not read for this page.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
