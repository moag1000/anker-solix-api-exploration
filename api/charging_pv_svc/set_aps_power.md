> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_aps_power

## Purpose

<!-- TODO -->

## Upstream name

`set_device_pv_power` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/charging_pv_svc/set_aps_power`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a5140/a5140home/a5140home_http_reposity.dart @0x3ee90e0`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | ? | ? | ? | `charging/ui/page/device/a5140/a5140home/a5140home_http_reposity.dart @0x3ee8ffc` |
| `power` | ? | ? | ? | `charging/ui/page/device/a5140/a5140home/a5140home_http_reposity.dart @0x3ee8ffc` |

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

- `charging/ui/page/device/a5140/a5140home/a5140home_http_reposity.dart`: `requestApsMaxPower` @0x3ee8ffc (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
