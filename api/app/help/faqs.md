> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# faqs

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/help/faqs`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x347fcf8`
(literal also at 2 more site(s) in `data/endpoints.json`)

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

- `charging/http/http_request_repository_impl.dart`: `getFaqs` @0x347fc70 (encryptionRequestHttp; encrypted: true)
- `charging/util/manager/http_manager.dart`: `<anonymous closure> in HttpRequestManager::requestHttp` @0x2cf6370 (URL literal only, no `*Http*` call; a path check inside the generic HTTP manager (`isDemoBlockPath`), not a request: no sender); `requestHttp` @0x2cf6108 (URL literal only, no `*Http*` call; a path check inside the generic HTTP manager (`isDemoBlockPath`), not a request: no sender)

Called from:

- `charging/http/http_request_repository.dart::getFaqs`
- `charging/ui/page/device/a1340/a1340setting/a1340setting_logic.dart::_gotoHelpPage`
- `charging/ui/page/device/a172x/a172xsetting/a172xsetting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/a1770/a1770setting/a1770setting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/a1780/a1780setting/a1780setting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/a1781/a1781setting/a1781setting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/a17b1/device_setting/a17b1device_setting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/a17b1/home_setting/home_setting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/a17c0/select_bluetooth_guide/select_bluetooth_guide_solarbank_fail_logic.dart::goFeedback`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/a17x7/a17x7setting/a17x7setting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/a17x8/a17x8setting/a17x8setting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/a2345/a2345setting/a2345setting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/a5101/ota/a5101_base_ota_logic.dart::gotoFAQHelpPage`
- `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/a5101/setting/solix_setting/solix_setting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/a5140/a5140setting/a5140setting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/a5150/homePage/a5150_home_logic.dart::gotoHelpPage`
- `charging/ui/page/device/a91b2/a91b2setting/a91b2setting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/cooler/a17a3setting/a17a3setting_logic.dart::gotoHelpPage`
- `charging/ui/page/device/cooler/coolerSetting/cooler_setting_logic.dart::gotoHelpPage`
- `charging/ui/page/message/messageDetailInfo/message_detail_info_logic.dart::getViewFAQ`
- `charging/ui/page/user/feedback/feedback_logic.dart::getFaqList`
- `charging/ui/page/user/help/help_logic.dart::onInit`
- `charging/util/manager/http_manager.dart::encryptionRequestHttp`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
