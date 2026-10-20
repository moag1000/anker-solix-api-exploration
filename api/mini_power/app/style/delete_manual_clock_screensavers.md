> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# delete_manual_clock_screensavers

## Purpose

Deletes one user-made clock screensaver of an A2345 charger (caller `deleteCustomClockScreenSavers` in the A2345 custom-clock logic) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/style/delete_manual_clock_screensavers` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3e21000`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3e20ff8`, in `HttpRequestControllerImpl::deleteA2345CustomClockScreenSavers` (`charging/http/http_request_repository_impl.dart @0x3e20f2c`), sent through `requestHttp` (`@0x3e21028`).

## Encrypted?

encrypted: `true` (asm-traced). `HttpRequestControllerImpl::requestHttp` declares `needEncryption = true` as its default (`charging/http/http_request_repository_impl.dart @0x2264944`) and this sender's argument descriptor names only `fail` and `showLoading` (`@0x3e21020`), so the default applies; the request then takes the decorator path described in `api/encryption.md`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::deleteA2345CustomClockScreenSavers` (`charging/http/http_request_repository_impl.dart @0x3e20f2c`) stores one key, `id`, unconditionally in a map literal with type arguments `<String, dynamic>` (`@0x3e20fb8`); the value is an unboxed 64-bit integer boxed by `BoxInt64Instr` (`@0x3e20fa0`). The caller parses its id from a String with `parse` (`charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart @0x3e20e54`) before the call (`@0x3e20e90`).

| field | type | required | example | source |
|---|---|---|---|---|
| `id` | int (unboxed, x) | yes | | `charging/http/http_request_repository_impl.dart @0x3e20f90` (map literal `<String, dynamic>` `charging/http/http_request_repository_impl.dart @0x3e20fb8`, value boxed by `BoxInt64Instr` `@0x3e20fa0`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the sender's success closure `charging/http/http_request_repository_impl.dart @0x2268374` forwards its argument to the stored callback unread (`ClosureCall` `@0x22683a8`); the callback in the only caller (closure `charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart @0x3e21158` in `A2345CustomClockLogic::deleteCustomClockScreenSavers`) never reads its argument slot (setup `@0x3e21164`), it dismisses the loading overlay, removes the item from the list and sends an event.

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "id": "<int>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. The failure closure `charging/http/http_request_repository_impl.dart @0x26c8be8` logs the code and message (`exeError`) and passes both on to the stored callback unread. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `deleteA2345CustomClockScreenSavers` @0x3e20f2c (requestHttp; encrypted: true, `needEncryption` default)

Called from:

- `charging/http/http_request_repository.dart::deleteA2345CustomClockScreenSavers`
- `charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart::deleteCustomClockScreenSavers`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the server does when the id does not exist or belongs to another user: the app ignores the answer body.
- Which id the caller passes beyond "the id of an entry listed by `get_manual_clock_screensavers`" (the caller parses it from a String field, `@0x3e20e54`).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
