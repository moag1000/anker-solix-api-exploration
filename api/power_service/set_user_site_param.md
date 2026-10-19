> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# set_user_site_param

## Purpose

Sets user-level site parameters in the cloud; the only traced wrapper takes the parameter map from its caller and has no caller in the asm, so what it carries is not known.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`). The matching reader is `/site/v1/get_user_site_param` (not described here).

## Method+URL

`POST /power_service/v1/set_user_site_param` (asm-traced): URL literal `@0x2886e20` in `HttpRequestControllerImpl.setUserParams` (`charging/http/http_request_repository_impl.dart @0x2886da0`), method object `Method.post` (pool entry `pp+0xa7e0`, `@0x2886e18`). Do not confuse it with the EV charger command `AKIotEVChargeCommand.setUserParams` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x405be14`), which sends `power_service/v1/app/user/set_user_params` through the SDK.

## Encrypted?

Yes by wrapper (asm-traced): ``setUserParams`` calls `encryptionRequestHttp` (`charging/http/http_request_repository_impl.dart @0x2886e48`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../encryption.md)); asm alone does not decide it. The loading overlay is off (`r30 = false`, `@0x2886e38`).

## Request

The body is the argument that `setUserParams` receives in register `r3` (stored at `@0x2886db4`, pushed for the call at `@0x2886e2c`); the other two arguments (`r2`, `r6`) become the callback closures. The function builds no keys itself. No direct call site of `HttpRequestControllerImpl::setUserParams` appears in the Blutter dump, but the dump omits mixin-deduplicated code, where the forwarder `AE100ApiExt.setUserParamsAsync` lives. UNCONFIRMED candidate (mixin dump incomplete): callers of that forwarder exist in `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/ae100/custom_mode_usage_scenario_logic.dart` (`@0x2886c44`, `@0x28874a8`, `@0x28876bc`) and pass a body of the shape `{site_id, user_params: [{param_type, param_value}]}`, with `param_type` raw `80002` (Smi, so 40001) and `param_value` the string `"2"`. That the forwarder reaches this wrapper and URL is not proven.

| field | type | required | example | source |
|---|---|---|---|---|
| (caller-supplied map) | map | yes | candidate (unconfirmed): `{"site_id": ..., "user_params": [{"param_type": 40001, "param_value": "2"}]}` | `charging/http/http_request_repository_impl.dart @0x2886da0`; candidate shape from `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/ae100/custom_mode_usage_scenario_logic.dart @0x2886c44`, `@0x28874a8`, `@0x28876bc` via the unseen mixin forwarder |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed; the success and failure closures are shared static closures (`@0x2268374`, `@0x226824c`).

## Response

No response field is read (asm-traced). The two callbacks are shared closures that forward to the caller's callbacks; their bodies were not read.

## Example request/response

No example: the body is only an unconfirmed candidate.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../errors.md).

## Callers in app

- `HttpRequestControllerImpl.setUserParams` (`charging/http/http_request_repository_impl.dart @0x2886da0`): no direct caller in the dump (the inventory lists none). UNCONFIRMED candidate callers (through `AE100ApiExt.setUserParamsAsync`, mixin dump incomplete): `charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/ae100/custom_mode_usage_scenario_logic.dart @0x2886c44`, `@0x28874a8`, `@0x28876bc`, the custom mode usage scenario page.

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- The request body keys are only a candidate (see Request); the forwarder is not in the dump.
- Which user-level site parameters the endpoint stores is not known.
- Whether the forwarder really calls this wrapper is not established (mixin code missing from the dump); the unit of `param_type` 40001 and the meaning of `param_value` "2" are not known.

## Device-tested by

none
