> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# report_event_data

## Purpose

Reports a device event to the cloud (the app log calls it the "425 event"): the app sends the device serial, the product code, the field `pn_payload` of the event object and the report time.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /devicecontrol/v1/app/report_event_data` (asm-traced): URL literal `@0x24127f0` in `DeviceFaultManager._reportEventToServer` (`business_common/msg/device_fault_manager.dart @0x2412574`), method object `Method.post` (pool entry `pp+0xa7e0`, `@0x24127e8`).

## Encrypted?

Yes by wrapper (asm-traced): ``_reportEventToServer`` calls `encryptionRequestHttp` (`business_common/msg/device_fault_manager.dart @0x2412814`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../encryption.md)); asm alone does not decide it.

## Request

Map literal with four pairs, `<String, Object>` (`r2 = 16`, `@0x2412664`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `"<device sn>"` | `business_common/msg/device_fault_manager.dart @0x2412678`; value is the field at offset 0x6b of the device object (`@0x2412688`) |
| `product_code` | String | yes | `"A17C5"` | `@0x2412694`; value from a getter (`@0x24126a8`); the example is a product code seen elsewhere in the app |
| `pn_payload` | not decoded | yes | not decoded | `@0x24126e8`; value is the field at offset 0x13 of the event object (`@0x24126f8`); that it carries the event payload is inferred from the key name, not decoded |
| `report_time` | int | yes | `1760000000` | `@0x2412728`; seconds since the epoch: current microseconds (`_getCurrentMicros`, `@0x2412734`) divided by 1000 twice with signed division (`sdiv`, `@0x241275c`, `@0x2412760`; the raw immediates `1000` at `@0x2412754` and `999` at `@0x2412748` are arithmetic operands, unboxed, real values); boxed at `@0x2412764` |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed.

## Response

No response field is read (asm-traced). The success closure (`business_common/msg/device_fault_manager.dart @0x24128e4`) logs `425 事件上报成功` ("425 event reported successfully", `@0x2412944`); the failure closure (`@0x2412830`) logs `425 事件上报失败` ("425 event report failed", `@0x2412864`) with the code and message.

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>", "product_code": "A17C5", "pn_payload": "<event payload>", "report_time": 1760000000 }
```

Response: no captured response; no field is read.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `DeviceFaultManager._reportEventToServer` (`business_common/msg/device_fault_manager.dart @0x2412574`), called from `_handleEventReport425` (the handler of the event message the log calls 425): the device fault manager of `business_common`, fed by incoming device messages (no UI page).

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- That `pn_payload` is the raw event payload is inferred from the name only.
- What "425" is (an event or message number of the device protocol) and the payload layout of `pn_payload` are not decoded here. — reclassified: device test row 157 (2026-10-20: event numbers of the device protocol are decided by the device, not by the app code)
- Server behaviour is not known (what the cloud does with the event: alarms, support tickets).

## Device-tested by

none
