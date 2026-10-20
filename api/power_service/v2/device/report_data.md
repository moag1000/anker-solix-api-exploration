> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# report_data

## Purpose

Uploads a low-battery warning of a device to the cloud: the device serial, the data type `battery_soc`, the state of charge and the report time; the app sends it when a device reports a battery level at or below the configured warning level.

## Upstream name

`none` for this URL (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 350).

## Method+URL

`POST /power_service/v2/device/report_data` (asm-traced): URL literal `@0x2603778` in `DeviceMainLogic._uploadLowBatteryWarning` (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x26031c4`), method object `Method.post` (pool entry `pp+0xa7e0`, `@0x2603770`).

## Encrypted?

Yes by wrapper (asm-traced): ``_uploadLowBatteryWarning`` calls `encryptionRequestHttp` (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x260379c`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

Map literal with four pairs, `<String, Object>` (`@0x2603728`); the third value is itself a `<String, int>` map.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `"<device sn>"` | `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x2603624`; value is a local variable stored at `@0x2603634` |
| `data_type` | String | yes | `"battery_soc"` | `@0x2603638`, literal value `"battery_soc"` `@0x2603644` |
| `data` | map | yes | `{ "soc": 20 }` | `@0x2603650`; inner map `<String, int>` with the key `soc` (`@0x2603664`, value stored at `@0x2603674`, a local int, not a literal) |
| `report_time` | int | yes | `1760000000` | `@0x26036b0`; seconds since the epoch: `DateTime` microseconds (`_getCurrentMicros`, `@0x26036bc`) divided by 1000 twice with signed division (`sdiv` by 1000 at `@0x26036e4`, `@0x26036e8`; the raw immediates `1000` at `@0x26036dc` and `999` at `@0x26036d0` are arithmetic operands, unboxed, so real values 1000 and 999) |

Gate before sending: the function reads the low-battery warning config (`getLowBatteryWarningConfig`, `@0x2603208`) and a stored map with `isPending`, `lastBattery` and `isUpload` (`@0x26033bc`, `@0x260341c`, `@0x2603478`), and only sends when its comparisons allow (the comparison logic is not decoded).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed.

## Response

No response field is read (asm-traced). The success closure (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x26038e0`) updates the stored map keys `isPending` (`@0x2603920`), `isUpload` (`@0x2603954`) and `lastBattery` (`@0x2603984`); the failure closure (`@0x260380c`) resets `isPending` (`@0x260384c`) and `lastBattery` (`@0x2603880`).

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>", "data_type": "battery_soc", "data": { "soc": 20 }, "report_time": 1760000000 }
```

Response: no captured response; no field is read.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `DeviceMainLogic._uploadLowBatteryWarning` (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x26031c4`), called from `DeviceMainLogic.onMessageDispatch`: the device main page of the station device home (package `charging`), triggered by incoming device messages.

Upload conditions seen so far (asm-traced, `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart`): `_uploadLowBatteryWarning` (`@0x26031c4`) returns without a request when `getLowBatteryWarningConfig` is null (`@0x260320c`), when the device connection status is not `bleBusinessConnected` (enum index 3, pool object `pp+0xca68`, compare `@0x2603244`; `pp.txt` line 9357) and when the `battery` value read from the device info is not an integer (type test `@0x26032dc`..`@0x26032e4`). It keeps per-device state under the keys `isPending` (`@0x26033bc`), `lastBattery` (`@0x260341c`) and `isUpload` (`@0x2603478`), compares an integer with the immediate 5 (`cmp x0, #5` `@0x2603504`, `@0x260354c`) and then builds the body with `device_sn`, `data_type` = `battery_soc` and `data` with `soc` and `report_time` (`@0x2603624`..`@0x26036b0`). The two call sites in `DeviceMainLogic.onMessageDispatch` (`@0x26027b0`, `@0x2602b64`) pass the `device` entry of the message payload (`r2 = "device"` `@0x260274c`, type check `IAnkerDevice?` `@0x2602798`).

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- The thresholds behind the compare with 5 (`cmp x0, #5` `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x2603504`, `@0x260354c`) and the fields of the low-battery warning config in `_uploadLowBatteryWarning` — traced 2026-10-20: the early exits (config null, connection status not `bleBusinessConnected`, `battery` not an integer), the per-device state keys `isPending` / `lastBattery` / `isUpload` and the two call sites in `onMessageDispatch` (`@0x26027b0`, `@0x2602b64`) were read; see Callers in app
- Whether other `data_type` values exist is not known; only `battery_soc` is sent by the traced sender.
- Server behaviour (what the cloud does with the report, for example push notifications) is not known.

## Device-tested by

none
