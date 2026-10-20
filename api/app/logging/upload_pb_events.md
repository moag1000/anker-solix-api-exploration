> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# upload_pb_events

## Purpose

Uploads batched protobuf device events (and, with the other type, TLV events) reported by a device; `HttpRequestControllerImpl::postEventData` is called from `BaseBleController::postEventDataRequest`, `IotAnkerController::_handleResponse` and `HttpServiceImpl::postEventData` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /app/logging/upload_pb_events` (asm-traced): `HttpRequestControllerImpl::postEventData` (`charging/http/http_request_repository_impl.dart @0x263e8c4`) holds a map from the event type to a path (`<String, String>` `@0x263e93c`): `"pb"` (`@0x263e90c`) maps to `/app/logging/upload_pb_events` (`@0x263e918`) and `"tlv"` (`@0x263e924`) to `/power_service/v1/app/report_tlv_event` (`@0x263e930`; the sibling endpoint `report_tlv_event` of `power_service`). A type that is not a key is logged as `postEventData failed, type is not in ` (`@0x263e988`) and nothing is sent. The path is passed to `requestHttp` (`@0x263ef38`) with the method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x263ef0c`.

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

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

- Types of `device_sn`, `version`, `local_time`, `device_type` and `device_model`: parameters and results of `getCurrentTime` stored into a `<String, Object>` literal.
- How the payload is encoded (the value of `events[].params.payload` is a String, by the inner literal type; whether it is base64 of a protobuf is not visible here).
- What the code at `charging/http/http_request_repository_impl.dart @0x263ee70` does after the body is built (`isLogin`, `getUserId` and two map lookups): it may add user identifiers to a header or the body, not decoded.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
