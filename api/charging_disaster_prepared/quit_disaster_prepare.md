> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# quit_disaster_prepare

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_disaster_prepared/quit_disaster_prepare`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a350c`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `type` | ? | ? | ? | `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a3384` |
| `identifier_id` | ? | ? | ? | `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a3384` |
| `is_ble` | ? | ? | ? | `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a3384` |
| `disaster_type` | ? | ? | ? | `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a3384` |

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

- `charging/ui/page/device/a1782/home/a1782_home_logic.dart`: `<anonymous closure> in _A1782DeviceLogic&AnkerBaseController&DeviceCountDownLogic&DeviceBatteryStatusLogic&GetTickerProviderStateMixin&PreparednessModuleMixin&AutoDisasterPreparednessMixin::onQuitCurrentEvent` @0x22a3384 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: string present in the object pool, no code reference found. since: ≤3.18.0.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
