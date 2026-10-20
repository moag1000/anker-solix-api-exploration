> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# mothly_report_list

## Purpose

Reads the list of monthly reports for the monthly report list page (caller `AnkerMonthlyReportListLogic::getMonthlyReportList`; builder `ProfileHttpRequestControllerImpl::getMonthlyReportList`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/mothly_report_list` (asm-traced): URL string at `charging/http/user/profile/profile_http_request_repository_impl.dart @0x2989ebc`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2989eb4`, in `ProfileHttpRequestControllerImpl::getMonthlyReportList` (`charging/http/user/profile/profile_http_request_repository_impl.dart @0x2989de8`), sent through `encryptionRequestHttp` (`@0x2989eec`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) No request fields: the only body candidate is an empty `<String, dynamic>` literal (`THR::empty_array`, type arguments `@0x2989e2c`, `Map._fromLiteral` `@0x2989e38`); a length test on it (`LoadInt32Instr` `@0x2989e5c`, `cbnz x2` `@0x2989e70`) replaces an empty map by `Null` (`@0x2989e74`), so no keys are sent.

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::MonthlyReportListModel`, parsed by `MonthlyReportListModel.fromJson` at `charging/http/user/profile/profile_http_request_repository_impl.dart @0x2989f5c`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `MonthlyReportListModel` top-level keys (`data/models.json`, `charging::MonthlyReportListModel`): `reports` (List<String?>), `year_reports` (List<YearReports>), `monthly_report_url` (String), `year` (int?).

## Example request/response

Request, synthesized: no body fields (the sender passes a null body).

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/user/profile/profile_http_request_repository_impl.dart`: `getMonthlyReportList` @0x2989de8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/anker_post/anker_monthly_report_list_logic.dart::getMonthlyReportList`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The length test is read from the compact-hash layout loads (`field_13`, `List_4[0]` `@0x2989e58..0x2989e6c`); that it is an `isEmpty` check is derived from the arithmetic, not from a symbol.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
