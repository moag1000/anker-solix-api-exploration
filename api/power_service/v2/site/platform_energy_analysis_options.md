> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# platform_energy_analysis_options

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v2/site/platform_energy_analysis_options`, method: not extracted by the inventory <!-- TODO -->; string-only: `ats_ax170/src/sdk/command/ax170_command.dart @0x23346d0`

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `path` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x2334664` |
| `method` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x2334664` |
| `param.site_id` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x2334664` |
| `param.device_sn` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x2334664` |
| `param.date_type` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x2334664` |
| `param.start_time` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x2334664` |
| `param.end_time` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x2334664` |
| `param.select_type` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x2334664` |

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

- `ats_ax170/src/sdk/command/ax170_command.dart`: `getPlatformEnergyAnalysisOptions` @0x2334664 (URL literal only, no `*Http*` call)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
