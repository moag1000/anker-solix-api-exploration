> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# remove_param_config_key

## Purpose

Removes a stored parameter key (the constant `use_time`) of a site/device when the user deletes a peak-valley entry (caller `ConfirmPeakValleyLogic::onDeletePeakValleyClick`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/device/remove_param_config_key` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x428bae0`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x428bad8`, in `HttpRequestControllerImpl::removeParamConfigKey` (`charging/http/http_request_repository_impl.dart @0x428b9e4`), sent through `encryptionRequestHttp` (`@0x428bb0c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) One map literal of 3 pairs (raw `r2 = 12` at `@0x428ba30`, so 6 slots) with type arguments `<String, String>` (`@0x428ba94`), so every value is a String; `site_id` and `device_sn` are replaced by the empty string when the parameter is false/null (`tbnz w1, #4` at `@0x428ba48` and `@0x428ba68`, then `r2 = ""` `@0x428ba4c` / `@0x428ba74`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | `charging/http/http_request_repository_impl.dart @0x428ba38` |
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x428ba5c` |
| `remove_key` | string | yes | `"use_time"` | `charging/http/http_request_repository_impl.dart @0x428ba7c` (value literal `@0x428ba88`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed in the builder (asm-traced): the success closure forwards the response object unchanged to the caller's callback (``@0x2268374`, `ClosureCall` `@0x22683a8``); the parse is in the caller, which was not read

## Response

Not read in the builder.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "site_id": "<site_id>",
  "device_sn": "<device_sn>",
  "remove_key": "use_time"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `removeParamConfigKey` @0x428b9e4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/feature/peak_valley/confirm/confirm_peak_valley_logic.dart::onDeletePeakValleyClick`
- `charging/http/http_request_repository.dart::removeParamConfigKey`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The response: the builder forwards it; `ConfirmPeakValleyLogic` was not decoded. — not traced 2026-10-20 in this pass (`ConfirmPeakValleyLogic` callback); the reason given in the bullet stands
- Which other `remove_key` values the server accepts (the builder sends the constant `use_time`).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
