> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# download_energy_statistics

## Purpose

Reads the energy statistics for download (`EnergyStatisticsModel`) through `ChartHttpReposity::getDownloadEnergyStatistics`; the only recorded caller is the dependency registration `DIInit` (string-only: no caller chain in `data/endpoints.json`, inferred from the builder name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/download_energy_statistics` (asm-traced): URL string at `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c558`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x301c550`, in `ChartHttpReposity::getDownloadEnergyStatistics` (`charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c460`), sent through `requestHttp` (`@0x301c580`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `ChartHttpReposity::getDownloadEnergyStatistics` (`charging/ui/page/device/a5101/charts/chart_http_repository.dart`, call `@0x301c580`, argument list `@0x301c578`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `ChartHttpReposity::getDownloadEnergyStatistics` (`charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c524`, 6 keys). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `start` | string | yes | `"<start>"` | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c4b4` |
| `end` | string | yes | `"<end>"` | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c4c4` |
| `productCode` | string | yes | `"<productCode>"` | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c4d4` |
| `dateType` | string | yes | `"<dateType>"` | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c4e8` |
| `siteId` | string | yes | `"<siteId>"` | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c4fc` |
| `sourceType` | string | yes | `"<sourceType>"` | `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c510` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::EnergyStatisticsModel`, parsed by `EnergyStatisticsModel.fromJson` at `charging/ui/page/device/a5101/charts/chart_http_repository.dart @0x301c5d4` (success closure `@0x301c59c`, `bl` target `[package:charging/model/a5101/a5101_statistics_model/energy_statistics_model.dart]`).

App side use of the model (traced 2026-10-20): the success closure of `A5101ChartDetailController::downloadData` (`charging/ui/page/device/a5101/charts/detail/detail_page_logic.dart @0x301cf80`) reads `fileUrl` (field `field_7`, null and empty-string test `@0x301cfb0`..`@0x301cfe4`); when it is null or empty the closure logs `model.fileUrl is null` (`@0x301d024`) and calls `downloadError`; otherwise it calls `downloadAndShare` (`@0x301d01c`) with the URL and the `fileName` key (`field_b`) or, when that is null, the constant file name `EnergyData.csv` (`@0x301d000`). `downloadAndShare` creates a directory, downloads the file with `downloadFile` (`@0x301d254`) into it; the sharing step is inferred from the function name only.

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::EnergyStatisticsModel`): `fileUrl` (String?), `fileName` (String?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "start": "<start>",
  "end": "<end>",
  "productCode": "<productCode>",
  "dateType": "<dateType>",
  "siteId": "<siteId>",
  "sourceType": "<sourceType>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5101/charts/chart_http_repository.dart`: `getDownloadEnergyStatistics` @0x301c460 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/util/demosite_util_impl.dart`: `DemoSiteUtilImpl` @0x4a33a6c (URL literal only, no `*Http*` call)

Called from:

- `charging/boostrap_impl.dart::DIInit`

Call sites (traced 2026-10-20): `getDownloadEnergyStatistics` is called from `A5101ChartDetailController::downloadData` (`charging/ui/page/device/a5101/charts/detail/detail_page_logic.dart @0x301c444`), whose arguments come from a map lookup with the key `type` (`_getValueOrData` `@0x301c3a8`, fallback `""` `@0x301c3d8`) and `chartType()` (`@0x301c3ec`); its failure closure logs `A5101ChartDetailController-downloadData error: code=` and calls `downloadError` (`@0x301ce7c`, `@0x301cec4`).

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which `dateType`, `sourceType` and `productCode` values `downloadData` passes: the values come from a map of the chart detail page (key `type`, `charging/ui/page/device/a5101/charts/detail/detail_page_logic.dart @0x301c3a8`) and `chartType()`, not decoded further — attempted 2026-10-20 (two-hop not readable: @0x301c3a8, @0x301c3ec, @0x301c444).
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
