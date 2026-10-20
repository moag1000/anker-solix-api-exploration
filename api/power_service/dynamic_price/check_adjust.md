> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# check_adjust

## Purpose

Sent once from `HomePageState::initState` (`home_page.dart @0x2b990ac`) when the home page is created; the callbacks log `adjustDynamicPrice success:` / `adjustDynamicPrice fail:` (log label strings).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/dynamic_price/check_adjust` (asm-traced): URL string at `home_page.dart @0x2b9913c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2b99134`, in `HomePageState::initState` (`home_page.dart @0x2b990ac`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is an empty map literal (`ldr x16, [THR, #0xa8]` empty array `@0x2b990f4`, `Map._fromLiteral` `@0x2b990fc`); the builder contains no `[]=` call, so no key is added. The map goes to `encryptionRequestHttp` (`@0x2b99164`).

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed. The success callback `home_page.dart @0x2b9a42c` loads its argument once, for the log string `"adjustDynamicPrice success: "`, and calls `exeInfo()`.

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (decrypted body as built by `initState`)

```json
{}
```

Response: none parsed.

## Errors seen

None traced. The failure callback `home_page.dart @0x2b9a3b8` logs `"adjustDynamicPrice fail: "`, the code and the message with `exeInfo()`; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/ui/page/home/home_page.dart`: `initState` @0x2b990ac (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- What the server does with this call: the app sends an empty body and reads nothing back; the log label `adjustDynamicPrice` is the only hint.
- Whether the call is skipped for logged-out users: the surrounding code in `initState` (`isLogin` check `@0x2b99210` follows the call) was not followed.

## Device-tested by

none
