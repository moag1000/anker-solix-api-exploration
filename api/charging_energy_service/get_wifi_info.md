> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_wifi_info

## Purpose

Reads the Wi-Fi name and signal strength of an A17B1 station for the Wi-Fi info page (caller chain `WifiInfoLogic::_getWifiInfo`, `HttpRequestController::getWifiInfoOf17B1`, in `data/endpoints.json`) (asm-traced).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_energy_service/get_wifi_info` (asm-traced): URL string `@0x344b3d8`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x344b3d0`, in `HttpRequestControllerImpl::getWifiInfoOf17B1` (`charging/http/http_request_repository_impl.dart @0x344b324`), sent through `HttpRequestControllerImpl::requestHttp` (`@0x344b3fc`).

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) One sender, one key. The map literal has the type arguments `<String, String>` (`charging/http/http_request_repository_impl.dart @0x344b38c`), so the value is a string; it is stored without a guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | string | yes | `"<sn>"` | `charging/http/http_request_repository_impl.dart @0x344b378` (value store `@0x344b388`, parameter) |

## `param_type`/`cmd`

n/a

## Response model (link)

[`WifiInfoModel`](../../models/connectivity.md#wifiinfomodel), parsed by `WifiInfoModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x344b450` in the success closure `@0x344b418`.

## Response

(asm-traced) Top-level keys of `WifiInfoModel` (`data/models.json`, `charging::WifiInfoModel`): `ssid` (String?), `rssi` (int?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "sn": "<sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure only logs `code` and `msg`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getWifiInfoOf17B1` @0x344b324 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getWifiInfoOf17B1`
- `charging/ui/page/device/a17b1/wifi_info/wifi_info_logic.dart::_getWifiInfo`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which serial number `WifiInfoLogic::_getWifiInfo` passes (the caller was not read).
- The unit and range of `rssi`: only the class field type is listed.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
