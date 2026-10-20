> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# faqs

## Purpose

Loads the FAQ entries (products and models with their help links); sent by `HttpRequestControllerImpl::getFaqs` for the device settings pages (`gotoHelpPage`), `HelpLogic::onInit`, `FeedbackLogic::getFaqList` and `MessageDetailInfoLogic::getViewFAQ` (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`GET /app/help/faqs` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x347fcf8`, method object `Method.get` (pool entry `pp+0x340e8`) at `@0x347fcf0`, in `HttpRequestControllerImpl::getFaqs` (`charging/http/http_request_repository_impl.dart @0x347fc70`), sent through `encryptionRequestHttp` (`@0x347fd20`).

The two other rows of the inventory (`charging/util/manager/http_manager.dart @0x2cf6108` and its closure `@0x2cf6370`) are not senders: the literal there is a path check inside the generic manager (see Callers in app).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No body field: the sender builds an empty map literal (`Map._fromLiteral` `charging/http/http_request_repository_impl.dart @0x347fcbc`, no key store before it).

## `param_type`/`cmd`

n/a

## Response model (link)

[`FaqModel`](../../../models/other.md#faqmodel), parsed by `FaqModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x347fe4c` in the element closure `@0x347fe24`; the success closure (`@0x347fd3c`) first resolves the list with `resolveListResponseData` (`@0x347fd68`) and maps each element through that closure to a `List<FaqModel>` (`@0x347fda8`), which it passes to the callback (`ClosureCall` `@0x347fe00`). Call target `#0x347fe68` in `charging/model/faq_model.dart`.

## Response

(asm-traced) The top level is a list of `FaqModel` (the helper `resolveListResponseData` extracts the list; its key handling was not read). Keys of `charging::FaqModel` (`data/models.json`): `faqs` (unknown), `index` (int?), `product_code` (String?), `model_name` (String?), `img_url` (String?).

## Example request/response

Request: no body fields are built (see Request). Response: not synthesized; no capture exists for this endpoint.

## Errors seen

none traced: no numeric error code is compared in the sender, its closures or the caller functions read for this page. Code meanings are owned by `api/errors.md`.

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

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- How `resolveListResponseData` finds the list in the response (a fixed key or the `data` array): the helper was not read.
- What the request does with the empty body map for a GET: how `Method.get` bodies are sent is described in `api/encryption.md`; the map has no entries here.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
