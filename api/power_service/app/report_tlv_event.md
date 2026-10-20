> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# report_tlv_event

## Purpose

Uploads a device TLV/protobuf event record to the cloud (callers `BaseBleController::postEventDataRequest`, `IotDeviceController::_handleResponse`, `HttpServiceImpl::postEventData`; builder `HttpRequestControllerImpl::postEventData`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/report_tlv_event` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x263e930`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x263ef0c`, in `HttpRequestControllerImpl::postEventData` (`charging/http/http_request_repository_impl.dart @0x263e8c4`), sent through `requestHttp` (`@0x263ef38`).

## Encrypted?

Plain-wrapper call (asm-traced): the sender calls `HttpRequestControllerImpl::requestHttp` (`charging/http/http_request_repository_impl.dart @0x2264938`) at `charging/http/http_request_repository_impl.dart @0x263ef38` without a `needEncryption` argument. So the default `needEncryption: true` applies and rule 3 of [encryption.md](../../encryption.md#rule-and-resulting-counts) holds: the SDK path is taken whenever the SDK reports a logged-in state and the URL passes the base-URL predicate, otherwise the plain Dio path; that is decided at run time by `HttpEncryptionDecorator::request` (`charging/http/HttpEncryptionDecorator.dart @0x4868ff4`), not by this page.

## Request

(asm-traced) `HttpRequestControllerImpl::postEventData` (`charging/http/http_request_repository_impl.dart @0x263e8c4`) picks the path from a map `{"pb": "/app/logging/upload_pb_events", "tlv": "/power_service/v1/app/report_tlv_event"}` (type arguments `<String, String>` `@0x263e93c`) by its type parameter; a type that is not in the map is logged ("postEventData failed, type is not in ...", `@0x263e988`) and nothing is sent. For `"tlv"` the body is a literal built from `device_sn`, `version`, `local_time` (`getCurrentTime()` `@0x263ec98`), `device_model` and `events` = a growable list `<Map<String, Map<String, String>>>` (`@0x263edb4`) holding `{params: {payload: <String>}}` (inner `<String, String>` literal `@0x263ed48`); the five-pair map is made by the `<String, Object>` literal `@0x263ee00` (`Map._fromLiteral` `@0x263ee10`) and then stored under the type key in the lookup map `<String, Map<String, Object>>` (`@0x263ee3c`, `@0x263ee4c`); the builder reads that map back with the `type` argument (`GDT[cid_x0 + 0x735]` index `@0x263eec4`) together with the path map (`@0x263ee98`), so the body that is sent is the five-pair map itself and the outer literals are lookup tables keyed by `"pb"` and `"tlv"`, not wrappers on the wire (a missing entry ends in a null-cast error, `@0x263ef60`, `@0x263ef64`). The builder calls `isLogin` (`@0x263ee70`) and `getUserId` (`@0x263ee80`) before that lookup but uses neither result afterwards in the instructions up to the request (`@0x263ef38`); `getCurrentTime` (`charging/util/date_util.dart @0x24a0e98`) calls `formatDate` (`@0x24a0f80`) with the tokens `yyyy`, `mm`, `dd`, `HH`, `mm`, `ss` joined by `-`, ` ` and `:` (`@0x24a0eec`..`@0x24a0f50`), so `local_time` is a string of the form `yyyy-mm-dd HH:mm:ss` as the app writes the pattern. The `"pb"` body uses `device_sn`, `version`, `local_time`, `device_type`, `protobuf_name` and `events`. The request goes through `requestHttp` (`@0x263ef38`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x263ec64` (`"tlv"` body; `"pb"` body `@0x263ea18`) |
| `version` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x263ec78` |
| `local_time` | string | yes | | `charging/http/http_request_repository_impl.dart @0x263ec8c` (value from `getCurrentTime()`) |
| `device_model` | ? | yes (`"tlv"` body) | ? | `charging/http/http_request_repository_impl.dart @0x263ecc8` |
| `events` | list | yes | ? | `charging/http/http_request_repository_impl.dart @0x263ed00` |
| `events[].params.payload` | string | yes | `"<payload>"` | `charging/http/http_request_repository_impl.dart @0x263ed34` (inner literal `<String, String>` `@0x263ed48`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed in the builder (asm-traced): both closures passed to `requestHttp` (`r4 = const [0x1, 0x7, 0x7, 0x5, fail, 0x6, showLoading, 0x5, null]` at `charging/http/http_request_repository_impl.dart @0x263ef30`) are not model parsers; the success handling was not decoded.

## Response

Not read in the builder.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "events": [
    {
      "params": {
        "payload": "<payload>"
      }
    }
  ],
  "device_sn": "<?>",
  "version": "<?>",
  "local_time": "<yyyy-mm-dd HH:mm:ss>",
  "device_model": "<?>"
}
```

Response: not synthesized (no capture exists for this endpoint). The body is the flat map shown above (see Request).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `postEventData` @0x263e8c4 (requestHttp, default `needEncryption: true`)

Called from:

- `charging/ble/base_ble_controller.dart::postEventDataRequest`
- `charging/ble/device/iot_anker_controller.dart::_handleResponse`
- `charging/http/http_request_repository.dart::postEventData`
- `charging/impl/http_service_impl.dart::postEventData`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `device_sn`, `version` and `device_model`: arguments of `HttpRequestControllerImpl::postEventData` (`charging/http/http_request_repository_impl.dart @0x263e8d0`) — attempted 2026-10-20 (two-hop not readable: the caller `S1S2HomeLogic._listenRealTimeData` (`s1_s2/src/page/home/s1_s2_home_logic.dart @0x3553344`) passes three values with the String literal `""` as null default, but which argument slot feeds which key is not shown by a symbol. Header stays string-only)
- The success closure of the call (not decoded) and what the server does with the event.

## Device-tested by

none
