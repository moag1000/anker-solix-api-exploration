> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# save_compatible_solar

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/compatible/save_compatible_solar`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x27535e8`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

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

- `charging/http/http_request_repository_impl.dart`: `saveCompatibleSolarApi` @0x2753564 (encryptionRequestHttp; encrypted: true)

Called from: `charging/http/http_request_repository.dart::saveCompatibleSolarApi`, `charging/ui/page/device/a17c0/ez1_select_mode/ez1_select_mode_logic.dart::next`, `charging/ui/page/device/a17c0/select_brand/select_brand_logic.dart::saveSelectSolarInfo`, `charging/ui/page/device/a17c0/select_solar_power/select_solar_power_logic.dart::saveSelectSolarInfo`, `charging/ui/page/qr_Scanner/qr_scanner_logic.dart::checkDeviceSnCode`, `charging/ui/page/qr_Scanner/qr_scanner_logic.dart::saveCompatibleSolar`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
