> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_world_monetary_unit

## Purpose

Reads the list of currencies (price units) that a site may use for its electricity prices; the app sends the site id and empty country and area filters.

## Upstream name

`none` for the installer URL (no upstream name). The consumer twin `/charging_hes_svc/get_world_monetary_unit` is the upstream key `get_monetary_units` of `API_HES_SVC_ENDPOINTS` (`api/apitypes.py` line 228; upstream-confirmed, `export.py` sends `{"siteId": siteId}`).

## Method+URL

`POST /charging_hes_installer_svc/get_world_monetary_unit` (asm-traced). The URL comes from the static getter `Api.getPriceUnitsConfig` (`base_service/api_url.dart @0x29ae8dc`): installer string `pp+0x7ca90` (`@0x29ae8e8`) when `isProApp` is true, otherwise `/charging_hes_svc/get_world_monetary_unit` (`pp+0x7ca98`, `@0x29ae8f4`); see [the variant selector](README.md#variant-selector-installer-app-versus-consumer-app). The sender `getPriceUnits` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x29ae3f4`) loads the field at `@0x29ae464` and passes `Method.post` (pool entry `pp+0xa7e0`, `@0x29ae514`).

## Encrypted?

Yes by wrapper (asm-traced): ``getPriceUnits`` calls `encryptionRequestHttp` (`electricity_usage_helper.dart @0x29ae540`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../encryption.md)); asm alone does not decide it. The loading overlay is on (`showLoading: true`, `@0x29ae528`).

## Request

Map literal of three string pairs, `<String, String>` (`r2 = 12`, `@0x29ae488`). No `isProApp` branch.

| field | type | required | example | source |
|---|---|---|---|---|
| `countryCodes` | String | yes | `""` | `electricity_usage_helper.dart @0x29ae494`; the value is the empty string literal (`@0x29ae4a0`) |
| `areaCodes` | String | yes | `""` | `@0x29ae4a8`; the value is the empty string literal (`@0x29ae4b4`) |
| `siteId` | String | yes | `"<site id>"` | `@0x29ae4bc`; the value is the function argument stored at `@0x29ae4cc` |

Upstream sends only `siteId` to the consumer twin (upstream-confirmed, `export.py` line 1488); whether the empty filters change the answer is not known.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed by the sender; the answer elements are passed on as a raw list. The model classes `CurrencyInfo` (see [../../models/pricing.md](../../models/pricing.md)), `CurrencyList` and `DefaultCurrency` (`base_service/bean/currency_info_model.dart`, `fromJson` `@0x29ad6e0`, `@0x289c8d8`, `@0x29ada28`) describe a currency list with `name` and `symbol` keys, but this sender does not call them.

## Response

The success closure `@0x29ae800` checks that the payload is a `Map<String, dynamic>`, reads one key and hands the list to the caller.

| field | type | required | example | source |
|---|---|---|---|---|
| `priceUnits` | list (element type not resolved) | no | `[ ... ]` | `electricity_usage_helper.dart @0x29ae850`; the list is cast with `List` (`@0x29ae890`) and passed to the caller's callback (`ClosureCall` `@0x29ae8b8`) |

## Example request/response

Request, synthesized

```json
{ "countryCodes": "", "areaCodes": "", "siteId": "<site id>" }
```

Response: no captured response; the element layout of `priceUnits` is not traced.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `getPriceUnits` (`electricity_usage_helper.dart @0x29ae3f4`), package `electricity_price`, the currency selection of the electricity price settings. The page that calls `getPriceUnits` was not traced.

## Since/changed

3.18.0: absent as an installer URL (the 3.18.0 pool holds no `installer_svc` string); the consumer twin `/charging_hes_svc/get_world_monetary_unit` is in the 3.18.0 pool. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- The element layout of `priceUnits` (probably `name` and `symbol` as in `CurrencyList`) is not traced.
- Whether empty `countryCodes` and `areaCodes` mean "all" is not known.
- Server behaviour and the difference between the installer and the consumer answer are not known.

## Device-tested by

none
