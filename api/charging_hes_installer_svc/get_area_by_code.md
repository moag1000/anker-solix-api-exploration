> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_area_by_code

## Purpose

Looks up the price area (Octopus group id) that belongs to an area code of a site; the dynamic-price provider page uses it to find the matching Octopus region.

## Upstream name

`none` for the installer URL (no upstream name). The consumer twin `/charging_hes_dynamic_price_svc/get_area_by_code` is listed without a key in `api/apitypes.py` (line 476, comment "needs owner").

## Method+URL

`POST /charging_hes_installer_svc/get_area_by_code` (asm-traced). The URL comes from the static getter `Api.getAreaByCode` (`base_service/api_url.dart @0x41e4a70`): installer string `pp+0x8e9b0` (`@0x41e4a7c`) when `isProApp` is true, otherwise `/charging_hes_dynamic_price_svc/get_area_by_code` (`pp+0x8e9b8`, `@0x41e4a88`; see [the variant selector](README.md#variant-selector-installer-app-versus-consumer-app)). The only sender, `ElectricityPriceProviderLogic.fetchAreaByCode` (`electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x41e44e4`), loads the field at `@0x41e4728` and passes `Method.post` (pool entry `pp+0xa7e0`).

## Encrypted?

Yes by wrapper (asm-traced): ``fetchAreaByCode`` calls `encryptionRequestHttp` (`electricity_price_provider_logic.dart @0x41e47a8`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../encryption.md)); asm alone does not decide it.

## Request

Map literal with one pair plus one more key that depends on the context (`code`, then `sn` or `siteId`, set with `[]=`).

| field | type | required | example | source |
|---|---|---|---|---|
| `code` | String | yes | `"<area code>"` | `electricity_price_provider_logic.dart @0x41e45c0`; the value is a function argument |
| `sn` | String | one of `sn` / `siteId` | `"<device sn>"` | `@0x41e463c`; set when the device scope applies |
| `siteId` | String | one of `sn` / `siteId` | `"<site id>"` | `@0x41e4670`; set otherwise |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the success closure reads one key from the raw map. The class `DynamicPriceCountryAreaModel` with `AreaInfo` (`area`, `area_name`; [../../models/pricing.md](../../models/pricing.md)) belongs to another page of the consumer app and is not called here.

## Response

The success closure `@0x41e4830` reads one key and filters its provider list with it.

| field | type | required | example | source |
|---|---|---|---|---|
| `groupId` | String | no | `"<group id>"` | `electricity_price_provider_logic.dart @0x41e4874`; read through a pool helper; if it is not the empty string (`@0x41e48d8`) the closure picks the first `OctopusArea` of the page's provider list (`firstWhereOrNull<OctopusArea>`, `@0x41e492c`; `OctopusArea` has `regionName` and `groupId`, [../../models/dynamic_price_company_model.md](../../models/dynamic_price_company_model.md)) and completes the pending future with a filtered list (`where`, `@0x41e4974`, `complete` `@0x41e49a4`) |

## Example request/response

Request, synthesized

```json
{ "code": "<area code>", "siteId": "<site id>" }
```

Response, synthesized

```json
{ "groupId": "<group id>" }
```

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../errors.md).

## Callers in app

- `ElectricityPriceProviderLogic.fetchAreaByCode` (`electricity_price/components/dynamic_price/setting/electricity_price_provider_logic.dart @0x41e44e4`), the provider selection page of the dynamic price setup (package `electricity_price`). The call site of `fetchAreaByCode` was not traced.

## Since/changed

3.18.0: absent as an installer URL (the 3.18.0 pool holds no `installer_svc` string); the consumer twin `/charging_hes_dynamic_price_svc/get_area_by_code` is in the 3.18.0 pool. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- The response may carry more keys than `groupId`; only that key is read.
- What `code` is (postcode, country code, grid area code) is not known; the example is a placeholder.
- Server behaviour is not known.

## Device-tested by

none
