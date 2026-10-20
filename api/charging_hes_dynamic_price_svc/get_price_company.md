> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_price_company

## Purpose

Lists the dynamic-price providers (companies) available for a site (callers `ChargeDischargeSettingLogic::getDynamicPriceCompany`, `ChargeDischargeSettingLogic_C5::getDynamicPriceCompany`, `DynamicPriceDetailInfoViewState::getDynamicPriceCompany`, `ElectricityCompanySelectLogic::getDynamicPriceCompany`, `ElectricityPriceProviderLogic::getDynamicPriceCompany`, `ElectricityPriceServiceImpl::_supportAutoTou`, `PowerUsageScenarioController::_requestDynamicPriceCompany`, `PowerUsageScenarioLogic::_requestDynamicPriceCompany`, `SystemPolicyLogic::_getDynamicPriceCompany`) (string-only: inferred from the function names; one sender is read).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_dynamic_price_svc/get_price_company` (asm-traced for the sender read): `ChargeDischargeSettingLogic::getDynamicPriceCompany` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b6424`) loads the URL from the static field `getPriceCompany` (`LoadStaticField(0xae0)` `@0x29b64b8`, initializer `Api.getPriceCompany`) and calls `HttpHelper::getDataFromService` (`@0x29b651c`), which sends with `Method.post` (pool entry `pp+0xa7e0`, `electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdb94`) through `encryptionRequestHttp` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdbc8`).

The URL is chosen at run time by `Api.getPriceCompany` (`base_service/api_url.dart @0x27bde38`): it loads the static flag at field offset `0xad8` (`@0x27bde38`, `tbnz` on the Dart false bit) and returns `/charging_hes_dynamic_price_svc/get_price_company` when the flag is false (`@0x27bde50`) and `/charging_hes_installer_svc/get_price_company` when it is true (`@0x27bde44`). The result is cached in the late static field at offset `0xae0`, which the senders read.

Fourteen further places load the static field `getPriceCompany` (for example `electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x29a791c`, `electricity_price/components/electricity_module/electricity_price_serviceImpl.dart @0x2891d18`, `ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x2a2f010`); those senders were not read.

## Encrypted?

encrypted: `true` (asm-traced: the sender read reaches `encryptionRequestHttp`, `electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdbc8`). Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: both field types are not read) One sender read. Its map literal has the type arguments `<String, dynamic>` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b64a8`), which name no value type; both keys are stored in the literal without a guard (array length raw 8 at `@0x29b645c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | ? | yes | `"<site_id>"` | `electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b6464` (value from a field of the logic object, `ldr w2` `@0x29b6478`, store `@0x29b6480`) |
| `pn` | ? | yes | `"<pn>"` | `electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b6484` (value `LoadField` `@0x29b649c`, store `@0x29b64a4`) |

## `param_type`/`cmd`

n/a

## Response model (link)

(string-only) not parsed in the sender read: the closures passed to `getDataFromService` were not read.

## Response

(string-only) The answer shape was not read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "siteId": "<site_id>",
  "pn": "<pn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender read. Code meanings are owned by `api/errors.md`.

## Callers in app

- `base_service/api_url.dart`: `getPriceCompany` @0x27bde38 (URL literal only, no `*Http*` call; sender `HttpHelper::getDataFromService` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bda38`) (HTTP helper wrapper), called from `ChargeDischargeSettingLogic::getDynamicPriceCompany` (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b6424`); also through `ChargeDischargeSettingLogic_C5::getDynamicPriceCompany`, `DynamicPriceDetailInfoViewState::getDynamicPriceCompany`, `ElectricityCompanySelectLogic::getDynamicPriceCompany`, `ElectricityPriceProviderLogic::getDynamicPriceCompany`, `ElectricityPriceServiceImpl::_supportAutoTou`; other senders: `PowerUsageScenarioController::_requestDynamicPriceCompany`, `PowerUsageScenarioController::getDynamicPriceCompany`, `PowerUsageScenarioLogic::_requestDynamicPriceCompany`, `SystemPolicyLogic::_getDynamicPriceCompany`; resolved from the URL literal at `base_service/api_url.dart @0x27bde50` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. Params changed: removed `pn`, `siteId`, `type` (`tools/out/diff_3.18.0_3.24.3.md`, string-level diff on the URL builder `Api.getPriceCompany`). In 3.24.3 the sender read still builds `siteId` and `pn` itself (`electricity_price/components/timeslot/page/charge_discharge_setting/charge_discharge_setting_logic.dart @0x29b6464`, `@0x29b6484`); `type` was not found in that sender.

## Known unknowns

- Types of `siteId` and `pn` (product name): the literal names no value type.
- Whether the other thirteen senders send `type` or other keys: only one sender was read.
- The response keys and how the provider list is parsed.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
