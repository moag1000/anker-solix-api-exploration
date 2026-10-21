> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_conn_net_tips

## Purpose

Reads the guide image for connecting a device to the network (`ItalyGuideImageModel`) through `FamilyMainHttpReposity::getImagePath`; the success closure logs `意大利自检的蓝牙引导图片` ("Italy self-check Bluetooth guide image", my translation) (string-only: no caller chain in `data/endpoints.json`, inferred from the builder name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_conn_net_tips` (asm-traced): URL string at `charging/ui/page/family/family_main_http_reposity.dart @0x479d2bc`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x479d2b4`, in `FamilyMainHttpReposity::getImagePath` (`charging/ui/page/family/family_main_http_reposity.dart @0x479d228`), sent through `requestHttp` (`@0x479d2e4`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `FamilyMainHttpReposity::getImagePath` (`charging/ui/page/family/family_main_http_reposity.dart`, call `@0x479d2e4`, argument list `@0x479d2dc`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `FamilyMainHttpReposity::getImagePath` (`charging/ui/page/family/family_main_http_reposity.dart @0x479d270`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `pn` | string | yes | `"<pn>"` | `charging/ui/page/family/family_main_http_reposity.dart @0x479d25c` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::ItalyGuideImageModel`, parsed by `ItalyGuideImageModel.fromJson` at `charging/ui/page/family/family_main_http_reposity.dart @0x479d328` (success closure `@0x479d300`, `bl` target `[package:charging/model/a5101/italy_guide_image_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::ItalyGuideImageModel`): `tips` (unknown).

Use of the answer (app side, traced 2026-10-20): the success closure takes the first element of `tips` when the list is set (`first` `charging/ui/page/family/family_main_http_reposity.dart @0x479d348`) and reads the field at offset 0x17 of it (`@0x479d34c`), which is `passwordImgUrl` in the `toJson` of `Tips` (`charging/model/a5101/italy_guide_image_model.dart`, load `@0x479d744` before the key string `@0x479d75c`), the empty string when null (`@0x479d360`); it logs the text `意大利自检的蓝牙引导图片 image:` with the value (`@0x479d374`..`@0x479d394`) and stores the string at offset 519 of `getA5101StationController()` (`@0x479d3ac`..`@0x479d3bc`). The only caller is `FamilyMainPageLogic::_changeDevice` (`charging/ui/page/family/family_main_page_logic.dart @0x479d20c`), which passes `field_d3` of its device object (`@0x479d200`) as `pn`.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "pn": "<pn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/family/family_main_http_reposity.dart`: `getImagePath` @0x479d228 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which product numbers have a guide image: decided by the answer of the cloud; the app sends `field_d3` of the device it switches to (see Response) and takes the first `tips` element without matching its `productCode` — traced 2026-10-20 (`charging/ui/page/family/family_main_http_reposity.dart @0x479d348`).
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
