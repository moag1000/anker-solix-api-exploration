> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# report_device_data

## Purpose

Renews the MQTT subscription of the station home page ("续约", renewal) by posting the renewal parameters when the MQTT connection is up (caller `renewMqtt` of the station chart mixin; 3.18.0 asm) (the meaning is taken from the function name and log text, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_energy_service/report_device_data`, method `POST` in the 3.18.0 asm: in `renewMqtt` (`charging/ui/page/station/mixin/station_chart_http_reposity.dart 0x1aea4e8`, 3.18.0 addresses) the method object `Instance_Method` is loaded at `0x1aea5c8` (3.18.0 pool entry `pp+0x9b18`, enum index 1, `post`), the URL string at `0x1aea5d0`, and the call goes through the mixin `requestHttp` (`0x1aea5f8`; options `fail`, `isAIotErrorCode`, `success`). In 3.24.3 the URL string exists only in the object pool, so no sender can be read.

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The sender body is not in the 3.24.3 dump (see Callers in app). In the 3.18.0 asm the body is the result of `A17b1StationLogic::mqttRenewParams` (`charging/ui/page/station/mixin/station_chart_http_reposity.dart 0x1aea590`); its keys are listed below.

Body keys (traced 2026-10-20): the builder `A17b1StationLogic::mqttRenewParams` is present in both trees (3.18.0 `charging/ui/page/station/A17b1/a17b1_station_logic.dart 0x1aec3a4`, 3.24.3 `@0x2409680`) and builds a `<String, Object>` literal of three pairs (array length raw 12, `@0x24096cc`): `siteIds`, a growable list with the type argument `<String>` and one element, the id of the current station (`getCurrentStation()` field `field_7` with the fallback `""`, 3.18.0 `0x1aec3d0`..`0x1aec3e4`, list `0x1aec424`), `ctrol` (sic, one `l`; raw immediate 2 in a 32-bit array slot, Smi 1; 3.24.3 `@0x2409724`, `@0x2409730`) and `duration` (raw 600, Smi 300; 3.24.3 `@0x2409738`, `@0x2409740`). The method is POST (3.18.0 `Obj!Method@2c736e1`, name `post`, see Method+URL).

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed as a model (3.18.0 asm): the success closure passed to the call (`charging/ui/page/station/mixin/station_chart_http_reposity.dart 0x1aec490`) logs the text `StationMqttMixin 触发设备续约 177` and reads no key.

## Response

No response key is read by the app in the 3.18.0 asm (see Response model).

## Example request/response

No example: the 3.24.3 sender body is not in the dump; the body keys are listed under Request.

## Errors seen

none traced: no 3.24.3 sender. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/station/mixin/station_chart_http_reposity.dart`: `renewMqtt` 0x1aea4e8 (3.18.0) (requestHttp; encrypted: default-true (requestHttp) — verify)

3.24.3 callers (traced 2026-10-20): the 3.24.3 dump holds no body for `renewMqtt` (it is a mixin-deduplicated function, like the sender of several other pages), but the app still calls it: `charging/ui/page/station/A17b1/a17b1_station_logic.dart @0x2407658`, `charging/ui/page/station/view/station_house.dart @0x28192b0`, `@0x28192f4` and, through `_renewMqttIfNeeded` (`station_house.dart @0x2bcb05c`, called at `@0x2bcafb8`), `@0x2bcb0a4`, `@0x2bcb110`. The builder of the body (`mqttRenewParams`) also stays in 3.24.3. So the app very likely still sends this request; the "removed" entry of the diff file is an artifact of the dump (the string load sits in the missing function).

## Since/changed

3.18.0: present (sender read in the 3.18.0 asm, addresses above are 3.18.0 addresses). 3.24.3: string present in the object pool, no code reference found. since: <=3.18.0. `tools/out/diff_3.18.0_3.24.3.md` lists the endpoint under removed endpoints.

## Known unknowns

- Whether the server still serves this URL: the 3.24.3 app still calls `renewMqtt` (see Callers in app), although the diff file lists the URL as removed; what the server does is not known from the app.
- The unit of `duration` (Smi 300) and the meaning of `ctrol` 1: the asm shows only the constants (3.24.3 `charging/ui/page/station/A17b1/a17b1_station_logic.dart @0x2409730`, `@0x2409740`) — traced 2026-10-20 (request keys read, see Request)
- How often `_renewMqttIfNeeded` triggers the renewal (the condition in `charging/ui/page/station/view/station_house.dart @0x2bcb05c` region was not decoded) — traced 2026-10-20: the renewal call is still present (see Callers in app)

## Device-tested by

none
