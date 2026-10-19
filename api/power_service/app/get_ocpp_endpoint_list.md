> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# get_ocpp_endpoint_list

## Purpose

<!-- TODO -->

## Upstream name

`get_ocpp_endpoint_list` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`/power_service/v1/app/get_ocpp_endpoint_list`, method: not extracted by the inventory <!-- TODO -->; string-only: `ev_charger/src/ev_charger/page/home/setting/ocpp/network/ocpp_network.dart @0x284a5ac`

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

- `ev_charger/src/ev_charger/page/home/setting/ocpp/network/ocpp_network.dart`: `getOcppEndpointList` @0x284a584 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
