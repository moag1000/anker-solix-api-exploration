> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# platform_get_site_savings

## Purpose

Reads the savings (income) statistics of a site for a chart period: the self-sufficiency split between solar and grid, the trend values per period, the total with its unit and the list of years; the income detail pages of the micro HES (A17E2) and the station home use it.

## Upstream name

`none` for the key; upstream lists the URL without a key in `api/apitypes.py` (line 354).

## Method+URL

`POST /power_service/v2/site/platform_get_site_savings` (asm-traced). Two senders: `A17e2BenifitsHttpRepository.getChartStatistics` (`charging/ui/page/device/a17e2/benifits/a17e2_benifits_http_repository.dart @0x2a47fd4`; URL literal `@0x2a48244`, `Method.post` pool entry `pp+0xa7e0`, `@0x2a4823c`) and `IncomeDetailController.getChartStatistics` (`station_home/src/ui/shared/income/income_detail/income_detail_controller.dart @0x2a43540`; URL literal `@0x2a436b0`).

## Encrypted?

A17E2 sender: `requestHttp` (`charging/ui/page/device/a17e2/benifits/a17e2_benifits_http_repository.dart @0x2a48284`, plain callee; its default `needEncryption` is `true` and is not overridden here, so the decorator tests apply; [which calls are encrypted](../../../encryption.md#which-calls-are-encrypted)). Income detail sender: `StationApiClient.request` (`station_home/src/ui/shared/income/income_detail/income_detail_controller.dart @0x2a436b8`), which sends through the SDK handler with the identifier `akiot.cloud_api` (path C; `station_home/src/http/station_api_client.dart @0x2a444c0`).

## Request

Both senders build the same five keys.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `"<site id>"` | `charging/ui/page/device/a17e2/benifits/a17e2_benifits_http_repository.dart @0x2a48198` (map literal), `station_home/src/ui/shared/income/income_detail/income_detail_controller.dart @0x2a435d8` (set with `[]=`; value is the late field `siteId`, offset 0xc7, `@0x2a435b8`) |
| `type` | int | yes | not decoded | `@0x2a481ac`, `@0x2a43600`; the income detail sender boxes an untagged int (`BoxInt64Instr`, `@0x2a43614`), i.e. an enum index or similar computed value, not a literal |
| `data_type` | not decoded | yes | not decoded | `@0x2a481bc`, `@0x2a43640` |
| `start_time` | not decoded | yes | not decoded | `@0x2a481d0`, `@0x2a43668` |
| `end_time` | not decoded | yes | not decoded | `@0x2a48210` (set with `[]=` after the literal), `@0x2a43698` |

The A17E2 sender also logs `getA17E2ChartStatistics: siteId=..., type=..., dataType=..., startTime=..., endTime=...` (`@0x2a48074`). It passes `debounceMills` as a call argument (raw `600` at `@0x2a48260`, a tagged argument, so 300 ms of debounce) and `showLoading`/`showDefaultError`: these are request options, not body keys.

## `param_type`/`cmd`

n/a

## Response model (link)

`IncomeDetailModel` and `A17e2BenifitsModel` ([../../../../models/income_detail_model.md](../../../../models/income_detail_model.md)): the same layout in two Dart classes. `IncomeDetailModel.fromJson` is called at `station_home/src/ui/shared/income/income_detail/income_detail_controller.dart @0x2a436f8`; `A17e2BenifitsModel.fromJson` at `charging/ui/page/device/a17e2/benifits/a17e2_benifits_http_repository.dart @0x2a48598` (in `_handleResponse`, called from the success closure `@0x2a4834c`).

## Response

All fields live in the model page (wrapper `code`, `msg`, `data` as in [encryption.md](../../../encryption.md#response-handling-and-error-codes)). The income detail sender passes the payload (`r0->field_7` of the `StationApiClient` result, `@0x2a436e4`) to `IncomeDetailModel.fromJson`; on failure it logs `platform_get_site_savings: message=...` (`@0x2a4372c`).

## Example request/response

Request, synthesized

```json
{ "site_id": "<site id>", "type": 1, "data_type": "<data type>", "start_time": "<start>", "end_time": "<end>" }
```

The values of `type`, `data_type`, `start_time` and `end_time` are placeholders. Response: no captured response; the key list is on the model page.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `A17e2BenifitsHttpRepository.getChartStatistics` (`charging/ui/page/device/a17e2/benifits/a17e2_benifits_http_repository.dart @0x2a47fd4`): the benefits (profit detail) page of the A17E2 system (package `charging`).
- `IncomeDetailController.getChartStatistics` (`station_home/src/ui/shared/income/income_detail/income_detail_controller.dart @0x2a43540`), called from `_executeChartDataRequest` and `_updateCurrentMonthDataIfNeeded`: the income detail page of the station home (package `station_home`).

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3. `IncomeDetailModel` and `A17e2BenifitsModel` are new in 3.24.3.

## Known unknowns

- The value domains and formats of `type`, `data_type`, `start_time` and `end_time` are not decoded.
- The unit and currency semantics of `total` and `unit` are not known.
- Server behaviour is not known.

## Device-tested by

none
