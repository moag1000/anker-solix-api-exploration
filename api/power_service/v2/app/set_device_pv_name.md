> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# set_device_pv_name

## Purpose

Renames one PV input of a device: the app sends the device serial, the key of the PV input and the new name typed by the user.

## Upstream name

`none` for the key; upstream lists the URL without a key in `api/apitypes.py` (line 348).

## Method+URL

`POST /power_service/v2/app/set_device_pv_name` (asm-traced): URL literal `@0x2f3adbc` in `requestRenamePV` (`ats_ax170/src/ats_ax170/page/station/system_ax170_flow_chart_controller.dart @0x2f3ac50`), method object `Method.post` (pool entry `pp+0xa7e0`, `@0x2f3adb4`).

## Encrypted?

Yes by wrapper (asm-traced): ``requestRenamePV`` calls `encryptionRequestHttp` (`ats_ax170/src/ats_ax170/page/station/system_ax170_flow_chart_controller.dart @0x2f3ade4`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../../encryption.md)); asm alone does not decide it. The loading overlay is on (`r30 = true`, `@0x2f3adcc`).

## Request

Map literal with three string pairs, `<String, String>` (`r2 = 12`, `@0x2f3ac90`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `"<device sn>"` | `ats_ax170/src/ats_ax170/page/station/system_ax170_flow_chart_controller.dart @0x2f3ac9c`; value is the first field of the argument object (`@0x2f3acac`), empty string if null (`@0x2f3acbc`) |
| `pv_key` | String | yes | `"pv1_name"` | `@0x2f3acc4`; value is the second field of the argument object (`@0x2f3acd0`), empty string if null (`@0x2f3ace0`); the example is a guess from the attribute names `pv1_name` to `pv4_name` of the `Attributes` class in `s1_s2_http.dart` |
| `pv_name` | String | yes | `"Garage roof"` | `@0x2f3acec`; the `trim()` of the text of the edit field (`@0x2f3ad18`) |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed.

## Response

No response field is read (asm-traced). The success closure (`ats_ax170/src/ats_ax170/page/station/system_ax170_flow_chart_controller.dart @0x2f3aef0`) logs `requestRenamePV success` (`@0x2f3af38`) and fires a `MessageEvent` (`@0x2f3afa0`) so that the page refreshes; the failure closure (`@0x2f3ae04`) logs `requestRenamePV fail`.

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>", "pv_key": "pv1_name", "pv_name": "Garage roof" }
```

Response: no captured response; no field is read.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `requestRenamePV` (`ats_ax170/src/ats_ax170/page/station/system_ax170_flow_chart_controller.dart @0x2f3ac50`), called from `system_ax170_flow_chart.dart` (`_editPvName`): the system flow chart of the AX170 (ATS) station page (package `ats_ax170`), the rename dialog of a PV input.

## Since/changed

3.18.0: present (the URL string is in the 3.18.0 pool and the sender file `ats_ax170/.../system_ax170_flow_chart_controller.dart` holds the keys `device_sn`, `pv_key`, `pv_name`). 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- Which PV keys exist (`pv_key` values) is not known beyond the example.
- Server behaviour (name length limits, whether the name appears in other apps) is not known.

## Device-tested by

none
