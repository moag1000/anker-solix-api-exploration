> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# installation_popup

## Purpose

Asks whether the "incompatible installation" pop-up has to be shown for a site on the station home and main pages (callers `StationHomeInfoLogic::getSiteInstallationPopup`, `StationMainPageLogic::getSiteInstallationPopup`; builder `getIncompatiblePopupApi`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/compatible/installation_popup` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x23f2784`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x23f277c`, in `HttpRequestControllerImpl::getIncompatiblePopupApi` (`charging/http/http_request_repository_impl.dart @0x23f26dc`), sent through `encryptionRequestHttp` (`@0x23f27a4`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) The body is one map literal of 1 pair (`AllocateArray`, raw `r2 = 4` at `@0x23f271c`, so 2 slots) with type arguments `<String, String?>` at `@0x23f2738`, so every value is typed in the literal; all keys are stored unconditionally. The value type is `String?`, so a null site id would be sent as JSON null.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string (nullable, `String?`) | yes | `"<site_id>"` | `charging/http/http_request_repository_impl.dart @0x23f2724` |

## `param_type`/`cmd`

n/a

## Response model (link)

no model class (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x23f27c0`) casts the response to `Map<String, dynamic>` (`@0x23f27f4`), reads the key `is_popup` (string literal `@0x23f2810`, index call `@0x23f2818`) and passes the value to the stored callback (`ClosureCall` `@0x23f283c`) without a cast.

## Response

| field | type | required | example | source |
|---|---|---|---|---|
| `is_popup` | bool (cast by both callers) | optional | | `charging/http/http_request_repository_impl.dart @0x23f2810` |

The callers cast the forwarded value to `bool` (asm-traced): `StationMainPageLogic.getSiteInstallationPopup` (`charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart @0x23f28dc`, type test `r8 = bool` `@0x23f298c`) and `StationHomeInfoLogic.getSiteInstallationPopup` (`charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart @0x2c209e8`, `@0x2c20a40`); the latter skips its action when the value is false (`tbnz w0, #4` `@0x2c20a54`). On the SDK path the decorator hands the success callback the JSON-decoded `data` member of the result (or an empty map when it is missing or empty): `charging/http/HttpEncryptionDecorator.dart @0x486ab9c` (key `"data"`), `@0x486ac18` (`JsonCodec.decode`), `@0x486ac28` and `@0x486ac64` (the two `ClosureCall`s); so the object this closure indexes is the content of `data` (background: [encryption.md](../../../encryption.md#response-handling-and-error-codes)).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "site_id": "<site_id>"
}
```

Response, synthesized (key read by the success closure; the value type is not cast)

```json
{
  "data": {
    "is_popup": "<?>"
  }
}
```

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getIncompatiblePopupApi` @0x23f26dc (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getIncompatiblePopupApi`
- `charging/ui/page/device/main/station_device_home/station_home_info/controller/station_home_info_logic.dart::getSiteInstallationPopup`
- `charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart::getSiteInstallationPopup`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
