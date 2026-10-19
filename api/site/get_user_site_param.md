> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_user_site_param

## Purpose

Reads the account's site-level user parameters (`/site/v1/get_user_site_param`); the generic `getUserParams` function of the HTTP repository sends it. The only caller candidate is the AE100 custom-mode usage scenario page, through a mixin function that the dump omits (UNCONFIRMED).

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`; upstream knows the `power_service` user-param endpoints `get_user_param`/`set_user_param` instead).

## Method+URL

`POST /site/v1/get_user_site_param` (asm-traced). Sender: `HttpRequestControllerImpl.getUserParams` (`charging/http/http_request_repository_impl.dart @0x288cac0`); the URL literal is loaded at `@0x288cb40` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x288cb38`).

## Encrypted?

Yes by wrapper (asm-traced): `getUserParams` calls `HttpRequestControllerImpl.encryptionRequestHttp` (`charging/http/http_request_repository_impl.dart @0x288cb68`) with the named argument `showLoading` only (`@0x288cb60`) and without `needEncryption`, so the default `true` applies ([encryption.md](../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../encryption.md)); asm alone does not decide it.

## Request

No body: no parameter map is built; the function passes only the response callbacks and `showLoading`.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the callbacks are supplied by the caller; the function itself parses nothing.

## Response

Not parsed by the sender; the callbacks come from the caller.

## Example request/response

Request, synthesized

```json
{}
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- UNCONFIRMED candidate: `AE100CustomModeUsageLogic._checkUserTypeAndShowUpgradeDialog` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/power_usage_scenario/ae100/custom_mode_usage_scenario_logic.dart @0x2886750`) calls `getUserParamsAsync` of the mixin application `_MixinApplication707&BaseBleController&CommonLocation&AE100ApiExt` (target `0x288c978`, which lies just before `getUserParams` at `0x288cac0`). The Blutter dump omits the mixin body, so the link to `getUserParams` is an address-adjacency guess. No direct `bl` to `HttpRequestControllerImpl::getUserParams` was found.

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x101a38`). since: 3.24.3.

## Known unknowns

- The link between the AE100 `getUserParamsAsync` mixin function and this URL is not confirmed; the request body (none is built by `getUserParams`) and the answer layout are unknown.
- Compare [get_user_params](../power_service/app/user/get_user_params.md) and the EV charger `get_user_params` sender, which use the `power_service` URL.

## Device-tested by

none
