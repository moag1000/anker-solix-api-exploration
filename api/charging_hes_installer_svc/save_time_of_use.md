> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# save_time_of_use

## Purpose

Switches a site to a time-of-use (TOU) price plan: the app sends the on/off switch, the id of the site or device and the TOU type, and for the auto-TOU result page also the provider name and provider parameters.

## Upstream name

`none` for the installer URL (no upstream name). The consumer twin `/charging_hes_dynamic_price_svc/save_time_of_use` is listed without a key in `api/apitypes.py` (line 479, comment "needs owner").

## Method+URL

`POST /charging_hes_installer_svc/save_time_of_use` (asm-traced). The URL comes from the static getter `Api.saveAutoTou` (`base_service/api_url.dart @0x2e82408`; the Dart name is `saveAutoTou`): installer string `pp+0x8aca0` (`@0x2e82414`) when `isProApp` is true, otherwise `/charging_hes_dynamic_price_svc/save_time_of_use` (`pp+0x8aca8`, `@0x2e82420`); see [the variant selector](README.md#variant-selector-installer-app-versus-consumer-app). Three senders load the field and call `HttpHelper.getDataFromService` (`Method.post`, `electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdb94`).

## Encrypted?

Yes by wrapper (asm-traced): the senders end in `encryptionRequestHttp` inside `HttpHelper::getDataFromService` (`http_helper.dart @0x27bdbc8`) without `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call goes through the SDK is decided at run time.

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `setMode` | bool | yes | `true` | map literal key in `ElectricityPriceModelApiHelper.changeToTouMode` (`electricity_price/components/electricity_price_common/electricity_price_model_api_helper.dart @0x2e8227c`, value `true` `@0x2e82288`) and `ElectricityPricePlanApiHelper.changeToTouPlan` (`electricity_price_plan_api_helper.dart @0x31aa07c`); also in `TOUAutoPricePkgResultLogic.save` (`electricity_price/components/electricity_price_common/tou_auto_preview/tou_auto_price_pkg_result_logic.dart @0x31b0f8c`, value from a parameter) |
| `touType` | int | yes | `52` | `changeToTouMode` `@0x2e82290`: the enum index of the argument (dispatch-table getter, `BoxInt64Instr` `@0x2e822bc`, plain int, no literal); `changeToTouPlan` `@0x31aa090` (same pattern); `TOUAutoPricePkgResultLogic.save` `@0x31b0fa0` with the literal raw `104` (`@0x31b0fac`) stored with `stur w16`, Smi, so 52 (`tools/smi.py`: `104 → stur w → 52`) |
| `sn` | String | one of `sn` / `siteId` | `"<device sn>"` | `changeToTouMode` `@0x2e82348`, `changeToTouPlan` `@0x31aa148`, `save` `@0x31b1028`; set when a mode flag is true and the device serial is non-empty |
| `siteId` | String | one of `sn` / `siteId` | `"<site id>"` | `@0x2e82374`, `@0x31aa174`, `@0x31b1050` |
| `companyName` | String | auto-TOU result page only | `"<provider name>"` | `tou_auto_price_pkg_result_logic.dart @0x31b0f44`; value is an observable's value (`@0x31b0f5c`) |

`TOUAutoPricePkgResultLogic.save` also reads `providerParams` from the page arguments (`@0x31b107c`); whether it merges the entries into this body (as the dynamic-price senders do, see [save_dynamic_price](save_dynamic_price.md#request)) was not checked. The body of the request is passed to `saveAuto` (`@0x31b11dc`), which calls `getDataFromService` with the field `Api.saveAutoTou` (`@0x31b1214`, call `@0x31b1274`).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed; the success closures only report success.

## Response

No response field is read by the helper senders (asm-traced). They pass two shared static closures to `getDataFromService` (`@0x2268374` and `@0x227d9ac`; Blutter names them after unrelated functions, `HttpRequestControllerImpl::postJML` and `AnkerWidgetImpl::showStationBuiltSuccessDialog`, because identical code is shared); which of the two is the success callback was not separated, and their bodies were not read. The `saveAuto` closures are `@0x31b12fc` and `@0x31b1290`, also not read.

## Example request/response

Request, synthesized

```json
{ "setMode": true, "touType": 1, "siteId": "<site id>" }
```

The value of `touType` here is a placeholder; the enum values are not decoded. Response: no captured response; no field is read.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../errors.md).

## Callers in app

- `ElectricityPriceModelApiHelper.changeToTouMode` (`electricity_price/components/electricity_price_common/electricity_price_model_api_helper.dart @0x2e821dc`; field load `@0x2e82388`, `getDataFromService` `@0x2e823ec`).
- `ElectricityPricePlanApiHelper.changeToTouPlan` (`electricity_price/components/electricity_price_common/electricity_price_plan_api_helper.dart @0x31a9fdc`; field load `@0x31aa188`, call `@0x31aa1ec`).
- `TOUAutoPricePkgResultLogic.save` (`electricity_price/components/electricity_price_common/tou_auto_preview/tou_auto_price_pkg_result_logic.dart @0x31b0ee0`) via `saveAuto` (`@0x31b11dc`), the auto-TOU result preview page.

## Since/changed

3.18.0: absent as an installer URL (the 3.18.0 pool holds no `installer_svc` string); the consumer twin `/charging_hes_dynamic_price_svc/save_time_of_use` is in the 3.18.0 pool. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- The enum values behind `touType` (the helper senders send an enum index) are not decoded; only the auto-TOU page sends a literal (52).
- Server behaviour is not known.
- Whether `providerParams` is merged into the body of the auto-TOU save is not checked.

## Device-tested by

none
