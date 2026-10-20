> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_popup

## Purpose

Queries the after-sale pop-up state of an A17Y0 site for the station main page (caller `StationMainPageLogic::getShow17YOPopup`; builder `queryA17Y0Popup`) (asm-traced for the call chain).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/after_sale/get_popup` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x23f1b84`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x23f1b7c`, in `HttpRequestControllerImpl::queryA17Y0Popup` (`charging/http/http_request_repository_impl.dart @0x23f1ad4`), sent through `encryptionRequestHttp` (`@0x23f1bac`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) One-pair map literal (`AllocateArray` raw `r2 = 4` at `@0x23f1b20`, so 2 slots) with type arguments `<String, dynamic>` (`@0x23f1b3c`); the value is a parameter of the builder (`fp-0x10`), no static type in the asm.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x23f1b28` |

## `param_type`/`cmd`

n/a

## Response model (link)

no model class in the builder (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x23f1bc8`) forwards its single argument unchanged to the stored callback (null check `@0x23f1bf4`, `ClosureCall` `@0x23f1c08`); what the caller does with it was not decoded.

## Response

Not read: the response is handed to the caller of `queryA17Y0Popup` (`StationMainPageLogic::getShow17YOPopup`) as it is.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "site_id": "<?>"
}
```

Response: not synthesized; the app passes the received object to the caller.

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `queryA17Y0Popup` @0x23f1ad4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::queryA17Y0Popup`
- `charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart::getShow17YOPopup`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `site_id` (parameter, `<String, dynamic>` literal).
- The response keys: the closure forwards the object; the parser in `StationMainPageLogic::getShow17YOPopup` was not decoded.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
