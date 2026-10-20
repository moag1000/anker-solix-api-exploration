> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

3.24.3: the URL literal is loaded by two closures of `EmsServiceImpl` (found by a string search of the asm on 2026-10-20; the endpoint inventory has no row for them, see Request); 3.18.0 has its own sender

# quit_disaster_prepare

## Purpose

Tells the cloud that the A1782 left the current disaster-preparedness event, before the app sends the quit command to the device (caller: the closure in `onQuitCurrentEvent` of the A1782 home logic mixin stack; the 3.18.0 success closure then refreshes the auto-disaster state and sends `setBackup` with `quitCurrentBackup`) (3.18.0 asm for the call chain; the meaning is string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_disaster_prepared/quit_disaster_prepare`, method `POST` in the 3.18.0 asm: in the closure `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a3384` (3.18.0 addresses) the method object `Instance_Method` is loaded at `@0x22a3504` (3.18.0 pool entry `pp+0x9b18`, enum index 1, `post`), the URL string at `@0x22a350c`, and the request goes through `HttpServiceImpl::encryptionRequestHttp` (`@0x22a3528`). In 3.24.3 the URL string exists only in the object pool, so no sender can be read.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys in 3.24.3 (no sender). In the 3.18.0 asm the map literal has the type arguments `<String, Object>` (`charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a34d4`), which name no value type; array length raw 16 (`charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a3460`), so four keys.

3.24.3 body (two `EmsServiceImpl` closures, traced 2026-10-20, file `ak_soft_ems/ems_service_impl.dart`):

| field | type | required | example | source |
|---|---|---|---|---|
| `type` | int (Smi, w) | yes | `2` (raw 4) | `ak_soft_ems/ems_service_impl.dart @0x33250d4` (key, first closure), value from the context constant `@0x3324ed0`, array slot `@0x3324ed8` |
| `identifier_id` | ? | yes | `"<id>"` | `ak_soft_ems/ems_service_impl.dart @0x33250e8` (key), value from the parameter in the context `field_f` `@0x3324ecc` |
| `is_ble` | int (Smi, w) | yes | `2` (raw 4) | `ak_soft_ems/ems_service_impl.dart @0x3325100` (key), value from the context `field_13` `@0x3324ed4` |
| `disaster_type` | int (Smi, w) | yes | `2` in the severe-weather closure, `1` in the manual-backup closure | `ak_soft_ems/ems_service_impl.dart @0x3325114` (key, first closure), constants `@0x3325120` (raw 4) and `@0x3325460` (raw 2, second closure) |

3.18.0 body (kept as history; the addresses in this table and in the paragraphs above and below that name `modules_logic.dart` or the 3.18.0 pool are 3.18.0 addresses):

| field | type | required | example | source |
|---|---|---|---|---|
| `type` | int (Smi, w) | yes | `1` (raw immediate 2, 32-bit store) | `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a3468` (value store `@0x22a3474`, constant `@0x22a3470`) |
| `identifier_id` | ? | yes | `"<id>"` | `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a3478` (store `@0x22a34a8`; value from a chain of field loads `@0x22a3488`, `@0x22a34a0`) |
| `is_ble` | int (Smi, w) | yes | `1` (raw immediate 2, 32-bit store) | `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a34ac` (value store `@0x22a34bc`, constant `@0x22a34b8`) |
| `disaster_type` | int (Smi, w) | yes | `2` (raw immediate 4, 32-bit store) | `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a34c0` (value store `@0x22a34d0`, constant `@0x22a34cc`) |

3.24.3 senders (app side, traced 2026-10-20): `EmsServiceImpl::showSevereWeatherModeDialog` (`ak_soft_ems/ems_service_impl.dart @0x3324e44`) and `EmsServiceImpl::showManualBackupModeDialog` (`ak_soft_ems/ems_service_impl.dart @0x3325198`) each pass a closure to `getDataFromService` that builds a four-key map `<String, Object?>` and sends it with the URL literal `/charging_disaster_prepared/quit_disaster_prepare` (closures `@0x33250a0` and `@0x33253e0`, literal `@0x332516c` and `@0x33254ac`, call `@0x332517c` and `@0x33254bc`). Keys and values: `type` is the context constant raw 4 (`@0x3324ed0`, array slot `@0x3324ed8`), so 2 under the Smi rule; `identifier_id` is a parameter of the function (context `field_f`, `@0x3324ecc`); `is_ble` is the context constant raw 4, so 2 (`@0x3324ed4`); `disaster_type` is the constant raw 4 (`@0x3325120`) in the severe-weather closure, so 2, and raw 2 (`@0x3325460`) in the manual-backup closure, so 1. The functions are called from the mode-tip handlers (`micro_hes/src/common_business/basic_station/module/mode_tip/mode_tip_logic.dart @0x443e5b0`, `@0x443e48c`; `base_service/view/device_mode_tips/mode_tips_item.dart @0x474ca7c`, `@0x474c9a4`; `station_home/src/ui/shared/mode_tip/mode_tip_action_handler.dart @0x3324214`, `@0x3324168`). `getDataFromService` is the shared helper described on [../charging_hes_dynamic_price_svc/get_price.md](../charging_hes_dynamic_price_svc/get_price.md) (post through the encrypted wrapper). The 3.18.0 reading further down is kept as history; this page was not re-audited field by field against the 3.24.3 sender.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the app as a model (3.18.0 asm): only a `success` closure is passed (argument descriptor `charging/ui/page/device/a1782/home/a1782_home_logic.dart @0x22a3520`); its body `@0x22a3560` logs a success line and calls `refreshAutoDisaster` (`@0x22a35dc`) and `AKIotDisasterPreparednessCommand::setBackup` (`@0x22a3640`); it reads no key of the response.

## Response

No response key is read by the app in the 3.18.0 asm (see Response model).

## Example request/response

Request, synthesized from the 3.18.0 asm (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "type": 1,
  "identifier_id": "<id>",
  "is_ble": 1,
  "disaster_type": 2
}
```

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: no 3.24.3 sender; the 3.18.0 closures read compare no numeric error code. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a1782/home/a1782_home_logic.dart`: `<anonymous closure> in _A1782DeviceLogic&AnkerBaseController&DeviceCountDownLogic&DeviceBatteryStatusLogic&GetTickerProviderStateMixin&PreparednessModuleMixin&AutoDisasterPreparednessMixin::onQuitCurrentEvent` @0x22a3384 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present (sender read in the 3.18.0 asm, addresses below are 3.18.0 addresses). 3.24.3: present (two senders in `EmsServiceImpl`, see Request). since: <=3.18.0. `tools/out/diff_3.18.0_3.24.3.md` lists the endpoint under removed endpoints because the inventory missed the 3.24.3 literals, not because the app dropped the call.

## Known unknowns

- Whether the server serves this URL for the 3.24.3 request: the app does send it (two `EmsServiceImpl` senders, see Request); the answer of the server is not known from the app.
- What `is_ble`, `disaster_type` and `type` select on the server: the 3.24.3 values are decoded in Request (type 2, is_ble 2, disaster_type 2 or 1); the 3.18.0 sender sent other values for `is_ble` and `type`, and what any value selects is not known from the app — traced 2026-10-20.
- Type of `identifier_id` (field-load chain, declared type not visible). — attempted 2026-10-20 (two-hop not readable: the six callers of `showSevereWeatherModeDialog` and `showManualBackupModeDialog` pass a slot or field of their own frames, `micro_hes/src/common_business/basic_station/module/mode_tip/mode_tip_logic.dart @0x443e598`, `@0x443e488`, `station_home/src/ui/shared/mode_tip/mode_tip_action_handler.dart @0x3324204`, `@0x3324164`)

## Device-tested by

none
