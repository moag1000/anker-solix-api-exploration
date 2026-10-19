> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# update_wifi_config

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/update_wifi_config`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x25f5d64`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `ssid` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x25f5c00` |
| `sn` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x25f5c00` |
| `rssi` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x25f5c00` |
| `encryption` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x25f5c00` |

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `updateWiFiConfig` @0x25f5c00 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::updateWiFiConfig`
- `charging/ui/page/device/a5101/deploy_wifi/deploy_wifi_progress_logic.dart::_updateWifiInfo`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
