> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_message_not_disturb

## Purpose

Reads the do-not-disturb setting of the message centre: `MessageSettingDetailLogic::requestCloudMessageDisturb`, the EV charger and Guardian diary setting logics and `MessageDisturbCacheUtil::fetchAndCacheDisturbSetting` call `getMessageDisturb`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/get_message_not_disturb` (asm-traced): URL string at `http_request_repository_impl.dart @0x273a634`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x273a62c`, in `HttpRequestControllerImpl::getMessageDisturb` (`http_request_repository_impl.dart @0x273a54c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is an empty map literal (`ldr x16, [THR, #0xa8]` empty array `@0x273a5d8`, `Map._fromLiteral` `@0x273a5e0`); the builder contains no `[]=` call, so no key is added. The map goes to `encryptionRequestHttp` (`@0x273a664`).

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::MsgDisturbHttpModel` (`data/models.json` key; fields on [`models/other.md`](../../models/other.md#msgdisturbhttpmodel)), parsed in the success closure `http_request_repository_impl.dart @0x273a734` by `MsgDisturbHttpModel.fromJson`.

## Response

Top-level keys of the model (from `data/models.json`): `end_time` (int), `start_time` (int), `disturb_switch` (bool), `disturb_scenes` (`DisturbScenesHttpModel`: `stop_charging`, `start_charging`, `paused_charging`, `paused_car_charging`, `restore_charging`, `smart_charging`, `boost_charging`, `guardian_log`, all bool).

## Example request/response

Request, synthesized

```json
{}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The builder's failure callback `@0x273a680` logs `"---> getMessageDisturb request failed, code: "` and the message, then calls `exeError()`; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getMessageDisturb` @0x273a54c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getMessageDisturb`
- `charging/ui/page/message/settingDetail/ev_charger_message_setting_logic.dart::requestCloudPushMessageSetting`
- `charging/ui/page/message/settingDetail/guardian_diary_message_setting_logic.dart::requestCloudPushMessageSetting`
- `charging/ui/page/message/settingDetail/message_setting_detail_logic.dart::requestCloudMessageDisturb`
- `charging/util/message_disturb_cache_util.dart::fetchAndCacheDisturbSetting`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `MsgDisturbHttpModel` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- Which of the response keys the server fills for a given account type: the model marks all nullable.
- How the written counterpart ([message_not_disturb](message_not_disturb.md)) maps onto these keys: its two senders send different key sets.

## Device-tested by

none
