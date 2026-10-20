> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_system_running_info

## Purpose

Reads the system profit and running data of a HES site (`A5101SystemProfitModel`) for the family page (`FamilyMainHttpReposity::getSystemProfit`) and for the device-logs site list (`DeviceLogsLogic::_requestHesSiteInfo`, called from `fetchHesSites`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_system_running_info` (asm-traced): URL string at `charging/ui/page/family/family_main_http_reposity.dart @0x23e3018`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x23e3010`, in `FamilyMainHttpReposity::getSystemProfit` (`charging/ui/page/family/family_main_http_reposity.dart @0x23e2edc`), sent through `requestHttp` (`@0x23e3040`).

Same URL and method object in the other sender(s) read:

- `DeviceLogsLogic::_requestHesSiteInfo` (`charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x2923848`): URL string `@0x292394c`, method object `Method.post` (`pp+0xa7e0`) at `@0x2923944`, sent through `requestHttp` (`@0x2923974`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `FamilyMainHttpReposity::getSystemProfit` (`charging/ui/page/family/family_main_http_reposity.dart`, call `@0x23e3040`, argument list `@0x23e3038`), `DeviceLogsLogic::_requestHesSiteInfo` (`charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart`, call `@0x2923974`, argument list `@0x292396c`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` / `<String, String?>` read at the cited address, so every value is a String: `FamilyMainHttpReposity::getSystemProfit` (`charging/ui/page/family/family_main_http_reposity.dart @0x23e2fcc`, 1 key); `DeviceLogsLogic::_requestHesSiteInfo` (`charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x2923900`, 1 key). No key is behind a null guard. The `String?` value type allows a null value for a key; the key itself is stored unconditionally.

| field | type | required | example | source |
|---|---|---|---|---|
| `siteId` | string | yes | `"<siteId>"` | `charging/ui/page/family/family_main_http_reposity.dart @0x23e2fb8`; `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x29238ec` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::A5101SystemProfitModel`, parsed by `A5101SystemProfitModel.fromJson` at `charging/ui/page/family/family_main_http_reposity.dart @0x23e31f4` (success closure `@0x23e31bc`, `bl` target `[package:charging/model/a5101/a5101_system_profit_model.dart]`).
- Also parsed by `A5101SystemProfitModel.fromJson` at `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart @0x29239c8` (success closure `@0x2923990`, `bl` target `[package:charging/model/a5101/a5101_system_profit_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::A5101SystemProfitModel`): `totalSystemSavings` (num?), `systemSavingsPriceUnit` (String?), `saveCarbonFootprint` (num?), `saveCarbonUnit` (String?), `totalSystemPowerGeneration` (num?), `systemPowerGenerationUnit` (String?), `mainSn` (String?), `mainDeviceModel` (String?), `connected` (bool?), `saveCarbonC` (num?), `catCount` (num?), `rePostTime` (int?), `batCount` (int?), `numberOfParallelDevice` (int?), `supportDiesel` (bool?), `net` (int?), `isAddHeatPump` (bool?), `realNet` (int?), `systemCode` (String?), `enwgs` (int?), `emsDisable` (bool?), `hasEvCharger` (bool?), `evChargerInfos` (List), `countryCode` (String?), `mode` (int?), `hasSwitch` (bool?).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "siteId": "<siteId>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/family/family_main_http_reposity.dart`: `getSystemProfit` @0x23e2edc (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart`: `_requestHesSiteInfo` @0x2923848 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/user/upload_log/device_logs/device_logs_logic.dart::fetchHesSites`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the family page does with the model: only the parse was read.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
