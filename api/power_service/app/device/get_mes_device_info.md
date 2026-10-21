> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_mes_device_info

## Purpose

Reads the laser serial number that belongs to a device for the A1340 settings page (callers `HttpRequestControllerImpl::getDeviceLaserSn` from `A1340settingLogic::_getDeviceLaserSn`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/device/get_mes_device_info` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x343b188`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x343b180`, in `HttpRequestControllerImpl::getDeviceLaserSn` (`charging/http/http_request_repository_impl.dart @0x343b0d4`), sent through `encryptionRequestHttp` (`@0x343b1a8`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 1 pair (`AllocateArray`, raw `r2 = 4` at `@0x343b120`, so 2 slots) with type arguments `<String, String>` at `@0x343b13c`, so every value is typed in the literal; all keys are stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x343b128` |

## `param_type`/`cmd`

n/a

## Response model (link)

no model class (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x343b1c4`) reads the key `laser_sn` (string literal `@0x343b1f8`), casts it to `String?` (`@0x343b238`), replaces null by the empty string (`@0x343b260`) and passes it to the stored callback (`ClosureCall` `@0x343b26c`).

## Response

| field | type | required | example | source |
|---|---|---|---|---|
| `laser_sn` | string (nullable, cast `String?`; null becomes `""`) | optional | `"<laser_sn>"` | `charging/http/http_request_repository_impl.dart @0x343b1f8` |

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>"
}
```

Response, synthesized (key read by the success closure; the value is a placeholder)

```json
{
  "data": {
    "laser_sn": "<laser_sn>"
  }
}
```

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getDeviceLaserSn` @0x343b0d4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getDeviceLaserSn`
- `charging/ui/page/device/a1340/a1340setting/a1340setting_logic.dart::_getDeviceLaserSn`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which devices have a laser serial number: server data; the builder falls back to the empty string (`@0x343b260`).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
