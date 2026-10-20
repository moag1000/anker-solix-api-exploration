> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_manual_clock_screensaver_name

## Purpose

Renames a user-made clock screensaver of an A2345 charger (caller `_saveScreenName` in the A2345 custom-clock logic) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/style/set_manual_clock_screensaver_name` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3e22a40`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3e22a38`, in `HttpRequestControllerImpl::editA2345CustomClockScreenSaversName` (`charging/http/http_request_repository_impl.dart @0x3e22940`), sent through `requestHttp` (`@0x3e22a68`).

## Encrypted?

encrypted: `true` (asm-traced). `HttpRequestControllerImpl::requestHttp` declares `needEncryption = true` as its default (`charging/http/http_request_repository_impl.dart @0x2264944`) and this sender's argument descriptor names only `fail` and `showLoading` (`@0x3e22a60`), so the default applies; the request then takes the decorator path described in `api/encryption.md`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced for the stores, `?` where the value is not typed) `HttpRequestControllerImpl::editA2345CustomClockScreenSaversName` (`charging/http/http_request_repository_impl.dart @0x3e22940`) stores three keys unconditionally in a map literal with type arguments `<String, dynamic>` (`@0x3e229f8`); `screensaver_id` is an unboxed 64-bit integer boxed by `BoxInt64Instr`, `sn` and `name` come from parameters and are not typed.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3e229ac` (parameter, not typed by the builder) |
| `screensaver_id` | int (unboxed, x) | yes | ? | `charging/http/http_request_repository_impl.dart @0x3e229c0` (value boxed by `BoxInt64Instr` `charging/http/http_request_repository_impl.dart @0x3e229d0`) |
| `name` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3e229e8` (parameter, not typed by the builder) |

## `param_type`/`cmd`

n/a

## Response model (link)

Not read: the sender's success closure `charging/http/http_request_repository_impl.dart @0x2268374` forwards its argument to the stored callback unread (`ClosureCall` `@0x22683a8`); the caller's success callback (`_saveScreenName` in `a2345custom_clock_logic.dart`) was not decoded.

## Response

No response key is confirmed read (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn": "<?>",
  "screensaver_id": "<int>",
  "name": "<?>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. The failure closure `charging/http/http_request_repository_impl.dart @0x276bbdc` logs the code and message (`exeError`) and passes both on to the stored callback unread. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `editA2345CustomClockScreenSaversName` @0x3e22940 (requestHttp; encrypted: true, `needEncryption` default)

Called from:

- `charging/http/http_request_repository.dart::editA2345CustomClockScreenSaversName`
- `charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart::_saveScreenName`

Caller side (traced 2026-10-20, app side): `A2345CustomClockLogic::_saveScreenName` (`charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart @0x3e2263c`) takes the new name from the text of an input controller (`field_d7`, `field_27` then `field_7`, `@0x3e22658`..`@0x3e22668`); its success closure (`@0x3e22a7c`, argument `dynamic`, not read) finds the entry in the local list (`indexWhere` `@0x3e22af0`) and updates the name there. No length check is made in these functions.

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `sn` and `name`: parameters stored into a `<String, dynamic>` literal; the caller's argument types were not read. — attempted 2026-10-20 (two-hop not readable: the caller closure passes slots (`charging/ui/page/device/a2345/a2345custom_clock/a2345custom_clock_logic.dart @0x3e2288c`..`@0x3e22894`))
- Name length or character limits. — traced 2026-10-20: `_saveScreenName` compares no length (see Callers in app); a limit, if any, is in the input widget (not read) or on the server
- Header stays `string-only` because the types of `sn` and `name` and the response model are missing. — rechecked 2026-10-20: still true; the typing attempts are recorded on the bullets of this section
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
