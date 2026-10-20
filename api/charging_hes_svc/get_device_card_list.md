> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_device_card_list

## Purpose

Reads the device card list of a station for the family page through `FamilyMainHttpReposity::getDeviceCard` (string-only: no caller chain in `data/endpoints.json`, inferred from the builder name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_device_card_list` (asm-traced): URL string at `charging/ui/page/family/family_main_http_reposity.dart @0x479c6a0`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x479c698`, in `FamilyMainHttpReposity::getDeviceCard` (`charging/ui/page/family/family_main_http_reposity.dart @0x479c5bc`), sent through `requestHttp` (`@0x479c6c8`).

The builder also calls `_startTimer` with the URL string (`charging/ui/page/family/family_main_http_reposity.dart @0x479c610`, `@0x479c624`, call `@0x479c634`) before it builds the body.

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `FamilyMainHttpReposity::getDeviceCard` (`charging/ui/page/family/family_main_http_reposity.dart`, call `@0x479c6c8`, argument list `@0x479c6c0`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `FamilyMainHttpReposity::getDeviceCard` (`charging/ui/page/family/family_main_http_reposity.dart @0x479c658`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes | `"<station_id>"` | `charging/ui/page/family/family_main_http_reposity.dart @0x479c644` |

Polling helper (app side, traced 2026-10-20, `charging/ui/page/family/family_main_http_reposity.dart`): `FamilyMainHttpReposity::_startTimer` (`@0x23e305c`) looks the URL up in a map field of the repository (`field_8b` `@0x23e30a8`, `_getValueOrData` `@0x23e30bc`), and when there is no entry it creates a `Timer.periodic` (`@0x23e30fc`) and stores it under the URL with `[]=` (`@0x23e310c`); the timer closure (`@0x23e3128`) calls `isLogin` (`@0x23e3168`) and skips its work when the app is not logged in (`tbnz` `@0x23e316c`). The period comes from the `loopSeconds` argument, whose body in `HttpRequestMixin` is not emitted.

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::DeviceCard`, parsed by `DeviceCard.fromJson` at `charging/ui/page/family/family_main_http_reposity.dart @0x479c730` (success closure `@0x479c6e4`, `bl` target `[package:charging/model/a5101/a5101_mqtt_device_info_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::DeviceCard`): `atsData` (AtsData?), `pcsData` (List?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/family/family_main_http_reposity.dart`: `getDeviceCard` @0x479c5bc (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The named argument `isAIotErrorCode` (`charging/ui/page/family/family_main_http_reposity.dart @0x479c6c0`) changes how the HTTP layer reads error codes; the layer was not read for it. — traced 2026-10-20: the name occurs only in the argument lists of the repository files (for example `charging/ui/page/family/family_main_http_reposity.dart @0x479c6c0`) and in no function of `charging/http/` or `charging/impl/http_service_impl.dart`, so no reader of the flag was found in the emitted code
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
