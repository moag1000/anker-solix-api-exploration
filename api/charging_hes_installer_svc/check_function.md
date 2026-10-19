> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# check_function

## Purpose

Asks the cloud whether the EMS (energy management) function of a system is switched off (`ems_disable`); the app uses the answer to update the VPP (virtual power plant) state of the station home screen.

## Upstream name

`none` (no upstream name). The consumer twin `/charging_hes_svc/check_function` is mentioned in the list of known endpoints in `api/apitypes.py` (line 430), without a key.

## Method+URL

`POST /charging_hes_installer_svc/check_function` (asm-traced). The URL comes from the static getter `Api.checkFunction` (`base_service/api_url.dart @0x2349c50`): installer string `pp+0x23ab0` (`@0x2349c5c`) when `isProApp` is true, otherwise `/charging_hes_svc/check_function` (`pp+0x23ab8`, `@0x2349c68`); see [the variant selector](README.md#variant-selector-installer-app-versus-consumer-app). Two senders use the getter, both with `Method.post` (`pp+0xa7e0`): `PowerUsageScenarioController._checkVppFunction` (`ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x2a273f4`, field load `@0x2a27540`) and `A17E2StationLogic._checkVppFunction` (`micro_hes/src/a17e2/station/home/a17e2_station_logic.dart @0x2349388`, field load `@0x234945c`). A third consumer-only sender, `HttpRequestControllerImpl::checkFunction` (`charging/http/http_request_repository_impl.dart @0x28e7e58`), hard-codes `/charging_hes_svc/check_function` (`@0x28e7f0c`) and is not an installer-URL sender.

## Encrypted?

Yes by wrapper (asm-traced): ``_checkVppFunction`` calls `encryptionRequestHttp` (`power_usage_scenario_controller.dart @0x2a275ac; a17e2_station_logic.dart @0x23494c8`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../encryption.md)); asm alone does not decide it.

## Request

Map literal with one string pair. Both senders skip the call when the site id is empty (`siteId is empty, skip check_function`, `@0x2a27448`, `@0x23493cc`).

| field | type | required | example | source |
|---|---|---|---|---|
| `system_code` | String | yes (installer variant, `isProApp` true) | `"<system code>"` | `power_usage_scenario_controller.dart @0x2a27494`; value is the object field at offset 0x7f (`@0x2a274a4`), its name is not in the asm |
| `station_id` | String | yes (consumer variant) | `"<site id>"` | `power_usage_scenario_controller.dart @0x2a274d4` (value is the field at offset 0x7b, the same field the empty-site-id test reads, `@0x2a27428`, `@0x2a27434`); `a17e2_station_logic.dart @0x23493f8` always sends `station_id`, with no `isProApp` test |

The `isProApp` test in `_checkVppFunction` of the EMS controller is `LoadStaticField(0xad8)` at `@0x2a27478` followed by `tbnz` at `@0x2a27480`.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed; the success closure reads one key from the raw map.

## Response

The success closures check that the payload is a `Map<String, dynamic>` and then read one key.

| field | type | required | example | source |
|---|---|---|---|---|
| `ems_disable` | bool (null counts as `false`) | no | `false` | `power_usage_scenario_controller.dart @0x2a2773c` (success closure `@0x2a2769c`); `a17e2_station_logic.dart @0x23495f0` (success closure `@0x2349560`) |

What the app does with it: the EMS controller stores the value in a controller field (`@0x2a277ec`) and logs `check_function success, ems_disable = ...` (`@0x2a27778`); the A17E2 closure logs the same, creates a `ModeTipLogic` and calls `updateVppStatus` (`@0x234970c`).

## Example request/response

Request, synthesized

```json
{ "station_id": "<site id>" }
```

Response, synthesized

```json
{ "ems_disable": false }
```

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `PowerUsageScenarioController._checkVppFunction` (`ak_soft_ems/ems_list/power_usage_scenario_controller.dart @0x2a273f4`), the power usage scenario (EMS) screen of the `ak_soft_ems` package.
- `A17E2StationLogic._checkVppFunction` (`micro_hes/src/a17e2/station/home/a17e2_station_logic.dart @0x2349388`), the station home of the A17E2 (micro HES) system.

## Since/changed

3.18.0: absent as an installer URL (the 3.18.0 pool holds no `installer_svc` string); the consumer twin `/charging_hes_svc/check_function` is in the 3.18.0 pool. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- Server behaviour and the exact semantics of `ems_disable` are not known (the name suggests that the EMS function of the system is disabled).
- The name behind the object fields at offsets 0x7b and 0x7f is not in the asm; they are named here only from the log text and the `station_id` / `system_code` keys.
- Whether the installer server accepts `station_id` (sent by the A17E2 sender regardless of `isProApp`) is not known.

## Device-tested by

none
