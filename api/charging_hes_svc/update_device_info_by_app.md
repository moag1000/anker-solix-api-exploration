> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# update_device_info_by_app

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_svc/update_device_info_by_app`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart @0x23b07e4`
(literal also at 1 more site(s) in `data/endpoints.json`)

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys found by the extractor. <!-- TODO -->

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart`: `_handleNewOtaVersion` @0x23b06a0 (requestHttp; encrypted: default-true (requestHttp) — verify); `_updateVersionInfo` @0x23b895c (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from: `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart::_handleOTAVersion`, `charging/ui/page/device/a5101/ota/a5101_mqtt_logic.dart::_listenEvenBus`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
