> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# adjust_station_price_unit

## Purpose

Tells the cloud to change the price unit (currency) of a station's electricity prices; the app sends the station id and the new unit and reads nothing from the answer.

## Upstream name

`none` (no upstream name). The consumer twin `/charging_hes_svc/adjust_station_price_unit` is mentioned in the list of known endpoints in `api/apitypes.py` (line 426), without a key.

## Method+URL

`POST /charging_hes_installer_svc/adjust_station_price_unit` (asm-traced). The URL comes from the static getter `Api.adjustStationPriceUnit` (`base_service/api_url.dart @0x29ae7dc`): the installer string `pp+0x71ae8` (`@0x29ae7e8`) when `isProApp` is true, otherwise the consumer twin `/charging_hes_svc/adjust_station_price_unit` (`pp+0x71af0`, `@0x29ae7f4`); see [the variant selector](README.md#variant-selector-installer-app-versus-consumer-app). The sender `changeCurrencyUnit` (`electricity_price/components/electricity_price_common/electricity_usage_helper.dart @0x29ae5f0`) loads the field at `@0x29ae69c` (`InitLateStaticField` `@0x29ae6b8`) and passes the method object `Method.post` (pool entry `pp+0xa7e0`, `@0x29ae794`).

## Encrypted?

Yes by wrapper (asm-traced): `HttpService.encryptionRequestHttp` calls `encryptionRequestHttp` (`electricity_usage_helper.dart @0x29ae7c0`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../encryption.md)); asm alone does not decide it.

## Request

Map literal of two string pairs (`r2 = 8`, i.e. 4 slots, `@0x29ae6f0`; both keys are chosen by the same `isProApp` test, `LoadStaticField(0xad8)` at `@0x29ae6c0`). The installer variant uses camelCase for the unit key, the consumer variant snake_case.

| field | type | required | example | source |
|---|---|---|---|---|
| `system_code` (installer) or `station_id` (consumer) | String | yes | `"<site or system id>"` | `electricity_usage_helper.dart @0x29ae6d0` (`system_code`), `@0x29ae6dc` (`station_id`); the value is an argument of `changeCurrencyUnit`, stored at `@0x29ae700`; the argument source is not traced |
| `priceUnit` (installer) or `price_unit` (consumer) | String | yes | `"EUR"` | `@0x29ae714` (`priceUnit`), `@0x29ae720` (`price_unit`); value is the second argument, stored at `@0x29ae734`; the example value is an assumption, the unit codes used by the app come from [get_world_monetary_unit](get_world_monetary_unit.md) |

The call also takes a boolean argument (null becomes `false`, `@0x29ae75c`) that is passed on as `showLoading` (`stp` at `@0x29ae7a4`).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed.

## Response

No response field is read (asm-traced). The success closure `@0x261b9a0` (a shared closure defined in `HttpRequestControllerImpl`, `charging/http/http_request_repository_impl.dart`) only calls the caller's completion callback; the failure closure (`electricity_usage_helper.dart @0x29ae55c`) calls the failure callback and logs `getSupportOption fail` (`@0x29ae5b0`), a log text copied from another function.

## Example request/response

Request, synthesized

```json
{ "system_code": "<system id>", "priceUnit": "EUR" }
```

Response: no captured response; the app ignores the payload.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../errors.md).

## Callers in app

- `changeCurrencyUnit` (`electricity_usage_helper.dart @0x29ae5f0`), package `electricity_price`, the price-unit selection of the electricity price settings. The page that calls `changeCurrencyUnit` was not traced.

## Since/changed

3.18.0: absent as an installer URL (the 3.18.0 pool holds no `installer_svc` string); the consumer twin `/charging_hes_svc/adjust_station_price_unit` is in the 3.18.0 pool. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- Server behaviour (which units are accepted, whether the unit applies to all price plans of the station) is not known.
- Whether the installer variant is accepted by the consumer server and the reverse is not tested.
- The caller of `changeCurrencyUnit` and the source of both arguments are not traced.

## Device-tested by

none
