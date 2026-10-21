> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# set_monthly_report_configs

## Purpose

Switches the monthly-report message setting on or off: `MessageSettingDetailLogic::monthlyReportHasChanged` (`message_setting_detail_logic.dart @0x402e8c0`) runs when the user changes the monthly-report switch and calls `setMonthlyReportConfigs`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/set_monthly_report_configs` (asm-traced): URL string at `msg_http_request_repository_impl.dart @0x402eaf8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x402eaf0`, in `MsgHttpRequestControllerImpl::setMonthlyReportConfigs` (`msg_http_request_repository_impl.dart @0x402ea60`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The caller builds the body: an outer 1-pair map typed `<String, Map<String, String>>` (`charging/ui/page/message/settingDetail/message_setting_detail_logic.dart @0x402e990`, pool `pp+0xbec0`) whose value is an inner 1-pair map typed `<String, String>` (`@0x402e958`, pool `pp+0xa4d0`). The builder `setMonthlyReportConfigs` (`msg_http_request_repository_impl.dart @0x402ea60`) forwards the map to `encryptionRequestHttp` (`@0x402eb28`).

| field | type | required | example | source |
|---|---|---|---|---|
| `configs` | object | yes | | key `charging/ui/page/message/settingDetail/message_setting_detail_logic.dart @0x402e910`, value store `@0x402e96c` (the inner map) |
| `configs.mothly_report_messages` | string | yes | `"1"` or `"0"` | key `charging/ui/page/message/settingDetail/message_setting_detail_logic.dart @0x402e928` (spelled `mothly`), value store `@0x402e954`; `"1"` (`@0x402e93c`) when the bool parameter is true, `"0"` (`@0x402e948`) when it is false (`tbnz w1, #4` `@0x402e938`, true when bit 4 is clear); the inner map is typed `<String, String>` |

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed. The success path calls the caller's callback with the constant `true` (`http_request_repository_impl.dart @0x261b9a0`, `r16 = true` `@0x261b9cc`, `ClosureCall` `@0x261b9d4`); that callback (`message_setting_detail_logic.dart @0x402eba8`) builds `MonthlyReportMsgConfigModel.fromJson` (`@0x402ebf0`) from `r1[0]`, the context slot the caller fills with the request body map (`@0x402e9b0`), and stores it with `setMonthlyReportMsgCache` (`@0x402ebfc`). The model has the single key `configs` (`data/models.json`, `charging::MonthlyReportMsgConfigModel`), the same shape as the request body.

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (decrypted body as built by `monthlyReportHasChanged`)

```json
{"configs": {"mothly_report_messages": "1"}}
```

Response: none parsed.

## Errors seen

None traced. The failure callback `message_setting_detail_logic.dart @0x402eb44` only writes the negated bool back into an Rx field (`eor x1, x0, #0x10` `@0x402eb7c`, `value=` `@0x402eb8c`); no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/user/msg/msg_http_request_repository_impl.dart`: `setMonthlyReportConfigs` @0x402ea60 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/message/settingDetail/message_setting_detail_logic.dart::monthlyReportHasChanged`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- The response body: not read by the app, so its keys are unknown. — reclassified: server (not visible in the app: the app does not read the body)
- Whether the server echoes the stored `configs` object: the app builds its local cache from the request body, not from an answer.
- Which other keys `configs` can hold on the server: the app sends only `mothly_report_messages`.

## Device-tested by

none
