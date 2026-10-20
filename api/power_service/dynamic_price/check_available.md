> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# check_available

## Purpose

Sent after a login: `LoginHandler::_postHasChangeCountryAsync` (`login_handler.dart`) and `LoginLogic::handleLoginSuccess` call `postHasChangeCountry`, whose callbacks log `postHasChangeCountry request success` / `failed`.

## Upstream name

`get_dynamic_price_sites` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/dynamic_price/check_available` (asm-traced): URL string at `http_request_repository_impl.dart @0x273bfcc`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x273bfc4`, in `HttpRequestControllerImpl::postHasChangeCountry` (`http_request_repository_impl.dart @0x273bf40`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is an empty map literal (`ldr x16, [THR, #0xa8]` empty array `@0x273bf84`, `Map._fromLiteral` `@0x273bf8c`); the builder contains no `[]=` call, so no key is added. The map goes to `encryptionRequestHttp` (`@0x273bff4`).

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed. The success callback `http_request_repository_impl.dart @0x273c0b8` loads its argument once, for the log string `"---> postHasChangeCountry request success"`, and calls `exeSuccess()`.

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (decrypted body as built by `postHasChangeCountry`)

```json
{}
```

Response: none parsed.

## Errors seen

None traced. The failure callback `@0x273c010` logs `"---> postHasChangeCountry failed, code "` and the message, then calls `exeError()`; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `postHasChangeCountry` @0x273bf40 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/account/handlers/login_handler.dart::_postHasChangeCountryAsync`
- `charging/http/http_request_repository.dart::postHasChangeCountry`
- `charging/ui/page/account/login/login_logic.dart::handleLoginSuccess`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- What the server derives from this empty call (the builder name `postHasChangeCountry` is the only hint).
- Why the URL is under `dynamic_price/check_available`: the app sends no parameter, so the server decides from the session.

## Device-tested by

none
