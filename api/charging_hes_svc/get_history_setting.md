> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_history_setting

## Purpose

Reads the history schedule mode and the last time-of-use set type of a site for the price settings (`GeneralPriceSettingLogic::queryLargeChargingDeviceHasSetMode`; the inventory also lists `TouAndTimeSlotSettingsDetailLogic` and `TouAndTimeslotSettingsPolyLogic`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`Api::getHistorySetting` (`base_service/api_url.dart @0x29a4950`) returns `/charging_hes_installer_svc/get_history_setting` (`@0x29a495c`) when the static flag `0xad8` is true and `/charging_hes_svc/get_history_setting` (`@0x29a4968`) otherwise (`tbnz w1, #4` `@0x29a4958` branches on false). The sender `GeneralPriceSettingLogic::queryLargeChargingDeviceHasSetMode` (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a412c`) loads the late static field `getHistorySetting` (`@0x29a41b0`) and calls `HttpHelper::getDataFromService` (`@0x29a4250`); the helper (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bda38`) sends with the method object `Method.post` (pool entry `pp+0xa7e0`, `@0x27bdb94`) through `encryptionRequestHttp` (`@0x27bdbc8`). That the late static field holds the result of `Api::getHistorySetting` was not read, so the URL link stays string-only.

## Encrypted?

encrypted: `true` (app side). Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app". The helper `HttpHelper::getDataFromService` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bda38`) calls `encryptionRequestHttp` (`@0x27bdbc8`).

## Request

The caller builds a `<String, dynamic>` literal (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a41e8`), which does not type the value, with the single key `station_id` (`@0x29a41cc`); the value is `field_7b` of the logic (load `@0x29a41dc`, stored `@0x29a41e4`). `GeneralPriceSettingLogic::onInit` (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x34f1210`) fills that field from the key `site_id` of its arguments with a cast to `String?` (`r8 = String?` `@0x34f13c8`, cast `@0x34f13d4`, store `@0x34f13e0`), so the value is a String. The map goes to `getDataFromService` (`@0x29a4250`).

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes | `"<station_id>"` | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a41cc` |

## `param_type`/`cmd`

n/a

## Response model (link)

no model: the success closure (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a42a8`) reads the keys of the response map directly (see Response).

## Response

(asm-traced) Keys read by the success closure: `history_schedule_mode` (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4438`, a map), `tou_last_set_type` (`@0x29a4480`, a map), `is_manual_tou_configured` (`@0x29a4598`, bool, default `false` `@0x29a45b4`) and `last_select_mode` (`@0x29a460c`, int); the integer is compared with tagged immediates and decides between `setToManualTou` (`@0x29a47f8`) and `setToAutoTou` (`@0x29a48f8`). A response that is not a map logs `historyScheduleMode error` (`@0x29a43f0`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a426c`) logs `getHistorySetting error` (`@0x29a4280`).

## Callers in app

- `base_service/api_url.dart`: `getHistorySetting` @0x29a4950 (URL literal only, no `*Http*` call; sender `HttpHelper::getDataFromService` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bda38`) (HTTP helper wrapper), called from `GeneralPriceSettingLogic::queryLargeChargingDeviceHasSetMode` (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a412c`); also through `TouAndTimeSlotSettingsDetailLogic::queryLargeChargingDeviceHasSetMode`, `TouAndTimeslotSettingsPolyLogic::queryLargeChargingDeviceHasSetMode`; resolved from the URL literal at `base_service/api_url.dart @0x29a4968` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. `tools/out/diff_3.18.0_3.24.3.md` lists `station_id` as removed for this URL (string-level), but the 3.24.3 sender still stores the key (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a41cc`), so that row only means the literal is not matched to the senders linked to this URL. The installer variant `/charging_hes_installer_svc/get_history_setting` is new in 3.24.3.

## Known unknowns

- The URL link stays string-only: the sender loads the late static `getHistorySetting` (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a419c`; offset 0xb08, declared `static late String getHistorySetting` in `base_service/api_url.dart`); its initializer was not found, so that it holds the result of `Api::getHistorySetting` rests on the shared name and offset.
- The values of `last_select_mode` that select manual or automatic time-of-use (compared with tagged immediates `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a46e0`..`@0x29a4744`): not decoded.
- Which of the two URLs is used at run time: it depends on the static flag `0xad8`, whose setter was not read.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
