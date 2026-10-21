> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# check_function

## Purpose

Queries which station functions are supported (`CheckFunctionModel`) for the NEM check of the home settings (`HomeSettingLogic::_checkNemFunction`) and the system policy page (`SystemPolicyLogic::getLatestSystemFunction`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/check_function` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x28e7f0c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x28e7f04`, in `HttpRequestControllerImpl::checkFunction` (`charging/http/http_request_repository_impl.dart @0x28e7e58`), sent through `requestHttp` (`@0x28e7f34`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::checkFunction` (`charging/http/http_request_repository_impl.dart`, call `@0x28e7f34`, argument list `@0x28e7f2c`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `HttpRequestControllerImpl::checkFunction` (`charging/http/http_request_repository_impl.dart @0x28e7ec0`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes | `"<station_id>"` | `charging/http/http_request_repository_impl.dart @0x28e7eac` |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`CheckFunctionModel`](../../models/hes.md#checkfunctionmodel), parsed by `CheckFunctionModel.fromJson` at `charging/http/http_request_repository_impl.dart @0x28e803c` (success closure `@0x28e8004`, `bl` target `[package:charging/model/a5101/check_function_model.dart]`).

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::CheckFunctionModel`): `auto_disaster` (bool?), `net_energy_meter` (bool?), `peak_shaving` (bool?), `ems_disable` (bool?), `soft2` (List<int>), `smartModeInfo` (unknown), `support` (bool?).

Use of the keys (app side, traced 2026-10-20): the success closure of `SystemPolicyLogic::getLatestSystemFunction` (`charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart @0x28e8760`..`@0x28e8890`) reads the model fields at offsets 0x7 (`auto_disaster`), 0xb (`net_energy_meter`), 0xf (`peak_shaving`), 0x13 (`ems_disable`) and, through `smartModeInfo`, `support` (`@0x28e877c`, `@0x28e87c0`, `@0x28e87f8`, `@0x28e8820`, `@0x28e887c`), writes each into an `Rx` of the page state with `value=` (`@0x28e879c`, `@0x28e87d4`, `@0x28e880c`; `ems_disable` through `_updateDisableEmsState` `@0x28e8840`) and uses `false` for a null (`@0x28e878c`, `@0x28e87d0`, `@0x28e8808`, `@0x28e8830`); the closure of `_checkNemFunction` (`charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart @0x34cd794`..`@0x34cd7f4`) reads the same offsets 0x7 to 0x1b with `false` for null (`@0x34cd7d4`, `@0x34cd808`). Neither closure reads the list `soft2`; the offset-to-key mapping is from the `toJson` of `charging/model/a5101/check_function_model.dart`. `A17E2StationLogic::_checkVppFunction` was not read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure (`charging/http/http_request_repository_impl.dart @0x28e7f50`) logs the code and message (`exeError`) without comparing the code.

## Callers in app

- `base_service/api_url.dart`: `checkFunction` @0x2349c50 (URL literal only, no `*Http*` call; sender `A17E2StationLogic::_checkVppFunction` (`micro_hes/src/a17e2/station/home/a17e2_station_logic.dart @0x2349388`), reached through callers `A17E2StationLogic::_checkVppFunction` (`micro_hes/src/a17e2/station/home/a17e2_station_logic.dart @0x2349388`); other senders: `PowerUsageScenarioController::checkVppFunction`; resolved from the URL literal at `base_service/api_url.dart @0x2349c68` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))
- `charging/http/http_request_repository_impl.dart`: `checkFunction` @0x28e7e58 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::checkFunction`
- `charging/ui/page/device/a5101/setting/homeSetting/home_setting_logic.dart::_checkNemFunction`
- `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart::getLatestSystemFunction`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- How `A17E2StationLogic::_checkVppFunction` (`micro_hes/src/a17e2/station/home/a17e2_station_logic.dart @0x2349388`) uses the keys of `CheckFunctionModel`, and what the page state flags enable on the screens: not read — traced 2026-10-20 (the two A5101 callers are in Response).
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
