> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_aiems_profit

## Purpose

Reads the AI-EMS profit of a site for the large-charger smart-mode card (`getAiModeStatus` in `charging/ui/page/device/a5101/setting/smartMode/smart_mode_card_logic.dart`, through `HttpRequestControllerImpl::queryLargeChargerAiEmsProfit`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_aiems_profit` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x23e3b64`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x23e3b5c`, in `HttpRequestControllerImpl::queryLargeChargerAiEmsProfit` (`charging/http/http_request_repository_impl.dart @0x23e3ab4`), sent through `encryptionRequestHttp` (`@0x23e3b8c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- `encryptionRequestHttp` forwards `needEncryption` with its default true to `requestHttp` (`api/encryption.md`): `HttpRequestControllerImpl::queryLargeChargerAiEmsProfit` (`charging/http/http_request_repository_impl.dart`, call `@0x23e3b8c`).

## Request

`HttpRequestControllerImpl::queryLargeChargerAiEmsProfit` (`charging/http/http_request_repository_impl.dart @0x23e3ab4`) stores one key in a map literal with type arguments `<String, dynamic>` (`@0x23e3b1c`), which do not type the value; the value is the parameter (`@0x23e3b18`). The key is stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x23e3b08` |

Value source of `siteId` (app side, traced 2026-10-20): the only listed caller `SmartModeCardLogic::getAiModeStatus` (`charging/ui/page/device/a5101/setting/smartMode/smart_mode_card_logic.dart @0x23e397c`) passes its own parameter, which it also stores in `field_8f` (`@0x23e392c`); `getAiModeStatus` has five callers outside this page (`charging/ui/page/family/family_main_page_logic.dart @0x23e366c`, `charging/ui/page/device/a17c5/ai_mode_success/ai_mode_success_logic.dart @0x28d5d08`, `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x262c920`, `@0x262e390`, `@0x262ef48`), each passing a value read from an `Rx` or a model field. The getter `SmartModeCardLogic::siteId` (`@0x23e39e0`, declared `String`) returns `field_7` of the value of the `Rx` at offset 451 of `getA5101StationController()` (`@0x23e3a0c`..`@0x23e3a30`), the empty string when null; this is the same offset and field that `FamilyMainPageLogic::_changeDevice` passes as `stationId` to `A5101MqttLogic` (`charging/ui/page/family/family_main_page_logic.dart @0x479d0f4`..`@0x479d110`), so the camel-case `siteId` key carries the same kind of value as `stationId`/`station_id` on the sibling endpoints of the service as far as the app code shows; the server side is not known.

## `param_type`/`cmd`

n/a

## Response model (link)

- [`LargeChargerAiEmsProfit`](../../models/energy.md#largechargeraiemsprofit), parsed by `LargeChargerAiEmsProfit.fromJson` at `charging/http/http_request_repository_impl.dart @0x23e3be0` (success closure `@0x23e3ba8`, `bl` target `[package:charging/model/green_energy/station/large_charger_aiems_profit.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::LargeChargerAiEmsProfit`): `aiemsIncome` (unknown), `aiemsIncreasesIncome` (unknown), `priceUnit` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "siteId": "<siteId>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure is the folded forwarder `charging/http/http_request_repository_impl.dart @0x2375ad8`, which passes the code and the message to the stored callback (`ClosureCall` `@0x2375b14`).

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `queryLargeChargerAiEmsProfit` @0x23e3ab4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::queryLargeChargerAiEmsProfit`
- `charging/ui/page/device/a5101/setting/smartMode/smart_mode_card_logic.dart::getAiModeStatus`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The type of `siteId`: the parameter is stored without conversion (`charging/http/http_request_repository_impl.dart @0x23e3b18`) into a `<String, dynamic>` map. — attempted 2026-10-20 (two-hop not readable: the five callers of `getAiModeStatus` pass values read from `Rx` or model fields, `family_main_page_logic.dart @0x23e366c`, `ai_mode_success_logic.dart @0x28d5d08`, `a17c1home_logic.dart @0x262c920`, `@0x262e390`, `@0x262ef48`; the declared `String` of the `siteId` getter is not the value that reaches the sender)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
