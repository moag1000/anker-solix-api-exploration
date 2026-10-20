> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# check

## Purpose

Asks whether features are enabled for a product: `PowerUsageScenarioController::_updateFeatureVisibility` (EMS scenario list; features `AIEMS` and `STORM-GUARD`), `PowerUsageScenarioLogic::getWhiteListStatus`, `UserMainPageLogic::_getWhileList` (refresh) and `HomeSettingLogic::_requestEvChargerWhiteList` call the white-list check.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/whitelist/feature/check` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `PowerUsageScenarioController::checkFeatureVisibility` (`power_usage_scenario_controller.dart @0x3565f9c`): URL string `@0x35662f8`, method object `Method.post` (`pp+0xa7e0`) `@0x35662f0`.
- `HttpRequestControllerImpl::getWhiteListStatusRes` (`http_request_repository_impl.dart @0x26ffad4`): URL string `@0x26ffc3c`, method object `Method.post` (`pp+0xa7e0`) `@0x26ffc34`.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Both senders build a body with one key `check_list`: a list of maps typed `<Map<String, String>>` inside a map typed `<String, List<Map<String, String>>>`, so the elements are Strings.

| field | type | required | example | source |
|---|---|---|---|---|
| `check_list` | list | yes | `[{"feature_code": "AIEMS", "product_code": "<product_code>"}]` | repository sender `getWhiteListStatusRes` (`http_request_repository_impl.dart @0x26ffad4`): key `@0x26ffb30`, value store `@0x26ffbc8`, one-element growable list (`AllocateGrowableArray` `@0x26ffba8`), outer type arguments `@0x26ffbec`; `PowerUsageScenarioController::checkFeatureVisibility` (`power_usage_scenario_controller.dart @0x3565f9c`): key `@0x35660a8`, a list of one map with `"AIEMS"` and a second map with `"STORM-GUARD"` added when a flag is set (`tbnz` `@0x3566174`) |
| `check_list[].feature_code` | string | yes | `"AIEMS"` | repository sender: key `@0x26ffb48`, store `@0x26ffb58` (parameter at `fp-0x18`), map type `<String, String>` `@0x26ffb70`; EMS sender: literals `"AIEMS"` (`@0x35660d0`) and `"STORM-GUARD"` (`@0x3566194`) |
| `check_list[].product_code` | string | yes | `"<product_code>"` | repository sender: key `@0x26ffb5c`, store `@0x26ffb68` (parameter at `fp-0x20`); EMS sender: key `@0x35660dc`, store `@0x35660f4` / `@0x35661b8` from `productCode()` (`@0x35660ec`, `@0x35661b0`) |

## `param_type`/`cmd`

n/a

## Response model (link)

None: no model class is parsed. The repository sender's success closure `http_request_repository_impl.dart @0x26ffd28` reads the keys `check_list` and `enabled` from the response map and hands the result to the callers, which cast `enabled` with `bool()` (`user_main_page_logic.dart @0x26ffe4c`, `power_usage_scenario_logic.dart @0x28a3944`); the EMS sender's closure `power_usage_scenario_controller.dart @0x356653c` reads `check_list`, `feature_code` and `enabled` and compares the feature code with `"AIEMS"`.

## Response

Keys read by the app: `check_list` (list), and per element `feature_code` (String) and `enabled` (cast to bool by the callers).

## Example request/response

Request, synthesized (decrypted body of `getWhiteListStatusRes`)

```json
{"check_list": [{"feature_code": "<feature_code>", "product_code": "<product_code>"}]}
```

Response, synthesized (keys read by the app; values are placeholders, not a capture)

```json
{"code": 0, "msg": "success", "data": {"check_list": [{"feature_code": "AIEMS", "enabled": true}]}}
```

## Errors seen

None traced. The failure callbacks (`http_request_repository_impl.dart @0x26ffc80`, `power_usage_scenario_controller.dart @0x3566484`) log the code and message and call `exeError()`; no code is compared (the 64-bit compares with 16076 in the EMS closure are class-id tests). Error codes are catalogued in `api/errors.md`.

## Callers in app

- `ak_soft_ems/ems_list/power_usage_scenario_controller.dart`: `checkFeatureVisibility` @0x3565f9c (encryptionRequestHttp; encrypted: true)
- `charging/http/http_request_repository_impl.dart`: `getWhiteListStatusRes` @0x26ffad4 (encryptionRequestHttp; encrypted: true)

Called from:

- `ak_soft_ems/ems_list/power_usage_scenario_controller.dart::_updateFeatureVisibility`
- `charging/http/http_request_repository.dart::getWhiteListStatusRes`
- `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart::_requestEvChargerWhiteList`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/power_usage_scenario_logic.dart::getWhiteListStatus`
- `charging/ui/page/user/main/user_main_page_logic.dart::_getWhileList`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- The full set of `feature_code` values the app asks for: the EMS sender uses `AIEMS` and `STORM-GUARD`; the repository sender takes the code from its caller (`APP_DEVICE_EMS_MODEL_SETUP` appears in a callback string, `power_usage_scenario_logic.dart @0x28a3944`).
- What the server returns for a feature it does not know: the callers read only `enabled`.
- Whether `enabled` is a JSON bool or a number: the callers cast it with `bool()`.

## Device-tested by

none
