> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# site_data_exported

## Purpose

The export of site energy data as a file: in 3.18.0 `SiteEnergyExportLogic` (mixin `DownloadFileLogic::requestSiteExportFileUrl`) posted a `toMap()` of the export parameters to this URL and the app downloaded the file URL it got back; upstream names the endpoint `get_site_csv_export`.

## Upstream name

`get_site_csv_export` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/site_data_exported`, method: not read. In 3.24.3 the URL string exists only in the object pool (`pp+0xc04e0`, `pp.txt` line 280620) and no instruction references that pool slot (a search for `pp+0xc04e0` in the 3.24.3 asm finds nothing), so no sender exists to read. The 3.18.0 sender sits in `site_energy_export_logic.dart` (3.18.0 asm: URL string `@0x2349b58`, `Instance_Method` object `@0x2349b50`, `encryptionRequestHttp` `@0x2349b7c`); its pool offset is not comparable with the 3.24.3 pool.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys in 3.24.3 (no sender). In 3.18.0 the body is the result of `toMap()` on the export parameter object (3.18.0 `@0x2349b18`); its keys were not read.

## `param_type`/`cmd`

n/a

## Response model (link)

None in 3.24.3 (no sender). 3.18.0: the success and failure closures passed to `encryptionRequestHttp` (3.18.0 `@0x2349b20`, `@0x2349b34`) were not read.

## Response

Not applicable in 3.24.3; not read in 3.18.0.

## Example request/response

No example: the 3.24.3 app has no sender, and the 3.18.0 body keys were not read.

## Errors seen

None traced: no 3.24.3 sender. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/widgets/data_export/energy_flow/site_energy_export_logic.dart`: `<anonymous closure> in _SiteEnergyExportLogic&BaseGetController&ChangeExportTimeRangeLogic&DownloadFileLogic::requestSiteExportFileUrl` @0x2349c3c (URL literal only, no `*Http*` call); `<anonymous closure> in _SiteEnergyExportLogic&BaseGetController&ChangeExportTimeRangeLogic&DownloadFileLogic::requestSiteExportFileUrl` @0x2349d0c (URL literal only, no `*Http*` call); `requestSiteExportFileUrl` @0x2349a2c (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present (sender in `site_energy_export_logic.dart`). 3.24.3: string present in the object pool (`pp+0xc04e0`), no code reference found. since: ≤3.18.0. `tools/out/diff_3.18.0_3.24.3.md` lists the endpoint under removed endpoints.

## Known unknowns

- Header stays string-only: no 3.24.3 sender exists to read (only the pool string).
- Whether the server still serves this URL: the 3.24.3 app no longer calls it; the diff file lists it as removed.
- What replaced the export download in 3.24.3: `SiteEnergyExportLogic` still exists (it calls [site_data_check](site_data_check.md)); the file request was not located.
- The 3.18.0 request keys (`toMap()` of the export parameters) and the response were not read for this page.

## Device-tested by

none
