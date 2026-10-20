> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_relate_belong

## Purpose

Reads the "belong type" (ownership relation) of a device for the A1790 home page (callers `HttpRequestControllerImpl::getDeviceBindInfo` from `A1790homeLogic::getA1790DeviceBindInfo`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/device/get_relate_belong` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x33d3e34`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x33d3e2c`, in `HttpRequestControllerImpl::getDeviceBindInfo` (`charging/http/http_request_repository_impl.dart @0x33d3d80`), sent through `encryptionRequestHttp` (`@0x33d3e64`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 1 pair (`AllocateArray`, raw `r2 = 4` at `@0x33d3dcc`, so 2 slots) with type arguments `<String, String>` at `@0x33d3de8`, so every value is typed in the literal; all keys are stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x33d3dd4` |

## `param_type`/`cmd`

n/a

## Response model (link)

no model class (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x33d3e80`) reads the key `belong_type` (string literal `@0x33d3eac`), casts it to `int?` (`@0x33d3ef8`) and passes it to the stored callback (`ClosureCall` `@0x33d3f20`).

## Response

| field | type | required | example | source |
|---|---|---|---|---|
| `belong_type` | int (nullable, cast `int?`) | optional | `?` | `charging/http/http_request_repository_impl.dart @0x33d3eac` |

Consumer of `belong_type` (asm-traced): `A1790homeLogic.getA1790DeviceBindInfo` (`charging/ui/page/device/a1790/a1790home_logic.dart @0x33d3c8c`) passes a success closure with an `int?` parameter (`@0x33d416c`). It tests the value: Smi 0 (`cbnz w0` `@0x33d4194`) calls `showUnbindDialog` (`@0x33d41a0`); the tagged 4, so 2 (`cmp w0, #4` `@0x33d41a8`), calls `showOtherBindDialog` (`@0x33d41d0`); any other value, and null, does nothing (`@0x33d41d4`). The error closure (`@0x33d3fe0`) logs `get A1790 Device Bind Info error` (`@0x33d4008`) and also calls `showUnbindDialog` (`@0x33d4024`). `objs.txt` holds no enum object with `belong` in its name (searched 2026-10-20), so the numbers have no app-side name beyond these two reactions.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>"
}
```

Response, synthesized (key read by the success closure; the value is not known)

```json
{
  "data": {
    "belong_type": "<int>"
  }
}
```

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getDeviceBindInfo` @0x33d3d80 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getDeviceBindInfo`
- `charging/ui/page/device/a1790/a1790home_logic.dart::getA1790DeviceBindInfo`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the numeric `belong_type` values mean beyond the two app reactions (0 shows the unbind dialog, 2 the other-bind dialog, other values do nothing; see Response). — reclassified: server (not visible in the app: no enum object or name for the numbers exists in the code read)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
