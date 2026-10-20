> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_power_range_support_protocols

## Purpose

Reads the protocols that the charger ports support per power range, for the charging-mode pages (callers `getRangeProtocols` in the A2345 and A2687 home logic) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/setting/get_power_range_support_protocols` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3472f74`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3472f6c`, in `HttpRequestControllerImpl::getPowerSupportProtocols` (`charging/http/http_request_repository_impl.dart @0x3472ea8`), sent through `encryptionRequestHttp` (`@0x3472f9c`).

Same URL and method object in the other sender(s) read:

- `POST /mini_power/v1/app/setting/get_power_range_support_protocols` (asm-traced): URL string at `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x2afcfe4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2afcfdc`, in `CustomChargeCloudApi::getPowerSupportProtocols` (`small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x2afcf10`), sent through `encryptionRequestHttp` (`@0x2afd00c`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) Both senders store two keys unconditionally in a map literal with type arguments `<String, String>` (`charging/http/http_request_repository_impl.dart @0x3472f28`; second sender `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x2afcfac`), so both values are Strings. `HttpRequestControllerImpl::getPowerSupportProtocols` is `charging/http/http_request_repository_impl.dart @0x3472ea8`, `CustomChargeCloudApi::getPowerSupportProtocols` is `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x2afcf10`.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_model` | string | yes | `"<device_model>"` | `charging/http/http_request_repository_impl.dart @0x3472f00` (map literal `<String, String>` `charging/http/http_request_repository_impl.dart @0x3472f28`) |
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x3472f14` (same literal) |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`PowerRangeProtocolsResponse`](../../../../models/charger.md#powerrangeprotocolsresponse), parsed by `PowerRangeProtocolsResponse.fromJson` at `charging/http/http_request_repository_impl.dart @0x3472ff0` (success closure `@0x3472fb8`; the closure hands the model's first field, `r0->field_13` `@0x3472ff8`, to the callback, `ClosureCall` `@0x347300c`).
- `small_charging_platform::PowerRangeProtocolsResponse` (`data/models.json`), parsed by `PowerRangeProtocolsResponse.fromJson` at `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x2afd06c` (success closure `@0x2afd02c`; callback `ClosureCall` `@0x2afd080`). Used by the `CustomChargeCloudApi` sender.

## Response

Top-level key per model (`data/models.json`): `port_list` in both `charging::PowerRangeProtocolsResponse` and `small_charging_platform::PowerRangeProtocolsResponse` (field type not extracted).

Element shapes (app side, traced 2026-10-20, `small_charging_platform/src/scp/chargingMode/custom_charge/power_range_protocols_model.dart`, `fromJson` casts): `port_list` is a list of `PortProtocolConfig`, which has `port` (`String?`) and `power_range_protocols_mapping`, a list of `PowerRangeProtocolMapping` with `min_power` and `max_power` (`int?`) and `protocols` (a list of strings).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_model": "<device_model>",
  "device_sn": "<device_sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getPowerSupportProtocols` @0x3472ea8 (encryptionRequestHttp; encrypted: true)
- `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart`: `getPowerSupportProtocols` @0x2afcf10 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/a2345/a2345home/a2345home_logic.dart::getRangeProtocols`
- `charging/ui/page/device/a2687/a2687home/a2687_home_logic.dart::getRangeProtocols`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. `tools/out/diff_3.18.0_3.24.3.md` lists the parameter `device_sn` as added in 3.24.3 (string-level diff); both senders read here store `device_sn`. `data/models.json` lists the `small_charging_platform` model as since 3.24.3; that sender was not compared with 3.18.0.

3.18.0 sender (traced 2026-10-20, 3.18.0 asm tree): `HttpRequestControllerImpl::getPowerSupportProtocols` (`charging/http/http_request_repository_impl.dart`, URL load `@0x24fd09c` in the 3.18.0 tree) stores exactly one key, `device_model`, in a `<String, String>` literal (`@0x24fd03c`..`@0x24fd050`), so 3.18.0 clients sent `device_model` alone and `device_sn` is new in 3.24.3.

## Known unknowns

- What the server returns when `device_model` and `device_sn` disagree.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
