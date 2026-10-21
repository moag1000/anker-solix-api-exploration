> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_extender_system_pn_ota

## Purpose

Reads the OTA information per product number for range-extender systems (`RangeExtenderNetwork::getExtenderSystemPnOta`, `oe_a7320`); the callers are listed under "Callers in app"; the description itself comes from the function name (string-only).

## Upstream name

`get_extender_system_pn_ota` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_extender_system_pn_ota` (asm-traced): the builder `RangeExtenderNetwork::getExtenderSystemPnOta` (`oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x22a1a68`) loads the path string at `@0x22a1a90` and calls `AkNetwork::requestHttp` (`@0x22a1a9c`); that function builds the SDK command map with the literal `"POST"` (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`) and hands it to the handler `akiot.cloud_api` (`handle`, `@0x21c3544`). There is no `Method` object on this path.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork::requestHttp`: the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory flag `default-true (requestHttp)` does not apply: `AkNetwork::requestHttp` has no `needEncryption` switch and goes straight to the SDK; what the SDK encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). The builder calls the helper at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x22a1a9c`.

## Request

(asm-traced) No request fields: the call to `AkNetwork::requestHttp` carries no named argument (`r4 = const [0, 0x1, 0, 0x1, null]` at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x22a1a98`), so no `params` map is sent by this builder; `AkNetwork::requestHttp` declares `params` as `{dynamic params = Null}` (`SetupParameters`, `base_service/util/ak_util/src/ak_network.dart @0x21c3450`) and stores the argument unchanged under `param` in the command map (`@0x21c3518`), so the map handed to the SDK handler carries `param: null` here (app side; how the native SDK serialises it is outside the asm).

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

- `RangeExtenderChecker.needOta` (`oe_a7320/src/oe_a7320/page/range_extender_system/tools/range_extender_checker.dart @0x229cf74`)
- `ReSystemBiz._getSupportDeviceModels` (`oe_a7320/src/oe_a7320/biz/re_system_biz.dart @0x286899c`)
- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `getExtenderSystemPnOta` @0x22a1a68 (`AkNetwork.requestHttp`, path C)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What `AkNetwork::requestHttp` sends in `param` when its `params` argument is null (the command map stores the argument as it is, `base_service/util/ak_util/src/ak_network.dart @0x21c3518`). — reclassified: server (not visible in the app: the SDK handler is outside the dumped Dart code)
- The element types behind `extender_system_relation_ota` and the list key `ExtenderSystemPnOtaModel` (`unknown` and `List` without an element class in `data/models.json`). — reclassified: server (not visible in the app: the model keeps both untyped)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
