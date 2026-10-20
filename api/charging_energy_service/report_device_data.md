> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# report_device_data

## Purpose

Renews the MQTT subscription of the station home page ("续约", renewal) by posting the renewal parameters when the MQTT connection is up (caller `renewMqtt` of the station chart mixin; 3.18.0 asm) (the meaning is taken from the function name and log text, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_energy_service/report_device_data`, method `POST` in the 3.18.0 asm: in `renewMqtt` (`charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x1aea4e8`, 3.18.0 addresses) the method object `Instance_Method` is loaded at `@0x1aea5c8` (3.18.0 pool entry `pp+0x9b18`, enum index 1, `post`), the URL string at `@0x1aea5d0`, and the call goes through the mixin `requestHttp` (`@0x1aea5f8`; options `fail`, `isAIotErrorCode`, `success`). In 3.24.3 the URL string exists only in the object pool, so no sender can be read.

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys in 3.24.3 (no sender). In the 3.18.0 asm the body is the result of `A17b1StationLogic::mqttRenewParams` (`charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x1aea590`); its keys were not read.

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed as a model (3.18.0 asm): the success closure passed to the call (`charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x1aec490`) logs the text `StationMqttMixin 触发设备续约 177` and reads no key.

## Response

No response key is read by the app in the 3.18.0 asm (see Response model).

## Example request/response

No example: the 3.24.3 app has no sender, and the 3.18.0 body keys (`mqttRenewParams`) were not read.

## Errors seen

none traced: no 3.24.3 sender. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/station/mixin/station_chart_http_reposity.dart`: `renewMqtt` @0x1aea4e8 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present (sender read in the 3.18.0 asm, addresses above are 3.18.0 addresses). 3.24.3: string present in the object pool, no code reference found. since: <=3.18.0. `tools/out/diff_3.18.0_3.24.3.md` lists the endpoint under removed endpoints.

## Known unknowns

- Whether the server still serves this URL: the 3.24.3 app has no sender for it; the diff file lists it as removed.
- The request keys: they are built by `A17b1StationLogic::mqttRenewParams` (`charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x1aea548`), which was not read.
- How the 3.24.3 app renews the MQTT subscription: no replacement call was located.

## Device-tested by

none
