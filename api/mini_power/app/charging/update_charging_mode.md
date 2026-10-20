> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# update_charging_mode

## Purpose

Saves the edited values of an existing custom charging mode of an A2345 or A2687 charger (`_updateCustomChargeModeToCloud` and `_applySCPBackwardCompatFixIfNeeded` in the A2345 and A2687 custom-charging edit logic classes) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /mini_power/v1/app/charging/update_charging_mode` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3469be8`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3469be0`, in `HttpRequestControllerImpl::updateCustomChargeMode` (`charging/http/http_request_repository_impl.dart @0x3469a84`), sent through `encryptionRequestHttp` (`@0x3469c10`).

Same URL and method object in the other sender(s) read:

- `POST /mini_power/v1/app/charging/update_charging_mode` (asm-traced): URL string at `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x3192630`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3192628`, in `CustomChargeCloudApi::updateCustomChargeMode` (`small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x319249c`), sent through `encryptionRequestHttp` (`@0x3192658`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced for the stores, `?` where the value is not typed) Two senders store seven keys unconditionally in one map literal with type arguments `<String, Object?>` (`charging/http/http_request_repository_impl.dart @0x3469b9c`; second sender `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x31925f4`), which does not type the values. `HttpRequestControllerImpl::updateCustomChargeMode` (`charging/http/http_request_repository_impl.dart @0x3469a84`) loads `id` and the other values from fields of one mode object. `CustomChargeCloudApi::updateCustomChargeMode` (`small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x319249c`) stores the same keys, with `power_settings` from `buildPowerSettingsForCloud` (`@0x31925c8`) and `has_charge_protocol` built the same way (`cmp w2, NULL` `@0x319259c`, `r2 = 1` `@0x31925a8`, `r2 = 0` `@0x31925b0`). Unlike `add_charging_mode` there is no `device_sn` and no `number`.

| field | type | required | example | source |
|---|---|---|---|---|
| `id` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3469ad8` (field load `charging/http/http_request_repository_impl.dart @0x3469ae8`) |
| `name` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3469af4` (field load `@0x3469afc`) |
| `total_power` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3469b08` (field load `@0x3469b14`) |
| `max_total_power` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3469b20` (field load `@0x3469b2c`) |
| `auto_exit` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3469b38` (field load `@0x3469b44`) |
| `has_charge_protocol` | int (Smi, w) | yes | `0` or `1` (not a constant) | `charging/http/http_request_repository_impl.dart @0x3469b50` (built from a bool field: `cmp w2, NULL` `@0x3469b64`, `r2 = 1` `@0x3469b70`, `r2 = 0` `@0x3469b78`) |
| `power_settings` | ? | yes | ? | `charging/http/http_request_repository_impl.dart @0x3469b84` (field load `@0x3469b90`; the second sender stores the result of `buildPowerSettingsForCloud` instead) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app (asm-traced): the success closure `charging/http/http_request_repository_impl.dart @0x261b9a0` calls the stored callback with the constant `true` (`@0x261b9cc`) and reads no response key; the second sender's success closure (`small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart @0x3192444`) does the same (`@0x3192470`).

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "id": "<?>",
  "name": "<?>",
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

- `charging/http/http_request_repository_impl.dart`: `updateCustomChargeMode` @0x3469a84 (encryptionRequestHttp; encrypted: true)
- `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_cloud_api.dart`: `updateCustomChargeMode` @0x319249c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::updateCustomChargeMode`
- `charging/ui/page/device/a2345/a2345CNcustom_charging_edit/a2345CNcustom_charging_edit_logic.dart::_applySCPBackwardCompatFixIfNeeded`
- `charging/ui/page/device/a2345/a2345CNcustom_charging_edit/a2345CNcustom_charging_edit_logic.dart::_updateCustomChargeModeToCloud`
- `charging/ui/page/device/a2345/a2345CNcustom_charging_edit/a2345CNcustom_platfrom_charging_edit_logic.dart::_updateCustomChargeModeToCloud`
- `charging/ui/page/device/a2345/a2345custom_charging_edit/a2345custom_charging_edit_logic.dart::_applySCPBackwardCompatFixIfNeeded`
- `charging/ui/page/device/a2345/a2345custom_charging_edit/a2345custom_charging_edit_logic.dart::_updateCustomChargeModeToCloud`
- `charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_custom_charge_edit/a2687_custom_charge_edit_logic.dart::_updateCustomChargeModeToCloud`
- `charging/ui/page/device/a2687/a2687setting/a2687_charge_mode/a2687_custom_charge_edit/a2687_custom_platform_charge_edit_logic.dart::_updateCustomChargeModeToCloud`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types). The `small_charging_platform` sender was not compared with 3.18.0.

## Known unknowns

- Types of `id`, `name`, `total_power`, `max_total_power`, `auto_exit` and `power_settings`: object-field values the builders do not type (map literal `<String, Object?>`); the mode object's class was not read. — attempted 2026-10-20 (two-hop not readable: the five callers pass the mode object as a slot of their own frame, `small_charging_platform/src/scp/chargingMode/custom_charge/custom_charge_platform_edit_logic.dart @0x3a9f6cc`, `charging/ui/page/device/a2345/a2345custom_charging_edit/a2345custom_charging_edit_logic.dart @0x3470d84`, `@0x3e31d4c`, `charging/ui/page/device/a2345/a2345CNcustom_charging_edit/a2345CNcustom_platfrom_charging_edit_logic.dart @0x3e05f0c`, `charging/ui/page/device/a2345/a2345CNcustom_charging_edit/a2345CNcustom_charging_edit_logic.dart @0x34699bc`; its class is not named in the asm)
- The element shape of `power_settings` (built by `buildPowerSettingsForCloud` in the second sender, not read).
- Whether the server requires every key or accepts a partial update: the app always sends all seven.
- Header stays `string-only` because the field types above are missing. — rechecked 2026-10-20: still true; the typing attempts are recorded on the bullets of this section
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
