> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_message_not_disturb

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/get_message_not_disturb`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x273a634`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys found by the extractor. <!-- TODO -->

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

- `charging/http/http_request_repository_impl.dart`: `getMessageDisturb` @0x273a54c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getMessageDisturb`
- `charging/ui/page/message/settingDetail/ev_charger_message_setting_logic.dart::requestCloudPushMessageSetting`
- `charging/ui/page/message/settingDetail/guardian_diary_message_setting_logic.dart::requestCloudPushMessageSetting`
- `charging/ui/page/message/settingDetail/message_setting_detail_logic.dart::requestCloudMessageDisturb`
- `charging/util/message_disturb_cache_util.dart::fetchAndCacheDisturbSetting`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
