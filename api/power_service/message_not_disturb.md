> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# message_not_disturb

## Purpose

Writes the do-not-disturb and push-scene settings of the message centre: `setEvChargerPushMessage` (called from `EvChargerMessageSettingLogic::chargerPushMessageHasChanged`) sends the EV charger scenes, `setMessageDisturb` (called from `MessageSettingDetailLogic::disturbHasChanged`, `showStartPicker`, `showEndPicker` and `GuardianDiaryMessageSettingLogic::guardianDiaryPushValueChange`) sends the time window, the switch and the Guardian log flag.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/message_not_disturb` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `HttpRequestControllerImpl::setEvChargerPushMessage` (`http_request_repository_impl.dart @0x402b348`): URL string `@0x402b4d4`, method object `Method.post` (`pp+0xa7e0`) `@0x402b4cc`.
- `HttpRequestControllerImpl::setMessageDisturb` (`http_request_repository_impl.dart @0x402c798`): URL string `@0x402c95c`, method object `Method.post` (`pp+0xa7e0`) `@0x402c954`.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Two senders with different key sets.

Sender `setEvChargerPushMessage` (`http_request_repository_impl.dart @0x402b348`): a 1-pair outer map typed `<String, Map<String, bool>>` (`@0x402b484`, pool `pp+0x36f90`) whose value is a 7-pair inner map typed `<String, bool>` (`AllocateArray r2 = 28` `@0x402b3b8`, type arguments `@0x402b44c`, pool `pp+0x9f90`), so the seven values are bool.

| field | type | required | example | source |
|---|---|---|---|---|
| `disturb_scenes` | object | yes | | key `@0x402b3a8`, value store `@0x402b460` |
| `disturb_scenes.start_charging` | bool | yes | `true` | key `@0x402b3c0`, value store `@0x402b3d0` (stack parameter `fp+0x20`) |
| `disturb_scenes.stop_charging` | bool | yes | `true` | key `@0x402b3d4`, value store `@0x402b3e4` (`fp+0x18`) |
| `disturb_scenes.paused_charging` | bool | yes | `true` | key `@0x402b3e8`, value store `@0x402b3f8` |
| `disturb_scenes.paused_car_charging` | bool | yes | `true` | key `@0x402b3fc`, value store `@0x402b40c` |
| `disturb_scenes.restore_charging` | bool | yes | `true` | key `@0x402b410`, value store `@0x402b420` |
| `disturb_scenes.smart_charging` | bool | yes | `true` | key `@0x402b424`, value store `@0x402b434` (`fp+0x28`) |
| `disturb_scenes.boost_charging` | bool | yes | `true` | key `@0x402b438`, value store `@0x402b448` |

Sender `setMessageDisturb` (`http_request_repository_impl.dart @0x402c798`): an empty `<String, Object>` map (`empty_array` `@0x402c7f8`, `Map._fromLiteral` `@0x402c800`) to which four keys are added with `Map.[]=`.

| field | type | required | example | source |
|---|---|---|---|---|
| `start_time` | int (unboxed, x) | yes | | key `@0x402c838`, `BoxInt64Instr` `@0x402c810`, `[]=` `@0x402c840` |
| `end_time` | int (unboxed, x) | yes | | key `@0x402c87c`, `BoxInt64Instr` `@0x402c850`, `[]=` `@0x402c884` |
| `disturb_switch` | ? | yes | | key `@0x402c8a4`, `[]=` `@0x402c8ac` (parameter at `fp-0x30`, loaded `@0x402c8a0`) |
| `disturb_scenes` | object | optional | | key `@0x402c910`, `[]=` `@0x402c918`; added only when the parameter at `fp-0x28` is non-null (`cmp w0, NULL` `@0x402c8bc`) |
| `disturb_scenes.guardian_log` | bool | yes | `true` | key `@0x402c8d4`, value store `@0x402c8e4`; the inner map is typed `<String, bool>` (`@0x402c8e8`) |

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed. The `setEvChargerPushMessage` success callback `http_request_repository_impl.dart @0x402b5cc` and the `setMessageDisturb` success callback `@0x402ca54` use their argument only for the log strings (`"---> setEvChargerPushMessage request success"`, `"---> setMessageDisturb request success, data: "`) and call `exeSuccess()`.

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (`setEvChargerPushMessage`)

```json
{"disturb_scenes": {"start_charging": true, "stop_charging": true, "paused_charging": true, "paused_car_charging": true, "restore_charging": true, "smart_charging": true, "boost_charging": true}}
```

Request, synthesized (`setMessageDisturb`, `disturb_switch` type unresolved)

```json
{"start_time": 0, "end_time": 0, "disturb_switch": "<disturb_switch>", "disturb_scenes": {"guardian_log": true}}
```

## Errors seen

None traced. The failure callbacks `@0x402b518` and `@0x402c9a0` log the code and message and call `exeError()`; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `setEvChargerPushMessage` @0x402b348 (encryptionRequestHttp; encrypted: true); `setMessageDisturb` @0x402c798 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::setEvChargerPushMessage`
- `charging/http/http_request_repository.dart::setMessageDisturb`
- `charging/ui/page/message/settingDetail/ev_charger_message_setting_logic.dart::chargerPushMessageHasChanged`
- `charging/ui/page/message/settingDetail/guardian_diary_message_setting_logic.dart::guardianDiaryPushValueChange`
- `charging/ui/page/message/settingDetail/message_setting_detail_logic.dart::disturbHasChanged`
- `charging/ui/page/message/settingDetail/message_setting_detail_logic.dart::showEndPicker`
- `charging/ui/page/message/settingDetail/message_setting_detail_logic.dart::showStartPicker`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. `tools/out/diff_3.18.0_3.24.3.md` (changed params) lists `guardian_log` as added and `disturb_switch`, `end_time`, `start_time` as removed. In 3.24.3 `setMessageDisturb` still sets the three "removed" keys with `[]=` (`@0x402c840`, `@0x402c884`, `@0x402c8ac`); the string-level diff sees map-literal keys, so the "removed" part is an artefact of how those keys are built. `guardian_log` sits in a map literal (`@0x402c8d4`).

## Known unknowns

- Type of `disturb_switch` (a parameter of `setMessageDisturb`; the four UI callers were not followed). Header stays string-only.
- Whether 3.18.0 sent the time window in a map literal (the diff suggests literal keys there): not read, 3.18.0 asm was not opened for this page.
- Which sender the server expects for which scene: the two key sets never appear together in one request.
- The response body: not read by the app.

## Device-tested by

none
