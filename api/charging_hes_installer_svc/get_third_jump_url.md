> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_third_jump_url

## Purpose

Asks the cloud for the URL of the third-party authorization page of a dynamic-price provider (Tibber or Flatpeak) together with a wait time and an aggregation frequency; the app opens the URL so the user can connect the provider account.

## Upstream name

`none` for the installer URL (no upstream name). The consumer twin `/charging_hes_dynamic_price_svc/get_third_jump_url` is listed without a key in `api/apitypes.py` (line 481).

## Method+URL

`POST /charging_hes_installer_svc/get_third_jump_url` (asm-traced). The URL comes from the static getter `Api.getThirdJumpUrl` (`base_service/api_url.dart @0x29acc3c`): installer string `pp+0x66610` (`@0x29acc48`) when `isProApp` is true, otherwise `/charging_hes_dynamic_price_svc/get_third_jump_url` (`pp+0x66618`, `@0x29acc54`); see [the variant selector](README.md#variant-selector-installer-app-versus-consumer-app). Two senders use it through `HttpHelper.getDataFromService` (`Method.post`, `electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdb94`): `_DynamicPriceHttpServer.getThirdJumpUrl` (`dynamic_price_http_server.dart @0x43917b8`, field load `@0x43918c0`, call `@0x4391924`) and `ElectricityPlaceConfirmPageLogic.getDynamicPriceCompany` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac204`, a misleading function name, field load `@0x29ac3c0`, call `@0x29ac420`).

## Encrypted?

Yes by wrapper (asm-traced): both senders end in `encryptionRequestHttp` inside `HttpHelper::getDataFromService` (`http_helper.dart @0x27bdbc8`) without `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)); the Tibber sender turns the loading overlay on (`r16 = true`, `dynamic_price_http_server.dart @0x4391908`). Whether the call goes through the SDK is decided at run time.

## Request

Two senders, two body shapes.

Tibber sender (`dynamic_price_http_server.dart`), `Map<String, String?>` with four pairs (`r2 = 16`, `@0x43917e0`):

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | String? | no | `"<site id>"` | `@0x43917e8`; function argument (null when unknown) |
| `sn` | String? | no | `"<device sn>"` | `@0x43917fc`; function argument; both keys are always present |
| `companyName` | String | yes | `"Tibber"` | `@0x4391810`, literal value `"Tibber"` `@0x439181c` |
| `type` | String | yes | `"IMPORT"` | `@0x4391828`, literal value `"IMPORT"` `@0x4391830` |

Flatpeak sender (`electricty_place_confirm_logic.dart`, function `getDynamicPriceCompany`, `<String, dynamic>`; keys set one by one):

| field | type | required | example | source |
|---|---|---|---|---|
| `pn` | String | yes | `"<product code>"` | `@0x29ac254`; value read from an object field (`@0x29ac264`, offset 0x9f chain) |
| `sn` / `siteId` | String | one of | `"<id>"` | `@0x29ac2e4`, `@0x29ac318`; `sn` when a device id exists and is non-empty (`@0x29ac2d0`), else `siteId` |
| `companyName` | String | yes | `"Flatpeak"` | `@0x29ac340`, literal `"Flatpeak"` `@0x29ac348` |
| `type` | String | yes | `"IMPORT"` or `"EXPORT"` | `@0x29ac37c` (`IMPORT`, `@0x29ac380`), `@0x29ac3a8` (`EXPORT`, `@0x29ac3ac`); the choice depends on the function's `type` argument (compared with raw `2` in the closure, `@0x29ac4f4`, so 1) |

## `param_type`/`cmd`

n/a

## Response model (link)

`ThirdJumpModel` ([../../models/dynamic_price_server_model.md](../../models/dynamic_price_server_model.md)), parsed with `ThirdJumpModel.fromJson` (`dynamic_price_server_model.dart @0x4391aa0`) at `dynamic_price_http_server.dart @0x4391a64` (Tibber sender). The Flatpeak sender reads the raw map instead (see Response).

## Response

Wrapper keys `code`, `msg`, `data` as in [../encryption.md](../encryption.md#response-handling-and-error-codes). The Tibber success closure passes the payload to `ThirdJumpModel.fromJson` (`jumpUrl`, `flatpeakWaitTime`, `aggregationFrequency`). The Flatpeak success closure (`electricty_place_confirm_logic.dart @0x29ac478`) reads keys directly:

| field | type | required | example | source |
|---|---|---|---|---|
| `flatpeakWaitTime` | int (null counts as 0) | no | `0` | `@0x29ac50c` |
| `aggregationFrequency` | int | no | not decoded | `@0x29ac5b0` (type `1` path) and `@0x29ac8ec` (other path); stored under the app-side names `buyAggregationFrequency` (`@0x29ac680`) and `saleAggregationFrequency` (`@0x29ac9bc`) |
| `jumpUrl` | String | yes | `"https://..."` | `@0x29ac698`, `@0x29ac9d4`; the app appends `&lang=` (`@0x29ac744`) and `&selectAddress=` (`@0x29ac7d4`) to it before opening it |

## Example request/response

Request, synthesized (Tibber sender)

```json
{ "siteId": "<site id>", "sn": null, "companyName": "Tibber", "type": "IMPORT" }
```

Response: no captured response; the key list is on the model page.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../errors.md).

## Callers in app

- `_DynamicPriceHttpServer.getThirdJumpUrl` (`electricity_price/components/dynamic_price/general_kit/http_server/dynamic_price_http_server.dart @0x43917b8`), Tibber setup; called from `ElectricityCompanySelectLogic` (`electricity_price/components/dynamic_price/setting/electricty_company_select_logic.dart @0x4391770`).
- `ElectricityPlaceConfirmPageLogic.getDynamicPriceCompany` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac204`), the place confirmation page of the Flatpeak setup.

## Since/changed

3.18.0: absent as an installer URL (the 3.18.0 pool holds no `installer_svc` string); the consumer twin `/charging_hes_dynamic_price_svc/get_third_jump_url` is in the 3.18.0 pool. 3.24.3: present (new). since: 3.24.3. `ThirdJumpModel.aggregationFrequency` is new in 3.24.3 (model page).

## Known unknowns

- Server behaviour is not known (what the Flatpeak or Tibber page does with the wait time).
- The unit of `flatpeakWaitTime` and `aggregationFrequency` is not documented.
- Whether the Tibber answer carries `flatpeakWaitTime` and `aggregationFrequency` as non-null (the model declares them non-null) is not tested.

## Device-tested by

none
