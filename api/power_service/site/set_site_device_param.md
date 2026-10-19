> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# set_site_device_param

## Purpose

Writes one site-level parameter set, selected by `param_type`, for a site; with `param_type` 19 it sets the system output power limit of a station.

## Upstream name

`set_device_parm` in `API_ENDPOINTS` of `api/apitypes.py`, called through `set_device_parm()` in `api/schedule.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/set_site_device_param` (asm-traced): URL string at `http_request_repository_impl.dart @0x435595c`, method object `Method.post` (pool entry `pp+0xa7e0`, `off_10: "post"`) at `@0x4355954`.

## Encrypted?

Yes (asm-traced): the type-19 wrapper sends the request through `HttpRequestControllerImpl::encryptionRequestHttp` (`http_request_repository_impl.dart @0x435598c`). The scheme is described in `api/encryption.md`.

## Request

The request body is a JSON object with four keys (the map literal is allocated with 8 slots, i.e. 4 key/value pairs, `http_request_repository_impl.dart @0x435587c`). The values below are those of the type-19 wrapper `setSiteDevicePowerLimit`; other wrappers fill the same four keys with their own values, see [../../param_types.md](../../param_types.md).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `"<site_id>"` | `http_request_repository_impl.dart @0x435588c` (value is the caller's site id, parameter r6) |
| `param_type` | String | yes | `"19"` | `http_request_repository_impl.dart @0x43558ac` (string literal, not a Smi) |
| `cmd` | int | yes | value per param_type, see [../../param_types.md](../../param_types.md) | `http_request_repository_impl.dart @0x43558b8` |
| `param_data` | String (JSON-encoded object) | yes | see the usage subsection below | `http_request_repository_impl.dart @0x43558cc`, encoded by `jsonEncode` at `@0x43558e0` |

`param_data` is a string that contains JSON, not a nested object: the wrapper builds a `Map<String, Object>` and passes it through `jsonEncode` before it is stored under `param_data` (`@0x43558e0` to `@0x43558e8`).

### Usage: param_type 19 (system output power limit)

Wrapper: `HttpRequestControllerImpl::setSiteDevicePowerLimit` (`http_request_repository_impl.dart @0x4355750`). The decoded `param_data` object has two keys (outer map, 4 slots, `@0x43557a4`):

| field | type | required | example | source |
|---|---|---|---|---|
| `display_type` | int | yes | `1` | `http_request_repository_impl.dart @0x43557b0` (key), value raw `2` at `@0x43557bc`, stored 32-bit (`stur w16`, `@0x43557c0`), Smi, so the value is 1. It is a constant, not a parameter. |
| `power_limit` | object | yes | `{"limit": 790, "limit_real": 790}` | `http_request_repository_impl.dart @0x43557c4` (inner map, 4 slots, `@0x43557d4`) |
| `power_limit.limit` | int | yes | `790` | `http_request_repository_impl.dart @0x43557e0` (key), value from parameter r3, boxed at `@0x43557f0` |
| `power_limit.limit_real` | int | yes | `790` | `http_request_repository_impl.dart @0x4355808` (key), value from parameter r5, boxed at `@0x4355818` |

In the app's only caller both `limit` and `limit_real` receive the same value, the slider value in watts: `_setOutputPowerLimit` passes the same register as r3 and r5 (`station_power_limit_logic.dart @0x435566c` and `@0x4355670`). The slider range and step are part of the flow, see [../../../flows/system_output_limit.md](../../../flows/system_output_limit.md).

Other param_types sent to this endpoint are not described here; each one has a row in [../../param_types.md](../../param_types.md).

## `param_type`/`cmd`

See [../../param_types.md](../../param_types.md).

## Response model (link)

n/a for param_type 19 (asm-traced): the success callback of `_setOutputPowerLimit` (closure `station_power_limit_logic.dart @0x4355a70`) only writes a log line and parses no model.

## Response

No endpoint-specific response fields are read by the type-19 caller (asm-traced, `station_power_limit_logic.dart @0x4355a70`). The failure callback receives an int code and a String message (closure `station_power_limit_logic.dart @0x43559f8`).

| field | type | required | example | source |
|---|---|---|---|---|
| (none read) | | | | `station_power_limit_logic.dart @0x4355a70` |

## Example request/response

Request, synthesized (decrypted body as built by `setSiteDevicePowerLimit` for a slider value of 790 W; the `cmd` value is owned by [../../param_types.md](../../param_types.md))

```json
{
  "site_id": "<site_id>",
  "param_type": "19",
  "cmd": 123,
  "param_data": "{\"display_type\":1,\"power_limit\":{\"limit\":790,\"limit_real\":790}}"
}
```

Response, synthesized (shape only; no captured response for this payload exists yet)

```json
{"code": 0, "msg": "success", "data": {}}
```

## Errors seen

None recorded for the app payload above. For a different payload (upstream library, `cmd` 17, no `display_type`, 790 W on A17C5) error `10004` (ItemNotFoundError) was reported in [thomluther/anker-solix-api#339](https://github.com/thomluther/anker-solix-api/issues/339); that report is not yet a complete `device-tested` record (firmware and date missing). Error codes are catalogued in `api/errors.md`.

## Callers in app

- `StationPowerLimitLogic::_setOutputPowerLimit` (`station_power_limit_logic.dart @0x4355598`) calls `setSiteDevicePowerLimit` at `@0x435567c`. UI: station settings, power limit page, output power slider; see [../../../flows/system_output_limit.md](../../../flows/system_output_limit.md). `setSiteDevicePowerLimit` has no other caller in the 3.24.3 asm.
- The URL string is referenced by 32 functions in the 3.24.3 asm (other wrappers such as `setSiteDeviceParam`, `setSafetySocParams`, `set17C1SiteDeviceParam`, `setStationCountryCode`, `setDynamicPrice`, `setThreePvInstallSwitch`, plus feature controllers). They belong to other param_types and are documented per row in [../../param_types.md](../../param_types.md) (pending Task 3.4).

## Since/changed

3.18.0: `setSiteDevicePowerLimit` (3.18.0 `http_request_repository_impl.dart @0x327fdc0`) sent the same four top-level keys with `param_type` `"19"` and `cmd` raw 246 stored 32-bit (`@0x327ff20`/`@0x327ff24`), i.e. 123; its `param_data` held only `power_limit` (`limit`, `limit_real`), typed `Map<String, Map<String, int>>`, with no `display_type`. 3.24.3: `display_type` (constant 1) is new in `param_data` (`@0x43557b0`); `cmd` is unchanged at 123; the request is still sent encrypted.

## Known unknowns

- What `display_type` means on the server side. A plausible reading is that it marks the value as a free slider value rather than an entry of `power_limit_option`; this is not verified.
- Whether the server accepts `cmd` 17 (as sent by the upstream library) as well as 123 for param_type 19, with and without `display_type`. A test matrix is pending with thomluther; no outcome is recorded here.
- Whether the encrypted request path is required, or whether a plain request with the same body is accepted.
- The response body for a successful type-19 call (not read by the app).

## Device-tested by

none
