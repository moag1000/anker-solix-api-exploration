> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_standby_exercise_plan

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/generator/v1/app/set_standby_exercise_plan`, method: not extracted by the inventory <!-- TODO -->; string-only: `ats_ax170/src/sdk/command/ax170_command.dart @0x38235ec`

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `path` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x3823588` |
| `method` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x3823588` |
| `param.device_sn` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x3823588` |
| `param.next_maintenance_time` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x3823588` |
| `param.interval_period_week` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x3823588` |
| `param.maintenance_time` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x3823588` |
| `param.status` | ? | ? | ? | `ats_ax170/src/sdk/command/ax170_command.dart @0x3823588` |

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

- `ats_ax170/src/sdk/command/ax170_command.dart`: `<anonymous closure>@0x3823588` @0x3823588 (URL literal only, no `*Http*` call)

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
