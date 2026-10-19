> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# mark_sn

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/after_sale/mark_sn`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_business_impl.dart @0x286075c`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `after_sale_type` | ? | ? | ? | `charging/http/http_business_impl.dart @0x28605c0` |
| `device_sns` | ? | ? | ? | `charging/http/http_business_impl.dart @0x28605c0` |
| `mark_type` | ? | ? | ? | `charging/http/http_business_impl.dart @0x28605c0` |

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

- `charging/http/http_business_impl.dart`: `afterSaleMarkSn` @0x28605c0 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_business_impl.dart::showNoIceBoxReplaceDialog`, `charging/ui/page/device/cooler/Battery_Relace_Ment/Battery_Replace_Contact_Sales/battery_replace_contact_sales_logic.dart::done`, `charging/ui/page/device/cooler/Battery_Relace_Ment/Battery_Replace_WebView/battery_replace_web_view.dart::build`, `charging/ui/page/device/cooler/Battery_Relace_Ment/battery_replace_ment_logic.dart::applicationSubmitted`, `charging/ui/page/user/feedback/feedback_logic.dart::showSuccessDialog`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
