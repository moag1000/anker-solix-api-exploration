> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# energy_analysis

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v2/device/energy_analysis`, method: not extracted by the inventory <!-- TODO -->; string-only: `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2991c7c`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `path` | ? | ? | ? | `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2991c18` |
| `method` | ? | ? | ? | `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2991c18` |
| `param.device_sn` | ? | ? | ? | `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2991c18` |
| `param.start_time` | ? | ? | ? | `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2991c18` |
| `param.end_time` | ? | ? | ? | `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2991c18` |
| `param.type` | ? | ? | ? | `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2991c18` |
| `device_sn` | ? | ? | ? | `third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca26f8` |
| `start_time` | ? | ? | ? | `third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca26f8` |
| `end_time` | ? | ? | ? | `third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca26f8` |
| `phase` | ? | ? | ? | `third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca26f8` |
| `type` | ? | ? | ? | `third_device/src/module/ae1x0/history/widget/meter_chart_logic.dart @0x2ca26f8` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

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

- `s1_s2/src/sdk/command/s1_s2_device_command.dart`: `getChargeSessionChartModel` @0x2991c18 (URL literal only, no `*Http*` call)
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
