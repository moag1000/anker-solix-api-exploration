> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# check_sn

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/after_sale/check_sn`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_business_impl.dart @0x261863c`

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

- `charging/http/http_business_impl.dart`: `afterSalesCheckSn` @0x2618594 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/account/handlers/login_handler.dart::_handleLoginSuccessAndReturnResult`
- `charging/ui/page/account/login/login_logic.dart::_loginSuccessAction`
- `charging/ui/page/account/region/region_logic.dart::confirmSwitchRegion`
- `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart::onMessageDispatch`
- `charging/ui/page/device/rename/rename_logic.dart::onInit`
- `charging/ui/page/home/home_page.dart::initMessageListener`
- `charging/util/third_party_service.dart::openAppOptional`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
