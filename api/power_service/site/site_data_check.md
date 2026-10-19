> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# site_data_check

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/site/site_data_check`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/widgets/data_export/energy_flow/site_energy_export_logic.dart @0x2c34e68`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | ? | ? | `charging/widgets/data_export/energy_flow/site_energy_export_logic.dart @0x2c34c20` |
| `current_time` | ? | ? | ? | `charging/widgets/data_export/energy_flow/site_energy_export_logic.dart @0x2c34c20` |

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

- `charging/widgets/data_export/energy_flow/site_energy_export_logic.dart`: `_checkDataOfSiteSupportExport` @0x2c34c20 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/widgets/data_export/energy_flow/site_energy_export_logic.dart::updateMode`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
