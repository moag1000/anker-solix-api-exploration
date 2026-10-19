> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# export_account_data

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/privacy_service/v1/export_account_data`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/user/dataExport/data_export_reposity.dart @0x298560c`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `account` | ? | ? | ? | `charging/ui/page/user/dataExport/data_export_reposity.dart @0x29854bc` |
| `send_email` | ? | ? | ? | `charging/ui/page/user/dataExport/data_export_reposity.dart @0x29854bc` |
| `access_token` | ? | ? | ? | `charging/ui/page/user/dataExport/data_export_reposity.dart @0x29854bc` |
| `export_data_type` | ? | ? | ? | `charging/ui/page/user/dataExport/data_export_reposity.dart @0x29854bc` |

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

- `charging/ui/page/user/dataExport/data_export_reposity.dart`: `exportAccountData` @0x29854bc (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
