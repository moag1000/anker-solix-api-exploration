> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# upload_pb_events

## Purpose

Uploads batched protobuf device events (and, with the other type, TLV events) reported by a device; `HttpRequestControllerImpl::postEventData` is called from `BaseBleController::postEventDataRequest`, `IotAnkerController::_handleResponse` and `HttpServiceImpl::postEventData` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/logging/upload_pb_events` (asm-traced): `HttpRequestControllerImpl::postEventData` (`charging/http/http_request_repository_impl.dart @0x263e8c4`) holds a map from the event type to a path (`<String, String>` `@0x263e93c`): `"pb"` (`@0x263e90c`) maps to `/app/logging/upload_pb_events` (`@0x263e918`) and `"tlv"` (`@0x263e924`) to `/power_service/v1/app/report_tlv_event` (`@0x263e930`; the sibling endpoint `report_tlv_event` of `power_service`). A type that is not a key is logged as `postEventData failed, type is not in ` (`@0x263e988`) and nothing is sent. The path is passed to `requestHttp` (`@0x263ef38`) with the method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x263ef0c`.

## Encrypted?

encrypted: `true` (asm-traced default): the sender calls `requestHttp` with the named arguments `fail` and `showLoading` only (`charging/http/http_request_repository_impl.dart @0x263ef30`), and `requestHttp` declares `needEncryption = true` (`charging/http/http_request_repository_impl.dart @0x2264944`). Scheme and header rules: `api/encryption.md`.

## Request

The body is built per type; this table is the `pb` variant (the TLV variant is described below). The outer map literal has type arguments `<String, Object>` (`charging/http/http_request_repository_impl.dart @0x263ec18`), not evidence of a value type.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x263ea18` |
| `version` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x263ea2c` |
| `local_time` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x263ea40` (value from `getCurrentTime` `@0x263ea4c`) |
| `device_type` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x263ea7c` |
| `protobuf_name` | string | yes | `""` when the argument is null | `charging/http/http_request_repository_impl.dart @0x263eab4` (null fallback `""` `@0x263eacc`) |
| `events` | list | yes | ? | `charging/http/http_request_repository_impl.dart @0x263eb08` (growable list of `Map<String, Map<String, String>>` `@0x263eb88`) |
| `events[].params.payload` | string | yes | ? | `charging/http/http_request_repository_impl.dart @0x263eb3c` (inner map `<String, String>` `@0x263eb50`, key `params` `@0x263eb24`) |

The `tlv` variant builds `device_sn` (`@0x263ec64`), `version` (`@0x263ec78`), `local_time` (`@0x263ec8c`), `device_model` (`@0x263ecc8`) and the same `events` structure (`events` `@0x263ed00`, `params` `@0x263ed1c`, `payload` `@0x263ed34`) and is sent to the TLV path.

Payload and type (traced 2026-10-20, app side): in the caller `IotAnkerController::_handleResponse` (`charging/ble/device/iot_anker_controller.dart`) a value is tested as `List<int>` (`@0x3b6a76c`) and, when it is one, encoded with `base64Encode` (`@0x3b6a7a0`), otherwise replaced by the empty string (`@0x3b6a7ac`); that text is the first value passed to `postEventData` (`@0x3b6aa50`), together with the type argument `"pb"` (`@0x3b6aa40`, `@0x3b6aa48`). So `events[].params.payload` is the base64 text of a byte list taken from the device answer (a `List<int>`); whether those bytes are a protobuf message is not visible in the Dart code (the endpoint and the key `protobuf_name` suggest it). The second caller `HttpServiceImpl::postEventData` (`charging/impl/http_service_impl.dart @0x35533a0`) also passes the constant `"pb"` (`@0x3553390`).

What the code after the body does (traced 2026-10-20): `postEventData` calls `isLogin` (`charging/http/http_request_repository_impl.dart @0x263ee70`) and, when it returns true, `getUserId` (`@0x263ee80`), but the result of `getUserId` is not stored (the next instructions load other registers, `@0x263ee84`..`@0x263ee8c`), so no user identifier is added to the body or a header here; the following two lookups (`[]` with the type argument as key, `@0x263ee98`, `@0x263eec4`) pick the per-type entries and are null-checked (`@0x263eeb0`, `@0x263eed8`).

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the sender passes no success callback to `requestHttp` (the named arguments are `fail` and `showLoading`, `charging/http/http_request_repository_impl.dart @0x263ef30`), so no `fromJson` or closure reads the response.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body of the `pb` variant; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>",
  "version": "<version>",
  "local_time": "<local_time>",
  "device_type": "<device_type>",
  "protobuf_name": "<protobuf_name>",
  "events": [
    {
      "params": {
        "payload": "<payload>"
      }
    }
  ]
}
```

Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender or its closures read for this page. Code meanings are owned by `api/errors.md`.

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

- Types of `device_sn`, `version`, `local_time`, `device_type` and `device_model`: parameters and results of `getCurrentTime` stored into a `<String, Object>` literal. — attempted 2026-10-20 (two-hop not readable: the three callers pass values of their own frame slots, `iot_anker_controller.dart @0x3b6aa50`..`@0x3b6aa60`, `http_service_impl.dart @0x35533a0`, `base_ble_controller.dart @0x263e83c` region; no declared type is read)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
