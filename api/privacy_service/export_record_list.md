> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# export_record_list

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/privacy_service/v1/export_record_list`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/user/dataExport/export_list/data_export_list_reposity.dart @0x29853fc`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys found by the extractor. <!-- TODO -->

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

- `charging/ui/page/user/dataExport/export_list/data_export_list_reposity.dart`: `getExportRecordList` @0x2985374 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
