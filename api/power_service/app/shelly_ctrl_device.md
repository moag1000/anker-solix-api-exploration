> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# shelly_ctrl_device

## Purpose

Toggles a Shelly plug: `StationEnergySystemLogic::changeShellyPlugSwitch` and the Shelly home logic call `changeShellyDeviceStatus` of the repository, and `SystemA17E2FlowChartLogic::homeLoadSwitchChanged` calls its own `changeShellyDeviceStatus`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/shelly_ctrl_device` (asm-traced) at the senders that load a `Method` object next to the URL string (pool entry `pp+0xa7e0`, `Method.post`):

- `HttpRequestControllerImpl::changeShellyDeviceStatus` (`http_request_repository_impl.dart @0x3073d34`): URL string `@0x3073dec`, method object `Method.post` (`pp+0xa7e0`) `@0x3073de4`.
- `SystemA17E2FlowChartLogic::changeShellyDeviceStatus` (`system_a17e2_flow_chart_logic.dart @0x3291774`): URL string `@0x3291884`, method object `Method.post` (`pp+0xa7e0`) `@0x329187c`.

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Both senders build a 3-pair map literal typed `<String, Object>` (`AllocateArray r2 = 12`: `charging/http/http_request_repository_impl.dart @0x3073d60`, `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart @0x32917e8`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | string (flow-chart sender); ? (repository sender) | yes | | key `http_request_repository_impl.dart @0x3073d68` in `HttpRequestControllerImpl::changeShellyDeviceStatus` (function `@0x3073d34`): store `@0x3073d78` (parameter r2); `SystemA17E2FlowChartLogic::changeShellyDeviceStatus` (`system_a17e2_flow_chart_logic.dart @0x3291774`): key `@0x32917f0`, store `@0x3291800` (parameter r2); the parameter types were not followed |
| `op_type` | string | yes | `"toggle"` | key `@0x3073d7c` and `@0x3291804`; value string literal `"toggle"` `@0x3073d88` and `@0x3291810` |
| `value` | int (Smi, w) | yes | `0` (repository sender) | repository sender: key `@0x3073d94`, `stur wzr` `@0x3073d9c` (Smi 0); flow-chart sender: key `@0x329181c`, from a bool parameter (`tst x1, #0x10` `@0x3291828`, `cset x2, eq` `@0x329182c`, `lsl x2, x2, #1` `@0x3291830`, store `@0x3291834`), so 1 when the bool is true and 0 when false |

Typing and callbacks (two-hop, asm-traced): the flow-chart sender is called by `SystemA17E2FlowChartLogic.homeLoadSwitchChanged` (`micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart @0x3291468`), which passes `field_5b` of an object with the String literal `""` as null default (`r3 = ""` `@0x3291400`) and a bool read with default `false` (`r6 = false` `@0x3291420`); so its `device_sn` is a string. The repository sender is called by `ShellyHomeLogic.changeShellyPlugSwitch` (`charging/ui/page/device/third_party_device/shelly/shellyhome/shellyhome_logic.dart @0x3074054`) and `StationEnergySystemLogic.changeShellyPlugSwitch` (`charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart @0x3073cb8`), which pass `field_6b` of an object (`@0x3074048`) with no default. Of the two callbacks of the flow-chart call, the first is a pool entry printed as the placeholder `Function: [dart:ui] _NativeScene::_NativeScene._` (`@0x3291430`) and unreadable; the second (`@0x3291fec`) loads no argument, flips a bool field of the logic (`eor x3, x2, #0x10` `@0x3292028`, `StoreField` `@0x329202c`), clears a second field (`@0x3292030`) and calls `refresh` (`@0x3292048`).

## `param_type`/`cmd`

n/a

## Response model (link)

None for the repository sender: its success callback `http_request_repository_impl.dart @0x3073ea8` loads its argument once for the log string `"changeShellyDeviceStatus success  data:"` and calls `exeSuccess()`; the failure callback `@0x3073e30` logs the code and message and calls `exeError()`. Not read for the flow-chart sender: it passes the `postJML` closure templates (`pp+0xf8de8`/`pp+0xf8df0`) that forward to callbacks of `homeLoadSwitchChanged`, which were not read.

## Response

No response key is read by the repository sender.

## Example request/response

Request, synthesized (repository sender)

```json
{"device_sn": "<device_sn>", "op_type": "toggle", "value": 0}
```

Response: none parsed by the repository sender.

## Errors seen

None traced: the repository sender's callbacks compare no code. The flow-chart sender's callbacks were not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `changeShellyDeviceStatus` @0x3073d34 (encryptionRequestHttp; encrypted: true)
- `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart`: `changeShellyDeviceStatus` @0x3291774 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::changeShellyDeviceStatus`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::changeShellyPlugSwitch`
- `charging/ui/page/device/third_party_device/shelly/shellyhome/shellyhome_logic.dart::changeShellyPlugSwitch`
- `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart::homeLoadSwitchChanged`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Type of `device_sn` in the repository sender: `field_6b` of an object (`charging/ui/page/device/third_party_device/shelly/shellyhome/shellyhome_logic.dart @0x3074048`) — attempted 2026-10-20 (two-hop not readable: both callers read it with no default and no declared type in the asm. Header stays string-only)
- Which of the two flow-chart callbacks handles success and which failure, and what the first one (an unreadable placeholder pool entry) does — traced 2026-10-20: the second callback (`system_a17e2_flow_chart_logic.dart @0x3291fec`) is described in the typing paragraph; the roles are not given by a symbol
- What the server does with `op_type` values other than `"toggle"`: the app never sends another value; with `value` always 0 on the repository path the toggle semantics are server side.

## Device-tested by

none
