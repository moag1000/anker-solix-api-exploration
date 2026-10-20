> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_ota_update

## Purpose

Starts the OTA of a third-party solar device that is attached to a solar bank (builder `setThirdOta`); the wrapper has no call site in the asm (see Callers in app), so the purpose is inferred from the builder name (string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/compatible/set_ota_update` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x406bb20`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x406bb18`, in `HttpRequestControllerImpl::setThirdOta` (`charging/http/http_request_repository_impl.dart @0x406ba10`), sent through `encryptionRequestHttp` (`@0x406bb40`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) One map literal of 4 pairs (raw `r2 = 16` at `@0x406ba64`, so 8 slots) with type arguments `<String, Object>` (`@0x406bad4`); all keys are stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x406ba70` |
| `solar_pn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x406ba84` |
| `insert_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x406ba98` |
| `rollback_install_mode` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x406baac` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure `charging/http/http_request_repository_impl.dart @0x261b9a0` calls the stored callback with `true` (`@0x261b9cc`); the other closure (`@0x406bb5c`) only logs "setThirdOta failed, code" and the message.

## Response

No response key is read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<?>",
  "solar_pn": "<?>",
  "insert_sn": "<?>",
  "rollback_install_mode": "<?>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `setThirdOta` @0x406ba10 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::setThirdOta`

No direct call site of the wrapper `HttpRequestController::setThirdOta` (`charging/http/http_request_repository.dart @0x406b9b0`) exists in the asm tree: a search for its call target address and for the function name found nothing outside the two repository files (2026-10-20); the app may reach it through a dispatch-table call, which Blutter does not name.

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of the four values (parameters; `<String, Object>` only says non-null) and what `rollback_install_mode` selects. — attempted 2026-10-20 (two-hop not readable: the wrapper `HttpRequestController::setThirdOta` has no call site, so there is no caller to read values from (`charging/http/http_request_repository.dart @0x406b9b0`); what `rollback_install_mode` selects is not recorded in the app) — reclassified: server
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
