> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_third_jump_url

## Purpose

Asks for the URL of a third-party provider page (Flatpeak) to which the app jumps to link a tariff for a site (callers `ElectricityPlaceConfirmPageLogic::getDynamicPriceCompany`, `_DynamicPriceHttpServer::getThirdJumpUrl`) (string-only: inferred from the function names and the constant company name).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_dynamic_price_svc/get_third_jump_url` (asm-traced for the sender read): `ElectricityPlaceConfirmPageLogic::getDynamicPriceCompany` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac204`) loads the URL from the static field `getThirdJumpUrl` (`LoadStaticField(0xae8)` `@0x29ac3c0`, initializer `Api.getThirdJumpUrl`) and calls `HttpHelper::getDataFromService` (`@0x29ac420`), which sends with `Method.post` (pool entry `pp+0xa7e0`, `electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdb94`) through `encryptionRequestHttp` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdbc8`).

The URL is chosen at run time by `Api.getThirdJumpUrl` (`base_service/api_url.dart @0x29acc3c`): it loads the static flag at field offset `0xad8` (`@0x29acc3c`, `tbnz` on the Dart false bit) and returns `/charging_hes_dynamic_price_svc/get_third_jump_url` when the flag is false (`@0x29acc54`) and `/charging_hes_installer_svc/get_third_jump_url` when it is true (`@0x29acc48`). The result is cached in the late static field at offset `0xae8`, which the senders read.

A second place loads the static field: `electricity_price/components/dynamic_price/general_kit/http_server/dynamic_price_http_server.dart @0x43918c0` (`_DynamicPriceHttpServer::getThirdJumpUrl`); it was not read.

## Encrypted?

encrypted: `true` (asm-traced: the sender read reaches `encryptionRequestHttp`, `electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdbc8`). Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: two field types are not read) One sender read. Its map literal has the type arguments `<String, dynamic>` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac278`), which name no value type; the string constants are typed from their loads.

| field | type | required | example | source |
|---|---|---|---|---|
| `pn` | string | yes | `"<pn>"` | `electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac254` (value `LoadField` `@0x29ac26c`, store `@0x29ac274`) |
| `sn` | string | optional | `"<sn>"` | `electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac2e4` (guard: a call result tested `tbnz` `@0x29ac2bc`, length test `cbz` `@0x29ac2d0`; store call `@0x29ac2ec`) |
| `siteId` | string | yes | `"<site_id>"` | `electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac318` (value `LoadField` `@0x29ac304`, store call `@0x29ac320`) |
| `companyName` | string | yes | `"Flatpeak"` | `electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac340` (constant `@0x29ac348`) |
| `type` | string | yes | `"IMPORT"` or `"EXPORT"` | `electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac37c` (constant `"IMPORT"` `@0x29ac380`); a second store of the same key with `"EXPORT"` (`@0x29ac3a8`, `@0x29ac3ac`) |

Types and branch (traced 2026-10-20, app side): in `electricty_place_confirm_logic.dart` `siteId` is the String field at `field_7b` (cast `@0x34f4438`..`@0x34f4440`, store `@0x34f444c`), `pn` is `field_13` of the `PN` enum member held in `field_9f` (cast `@0x34f4588`, store `@0x34f4594`, load `@0x29ac26c`; enum texts on [get_price_company](get_price_company.md#request)), and `sn` is a text from `field_53.field_7` sent only when `field_d3` is non-null and non-empty (`@0x29ac290`..`@0x29ac2cc`). The two stores of `type` are the two arms of one branch: when the integer parameter in the context equals 1 (`cmp w0, #2` on the tagged value, `@0x29ac364`) the sender stores `"IMPORT"` (`@0x29ac380`), otherwise `"EXPORT"` (`@0x29ac39c` branch). The second sender `_DynamicPriceHttpServer::getThirdJumpUrl` (`electricity_price/components/dynamic_price/general_kit/http_server/dynamic_price_http_server.dart @0x43917b8`) stores the constants `companyName` `"Tibber"` (`@0x439181c`) and `type` `"IMPORT"` (`@0x4391830`) next to `siteId` and `sn`.

## `param_type`/`cmd`

n/a

## Response model (link)

(string-only) not parsed in the sender read: the closures passed to `getDataFromService` were not read.

## Response

(string-only) The answer shape was not read; the function name says the answer holds a URL.

What the callback reads (traced 2026-10-20, app side): the success closure of `ElectricityPlaceConfirmPageLogic::getDynamicPriceCompany` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac478`) logs `getThirdJumpUrl:` with the type (`@0x29ac4ac`, `@0x29ac4c0`), compares the type with 1 (`cmp w1, #2`, tagged, `@0x29ac4f4`) and reads `flatpeakWaitTime` (cast `int`, `@0x29ac50c`..`@0x29ac580`), `aggregationFrequency` (cast `int`, `@0x29ac5b0`..`@0x29ac624`) and `jumpUrl` (cast `String`, `@0x29ac698`..`@0x29ac708`); it stores the frequency under the key `buyAggregationFrequency` in the import branch (`@0x29ac680`) and `saleAggregationFrequency` in the other (`@0x29ac9bc`), and builds the address to open from `jumpUrl` + `&lang=` + the app language (`@0x29ac744`) + `&selectAddress=` (`@0x29ac7d4`). The model keys `jumpUrl`, `flatpeakWaitTime` and `aggregationFrequency` are on [dynamic_price_server_model](../../models/dynamic_price_server_model.md). The failure closure (`@0x29ac43c`) logs `getThirdJumpUrl:fail` (`@0x29ac450`).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "pn": "<pn>",
  "sn": "<sn>",
  "siteId": "<site_id>",
  "companyName": "Flatpeak",
  "type": "IMPORT"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender read. Code meanings are owned by `api/errors.md`.

## Callers in app

- `base_service/api_url.dart`: `getThirdJumpUrl` @0x29acc3c (URL literal only, no `*Http*` call; sender `HttpHelper::getDataFromService` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bda38`) (HTTP helper wrapper), called from `ElectricityPlaceConfirmPageLogic::getDynamicPriceCompany` (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac204`); also through `_DynamicPriceHttpServer::getThirdJumpUrl`; resolved from the URL literal at `base_service/api_url.dart @0x29acc54` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. Params changed: removed `companyName`, `pn`, `siteId`, `sn`, `type` (`tools/out/diff_3.18.0_3.24.3.md`, string-level diff on the URL builder `Api.getThirdJumpUrl`). In 3.24.3 the sender read builds all five keys itself (`electricity_price/components/dynamic_price/setting/electricty_place_confirm_logic.dart @0x29ac254`..`@0x29ac37c`), so no key is absent.

## Known unknowns

- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
