> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# mothly_report_list

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/mothly_report_list`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/user/profile/profile_http_request_repository_impl.dart @0x2989ebc`

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

- `charging/http/user/profile/profile_http_request_repository_impl.dart`: `getMonthlyReportList` @0x2989de8 (encryptionRequestHttp; encrypted: true)

Called from: `charging/ui/page/anker_post/anker_monthly_report_list_logic.dart::getMonthlyReportList`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
