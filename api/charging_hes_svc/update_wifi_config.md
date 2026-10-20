> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# update_wifi_config

## Purpose

Reports the Wi-Fi credentials set during device deployment (`DeployWifiProgressLogic::_updateWifiInfo` through `HttpRequestControllerImpl::updateWiFiConfig`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/update_wifi_config` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x25f5d64`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x25f5d5c`, in `HttpRequestControllerImpl::updateWiFiConfig` (`charging/http/http_request_repository_impl.dart @0x25f5c00`), sent through `requestHttp` (`@0x25f5d8c`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::updateWiFiConfig` (`charging/http/http_request_repository_impl.dart`, call `@0x25f5d8c`, argument list `@0x25f5d84`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`HttpRequestControllerImpl::updateWiFiConfig` (`charging/http/http_request_repository_impl.dart @0x25f5c00`) stores 4 keys in a map literal with type arguments `<String, Object?>` (`@0x25f5d14`), which do not type the values. `ssid`, `sn` and `rssi` are stored as received (`@0x25f5c74`, `@0x25f5c88`, `@0x25f5c9c`); `encryption` is `Null` when its parameter is null (`cmp w0, NULL` `@0x25f5cb0`, `@0x25f5cb8`) and otherwise the result of an unnamed call on the parameter (`GDT[cid_x0 + 0x5360]` `@0x25f5cdc`), stored at `@0x25f5cf0`; its type stays `?`.

| field | type | required | example | source |
|---|---|---|---|---|
| `ssid` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x25f5c64` |
| `sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x25f5c78` |
| `rssi` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x25f5c8c` |
| `encryption` | ? | yes | `null` or the result of an unnamed call on the parameter (selector not named) | `charging/http/http_request_repository_impl.dart @0x25f5ca0` |

Values the only caller sends (traced 2026-10-20, app side): `HttpRequestController::updateWiFiConfig` (`charging/http/http_request_repository.dart @0x25f5aa0`) declares the named parameters `encryption` (default `Null`), `rssi` (default `Null`) and `showLoading` (default `true`) (`SetupParameters` `@0x25f5aac`). `DeployWifiProgressLogic::_updateWifiInfo` (`charging/ui/page/device/a5101/deploy_wifi/deploy_wifi_progress_logic.dart @0x277c28c`) passes two data values and the two callbacks and no named argument (argument descriptor `[0, 0x5, 0, 0x5, null]` `@0x277c288`), so from this caller `rssi` and `encryption` are sent as JSON `null`. The two data values are `field_9f` of the object in `field_83` with the fallback `""` (`@0x277c214`..`@0x277c240`) and `field_6b` of a device object reached through `field_7f` (`@0x277c1e8`..`@0x277c208`, the call is skipped when that object is null, `@0x277c204`).

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the sender (asm-traced): the success closure is the folded forwarder `charging/http/http_request_repository_impl.dart @0x2268374`, which passes the response object unchanged to the callback stored in the context (`ClosureCall` `@0x22683a8`); the failure closure is the folded forwarder `@0x226824c` (`ClosureCall` `@0x2268288`).

## Response

No response key is read in the sender.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "ssid": "<ssid>",
  "sn": "<sn>",
  "rssi": "<rssi>",
  "encryption": "<encryption>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `updateWiFiConfig` @0x25f5c00 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::updateWiFiConfig`
- `charging/ui/page/device/a5101/deploy_wifi/deploy_wifi_progress_logic.dart::_updateWifiInfo`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The types of all four keys: the values are parameters, converted only for `encryption`. — attempted 2026-10-20 (two-hop not readable: `_updateWifiInfo` (`charging/ui/page/device/a5101/deploy_wifi/deploy_wifi_progress_logic.dart @0x277c28c`) pass slots or fields of their own frames; no literal or declared type in the argument setups)
- The meaning of `encryption` when a value is sent: the only caller sends none (see Request), so the Wi-Fi security enum behind the unnamed call (`charging/http/http_request_repository_impl.dart @0x25f5ca0`) is not reached by the 3.24.3 app code read — traced 2026-10-20
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
