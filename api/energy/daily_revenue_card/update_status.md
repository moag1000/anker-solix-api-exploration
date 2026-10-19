> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# update_status

## Purpose

Tells the cloud that the user has seen or completed the "yesterday earnings" card of a station (the card's tap flow calls it once), so the card status moves on.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /energy/v1/daily_revenue_card/update_status` (asm-traced). Sender: `YesterdayEarningTipsLogic._updateRevenueStatus` (`micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x2e8dd9c`); the URL literal is loaded at `@0x2e8df30` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x2e8df28`).

## Encrypted?

Yes by wrapper (asm-traced): `_updateRevenueStatus` calls `HttpServiceImpl.encryptionRequestHttp` (`micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x2e8df58`) with the named arguments `fail`, `showLoading` and `success` (`@0x2e8df50`) and without `needEncryption`, so the default `true` applies ([encryption.md](../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../encryption.md)); asm alone does not decide it.

## Request

Body is a one-pair map (`r2 = 4`, `@0x2e8dec8`); the sender logs `updateViewStatus siteId=...` first (`@0x2e8ddfc`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `<site id>` | `yesterday_earning_tips_view.dart @0x2e8ded0` |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model; the success closure reads one key.

## Response

The success closure (`micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x2e8e068`) checks that the data is a `Map<String, dynamic>` (`@0x2e8e0a8`), reads the key `success` (`@0x2e8e0b8`), defaults to `false` (`@0x2e8e0d4`) and logs `updateViewStatus success=...`. Exceptions are logged as `updateViewStatus exception: ...` (`@0x2e8df74`).

| field | type | required | example | source |
|---|---|---|---|---|
| `success` | bool | no | `true` | `yesterday_earning_tips_view.dart @0x2e8e0b8` |

## Example request/response

Request, synthesized

```json
{ "site_id": "<site id>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `YesterdayEarningTipsLogic.completeTapFlow` (`micro_hes/src/common_business/basic_station/module/income_statistics/yesterday_earning_tips_view.dart @0x2e8dd10`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x167c48`). since: 3.24.3.

## Known unknowns

- What the server changes in the card status after the call is not known; the next `status` call shows the new state.

## Device-tested by

none
