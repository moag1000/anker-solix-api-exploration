> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_power_cutoff

## Purpose

Writes the discharge cut-off (SoC) setting of an A17C0/A17C1 solar bank from the settings dialogs and after a manual factory reset (callers `A17c0settingLogic::showSocDialog`, `A17C1homeLogic::onMessageDispatch`, `A17C1SettingLogic::onTapSafetySoC` and `showSocDialog`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`set_cutoff` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/compatible/set_power_cutoff` (asm-traced): URL string at `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x3d60a14`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3d60a0c`, in `A17c0settingLogic::requestToSetSoc` (`charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x3d60820`), sent through `encryptionRequestHttp` (`@0x3d60a30`).

Same URL and method object in the other sender(s) read:

- `POST /power_service/v1/app/compatible/set_power_cutoff` (asm-traced): URL string at `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x263106c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2631064`, in `A17C1homeLogic::_dealWithBleResponse` (`charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x263087c`), sent through `encryptionRequestHttp` (`@0x2631080`).
- `POST /power_service/v1/app/compatible/set_power_cutoff` (asm-traced): URL string at `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d959d4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3d959cc`, in `A17C1SettingLogic::requestNewSetSoc` (`charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d95764`), sent through `encryptionRequestHttp` (`@0x3d959f8`).
- `POST /power_service/v1/app/compatible/set_power_cutoff` (asm-traced): URL string at `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d94e2c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3d94e24`, in `A17C1SettingLogic::requestToSetSoc` (`charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d94c6c`), sent through `encryptionRequestHttp` (`@0x3d94e48`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) Four senders. The three older ones send two keys: `A17c0settingLogic::requestToSetSoc` (`charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x3d60820`, literal `<String, Object?>` at `@0x3d609d8`), `A17C1homeLogic::_dealWithBleResponse` (`charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x263087c`, `<String, Object>` at `@0x263104c`, constant `cutoff_data_id` from raw 2, so 1, `@0x2631038..0x2631048`) and `A17C1SettingLogic::requestToSetSoc` (`charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d94c6c`, `<String, Object?>`). The new `A17C1SettingLogic::requestNewSetSoc` (`@0x3d95764`, literal `<String, Object?>`) adds five keys; `cmd_type` is the constant raw 2, so 1 (`@0x3d95980`). Values are fields of the settings objects.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | ? | yes | ? | `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x3d60920`, `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x2630ffc`, `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d95820`, `@0x3d94d78` |
| `cutoff_data_id` | ?; int (Smi, w) constant 1 in `_dealWithBleResponse` | yes | `1` (only in `_dealWithBleResponse`) | `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x3d60990`; constant `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x2631038`; `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d957c0`, `@0x3d94da8` |
| `charge_upper_limit` | ? | yes (`requestNewSetSoc` only) | ? | `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d95878` |
| `discharge_lower_limit` | ? | yes (`requestNewSetSoc` only) | ? | `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d958c0` |
| `backup_reserve` | ? | yes (`requestNewSetSoc` only) | ? | `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d958fc` |
| `backup_reserve_switch` | ? | yes (`requestNewSetSoc` only) | ? | `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d95938` |
| `cmd_type` | int (Smi, w) | yes (`requestNewSetSoc` only) | `1` | `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d95974` (raw 2 stored by a 32-bit store `@0x3d95984`) |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed as a model in the senders read (asm-traced): the success closure of `A17c0settingLogic.requestToSetSoc` calls `setSoc` with a context variable (`ArrayLoad r0 = r2[0]`, default raw 10 in an unboxed register when null, so 10; `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x3d60b00`..`@0x3d60b24`), i.e. the value the user chose, not a response value, and then fires an event on `EventBusManager` (`@0x3d60b3c`); the success closures read call `setSoc` (`charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart @0x3d60b24`, `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d95b44`) or fire a `MessageEvent` (`@0x3d94ee0`); no `fromJson` or response key is read in them.

## Response

Not read: no response key is read in the senders.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "device_sn": "<?>",
  "cutoff_data_id": "<?>"
}
```

Response: not synthesized (the app does not read keys). 3.24.3 adds a second body shape:

```json
{
  "cutoff_data_id": "<?>",
  "device_sn": "<?>",
  "charge_upper_limit": "<?>",
  "discharge_lower_limit": "<?>",
  "backup_reserve": "<?>",
  "backup_reserve_switch": "<?>",
  "cmd_type": 1
}
```

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart`: `requestToSetSoc` @0x3d60820 (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart`: `_dealWithBleResponse` @0x263087c (encryptionRequestHttp; encrypted: true)
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart`: `requestNewSetSoc` @0x3d95764 (encryptionRequestHttp; encrypted: true); `requestToSetSoc` @0x3d94c6c (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/page/device/a17c0/a17c0setting/a17c0setting_logic.dart::showSocDialog`
- `charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart::onMessageDispatch`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::onTapSafetySoC`
- `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart::showSocDialog`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. Param delta in `tools/out/diff_3.18.0_3.24.3.md`: 3.24.3 added `backup_reserve`, `backup_reserve_switch`, `charge_upper_limit`, `cmd_type` and `discharge_lower_limit` (the `requestNewSetSoc` sender, `charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d95764`).

## Known unknowns

- Types of `device_sn`, `cutoff_data_id` and the four SoC values: fields of settings objects; the literals are `<String, Object?>`/`<String, Object>` and carry no field type. — attempted 2026-10-20 (two-hop not readable: the values are field reads of settings objects with no declared type in the asm (`charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d957c0`, `@0x3d95878`..`@0x3d95938`). Header stays string-only)
- Which sender writes which `cutoff_data_id` value (the id is the `SocModel.id` the user picked, see [get_power_cutoff](get_power_cutoff.md); the mapping was not decoded). — traced 2026-10-20: the `cutoff_data_id` values are the `SocModel.id` of the entry the user picked (field read of a settings object, no literal except the constant 1 in `_dealWithBleResponse`); the readers of the pick were not followed
- What `cmd_type` 1 selects on the server and whether the old two-key body is still accepted for A17C1 devices (server behaviour).
- The effect of `setSoc` in `A17C1SettingLogic.requestToSetSoc` and `requestNewSetSoc` on the UI state (`charging/ui/page/device/a17c1/a17c1setting/a17c1setting_logic.dart @0x3d95b44`) — traced 2026-10-20: only the A17c0 closure was read (see Response model); the A17C1 closures were not

## Device-tested by

none
