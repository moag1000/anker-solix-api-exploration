> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# user_fault_alarm

## Purpose

Reports the faults of a station to the cloud from the device main page (`DeviceMainLogic::requesetDeviceReport`, through `HttpRequestControllerImpl::sendDeviceReport`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/user_fault_alarm` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x2605634`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x260562c`, in `HttpRequestControllerImpl::sendDeviceReport` (`charging/http/http_request_repository_impl.dart @0x26055b4`), sent through `requestHttp` (`@0x260565c`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::sendDeviceReport` (`charging/http/http_request_repository_impl.dart`, call `@0x260565c`, argument list `@0x2605654`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

The body is not built in the sender: `HttpRequestControllerImpl::sendDeviceReport` (`charging/http/http_request_repository_impl.dart @0x26055b4`) receives the map as a parameter. It is built in the caller `DeviceMainLogic::requesetDeviceReport` (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x2605210`) as a `<String, Object?>` literal (`@0x26054fc`), which does not type the values; the call is `sendDeviceReport` (`@0x2605544`). `timeStamp` is the current time in seconds: `_getCurrentMicros` divided twice by 1000 (`sdiv` `@0x260529c`, `@0x26052a0`) and boxed from an unboxed 64-bit integer (`BoxInt64Instr` `@0x2605478`). `stationId` is `field_7` of the `StationMainPageLogic` value (load `@0x26053d0`, fallback `""` `@0x26053e0`); `StationMainPageLogic` holds an `Rx<StationModel>` (`charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart @0x22597b0`) and `StationModel.field_7` is declared `String?` (cast `@0x238e858`, store `@0x238e870` in `base_service/ak_iot_kit/business/basic/model/station_model.dart`). `pn` is a field of `A5101BleLogic` or `Null` (`@0x2605368`); `errorInfos`, `isClearAllFaults` and `isFirstFaultReport` are parameters stored as received; `localTime` is the result of `getDateTimeFormat` (`@0x26052f0`).

| field | type | required | example | source |
|---|---|---|---|---|
| `pn` | ? | yes | ? | `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x2605308` |
| `stationId` | string | yes | `"<stationId>"` | `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x26053a4` |
| `errorInfos` | ? | yes | ? | `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x2605424` |
| `isClearAllFaults` | ? | yes | ? | `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x260545c` |
| `timeStamp` | int (unboxed, x) | yes | current time in seconds | `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x260546c` |
| `localTime` | ? | yes | a formatted time text | `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x26054b4` |
| `isFirstFaultReport` | ? | yes | ? | `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x26054ec` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the sender (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x2605678`) applies `jsonEncode` to the response (`@0x26056a8`) and passes the text to the stored callback (`ClosureCall` `@0x26056c4`); the failure closure is the folded forwarder `@0x226824c`.

## Response

No response key is read in the sender; the whole response is handed on as JSON text.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "pn": "<pn>",
  "stationId": "<stationId>",
  "errorInfos": "<errorInfos>",
  "isClearAllFaults": "<isClearAllFaults>",
  "timeStamp": "<timeStamp>",
  "localTime": "<localTime>",
  "isFirstFaultReport": "<isFirstFaultReport>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `sendDeviceReport` @0x26055b4 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::sendDeviceReport`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::requesetDeviceReport`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The types of `pn`, `errorInfos`, `isClearAllFaults`, `localTime` and `isFirstFaultReport`: the values are parameters, fields or call results not typed at a readable declaration. — attempted 2026-10-20 (two-hop not readable: `requesetDeviceReport` (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x2605544`) pass slots or fields of their own frames; no literal or declared type in the argument setups)
- The structure of `errorInfos`: it is the parameter `fp-0x18` of `requesetDeviceReport` stored as received (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x2605438`).
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
