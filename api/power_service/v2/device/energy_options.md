> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# energy_options

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v2/device/energy_options`, method: not extracted by the inventory <!-- TODO -->; string-only: `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2998ed4`

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `path` | ? | ? | ? | `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2998e7c` |
| `param.device_sn` | ? | ? | ? | `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2998e7c` |

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

- `s1_s2/src/sdk/command/s1_s2_device_command.dart`: `getStartUseTime` @0x2998e7c (URL literal only, no `*Http*` call)

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
