> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# mark_sn

## Purpose

Marks devices as handled in the fridge-battery recall flow ("after-sale mark") when the user confirms the replace dialog or submits the replacement application (callers `HttpBusinessImpl::showNoIceBoxReplaceDialog`, `BatteryReplaceContactSalesLogic::done`, `BatteryReplaceMentLogic::applicationSubmitted`, `FeedbackLogic::showSuccessDialog`) (asm-traced).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/after_sale/mark_sn` (asm-traced): URL string at `charging/http/http_business_impl.dart @0x286075c` in `HttpBusinessImpl::afterSaleMarkSn` (`@0x28605c0`), sent through `HttpBusinessImpl::encryptionRequestHttp` (`@0x2860778` call), which passes `Method.post` (pool entry `pp+0xa7e0`) at `charging/http/http_business_impl.dart @0x261877c` to `requestHttp` (`@0x26187b8`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) One map literal of 3 pairs (`AllocateArray` raw `r2 = 12` at `@0x28606cc`, so 6 slots) with type arguments `<String, Object>` (`@0x2860718`); all keys are stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `after_sale_type` | int (Smi, w) | yes | `1` | `charging/http/http_business_impl.dart @0x28606d4` (raw 2 stored by 32-bit store `@0x28606e4`, so 1) |
| `device_sns` | ? | yes | ? | `charging/http/http_business_impl.dart @0x28606e8` (value loaded from a field of the builder's receiver, `LoadField field_f` `@0x28606f8`) |
| `mark_type` | int (Smi, w) | yes | `1` | `charging/http/http_business_impl.dart @0x2860704` (raw 2 stored by 32-bit store `@0x2860714`, so 1) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure (`charging/http/http_business_impl.dart @0x2860874`) logs a success string (`exeInfo`), takes `first` of a list and calls `removeAfterSalesDeviceSns` (`@0x2860928`); it reads no response key: the closure's own argument (the response, `ldr x1, [fp, #0x10]` `@0x28608d8`) is only interpolated into the log text (`_interpolate` `@0x28608e4`, `exeInfo` `@0x28608f0`), and `first` (`@0x286091c`) is applied to `field_f` of a static object (`LoadStaticField(0xc18)` `@0x28608f4`, `LoadField` `@0x2860914`), i.e. a locally held list, not to the response; the result goes to `removeAfterSalesDeviceSns` (`@0x2860928`).

## Response

No response key is read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "after_sale_type": 1,
  "device_sns": "<?>",
  "mark_type": 1
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_business_impl.dart`: `afterSaleMarkSn` @0x28605c0 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_business_impl.dart::showNoIceBoxReplaceDialog`
- `charging/ui/page/device/cooler/Battery_Relace_Ment/Battery_Replace_Contact_Sales/battery_replace_contact_sales_logic.dart::done`
- `charging/ui/page/device/cooler/Battery_Relace_Ment/Battery_Replace_WebView/battery_replace_web_view.dart::build`
- `charging/ui/page/device/cooler/Battery_Relace_Ment/battery_replace_ment_logic.dart::applicationSubmitted`
- `charging/ui/page/user/feedback/feedback_logic.dart::showSuccessDialog`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Type of `device_sns` (a field value; `<String, Object>` only says non-null) and its element format. — attempted 2026-10-20 (two-hop not readable: the value is `field_f` of an object held by the builder (`charging/http/http_business_impl.dart @0x28606f8`); the five callers (`showNoIceBoxReplaceDialog`, `battery_replace_contact_sales_logic.dart::done`, `battery_replace_web_view.dart::build`, `battery_replace_ment_logic.dart::applicationSubmitted`, `feedback_logic.dart::showSuccessDialog`) reach it through that object and no declared type is shown. Header stays string-only)
- What `after_sale_type` and `mark_type` values other than 1 would do (the sender sends constants). — reclassified: server
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
