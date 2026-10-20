> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_installation

## Purpose

Saves the installation (solar integration) mode of a site or solar bank during EZ1 mode selection and the A17Y0-uses-A17C0 OTA (callers `EZ1SelectModeLogic::next`, `A17Y0UseA17C0OtaLogic::startOTA`, `PollProgressOTALogic::startOTA`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`set_installation` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/compatible/set_installation` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3d65450`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3d65448`, in `HttpRequestControllerImpl::setInstallationApi` (`charging/http/http_request_repository_impl.dart @0x3d6528c`), sent through `encryptionRequestHttp` (`@0x3d65478`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::setInstallationApi` (`charging/http/http_request_repository_impl.dart @0x3d6528c`) starts from an empty map literal (`THR::empty_array`, `@0x3d652e0`) and replaces it by one of two literals of 3 pairs (raw `r2 = 12` at `@0x3d65318` and `@0x3d65390`): `{install_mode, site_id, is_save}` when a comparison with the empty string (`r16 = ""` `@0x3d652f0`) is false (`tbz w0, #4` `@0x3d65304` jumps to the second literal when it is true), else `{install_mode, solarbank_sn, is_save}`. The type arguments of both literals are not visible in the asm text.

| field | type | required | example | source |
|---|---|---|---|---|
| `install_mode` | ? | yes (in both literals) | ? | `charging/http/http_request_repository_impl.dart @0x3d65324` / `@0x3d653ac` |
| `site_id` | ? | optional (first literal only) | ? | `charging/http/http_request_repository_impl.dart @0x3d6534c` |
| `solarbank_sn` | ? | optional (second literal only) | ? | `charging/http/http_request_repository_impl.dart @0x3d653d4` |
| `is_save` | ? | yes (in both literals) | ? | `charging/http/http_request_repository_impl.dart @0x3d65360` / `@0x3d653e8` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed in the builder (asm-traced): the closures it passes are the forwarding closures `@0x2268374` (one argument, `ClosureCall` `@0x22683a8`) and `@0x238cda4` (two arguments, null-checked `@0x238cdd0`); what the caller parses was not read.

## Response

Not read: the response object is handed to the caller.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "install_mode": "<?>",
  "site_id": "<?>",
  "is_save": "<?>"
}
```

Response: not synthesized (the app forwards the object to the caller). Alternative body with `solarbank_sn` instead of `site_id`.

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `setInstallationApi` @0x3d6528c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::setInstallationApi`
- `charging/ui/page/device/a17c0/ez1_select_mode/ez1_select_mode_logic.dart::getOTAUpdateStatus`
- `charging/ui/page/device/a17c0/ez1_select_mode/ez1_select_mode_logic.dart::next`
- `charging/ui/page/device/a17y0/a17y0ota/a17y0_use_a17c0_ota_logic.dart::startOTA`
- `charging/ui/page/device/anker_ota/poll_progress_ota_page/poll_progress_ota_logic.dart::startOTA`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Types of `install_mode`, `site_id`, `solarbank_sn` and `is_save` (parameters; the literal type arguments are not shown).
- Which parameter the comparison with the empty string (`@0x3d652f0`, branch `@0x3d65304`) tests and which callers pass which key.
- The response: forwarded by the closures; the callers were not decoded.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
