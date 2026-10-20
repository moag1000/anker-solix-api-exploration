> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# save_ota_complete_status

## Purpose

Reports that the OTA of a third-party solar device finished (builder `saveThirdOtaInfo`); no UI caller is recorded in `data/endpoints.json`, so the purpose is inferred from the builder name (string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/compatible/save_ota_complete_status` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x372f644`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x372f63c`, in `HttpRequestControllerImpl::saveThirdOtaInfo` (`charging/http/http_request_repository_impl.dart @0x372f57c`), sent through `encryptionRequestHttp` (`@0x372f66c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) One map literal of 2 pairs (raw `r2 = 8` at `@0x372f5c8`, so 4 slots) with type arguments `<String, Object>` (`@0x372f5f8`); both keys are stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `solarbank_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x372f5d0` |
| `ota_complete_status` | int (Smi, w) | yes | `2` | `charging/http/http_request_repository_impl.dart @0x372f5e4` (raw 4 stored by a 32-bit store at `@0x372f5f4`, so 2) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure `charging/http/http_request_repository_impl.dart @0x261b9a0` calls the stored callback with `true` (`@0x261b9cc`); the other closure (`@0x372f688`) only logs "saveThirdOtaInfo failed, code" and the message.

## Response

No response key is read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "solarbank_sn": "<?>",
  "ota_complete_status": 2
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `saveThirdOtaInfo` @0x372f57c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::saveThirdOtaInfo`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `solarbank_sn` (a parameter; `<String, Object>` only says non-null).
- What `ota_complete_status` values other than 2 mean (the builder sends the constant 2).
- No UI caller is recorded for this builder in `data/endpoints.json`.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
