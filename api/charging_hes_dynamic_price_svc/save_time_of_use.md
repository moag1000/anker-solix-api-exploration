> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# save_time_of_use

## Purpose

Switches a site to automatic time-of-use pricing (callers `ElectricityPriceModeApiHelper::changeToTouMode`, `ElectricityPricePlanApiHelper::changeToTouPlan`, `TOUAutoPricePkgResultLogic::saveAuto`) (string-only: inferred from the function names; one sender is read).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_dynamic_price_svc/save_time_of_use` (asm-traced for the sender read): `ElectricityPriceModeApiHelper::changeToTouMode` (`electricity_price/components/electricity_price_common/electricity_price_model_api_helper.dart @0x2e821dc`) loads the URL from the static field `saveAutoTou` (`LoadStaticField(0xaf0)` `@0x2e82388`, initializer `Api.saveAutoTou`) and calls `HttpHelper::getDataFromService` (`@0x2e823ec`), which sends with `Method.post` (pool entry `pp+0xa7e0`, `electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdb94`) through `encryptionRequestHttp` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdbc8`).

The URL is chosen at run time by `Api.saveAutoTou` (`base_service/api_url.dart @0x2e82408`): it loads the static flag at field offset `0xad8` (`@0x2e82408`, `tbnz` on the Dart false bit) and returns `/charging_hes_dynamic_price_svc/save_time_of_use` when the flag is false (`@0x2e82420`) and `/charging_hes_installer_svc/save_time_of_use` when it is true (`@0x2e82414`). The result is cached in the late static field at offset `0xaf0`, which the senders read.

Two further places load the static field: `electricity_price/components/electricity_price_common/electricity_price_plan_api_helper.dart @0x31aa188` and `electricity_price/components/electricity_price_common/tou_auto_preview/tou_auto_price_pkg_result_logic.dart @0x31b1214`; they were not read.

## Encrypted?

encrypted: `true` (asm-traced: the sender read reaches `encryptionRequestHttp`, `electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bdbc8`). Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: two field types are not read) One sender read. Its map literal has the type arguments `<String, dynamic>` (`electricity_price/components/electricity_price_common/electricity_price_model_api_helper.dart @0x2e822f8`), which name no value type; `setMode` and `touType` are typed from their stores.

| field | type | required | example | source |
|---|---|---|---|---|
| `setMode` | bool | yes | `true` | `electricity_price/components/electricity_price_common/electricity_price_model_api_helper.dart @0x2e8227c` (constant `r16 = true` `@0x2e82288`, store `@0x2e8228c`) |
| `touType` | int (unboxed, x) | yes | `<tou_type>` | `electricity_price/components/electricity_price_common/electricity_price_model_api_helper.dart @0x2e82290` (a call result `@0x2e822ac` boxed by `BoxInt64Instr` `@0x2e822bc`) |
| `sn` | ? | optional | `"<sn>"` | `electricity_price/components/electricity_price_common/electricity_price_model_api_helper.dart @0x2e82348` (guard: a call result tested `tbnz` `@0x2e82328`, length test `cbz` `@0x2e82334`; store call `@0x2e82350`) |
| `siteId` | ? | optional | `"<site_id>"` | `electricity_price/components/electricity_price_common/electricity_price_model_api_helper.dart @0x2e82374` (same guard; store call `@0x2e8237c`) |

## `param_type`/`cmd`

n/a

## Response model (link)

(string-only) not parsed in the sender read: the closures passed to `getDataFromService` were not read.

## Response

(string-only) The answer shape was not read.

Callbacks (traced 2026-10-20, app side): the sender passes the shared success forwarder `charging/http/http_request_repository_impl.dart @0x2268374` (it calls the stored callback with the answer unchanged) and a failure closure (shared code, `charging/ui/widget/anker_widget_impl.dart @0x227d9ac`); no key of the answer is read in this helper.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "setMode": true,
  "touType": "<int>",
  "sn": "<sn>",
  "siteId": "<site_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender read. Code meanings are owned by `api/errors.md`.

## Callers in app

- `base_service/api_url.dart`: `saveAutoTou` @0x2e82408 (URL literal only, no `*Http*` call; sender `HttpHelper::getDataFromService` (`electricity_price/components/electricity_price_common/http/http_helper.dart @0x27bda38`) (HTTP helper wrapper), called from `ElectricityPriceModeApiHelper::changeToTouMode` (`electricity_price/components/electricity_price_common/electricity_price_model_api_helper.dart @0x2e821dc`); also through `ElectricityPricePlanApiHelper::changeToTouPlan`, `TOUAutoPricePkgResultLogic::saveAuto`; resolved from the URL literal at `base_service/api_url.dart @0x2e82420` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. Params changed: removed `setMode`, `touType` (`tools/out/diff_3.18.0_3.24.3.md`, string-level diff on the URL builder `Api.saveAutoTou`). In 3.24.3 the sender read builds both keys itself (`electricity_price/components/electricity_price_common/electricity_price_model_api_helper.dart @0x2e8227c`, `@0x2e82290`), so neither key is absent.

## Known unknowns

- Types of `sn` and `siteId`: the literal names no value type. — attempted 2026-10-20 (two-hop not readable: both come from parameters of `ElectricityPriceModeApiHelper::changeToTouMode` (`electricity_price/components/electricity_price_common/electricity_price_model_api_helper.dart @0x2e821dc`, `SetupParameters` `@0x2e821e8`) and are tested with a length load (`field_7` `@0x2e82330`), which is not a type proof)
- Which values `touType` takes: the value is the result of a call (`electricity_price/components/electricity_price_common/electricity_price_model_api_helper.dart @0x2e822ac`, selector not named by Blutter) boxed as an unboxed integer; the enum behind it was not decoded. — traced 2026-10-20: the value is the result of an argument-less selector on a parameter of `changeToTouMode` (`GDT[cid_x0 + -0x65c]` `@0x2e822ac`), boxed from an unboxed integer, which fits the `index` getter of an enum; the enum with the matching name is `TouMode` with `none` 0, `manual` 1 and `auto` 2 (`objs.txt Obj!TouMode@4208b11`, `@4208b31`, `@4208b51`), but the parameter is not declared with that type in the dump, so the mapping is a reading by name; the auto-TOU page sends the literal 52 (see [the installer variant](../charging_hes_installer_svc/save_time_of_use.md))
- Which of the two other senders send other keys. — traced 2026-10-20: `ElectricityPricePlanApiHelper::changeToTouPlan` and `TOUAutoPricePkgResultLogic::saveAuto` (listed under Callers in app) were not compared with this sender
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
