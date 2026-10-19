> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# report_device_data

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_energy_service/report_device_data`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/page/station/mixin/station_chart_http_reposity.dart @0x1aea5d0`

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

- `charging/ui/page/station/mixin/station_chart_http_reposity.dart`: `renewMqtt` @0x1aea4e8 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: string present in the object pool, no code reference found. since: ≤3.18.0.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
