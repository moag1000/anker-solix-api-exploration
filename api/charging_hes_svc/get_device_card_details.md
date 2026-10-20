> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_device_card_details

## Purpose

Reads the detail card of one device of a station through `DevcieHomeHttpRepository::getDeviceDetails` (string-only: no caller chain in `data/endpoints.json`, inferred from the builder name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_device_card_details` (asm-traced): URL string at `charging/ui/page/device/a5101/device_home_page/device_home_http_reposity.dart @0x33c4d3c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x33c4d34`, in `DevcieHomeHttpRepository::getDeviceDetails` (`charging/ui/page/device/a5101/device_home_page/device_home_http_reposity.dart @0x33c4c58`), sent through `encryptionRequestHttp` (`@0x33c4d60`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- `encryptionRequestHttp` forwards `needEncryption` with its default true to `requestHttp` (`api/encryption.md`): `DevcieHomeHttpRepository::getDeviceDetails` (`charging/ui/page/device/a5101/device_home_page/device_home_http_reposity.dart`, call `@0x33c4d60`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `DevcieHomeHttpRepository::getDeviceDetails` (`charging/ui/page/device/a5101/device_home_page/device_home_http_reposity.dart @0x33c4cf0`, 3 keys). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes | `"<station_id>"` | `charging/ui/page/device/a5101/device_home_page/device_home_http_reposity.dart @0x33c4cb4` |
| `device_type` | string | yes | `"<device_type>"` | `charging/ui/page/device/a5101/device_home_page/device_home_http_reposity.dart @0x33c4cc8` |
| `device_Sn` | string | yes | `"<device_Sn>"` | `charging/ui/page/device/a5101/device_home_page/device_home_http_reposity.dart @0x33c4cdc` |

## `param_type`/`cmd`

n/a

## Response model (link)

no model class: the success closure (`charging/ui/page/device/a5101/device_home_page/device_home_http_reposity.dart @0x33c558c`, argument typed `Map<String, dynamic>`) wraps the whole map in a `CacheData` object (`@0x33c55bc`, `StoreField` `@0x33c55c8`) and passes it to the stored callback (`ClosureCall` `@0x33c55d8`); the builder also declares the result type `Map<String, dynamic>` (`@0x33c4d28`).

## Response

No key of the response is read in the sender: the map is handed on unchanged.

App side keys read (traced 2026-10-20): the callback of `A5101DeviceHomeLogic::getDeviceCardDetails` (`charging/ui/page/device/a5101/device_home_page/device_home_logic.dart`, sender call `@0x33c4c3c`, closure `@0x33c5608`) looks up the keys `main_sn` (default `""`, stored in `field_9b` `@0x33c56e8`), `pn` (default `""`, `field_9f` `@0x33c579c`), `station_name` (default `""`), `grid_status` (default Smi 1: raw `r3 = 2` `@0x33c58c0`, tagged slot) and `pack_details` (`@0x33c5914`); after the lookups it calls `update` with the list `["packlist", "device"]` (array length raw 4 = 2 elements, `@0x33c5988`..`@0x33c59d0`). The key types are not checked here. Value meanings are not read from the asm.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "device_type": "<device_type>",
  "device_Sn": "<device_Sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5101/device_home_page/device_home_http_reposity.dart`: `getDeviceDetails` @0x33c4c58 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which `device_type` values exist: the parameter is passed through (`charging/ui/page/device/a5101/device_home_page/device_home_http_reposity.dart @0x33c4cc8`). — attempted 2026-10-20 (two-hop not readable: the two callers pass slots of their own frames, `charging/ui/page/device/a5101/device_home_page/device_home_logic.dart @0x33c4c3c` and `charging/ui/page/device/main/station_device_home/station_set_time/station_set_time_page.dart @0x4000c78`)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
