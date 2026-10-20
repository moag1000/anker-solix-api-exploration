> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_wifi_info

## Purpose

Reads the Wi-Fi information of a device from the home-setting and family pages (`A5101HomeSettingHttpReposity::getWifiInfo` and `FamilyMainHttpReposity::getWifiInfo`) (string-only: no caller chain in `data/endpoints.json`, inferred from the builder name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_wifi_info` (asm-traced): URL string at `charging/ui/page/device/a5101/setting/homeSetting/home_setting_http_reposity.dart @0x25f6178`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x25f6170`, in `A5101HomeSettingHttpReposity::getWifiInfo` (`charging/ui/page/device/a5101/setting/homeSetting/home_setting_http_reposity.dart @0x25f6064`), sent through `requestHttp` (`@0x25f61a8`).

Same URL and method object in the other sender(s) read:

- `FamilyMainHttpReposity::getWifiInfo` (`charging/ui/page/family/family_main_http_reposity.dart @0x25f69e4`): URL string `@0x25f6af8`, method object `Method.post` (`pp+0xa7e0`) at `@0x25f6af0`, sent through `requestHttp` (`@0x25f6b28`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `A5101HomeSettingHttpReposity::getWifiInfo` (`charging/ui/page/device/a5101/setting/homeSetting/home_setting_http_reposity.dart`, call `@0x25f61a8`, argument list `@0x25f61a0`), `FamilyMainHttpReposity::getWifiInfo` (`charging/ui/page/family/family_main_http_reposity.dart`, call `@0x25f6b28`, argument list `@0x25f6b20`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `A5101HomeSettingHttpReposity::getWifiInfo` (`charging/ui/page/device/a5101/setting/homeSetting/home_setting_http_reposity.dart @0x25f612c`, 1 key); `FamilyMainHttpReposity::getWifiInfo` (`charging/ui/page/family/family_main_http_reposity.dart @0x25f6aac`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | string | yes | `"<sn>"` | `charging/ui/page/device/a5101/setting/homeSetting/home_setting_http_reposity.dart @0x25f6118`; `charging/ui/page/family/family_main_http_reposity.dart @0x25f6a98` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::A5101WifiInfoModel`, parsed by `A5101WifiInfoModel.fromJson` at `charging/ui/page/family/family_main_http_reposity.dart @0x25f6ba0` (success closure `@0x25f6b3c`, `bl` target `[package:charging/ui/page/device/a5101/setting/wifi_info/a5101_wifi_info_model.dart]`). Both senders allocate the same closure `@0x25f6b3c` (identical code folded), which holds the parse.

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::A5101WifiInfoModel`): `wifiInfos` (List?), `ssid` (String?), `rssi` (int?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn": "<sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5101/setting/homeSetting/home_setting_http_reposity.dart`: `getWifiInfo` @0x25f6064 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/family/family_main_http_reposity.dart`: `getWifiInfo` @0x25f69e4 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- `cacheKey` is passed by name (`charging/ui/page/device/a5101/setting/homeSetting/home_setting_http_reposity.dart @0x25f61a8`, `charging/ui/page/family/family_main_http_reposity.dart @0x25f6b28`); the cache key value and the cache lifetime were not read.
- The value of `sn`: both senders pass a parameter (`charging/ui/page/device/a5101/setting/homeSetting/home_setting_http_reposity.dart @0x25f6128`, `charging/ui/page/family/family_main_http_reposity.dart @0x25f6aa8`).
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
