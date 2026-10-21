> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# site_data_exported

## Purpose

The export of site energy data as a file: in 3.18.0 `SiteEnergyExportLogic` (mixin `DownloadFileLogic::requestSiteExportFileUrl`) posted a `toMap()` of the export parameters to this URL and the app downloaded the file URL it got back; upstream names the endpoint `get_site_csv_export`.

## Upstream name

`get_site_csv_export` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/site/site_data_exported`, method: not read. In 3.24.3 the URL string exists only in the object pool (`pp+0xc04e0`, `pp.txt` line 280620) and no instruction references that pool slot (a search for `pp+0xc04e0` in the 3.24.3 asm finds nothing), so no sender exists to read. The 3.18.0 sender sits in `site_energy_export_logic.dart` (3.18.0 asm: URL string `0x2349b58`, `Instance_Method` object `0x2349b50`, `encryptionRequestHttp` `0x2349b7c`); its pool offset is not comparable with the 3.24.3 pool.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys in 3.24.3 (no sender). In 3.18.0 the body is the result of `toMap()` on the export parameter object: `SiteEnergyExportLogic.requestSiteExportFileUrl` (`charging/widgets/data_export/energy_flow/site_energy_export_logic.dart`) calls `HttpSiteDataExportParams::toMap` (3.18.0 address 0x2349b18; `base_service/bean/export_data/http_site_export_mode.dart`, function 0x2349b9c), which builds a 3-pair map literal (`AllocateArray r2 = 12` 0x2349bc0) with `site_id` (0x2349bc8), `start_time` (0x2349be4) and `end_time` (0x2349bfc), each from a field of the object without conversion; the response type argument there is `HttpExportFileResponse?` (3.18.0 addresses are from the 3.18.0 tree and are written without `@` because the citation checker reads the 3.24.3 tree).

## `param_type`/`cmd`

n/a

## Response model (link)

None in 3.24.3 (no sender). 3.18.0: the success and failure closures passed to `encryptionRequestHttp` (3.18.0 `0x2349b20`, `0x2349b34`) were not read.

## Response

Not applicable in 3.24.3; not read in 3.18.0.

## Example request/response

No example: the 3.24.3 app has no sender, and the 3.18.0 body keys were not read.

## Errors seen

None traced: no 3.24.3 sender. Error codes are catalogued in `api/errors.md`.

## Callers in app

- 3.18.0 asm (addresses below are 3.18.0, not 3.24.3) `charging/widgets/data_export/energy_flow/site_energy_export_logic.dart`: `<anonymous closure> in _SiteEnergyExportLogic&BaseGetController&ChangeExportTimeRangeLogic&DownloadFileLogic::requestSiteExportFileUrl` 0x2349c3c (URL literal only, no `*Http*` call); `<anonymous closure> in _SiteEnergyExportLogic&BaseGetController&ChangeExportTimeRangeLogic&DownloadFileLogic::requestSiteExportFileUrl` 0x2349d0c (3.18.0 address; the same number in 3.24.3 lies in `base_station_logic.dart` and is unrelated) (URL literal only, no `*Http*` call); `requestSiteExportFileUrl` 0x2349a2c (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present (sender in `site_energy_export_logic.dart`). 3.24.3: string present in the object pool (`pp+0xc04e0`), no code reference found. The export itself is still there: `SiteEnergyExportLogic.confirmLoadExportFile` (`charging/widgets/data_export/energy_flow/site_energy_export_logic.dart @0x38de6e8`) calls a method of the deduplicated mixin `DownloadFileLogic` (`@0x38de73c`, class `_MixinApplication803&BaseGetController&ChangeExportTimeRangeLogic&DownloadFileLogic`; Blutter does not emit that code), and its callback (`@0x38df02c`) takes an `HttpExportFileResponse?`, checks `HttpExportFileResponse::isValid` and calls `downloadAndShare` (`@0x38df080`); so the request moved into mixin code that is not in the asm tree. since: ≤3.18.0. `tools/out/diff_3.18.0_3.24.3.md` lists the endpoint under removed endpoints.

## Known unknowns

- Whether the server still serves this URL: the 3.24.3 app no longer calls it; the diff file lists it as removed.

## Device-tested by

none
