> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_utility_rate_plans

## Purpose

Reads the utility rate plan of a large (HES) station: the price source type, the fixed rate or the peak/valley (time-of-use) price table, and, in the new TOU flow, the peak sessions and the price unit.

## Upstream name

`none` for the installer URL (no upstream name). The consumer twin `/charging_hes_svc/get_utility_rate_plans` has no upstream key; `api/apitypes.py` lists the different, older URLs `charging_energy_service/get_utility_rate_plan` (key `get_utility_rate_plan`, line 213) and `charging_hes_svc/get_utility_rate_plan` (line 454, comment "page not found?").

## Method+URL

`POST /charging_hes_installer_svc/get_utility_rate_plans` (asm-traced). The URL comes from the static getter `Api.getHesUtilityRatePlans` (`base_service/api_url.dart @0x24a5d58`): installer string `pp+0x664a0` (`@0x24a5d64`) when `isProApp` is true, otherwise `/charging_hes_svc/get_utility_rate_plans` (`pp+0x664a8`, `@0x24a5d70`); see [the variant selector](README.md#variant-selector-installer-app-versus-consumer-app). Ten functions load the field; seven of them build and send the request (table under "Callers in app"), three only compare the field with another URL to choose a request shape (`getPriceTypeUrl` `general_price_setting.dart @0x29a4dd4`, `getElectricityUsagePolicyUrl` `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x292e664`, the closure at `@0x292e848`). All senders use `Method.post` (pool entry `pp+0xa7e0`).

## Encrypted?

Yes by wrapper (asm-traced): the senders call `encryptionRequestHttp` (addresses in the table under "Callers in app"); `TouHttpService.getUtilityRatePlans` goes through `HttpHelper.request`, which calls `HttpServiceImpl::encryptionRequestHttp` (`api/encryption.md`, wrapper table). `needEncryption` is not passed, so the default `true` applies ([which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call goes through the SDK is decided at run time; asm alone does not decide it.

## Request

The body is a small map with the station id and two number keys. The key spelling differs by sender: the new TOU flow and the AI-mode sender use camelCase for the Nem flag, the others snake_case. None of the senders has an `isProApp` branch for the body, so the installer URL receives `station_id`.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | String | yes | `"<site id>"` | all senders, for example `tou_http_service.dart @0x4879118`, `system_policy_logic.dart @0x24a5490` |
| `not_include_nem` (snake_case senders) or `notIncludeNem` (camelCase senders) | int | yes | `1` | snake_case: `system_policy_logic.dart @0x24a54d0`, `smart_mode_logic.dart @0x3eae3d8`, `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x292e4f8`, `tou_plan_logic.dart @0x2c4941c`, `general_price_setting.dart @0x29a4bfc`; camelCase: `tou_http_service.dart @0x4879140`, `ems_ai_mode_condition_logic.dart @0x2a30d7c`. Raw `2` in each case (table at the end), a tagged Smi, so 1 |
| `accuracy` | int | yes | `5` | `tou_http_service.dart @0x487912c`, `system_policy_logic.dart @0x24a54e4`, `smart_mode_logic.dart @0x3eae3ec`, `ems_ai_mode_condition_logic.dart @0x2a30d90`, `electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x292e520`, `tou_plan_logic.dart @0x2c493f4`, `general_price_setting.dart @0x29a4c24`; raw `10`, so 5 |
| `currency` | int | no | `5` | only `general_price_setting.dart @0x29a4c10` (`getDevicePriceType`); raw `10` (`@0x29a4c1c`, stored with `stur w16`), so 5; the key looks odd for a currency and the value equals `accuracy`, the meaning is not known |

Integer table (raw immediate, address, store, decoded; all Smi): `not_include_nem` / `notIncludeNem` raw 2 at `general_price_setting.dart @0x29a4c08`, `tou_http_service.dart @0x487914c`, `ems_ai_mode_condition_logic.dart @0x2a30d88`, `system_policy_logic.dart @0x24a54dc`, `smart_mode_logic.dart @0x3eae3e4` (each `stur w`, `tools/smi.py`: 1); `electricity_usage_helper.dart @0x292e500`, `tou_plan_logic.dart @0x2c49424` (register passed as the value argument of a map `[]=` call, a tagged object argument, so 1); `accuracy` raw 10 at `general_price_setting.dart @0x29a4c30`, `tou_http_service.dart @0x4879138`, `ems_ai_mode_condition_logic.dart @0x2a30d9c`, `system_policy_logic.dart @0x24a54f0`, `smart_mode_logic.dart @0x3eae3f8` (`stur w`, 5); `electricity_usage_helper.dart @0x292e528`, `@0x2c4f874`, `tou_plan_logic.dart @0x2c493fc` (map `[]=` argument, 5).

## `param_type`/`cmd`

n/a

## Response model (link)

Only the new TOU flow uses a model: [`UtilityRatePlansResponse`](../../models/utility_rate_plans_response.md) (`peak_sessions`, `price_unit`), passed as the closure `UtilityRatePlansResponse.fromJson` to `HttpHelper.request` (`tou_http_service.dart @0x4879170`). The other senders read keys from the raw map (see Response).

## Response

New TOU flow: the answer is parsed by `UtilityRatePlansResponse.fromJson` (model page). The older senders read single keys in their success closures:

| field | type | required | example | source |
|---|---|---|---|---|
| `price_source_type` | not decoded | no | not decoded | `system_policy_logic.dart @0x24a592c`, `smart_mode_logic.dart @0x3eae690`, `ems_ai_mode_condition_logic.dart @0x2a3100c` |
| `price_source_sub_type` | not decoded | no | not decoded | `@0x24a59d0`, `@0x3eae734`, `@0x2a310ac` |
| `fixed_rate` | map | no | not decoded | `@0x24a5738`, `@0x3eae7e0` |
| `peak_valley_prices` | map/list with `buy` and `sell` | no | not decoded | `@0x24a5754`, `@0x3eae7fc`; `buy` `@0x24a57e0`, `sell` `@0x24a5864` (`smart_mode_logic.dart`: `@0x3eae870`, `@0x3eae8c4`) |
| `electricity_strategy_mode` | not decoded | no | not decoded | `system_policy_logic.dart @0x24a5a68` |
| `tou_last_set_type` | not decoded | no | not decoded | `system_policy_logic.dart @0x24a5b8c`; `tou_plan_logic.dart`/`general_price_setting.dart` read the same key from their own closures |

The classes `UtilityRatePlan`, `FixedRate` and `PeakValleyPrices` that describe these keys on the consumer side are in [../../models/hes.md](../../models/hes.md) (legacy page); whether the installer answer has the same layout is not tested.

## Example request/response

Request, synthesized (snake_case sender)

```json
{ "station_id": "<site id>", "not_include_nem": 1, "accuracy": 5 }
```

Response: no captured response; see the model page for the new TOU flow.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

| sender (function `@0xADDR`) | UI page | call `@0xADDR` |
|---|---|---|
| `TouHttpService.getUtilityRatePlans` (`electricity_price/components/tou/impl_v2/service/tou_http_service.dart @0x48790cc`) | new TOU flow (`LargeTouRepository`, call `@0x4878f8c`) | `HttpHelper.request` (field load `@0x48790fc`) |
| `_getLargeUtilityRatePlan` (`ak_soft_ems/ems_list/ems_ai_mode_condition_logic.dart @0x2a30cd4`) | AI mode condition screen | `@0x2a30e14` |
| `_getUtilityRatePlan` (`charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart @0x24a53e8`) | A5101 system policy page | `@0x24a5570` |
| `_getUtilityRatePlan` (`charging/ui/page/device/a5101/setting/smartMode/smart_mode_logic.dart @0x3eae334`) | A5101 smart mode page | `@0x3eae478` |
| `getDataFromAPi` (`electricity_price/components/electricity_price_common/view/tou_plan_logic.dart @0x2c49144`) | TOU plan view | `@0x2c49590` |
| `getCurEmsModeType` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x292e1f4`) | usage policy lookup of the price module | `@0x292e5cc` |
| `getDevicePriceType` (`electricity_price/components/fixed_price/general_electricity_price_settting/general_price_setting.dart @0x29a4974`) | general price setting page | `@0x29a4ce8` |

`assembleRemoteApiParametersWidthGetDetail` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x2c4f694`) builds the same three keys (`@0x2c4f848`, `@0x2c4f86c`, `@0x2c4f894`) for `getManualSetTOUDetailWithUrl`; the request call itself was not traced.

## Since/changed

3.18.0: absent as an installer URL (the 3.18.0 pool holds no `installer_svc` string); the consumer twin `/charging_hes_svc/get_utility_rate_plans` is in the 3.18.0 pool. 3.24.3: present (new). since: 3.24.3. `UtilityRatePlansResponse` is new in 3.24.3.

## Known unknowns

- The meaning of `currency: 5` in `getDevicePriceType` and of `accuracy` is not known.
- Value types of the single-key responses are not decoded; no captured response exists.
- The two key spellings (`not_include_nem` and `notIncludeNem`) may both be accepted by the server or one may be ignored; not tested.

## Device-tested by

none
