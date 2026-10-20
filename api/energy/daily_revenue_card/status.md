> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# status

## Purpose

Reads the state of the "yesterday earnings" card of a micro-HES station (status, revenue with currency, link, dynamic-price and abnormal flags).

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /energy/v1/daily_revenue_card/status` (asm-traced). Sender: `YesterdayEarningTipsLogic.fetchCardStatus` (`micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x27e8698`); the URL literal is loaded at `@0x27e8a10` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x27e8a08`).

## Encrypted?

Yes by wrapper (asm-traced): `fetchCardStatus` calls `HttpServiceImpl.encryptionRequestHttp` (`micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x27e8a44`) with the named arguments `cancelToken`, `complete`, `fail`, `showLoading` and `success` (`@0x27e8a3c`) and without `needEncryption`, so the default `true` applies ([encryption.md](../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../encryption.md)); asm alone does not decide it.

## Request

Body is a one-pair map (`r2 = 4`, `@0x27e8980`) built from the site id; the sender logs `fetchCardStatus siteId=..., reload=...` first (`@0x27e8734`) and skips the call when a request is already running (`Reload requested` path, `@0x27e8854`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `<site id>` | `yesterday_earning_tips_view.dart @0x27e8988`; the logic object's site id field |

## `param_type`/`cmd`

n/a

## Response model (link)

`DailyRevenueCardStatus` ([../../../models/daily_revenue_card_status.md](../../../models/daily_revenue_card_status.md#dailyrevenuecardstatus)): the success closure (`micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x27e8c28`) checks that the data is a `Map<String, dynamic>` (`@0x27e8ca8`), calls `DailyRevenueCardStatus.fromJson` (`@0x27e8cc0`) and stores the object in an observable (`value=`, `@0x27e8ccc`).

## Response

The failure closure (`@0x27e8abc`) ignores a cancelled request (`cancel`, `@0x27e8af4`) and otherwise logs `fetchCardStatus failed: code=... msg=...` and resets the observable (`@0x27e8b50`); the completion closure (`@0x27e8a68`) sets another observable to `false` (a loading flag, `@0x27e8a94`).

| field | type | required | example | source |
|---|---|---|---|---|
| `status`, `is_dynamic`, `revenue`, `currency_unit`, `link_url`, `is_abnormal` | see model page | no | `{ "status": 1, "is_dynamic": false, "revenue": "1.20", "currency_unit": "EUR", "link_url": "...", "is_abnormal": false }` | `yesterday_earning_tips_view.dart @0x27e8dcc` to `@0x27e9018`; [model page](../../../models/daily_revenue_card_status.md#dailyrevenuecardstatus) |

## Example request/response

Request, synthesized

```json
{ "site_id": "<site id>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- an anonymous closure in `YesterdayEarningTipsLogic` (`micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x27e8680`)
- `YesterdayEarningTipsLogic.updateSiteId` (`micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x3548970`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x175580`). since: 3.24.3.

## Known unknowns

- The meaning of the `status` codes and the unit of `revenue` are not decoded. — reclassified: server (2026-10-20: status codes and the revenue unit are server data)
- The example response values are placeholders of the right JSON types, not a capture.

## Device-tested by

none
