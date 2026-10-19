> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

Removed in 3.24.3 — present in 3.18.0 only

# site_data_exported

## Purpose

<!-- TODO -->

## Upstream name

`get_site_csv_export` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/site_data_exported`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/widgets/data_export/energy_flow/site_energy_export_logic.dart @0x2349b58`
(literal also at 2 more site(s) in `data/endpoints.json`)

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

- `charging/widgets/data_export/energy_flow/site_energy_export_logic.dart`: `<anonymous closure> in _SiteEnergyExportLogic&BaseGetController&ChangeExportTimeRangeLogic&DownloadFileLogic::requestSiteExportFileUrl` @0x2349c3c (URL literal only, no `*Http*` call); `<anonymous closure> in _SiteEnergyExportLogic&BaseGetController&ChangeExportTimeRangeLogic&DownloadFileLogic::requestSiteExportFileUrl` @0x2349d0c (URL literal only, no `*Http*` call); `requestSiteExportFileUrl` @0x2349a2c (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: absent (removed). since: ≤3.18.0.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
