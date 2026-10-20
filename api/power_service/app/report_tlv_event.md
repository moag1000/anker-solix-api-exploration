> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# report_tlv_event

## Purpose

Uploads a device TLV/protobuf event record to the cloud (callers `BaseBleController::postEventDataRequest`, `IotDeviceController::_handleResponse`, `HttpServiceImpl::postEventData`; builder `HttpRequestControllerImpl::postEventData`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/report_tlv_event` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x263e930`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x263ef0c`, in `HttpRequestControllerImpl::postEventData` (`charging/http/http_request_repository_impl.dart @0x263e8c4`), sent through `requestHttp` (`@0x263ef38`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::postEventData` (`charging/http/http_request_repository_impl.dart @0x263e8c4`) picks the path from a map `{"pb": "/app/logging/upload_pb_events", "tlv": "/power_service/v1/app/report_tlv_event"}` (type arguments `<String, String>` `@0x263e93c`) by its type parameter; a type that is not in the map is logged ("postEventData failed, type is not in ...", `@0x263e988`) and nothing is sent. For `"tlv"` the body is a literal built from `device_sn`, `version`, `local_time` (`getCurrentTime()` `@0x263ec98`), `device_model` and `events` = a growable list `<Map<String, Map<String, String>>>` (`@0x263edb4`) holding `{params: {payload: <String>}}` (inner `<String, String>` literal `@0x263ed48`); it is wrapped by two further literals (`<String, Object>` `@0x263ee00`, `<String, Map<String, Object>>` `@0x263ee3c`) whose key layout was not decoded. The `"pb"` body uses `device_sn`, `version`, `local_time`, `device_type`, `protobuf_name` and `events`. The request goes through `requestHttp` (`@0x263ef38`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x263ec64` (`"tlv"` body; `"pb"` body `@0x263ea18`) |
| `version` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x263ec78` |
| `local_time` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x263ec8c` (value from `getCurrentTime()`) |
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
  "local_time": "<?>",
  "device_model": "<?>"
}
```

Response: not synthesized (no capture exists for this endpoint). The real nesting around these keys is not decoded (see Request).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `postEventData` @0x263e8c4 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ble/base_ble_controller.dart::postEventDataRequest`
- `charging/ble/device/iot_anker_controller.dart::_handleResponse`
- `charging/http/http_request_repository.dart::postEventData`
- `charging/impl/http_service_impl.dart::postEventData`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The outer nesting of the `"tlv"` body (two extra literals wrap the inner one) and the exact key layout.
- Types of `device_sn`, `version`, `local_time` and `device_model`.
- How the builder uses the logged-in user id and token it reads before the call (`isLogin` `@0x263ee70`, `getUserId` `@0x263ee80`; two map reads `@0x263ee98`, `@0x263eec4` that fail with a null-cast error when absent).
- The success closure of the call (not decoded) and what the server does with the event.
- The call goes through `requestHttp`, not `encryptionRequestHttp`; whether the plain path encrypts it is decided in `HttpEncryptionDecorator` (`api/encryption.md`), the "Encrypted?" line above is the inventory default.

## Device-tested by

none
