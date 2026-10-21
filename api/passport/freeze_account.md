> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# freeze_account

## Purpose

Freezes the logged-in account; sent by `FreezeAccountLogic::_freezeAccountRequest` (`charging/ui/page/user/freeze_account/freeze_account_logic.dart @0x404c5b8`), whose success closure logs the user out (`performLogout` `@0x404c8a8`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /passport/freeze_account` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x404c770`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x404c768`, in `HttpRequestControllerImpl::freezeAccount` (`charging/http/http_request_repository_impl.dart @0x404c6bc`), sent through `encryptionRequestHttp` (`@0x404c798`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `account` | string | yes | `"<account>"` | `charging/http/http_request_repository_impl.dart @0x404c710` (value store `@0x404c720`) |

The value is a String: map literal with type arguments `<String, String>` (`charging/http/http_request_repository_impl.dart @0x404c724`). The caller (`charging/ui/page/user/freeze_account/freeze_account_logic.dart`) reads the stored user phone (`getUserPhone` `@0x404c604`) before the send; that this is the value of `account` was not decoded.

Source of `account` (traced 2026-10-20, app side): `FreezeAccountLogic::_freezeAccountRequest` (`charging/ui/page/user/freeze_account/freeze_account_logic.dart`) stores the result of `getUserPhone` (`@0x404c604`) in its frame (`stur x0, [fp, #-0x10]`) and passes that slot as the first argument of `freezeAccount` (`@0x404c634`, call `@0x404c640`), so `account` is the stored user phone. `SpUtilImpl::getUserPhone` (`charging/util/save/sp_util_impl.dart @0x34e4608`) reads the shared-preferences key `phone`, decrypts it with the local-info routine (`decryptLocalInfo` `@0x34e4690`) and returns `""` when nothing is stored (`@0x34e466c`, `@0x34e469c`), so the value is a String. The page does not send the e-mail address.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x261b9a0`) reads no response key and calls the stored callback with `true` (`@0x261b9cc`, `ClosureCall` `@0x261b9d4`).

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "account": "<account>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `freezeAccount` @0x404c6bc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::freezeAccount`
- `charging/ui/page/user/freeze_account/freeze_account_logic.dart::_freezeAccountRequest`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the server does with the frozen account (reversibility, session invalidation): not visible in the app; the app logs out after success (`@0x404c8a8`).
- The failure closure of the sender (`charging/http/http_request_repository_impl.dart @0x404c7b4`) logs the code and message and compares no code; the caller's failure callback is the shared closure `StationEnergySystemLogic` `(int, String)` at `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart @0x238c8d0`, which calls `show` with the message string (`@0x238c8ec`) — traced 2026-10-20
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
