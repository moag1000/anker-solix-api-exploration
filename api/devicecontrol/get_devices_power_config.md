> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_devices_power_config

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/devicecontrol/v1/get_devices_power_config`, method: not extracted by the inventory <!-- TODO -->; string-only: `settings/src/sdk/util/grid_connect_util.dart @0x2af18c8`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `devices` | ? | ? | ? | `settings/src/sdk/util/grid_connect_util.dart @0x2af17a4` |

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

- `settings/src/sdk/util/grid_connect_util.dart`: `getBatchPowerConfig` @0x2af17a4 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
