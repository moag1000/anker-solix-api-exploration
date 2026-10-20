> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_system_running_time

## Purpose

Reads the running time of a system for the system-info page (`SystemInfoLogic::_getSystemRunTime` through `HttpRequestControllerImpl::getDeviceRunTime`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_system_running_time` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x293a134`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x293a12c`, in `HttpRequestControllerImpl::getDeviceRunTime` (`charging/http/http_request_repository_impl.dart @0x293a034`), sent through `requestHttp` (`@0x293a15c`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getDeviceRunTime` (`charging/http/http_request_repository_impl.dart`, call `@0x293a15c`, argument list `@0x293a154`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) `HttpRequestControllerImpl::getDeviceRunTime` (`charging/http/http_request_repository_impl.dart @0x293a034`) creates an empty map literal with type arguments `<String, String>` (`@0x293a084`, empty array `@0x293a08c`) and adds keys with `[]=`, so both values are Strings (map type argument read). `sn` is only added when the parameter is non-null (`cmp w3, NULL` `@0x293a0a4`, branch `@0x293a0a8`) and not empty (`cbz w0` `@0x293a0b0`); `stationId` is added unconditionally (`@0x293a0f0`).

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | string | optional | `"<sn>"` | `charging/http/http_request_repository_impl.dart @0x293a0c0` |
| `stationId` | string | yes | `"<stationId>"` | `charging/http/http_request_repository_impl.dart @0x293a0e8` |

## `param_type`/`cmd`

n/a

## Response model (link)

read key by key, no `fromJson`: the success closure (`charging/http/http_request_repository_impl.dart @0x293a220`) logs the body (`@0x293a254`, `exeSuccess` `@0x293a278`), reads the key `runningTime` (`@0x293a280`, lookup `@0x293a2a0`, cast to `int?` `@0x293a2d8`), builds an `A5101SystemInfoModel` (`@0x293a2dc`) and passes it to the stored callback (`ClosureCall` `@0x293a300`). `A5101SystemInfoModel` has no row in `data/models.json`.

## Response

(asm-traced) One key is read by the app: `runningTime` (int?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn": "<sn>",
  "stationId": "<stationId>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure (`charging/http/http_request_repository_impl.dart @0x293a178`) was not read for compares.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getDeviceRunTime` @0x293a034 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getDeviceRunTime`
- `charging/ui/page/device/a5101/setting/system_info/system_info_logic.dart::_getSystemRunTime`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The unit of `runningTime`: the app stores the number in `A5101SystemInfoModel`; the page that shows it was not read.
- Which of `sn` and `stationId` the system-info page fills: only the sender was read.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
