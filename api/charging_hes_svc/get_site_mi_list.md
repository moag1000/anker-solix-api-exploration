> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_site_mi_list

## Purpose

Reads the micro-inverter list of a site for the A5150 ECU card (`A5150EcuMiListModel`) through `FamilyMainHttpReposity::getEcuCardList` (string-only: no caller chain in `data/endpoints.json`, inferred from the builder name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_site_mi_list` (asm-traced): URL string at `charging/ui/page/family/family_main_http_reposity.dart @0x43375a8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x43375a0`, in `FamilyMainHttpReposity::getEcuCardList` (`charging/ui/page/family/family_main_http_reposity.dart @0x43374ec`), sent through `requestHttp` (`@0x43375d8`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `FamilyMainHttpReposity::getEcuCardList` (`charging/ui/page/family/family_main_http_reposity.dart`, call `@0x43375d8`, argument list `@0x43375d0`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `FamilyMainHttpReposity::getEcuCardList` (`charging/ui/page/family/family_main_http_reposity.dart @0x4337560`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes | `"<station_id>"` | `charging/ui/page/family/family_main_http_reposity.dart @0x433754c` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::A5150EcuMiListModel`, parsed by `A5150EcuMiListModel.fromJson` at `charging/ui/page/family/family_main_http_reposity.dart @0x4337638` (success closure `@0x43375ec`, `bl` target `[package:charging/model/a5150/a5150_ecu_mi_list_model/a5150_ecu_mi_list_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::A5150EcuMiListModel`): `ecu_sn` (unknown), `ecu_pn` (unknown), `ecu_device_name` (unknown), `ecu_is_online` (unknown), `true` (unknown), `mi_details` (List?).

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

- `charging/ui/page/family/family_main_http_reposity.dart`: `getEcuCardList` @0x43374ec (requestHttp; encrypted: default-true (requestHttp) — verify)

Call sites (grep of the whole asm tree, traced 2026-10-20): the name `getEcuCardList` occurs only at its definition (`charging/ui/page/family/family_main_http_reposity.dart`, function header and its own closure `@0x43375ec`); no `r0 = getEcuCardList()` call site exists in 3.24.3, so the app does not call this sender.

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What `loopSeconds` (argument list `charging/ui/page/family/family_main_http_reposity.dart @0x43375d8`) does in the HTTP layer: it was not read for it. — traced 2026-10-20: the argument is consumed by the `HttpRequestMixin` code of `FamilyMainHttpReposity`, and Blutter emits no body for `HttpRequestMixin` (class `abstract class HttpRequestMixin extends BaseGetController` is empty in `charging/http/http_request_mixin.dart`; only `Debouncer::run` `@0x230f7f0` is emitted), so the effect of the named argument is not in the asm
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
