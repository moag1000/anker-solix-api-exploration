> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_monthly_report_configs

## Purpose

Reads the monthly-report message settings for the message setting detail page (caller `MessageSettingDetailLogic::requestMonthlyReportMsg`; builder `MsgHttpRequestControllerImpl::getMonthlyReportConfigs`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/get_monthly_report_configs` (asm-traced): URL string at `charging/http/user/msg/msg_http_request_repository_impl.dart @0x29826f4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x29826ec`, in `MsgHttpRequestControllerImpl::getMonthlyReportConfigs` (`charging/http/user/msg/msg_http_request_repository_impl.dart @0x2982670`), sent through `encryptionRequestHttp` (`@0x2982720`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) No request fields: the `data` argument of `encryptionRequestHttp` is `NULL` (`stp x0, NULL, [SP, #0x18]` at `charging/http/user/msg/msg_http_request_repository_impl.dart @0x2982700`; the stack slot after the URL slot holds NULL, no map is built in the builder).

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::MonthlyReportMsgConfigModel`, parsed by `MonthlyReportMsgConfigModel.fromJson` at `charging/http/user/msg/msg_http_request_repository_impl.dart @0x298276c`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `MonthlyReportMsgConfigModel` top-level keys (`data/models.json`, `charging::MonthlyReportMsgConfigModel`): `configs` (Map).

## Example request/response

Request, synthesized: no body fields (the sender passes a null body).

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/user/msg/msg_http_request_repository_impl.dart`: `getMonthlyReportConfigs` @0x2982670 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/message/settingDetail/message_setting_detail_logic.dart::requestMonthlyReportMsg`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Which stack slot of the call carries the body: the call descriptor `r4 = const [0x1, 0x8, 0x8, 0x6, isLogResponse, 0x6, showLoading, 0x7, null]` and the `NULL` pair store were read together with the signature of `encryptionRequestHttp` (`charging/http/http_request_repository_impl.dart @0x226451c`: positionals method, url, data, fail, success); the slot assignment is derived from that, not from a symbol.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
