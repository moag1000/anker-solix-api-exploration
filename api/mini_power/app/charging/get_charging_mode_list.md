> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_charging_mode_list

## Purpose

Lists the custom charging modes of an A2345 or A2687 charger for the charging-mode pages (`getCustomChargeModelList` and `_getCustomChargeModeListByCloud` in the A2345 and A2687 logic classes) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`charger_get_charging_modes` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /mini_power/v1/app/charging/get_charging_mode_list` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x26c1398`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x26c1390`, in `HttpRequestControllerImpl::getCustomChargeModeList` (`charging/http/http_request_repository_impl.dart @0x26c12e0`), sent through `encryptionRequestHttp` (`@0x26c13c0`).

Same URL and method object in the other sender(s) read:

- `POST /mini_power/v1/app/charging/get_charging_mode_list` (asm-traced): URL string at `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x2afb80c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2afb804`, in `CustomChargeCloudApi::getCustomChargeModeList` (`small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x2afb74c`), sent through `encryptionRequestHttp` (`@0x2afb834`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) Both senders store one key, `device_sn`, unconditionally in a map literal with type arguments `<String, String>` (`charging/http/http_request_repository_impl.dart @0x26c134c`; second sender `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x2afb7d4`), so the value is a String.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string | yes | `"<device_sn>"` | `charging/http/http_request_repository_impl.dart @0x26c1338` (map literal `<String, String>` `charging/http/http_request_repository_impl.dart @0x26c134c`) |

## `param_type`/`cmd`

n/a

## Response model (link)

- [`A2345CustomModeList`](../../../../models/charger.md#a2345custommodelist), parsed by `A2345CustomModeList.fromJson` at `charging/http/http_request_repository_impl.dart @0x26c1414` (success closure `@0x26c13dc`; the closure hands the model's first field, `r0->field_13` `@0x26c141c`, to the callback, `ClosureCall` `@0x26c1430`).
- `small_charging_platform::CustomChargeModeList` (`data/models.json`), parsed by `CustomChargeModeList.fromJson` at `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x2afb894` (success closure `@0x2afb854`; callback `ClosureCall` `@0x2afb8a8`). Used by the `CustomChargeCloudApi` sender.

## Response

Top-level keys per model (`data/models.json`): `charging::A2345CustomModeList` has `charging_mode_list` (field type not extracted); `small_charging_platform::CustomChargeModeList` has `charging_mode_list` (`List<CustomChargeModeItem>`).

Element shape (app side, traced 2026-10-20, `charging/model/a2345/a2345_custom_mode_list.dart`, `fromJson` casts): `charging_mode_list` is a list of `A2345CustomModeItem` with `id`, `number`, `total_power`, `max_total_power` and `auto_exit` (`int?`), `name` (`String?`), `has_charge_protocol` and `power_settings`, a list of `PowerSetting` with `name` (`String?`), `power` and `max_power` (`int?`) and the protocol keys `scp`, `ufcs`, `pd12v`, `pps11v`, `pps16v`, `pps20v`, `huawei`.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<device_sn>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getCustomChargeModeList` @0x26c12e0 (encryptionRequestHttp; encrypted: true)
- `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart`: `getCustomChargeModeList` @0x2afb74c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getCustomChargeModeList`
- `charging/ui/page/device/a2345/a2345charging_model/a2345charging_model_logic.dart::getCustomChargeModelList`
- `charging/ui/page/device/a2345/a2345custom_charging_mode/a2345custom_charging_mode_logic.dart::_getCustomChargeModeListByCloud`
- `charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_charge_mode_logic.dart::getCustomChargeModelList`
- `charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_custom_charge_mode/a2687_custom_charge_mode_logic.dart::_getCustomChargeModeListByCloud`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types). `data/models.json` lists `CustomChargeModeList` (the `small_charging_platform` model) as since 3.24.3; the `small_charging_platform` sender was not compared with 3.18.0.

## Known unknowns

- Whether the two senders return different lists for the same `device_sn` (the second one belongs to the small-charging-platform module). — reclassified: server (2026-10-20: both senders post the same single key `device_sn` to the same URL; whether the answers differ is decided by the server, the two response models are listed under Response model)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
