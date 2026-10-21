> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_site_device_disaster

## Purpose

Reads the disaster-preparedness (backup power) switches of a site for the A17E2 flow chart (caller `SystemA17E2FlowChartLogic::_fetchDisasterSetting`, started from `onInit` and from an event-bus listener) (asm-traced for the call; the meaning of the switches is taken from the model key names, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_disaster_prepared/get_site_device_disaster` (asm-traced): URL string `@0x35614c0`, method object `Method.post` (pool entry `pp+0xa7e0`) `@0x35614b8`, in `SystemA17E2FlowChartLogic::_fetchDisasterSetting` (`micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart @0x3561310`), sent through `HttpServiceImpl::encryptionRequestHttp` (`@0x35614e8`). The call is skipped, with a log line, when the site id string is empty (`cbnz` `@0x35613cc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(string-only: one field type is not read) One sender. The map literal has the type arguments `<String, Object>` (`micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart @0x3561474`), which name no value type.

| field | type | required | example | source |
|---|---|---|---|---|
| `type` | int (Smi, w) | yes | `2` (raw immediate 4, 32-bit store) | `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart @0x3561450` (value store `@0x356145c`, constant `@0x3561458`) |
| `identifier_id` | ? | yes | `"<site_id>"` | `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart @0x3561460` (value from the current station model, `LoadField` `@0x35613b4`, store `@0x3561470`) |

## `param_type`/`cmd`

n/a

## Response model (link)

`base_service::DisasterSetting` (no `models/` page), parsed by `DisasterSetting.fromJson` at `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart @0x3561660` in the success closure `@0x35615bc` of `_fetchDisasterSetting`.

## Response

(asm-traced for the model) Top-level keys of `DisasterSetting` (`data/models.json`, `base_service::DisasterSetting`): `auto_disaster_switch` (bool), `manual_disaster_switch` (bool), `disaster_details` (int). The success closure copies the parsed values into the scene model and logs the old and new `manualDisasterSwitch` and `autoDisasterSwitch` (`micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart @0x35616d4`, `@0x3561710`); it adds no wrapper field.

## Example request/response

Request, synthesized (decrypted body as built by `_fetchDisasterSetting`; `<...>` are placeholders, not captured values)

```json
{
  "type": 2,
  "identifier_id": "<site_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page (the failure closure `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart @0x3561544` logs `code=` and `msg=`). Code meanings are owned by `api/errors.md`.

## Callers in app

- `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart`: `_fetchDisasterSetting` @0x3561310 (encryptionRequestHttp; encrypted: true)

Called from:

- `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart::_setupEventBusListener`
- `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart::onInit`

## Since/changed

3.18.0: absent. 3.24.3: present (listed under added endpoints in `tools/out/diff_3.18.0_3.24.3.md`). since: 3.24.3.

## Known unknowns

- Type of `identifier_id`: a value loaded from a station model field whose declared type is not visible. — attempted 2026-10-20 (two-hop not readable: the sender is in a closure of `SystemA17E2FlowChartLogic` (`micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart @0x35614c0`) and the station model field behind `identifier_id` has no declaration in the asm)
- Which other `type` values exist: the app stores the constant 2 here; `type` 1 appears in the removed 3.18.0 senders of the sibling endpoints (see [clear](clear.md)). What the numbers select on the server is not known.
- What `disaster_details` encodes (int): only the class field is listed; no reader was followed. — reclassified: server (2026-10-20: the app class holds the integer; its meaning is not derivable here)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
