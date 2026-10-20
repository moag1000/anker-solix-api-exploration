> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# add_charging_mode

## Purpose

Creates one custom charging mode of an A2345 or A2687 charger when the user saves a new mode on the custom-charging edit pages (`_addCustomChargeModeToCloud` in the A2345 and A2687 edit logic classes) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/charging/add_charging_mode` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x38b75d4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x38b75cc`, in `HttpRequestControllerImpl::addCustomChargeMode` (`charging/http/http_request_repository_impl.dart @0x38b7458`), sent through `encryptionRequestHttp` (`@0x38b75fc`).

Same URL and method object in the other sender(s) read:

- `POST /mini_power/v1/app/charging/add_charging_mode` (asm-traced): URL string at `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x3aa5fc8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3aa5fc0`, in `CustomChargeCloudApi::addCustomChargeMode` (`small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x3aa5e14`), sent through `encryptionRequestHttp` (`@0x3aa5ff0`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced for the stores, `?` where the value is not typed) Two senders store the same eight keys unconditionally in one map literal with type arguments `<String, Object?>` (`charging/http/http_request_repository_impl.dart @0x38b7588`, second sender `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x3aa5f8c`), which does not type the values. `HttpRequestControllerImpl::addCustomChargeMode` (`charging/http/http_request_repository_impl.dart @0x38b7458`) takes `device_sn` from a parameter and the other values from fields of a mode object. `CustomChargeCloudApi::addCustomChargeMode` (`small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x3aa5e14`) stores the same keys; its `power_settings` value is the result of `buildPowerSettingsForCloud` (`@0x3aa5f60`, stored `@0x3aa5f68`) and its `has_charge_protocol` is built the same way (`cmp w2, NULL` `@0x3aa5f34`, `tbnz w2, #4` `@0x3aa5f3c`, `lsl x3, x2, #1` `@0x3aa5f4c`). The worksheet `tools/out/request_fields_all.json` lists `has_charge_protocol` as the constant `0`; the asm shows a 0 or 1 computed from a bool field.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x38b74b0` (parameter, not typed by the builder) |
| `name` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x38b74c4` (value loaded from a field of the mode object, `charging/http/http_request_repository_impl.dart @0x38b74d0`) |
| `number` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x38b74dc` (field load `@0x38b74e8`) |
| `total_power` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x38b74f4` (field load `@0x38b7500`) |
| `max_total_power` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x38b750c` (field load `@0x38b7518`) |
| `auto_exit` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x38b7524` (field load `@0x38b7530`) |
| `has_charge_protocol` | int (Smi, w) | yes | `0` or `1` (not a constant) | `charging/http/http_request_repository_impl.dart @0x38b753c` (built from a bool field: `cmp w2, NULL` `@0x38b7550`, `tbnz w2, #4` `@0x38b7558`, `r2 = 1` `@0x38b755c`, `r2 = 0` `@0x38b7564`, tagged by `lsl x3, x2, #1` `@0x38b7568`, stored `@0x38b756c`) |
| `power_settings` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x38b7570` (field load `@0x38b757c`; the second sender stores the result of `buildPowerSettingsForCloud` instead) |

## `param_type`/`cmd`

n/a

## Response model (link)

No model class (asm-traced): the success closure of `HttpRequestControllerImpl::addCustomChargeMode` (`charging/http/http_request_repository_impl.dart @0x38b7618`) reads one key, `id` (`@0x38b7654`), casts it to `int` (`r8 = int` `@0x38b7690`) and passes it to the stored callback (`ClosureCall` `@0x38b76b0`). The second sender's closure (`small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x3aa6010`) reads `id` (`@0x3aa6044`), converts it through a dispatch-table call when its class id is in the numeric range (`@0x3aa6080`..`@0x3aa60a0`) and otherwise casts it with `as int` (`@0x3aa60c0`), then calls the callback with the boxed result (`@0x3aa6128`).

## Response

Top-level key read by the app: `id` (integer; the id of the new mode, the callback receives it as `int`). No other response key is read.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<?>",
  "name": "<?>",
  "number": "<?>",
  "total_power": "<?>",
  "max_total_power": "<?>",
  "auto_exit": "<?>",
  "has_charge_protocol": "<int>",
  "power_settings": "<?>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `charging/http/http_request_repository_impl.dart @0x226824c` forwards code and message to a stored callback without reading them). Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `addCustomChargeMode` @0x38b7458 (encryptionRequestHttp; encrypted: true)
- `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart`: `addCustomChargeMode` @0x3aa5e14 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::addCustomChargeMode`
- `charging/ui/page/device/a2345/a2345CNcustom_charging_edit/a2345CNcustom_charging_edit_logic.dart::_addCustomChargeModeToCloud`
- `charging/ui/page/device/a2345/a2345CNcustom_charging_edit/a2345CNcustom_platfrom_charging_edit_logic.dart::_addCustomChargeModeToCloud`
- `charging/ui/page/device/a2345/a2345custom_charging_edit/a2345custom_charging_edit_logic.dart::_addCustomChargeModeToCloud`
- `charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_custom_charge_edit/a2687_custom_charge_edit_logic.dart::_addCustomChargeModeToCloud`
- `charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_custom_charge_edit/a2687_custom_platform_charge_edit_logic.dart::_addCustomChargeModeToCloud`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types). The `small_charging_platform` sender was not compared with 3.18.0.

## Known unknowns

- Types of `device_sn`, `name`, `number`, `total_power`, `max_total_power`, `auto_exit` and `power_settings`: they are parameter or object-field values the builders do not type (map literal `<String, Object?>`); the mode object's class and the callers' argument types were not read. — attempted 2026-10-20 (two-hop not readable: the three `_addCustomChargeModeToCloud` callers pass the `value` of an observable (`value()` `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_platform_edit_logic.dart @0x3aa5db4`, `charging/ui/page/device/a2345/a2345custom_charging_edit/a2345custom_charging_edit_logic.dart @0x3e32070`, `charging/ui/page/device/a2345/a2345CNcustom_charging_edit/a2345CNcustom_platfrom_charging_edit_logic.dart @0x3e06cf4`) and slots of their frames; the class of the mode object is not named)
- The element shape of `power_settings` (the second sender builds it in `buildPowerSettingsForCloud`, which was not read).
- Whether the answer carries keys besides `id`: the app reads only `id` and hands the integer to the callback.
- Header stays `string-only` because the field types above are missing. — rechecked 2026-10-20: still true; the typing attempts are recorded on the bullets of this section
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
