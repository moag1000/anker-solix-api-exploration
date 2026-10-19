> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# cancel_pop

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/cancel_pop`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479e300`

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `stationId` | ? | ? | ? | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479e240` |
| `version` | ? | ? | ? | `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x479e240` |

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

- `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart`: `cancelOtaUpdate` @0x479e240 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart::checkOtaVersion`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
