> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_user_fault_info

## Purpose

Reads the fault list of a station (`HesPushMessageModel` entries) through `FamilyMainHttpReposity::getDeviceExceptions` (string-only: no caller chain in `data/endpoints.json`, inferred from the builder name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_user_fault_info` (asm-traced): URL string at `charging/ui/page/family/family_main_http_reposity.dart @0x23f0038`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x23f0030`, in `FamilyMainHttpReposity::getDeviceExceptions` (`charging/ui/page/family/family_main_http_reposity.dart @0x23eff84`), sent through `requestHttp` (`@0x23f0060`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `FamilyMainHttpReposity::getDeviceExceptions` (`charging/ui/page/family/family_main_http_reposity.dart`, call `@0x23f0060`, argument list `@0x23f0058`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `FamilyMainHttpReposity::getDeviceExceptions` (`charging/ui/page/family/family_main_http_reposity.dart @0x23effec`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes | `"<station_id>"` | `charging/ui/page/family/family_main_http_reposity.dart @0x23effd8` |

## `param_type`/`cmd`

n/a

## Response model (link)

parsed from the key `faultInfos`, no `fromJson` on the whole body: the success closure (`charging/ui/page/family/family_main_http_reposity.dart @0x23f007c`) casts the response to `Map<String, dynamic>` (`@0x23f00bc`), reads `faultInfos` (`@0x23f00d8`, lookup `@0x23f00e0`, cast to `List?` `@0x23f0128`), maps every element with a closure that calls `HesPushMessageModel.fromJson` (`@0x23f0238`), builds a list (`@0x23f01a4`) and passes it to the stored callback (`ClosureCall` `@0x23f01d0`). Model: `charging::HesPushMessageModel` in `data/models.json`.

## Response

(asm-traced) One response key is read: `faultInfos` (List?), each element parsed as `HesPushMessageModel` with the keys `productCode` (String), `stationId` (String), `sn` (String), `subSn` (String), `deviceType` (String), `failureCode` (String), `failureLevel` (int), `failureTime` (String), `failureTimeUnix` (int), `failureType` (int), `failureDesc` (String), `redirectPage` (String), `appDisplayChannels` (List<int>), `appPopUp` (int), `id` (int), `source` (int), `handlingSuggestion` (String), `dataSource` (int).

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

- `charging/ui/page/family/family_main_http_reposity.dart`: `getDeviceExceptions` @0x23eff84 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which fault codes and levels the server sends: no capture exists; the app only parses the list.
- No caller of `getDeviceExceptions` is recorded in `data/endpoints.json`.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
