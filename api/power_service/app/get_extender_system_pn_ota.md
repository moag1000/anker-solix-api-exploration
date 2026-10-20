> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_extender_system_pn_ota

## Purpose

Reads the OTA information per product number for range-extender systems (`RangeExtenderNetwork::getExtenderSystemPnOta`, `oe_a7320`); no UI caller is recorded in `data/endpoints.json`, so the purpose is inferred from the function name (string-only).

## Upstream name

`get_extender_system_pn_ota` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_extender_system_pn_ota` (asm-traced): the builder `RangeExtenderNetwork::getExtenderSystemPnOta` (`oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x22a1a68`) loads the path string at `@0x22a1a90` and calls `AkNetwork::requestHttp` (`@0x22a1a9c`); that function builds the SDK command map with the literal `"POST"` (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`) and hands it to the handler `akiot.cloud_api` (`handle`, `@0x21c3544`). There is no `Method` object on this path.

## Encrypted?

encrypted: "default-true (requestHttp) — verify". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) No request fields: the call to `AkNetwork::requestHttp` carries no named argument (`r4 = const [0, 0x1, 0, 0x1, null]` at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x22a1a98`), so no `params` map is sent by this builder.

## `param_type`/`cmd`

n/a

## Response model (link)

- `oe_a7320::ExtenderSystemPnOtaModel`, parsed by `ExtenderSystemPnOtaModel.fromJson` at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x22a1ad0`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `ExtenderSystemPnOtaModel` top-level keys (`data/models.json`, `oe_a7320::ExtenderSystemPnOtaModel`): `extender_system_relation_ota` (unknown), `ExtenderSystemPnOtaModel` (List).

## Example request/response

Request, synthesized: no params argument is passed (no body fields).

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `getExtenderSystemPnOta` @0x22a1a68 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What `AkNetwork::requestHttp` sends in `param` when its `params` argument is null (the command map stores the argument as it is, `base_service/util/ak_util/src/ak_network.dart @0x21c3518`; the SDK handler is outside the asm tree read).
- No UI caller is recorded for this builder in `data/endpoints.json`.
- Encryption: path C (`AkNetwork::requestHttp` to the SDK handler), see `api/encryption.md`; the "Encrypted?" line above is the inventory default.

## Device-tested by

none
