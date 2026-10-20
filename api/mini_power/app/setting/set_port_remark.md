> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# set_port_remark

## Purpose

Saves the remark (name) a user gives to a charger port on the A2345 home page (caller `_saveDeviceName` in the A2345 home logic) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/setting/set_port_remark` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3e44a24`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3e44a1c`, in `HttpRequestControllerImpl::setPortRemark` (`charging/http/http_request_repository_impl.dart @0x3e44940`), sent through `encryptionRequestHttp` (`@0x3e44a4c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::setPortRemark` (`charging/http/http_request_repository_impl.dart @0x3e44940`) stores three keys unconditionally in a map literal with type arguments `<String, String>` (`@0x3e449d8`), so all three values are Strings.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x3e4499c` (map literal `<String, String>` `charging/http/http_request_repository_impl.dart @0x3e449d8`) |
| `port_name` | string | yes | `"<port_name>"` | `charging/http/http_request_repository_impl.dart @0x3e449b0` (same literal) |
| `remark` | string | yes | `"<remark>"` | `charging/http/http_request_repository_impl.dart @0x3e449c4` (same literal) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the sender's success closure `charging/http/http_request_repository_impl.dart @0x2268374` forwards its argument to the stored callback (`ClosureCall` `@0x22683a8`); the callback in the only caller (closure `charging/ui/page/device/a2345/a2345home/a2345home_logic.dart @0x3e44afc` in `A2345homeLogic::_saveDeviceName`) declares no parameter use: it closes the name sheet (`_closeDeviceNameSheet` `@0x3e44b44`) and reloads the port names (`getDevicePortNames` `@0x3e44b54`), and its setup (`@0x3e44b08`) names only the logic object.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>",
  "port_name": "<port_name>",
  "remark": "<remark>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`. The caller's failure callback (closure `charging/ui/page/device/a2345/a2345home/a2345home_logic.dart @0x3e44a68`) shows a dialog with no code comparison.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `setPortRemark` @0x3e44940 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::setPortRemark`
- `charging/ui/page/device/a2345/a2345home/a2345home_logic.dart::_saveDeviceName`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which `port_name` values are valid: `get_port_remarks` lists `C1`, `C2`, `C3`, `C4`, `A1` and `A2` on the read side; whether the server restricts the write side to them is not shown.
- Length or character limits of `remark`: the caller trims a text value before the call (`trim` in `charging/ui/page/device/a2345/a2345home/a2345home_logic.dart @0x3e44868`, closure `@0x3e447c0`) but no limit was read.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
