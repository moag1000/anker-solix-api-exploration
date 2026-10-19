> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_device_exercise_details

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/get_device_exercise_details`, method: not extracted by the inventory <!-- TODO -->; string-only: `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dc870`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | ? | ? | `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x29dc75c` |

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

- `oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart`: `getDeviceExerciseDetailsRequest` @0x29dc75c (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
