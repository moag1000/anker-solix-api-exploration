> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# energy_analysis

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v2/device/energy_analysis`, method: not extracted by the inventory <!-- TODO -->; string-only: `third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca2ba8`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca26f8` |
| `start_time` | ? | ? | ? | `third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca26f8` |
| `end_time` | ? | ? | ? | `third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca26f8` |
| `phase` | ? | ? | ? | `third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca26f8` |
| `type` | ? | ? | ? | `third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca26f8` |

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

- `third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart`: `requestChartData` @0x2ca26f8 (encryptionRequestHttp; encrypted: true)

Called from:

- `third_device/src/module/ae1x0/history/ae1x0_history_page.dart::didPop`
- `third_device/src/module/ae1x0/history/widget/meter_chart_widget.dart::build`
- `third_device/src/module/ae1x0/history/widget/meter_chart_widget.dart::initState`
- `third_device/src/module/ae1x0/home/ae1x0_home_logic.dart::_updateWifiSignal`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
