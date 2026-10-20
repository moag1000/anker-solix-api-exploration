> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# check_sn

## Purpose

Checks the account's devices against the fridge-battery recall list (after-sale SN check) after login, region switch and device updates (callers `LoginHandler::_handleLoginSuccessAndReturnResult`, `LoginLogic::_loginSuccessAction`, `RegionLogic::confirmSwitchRegion`, `DeviceMainLogic::onMessageDispatch`, `HomePage::initMessageListener` and others); the builder logs "fridge battery recall" strings (asm-traced).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/after_sale/check_sn` (asm-traced): URL string at `charging/http/http_business_impl.dart @0x261863c` in `HttpBusinessImpl::afterSalesCheckSn` (`@0x2618594`), sent through `HttpBusinessImpl::encryptionRequestHttp` (`@0x2618658` call, body `@0x2618680`), which passes the method object `Method.post` (pool entry `pp+0xa7e0`) at `charging/http/http_business_impl.dart @0x261877c` to `requestHttp` (`@0x26187b8`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) No request fields: the body argument is the empty map literal (`THR::empty_array`, `Map._fromLiteral` at `charging/http/http_business_impl.dart @0x2618604`). The request is sent only when `isChinaRegion()` is false: `tbnz w0, #4` at `@0x26185b4` branches on false to the request code at `@0x26185fc`; when it is true the builder calls `setAfterSalesDeviceSns` with an empty list (`@0x26185e8`) and returns without a request (`ret` `@0x26185f8`).

`DeviceUtil::isChinaRegion` (`charging/util/device_util.dart @0x224edac`) takes the region code from `getCurrentRegion` (`@0x224edcc`), uses the String literal `"US"` when it is null (`@0x224ede0`) and compares it with the String literal `"CN"` (`@0x224edf8`, equality dispatch call `@0x224ee10`): the request is skipped exactly when the current region code equals `"CN"` (app side).

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::AfterSalesCheckSnModel`, parsed by `AfterSalesCheckSnModel.fromJson` at `charging/http/http_business_impl.dart @0x261890c`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `AfterSalesCheckSnModel` top-level keys (`data/models.json`, `charging::AfterSalesCheckSnModel`): `web_url` (String?), `device_list` (unknown).

## Example request/response

Request, synthesized: the body is the empty object.

```json
{}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

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

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Why the app skips the request for the region code `"CN"` (see Request) is not stated in the app — reclassified: server
- What the response keys mean beyond the model field names, and what the server returns for an account without recall devices.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
