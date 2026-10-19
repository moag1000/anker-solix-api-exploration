> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_history_setting

## Purpose

Reads the history of the TOU (time-of-use) schedule settings of a large (HES) station, i.e. which price mode was last set; the price settings pages use it to decide whether a manual or an automatic TOU mode is already configured.

## Upstream name

`none` for the installer URL (no upstream name). The consumer twin `/charging_hes_svc/get_history_setting` is listed without a key in `api/apitypes.py` (line 447, comment "needs owner").

## Method+URL

`POST /charging_hes_installer_svc/get_history_setting` (asm-traced). The URL comes from the static getter `Api.getHistorySetting` (`base_service/api_url.dart @0x29a4950`): installer string `pp+0x7c590` (`@0x29a495c`) when `isProApp` is true, otherwise `/charging_hes_svc/get_history_setting` (`pp+0x7c598`, `@0x29a4968`); see [the variant selector](README.md#variant-selector-installer-app-versus-consumer-app). Three senders, all named `queryLargeChargingDeviceHasSetMode` and using `HttpHelper.getDataFromService` (`Method.post`, `http_helper.dart @0x27bdb94`).

## Encrypted?

Yes by wrapper (asm-traced): the senders end in `encryptionRequestHttp` inside `HttpHelper::getDataFromService` (`http_helper.dart @0x27bdbc8`) without `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call goes through the SDK is decided at run time.

## Request

Map literal with one string pair in all three senders; there is no `isProApp` branch, so the installer URL also receives `station_id`.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | String | yes | `"<site id>"` | `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a41cc`; `electricity_price/components/electricity_module/page/tou_and_timeslot_settings_detail_logic.dart @0x29af96c` (value is the object field at offset 0x67, `@0x29af984`); `tou_and_timeslot_settings_poly_logic.dart @0x29afac4` |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model class is parsed; the success closure reads single keys from the raw map. A class `HistoryScheduleMode` exists in `charging/model/a5101/a5101_device_command_model.dart` (see [../../models/hes.md](../../models/hes.md)), but this closure does not call it.

## Response

Read by the success closure of `tou_and_timeslot_settings_detail_logic.dart` (`@0x29b0338`); the poly page has the same closure shape.

| field | type | required | example | source |
|---|---|---|---|---|
| `history_schedule_mode` | map | no | `{ ... }` | `@0x29b04f4`; on error the closure logs `historyScheduleMode error` (`@0x29b04a4`) |
| `tou_last_set_type` | int or String (not decoded) | no | not decoded | `@0x29b053c` |
| `is_manual_tou_configured` | bool (not decoded) | no | not decoded | `@0x29b0568`; the result is stored under the app-side key `hasSetManualTou` (`@0x29b05c8`, also `@0x29b08d0`, `@0x29b0ab8`) |
| `last_select_mode` | not decoded | no | not decoded | `@0x29b0718` |
| `price_sub_source_type` | not decoded | no | not decoded | `@0x29b0740` |

The nesting of the last four keys under `history_schedule_mode` is inferred from the order of the reads; the app also derives `hasSetAutoTouMode` (`@0x29b0914`, `@0x29b0afc`).

## Example request/response

Request, synthesized

```json
{ "station_id": "<site id>" }
```

Response: no captured response; the key types are not decoded.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `queryLargeChargingDeviceHasSetMode` in `electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a412c` (field load `@0x29a41b0`, call `getDataFromService` `@0x29a4250`), in `electricity_price/components/electricity_module/page/tou_and_timeslot_settings_detail_logic.dart @0x29af908` (`@0x29af950`; `@0x29af9d8`) and in `tou_and_timeslot_settings_poly_logic.dart @0x29afa60` (`@0x29afaa8`; `@0x29afb2c`): the TOU and time-slot settings pages of the price module (package `electricity_price`).

## Since/changed

3.18.0: absent as an installer URL (the 3.18.0 pool holds no `installer_svc` string); the consumer twin `/charging_hes_svc/get_history_setting` is in the 3.18.0 pool. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- Value types of the five response keys are not decoded.
- Server behaviour and the semantics of `tou_last_set_type` and `last_select_mode` are not known.

## Device-tested by

none
