> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_port_remarks

## Purpose

Reads the user-given remarks of the charger ports for the A2345 home page (caller `getDevicePortNames` in the A2345 home logic) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/setting/get_port_remarks` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3473b70`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3473b68`, in `HttpRequestControllerImpl::getPortRemarks` (`charging/http/http_request_repository_impl.dart @0x3473abc`), sent through `encryptionRequestHttp` (`@0x3473b98`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::getPortRemarks` (`charging/http/http_request_repository_impl.dart @0x3473abc`) stores one key, `device_sn`, unconditionally in a map literal with type arguments `<String, String>` (`@0x3473b24`), so the value is a String.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x3473b10` (map literal `<String, String>` `charging/http/http_request_repository_impl.dart @0x3473b24`) |

## `param_type`/`cmd`

n/a

## Response model (link)

No model class (asm-traced): the sender's success closure `charging/http/http_request_repository_impl.dart @0x2268374` forwards the response to the stored callback unread (`ClosureCall` `@0x22683a8`). The callback of the only caller (closure `charging/ui/page/device/a2345/a2345home/a2345home_logic.dart @0x3473c2c` in `A2345homeLogic::getDevicePortNames`, `@0x34739bc`) reads the key `port_remarks` (`@0x3473c78`), casts it to `List` (`@0x3473d5c`) and reads from each element the keys `port_name` (`@0x3473e38`, cast `String?` `@0x3473e88`) and `remark` (`@0x3473e9c`, cast `String?` `@0x3473eec`); it compares the port names with the literals `C1` (`@0x3473f68`), `C2` (`@0x3473fcc`), `C3` (`@0x3474030`), `C4` (`@0x3474098`), `A1` (`@0x3474100`) and `A2` (`@0x3474168`) and stores the result with `setDevicePortRemarks` (`@0x34743d0`).

## Response

Top-level key read by the app: `port_remarks` (list). Keys of one element read by the app: `port_name` (String?) and `remark` (String?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getPortRemarks` @0x3473abc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getPortRemarks`
- `charging/ui/page/device/a2345/a2345home/a2345home_logic.dart::getDevicePortNames`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Whether the server returns ports other than `C1`, `C2`, `C3`, `C4`, `A1` and `A2`: the caller only matches these six names; other names are not shown to be handled.
- Whether the server can omit `port_remarks` entirely: the closure casts the key to `List` without a null branch (`@0x3473d5c`).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
