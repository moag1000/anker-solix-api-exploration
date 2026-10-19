> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# message_not_disturb

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/message_not_disturb`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x402b4d4`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `disturb_scenes.start_charging` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x402b348` |
| `disturb_scenes.stop_charging` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x402b348` |
| `disturb_scenes.paused_charging` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x402b348` |
| `disturb_scenes.paused_car_charging` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x402b348` |
| `disturb_scenes.restore_charging` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x402b348` |
| `disturb_scenes.smart_charging` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x402b348` |
| `disturb_scenes.boost_charging` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x402b348` |
| `guardian_log` | ? | ? | ? | `charging/http/http_request_repository_impl.dart @0x402c798` |

Rows are the union over 2 senders; `source` is the first sender that sets the key.

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

- `charging/http/http_request_repository_impl.dart`: `setEvChargerPushMessage` @0x402b348 (encryptionRequestHttp; encrypted: true); `setMessageDisturb` @0x402c798 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::setEvChargerPushMessage`, `charging/http/http_request_repository.dart::setMessageDisturb`, `charging/ui/page/message/settingDetail/ev_charger_message_setting_logic.dart::chargerPushMessageHasChanged`, `charging/ui/page/message/settingDetail/guardian_diary_message_setting_logic.dart::guardianDiaryPushValueChange`, `charging/ui/page/message/settingDetail/message_setting_detail_logic.dart::disturbHasChanged`, `charging/ui/page/message/settingDetail/message_setting_detail_logic.dart::showEndPicker`, `charging/ui/page/message/settingDetail/message_setting_detail_logic.dart::showStartPicker`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
