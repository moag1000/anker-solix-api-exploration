> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

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
| `site_id` | string | yes | | `charging/http/http_request_repository_impl.dart @0x23f1b28` |

Typing (two-hop, asm-traced): the value of `site_id` is an untyped parameter of the builder; its only caller, `StationMainPageLogic.getShow17YOPopup` (`charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart @0x23f1a60`), passes `field_7` of the `.value` of an Rx field (`@0x23f1a08`, `@0x23f1a0c`) and replaces null by the String literal `""` (`@0x23f1a1c`), so the field is a string.

## `param_type`/`cmd`

n/a

## Response model (link)

no model class in the builder (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x23f1bc8`) forwards its single argument unchanged to the stored callback (null check `@0x23f1bf4`, `ClosureCall` `@0x23f1c08`); the caller `StationMainPageLogic.getShow17YOPopup` (`charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart`) passes its own success closure (`@0x23f1ca8`), which indexes the received object for two keys without a model class: `is_popup` (key `@0x23f1cd4`, cast to `bool`, default `false` `@0x23f1d00`) and `popup_code` (key `@0x23f1d48`, cast to `int`, default raw -2 in a tagged slot, so -1, `@0x23f1d74`). When `is_popup` is false the closure sets a state flag (`field_e3` of the logic, `value=` `@0x23f1e18`) to false; otherwise it compares `popup_code` with the tagged immediate 0x7d2 (`cmp w0, #0x7d2` `@0x23f1dc8`, so 1001) and sets the flag to true when equal (`@0x23f1dec`) and to false when not (`@0x23f1e18`).

## Response

The builder hands the object to the caller; the caller reads two keys (see Response model): `is_popup` (bool) and `popup_code` (int).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "site_id": "<site_id>"
}
```

Response, synthesized (keys read by the caller's closure; values are placeholders)

```json
{
  "is_popup": "<bool>",
  "popup_code": "<int>"
}
```

Whether these keys sit under `data` or at the top of the body is decided by the call layer, not by this closure (it indexes the object it receives).

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

- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
