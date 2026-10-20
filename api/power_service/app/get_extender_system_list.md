> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_extender_system_list

## Purpose

Lists the range-extender systems with their devices (`RangeExtenderNetwork::getRangeExtenderSystemsDevicesList`, `oe_a7320`); the callers are listed under "Callers in app"; the description itself comes from the function name (string-only).

## Upstream name

`get_extender_system_list` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/app/get_extender_system_list` (asm-traced): the builder `RangeExtenderNetwork::getRangeExtenderSystemsDevicesList` (`oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x22a385c`) loads the path string at `@0x22a3884` and calls `AkNetwork::requestHttp` (`@0x22a3890`); that function builds the SDK command map with the literal `"POST"` (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`) and hands it to the handler `akiot.cloud_api` (`handle`, `@0x21c3544`). There is no `Method` object on this path.

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork::requestHttp`: the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory flag `default-true (requestHttp)` does not apply: `AkNetwork::requestHttp` has no `needEncryption` switch and goes straight to the SDK; what the SDK encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)). The builder calls the helper at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x22a3890`.

## Request

(asm-traced) No request fields: the call to `AkNetwork::requestHttp` carries no named argument (`r4 = const [0, 0x1, 0, 0x1, null]` at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x22a388c`), so no `params` map is sent by this builder; `AkNetwork::requestHttp` declares `params` as `{dynamic params = Null}` (`SetupParameters`, `base_service/util/ak_util/src/ak_network.dart @0x21c3450`) and stores the argument unchanged under `param` in the command map (`@0x21c3518`), so the map handed to the SDK handler carries `param: null` here (app side; how the native SDK serialises it is outside the asm).

## `param_type`/`cmd`

n/a

## Response model (link)

- `oe_a7320::RangeExtenderSystemsModel`, parsed by `RangeExtenderSystemsModel.fromJson` at `oe_a7320/src/oe_a7320/network/range_extender_network.dart @0x22a38c4`

## Response

(asm-traced) For each sender that parses a model, the keys below are the top-level keys of the model; that sender adds no wrapper fields of its own in the code read.

- `RangeExtenderSystemsModel` top-level keys (`data/models.json`, `oe_a7320::RangeExtenderSystemsModel`): `range_extender_systems` (unknown).

## Example request/response

Request, synthesized: no params argument is passed (no body fields).

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `ReSystemDeviceListManager.loadData` (`oe_a7320/src/oe_a7320/page/generator_pps_cards/re_system_device_list_manager.dart @0x228b168`)
- `ReSystemBiz.reSystemInfoFromCloud` (`oe_a7320/src/oe_a7320/biz/re_system_biz.dart @0x365488c`)
- `ReSystemBiz.updateReSystemsModel` (`oe_a7320/src/oe_a7320/biz/re_system_biz.dart @0x3a2340c`)
- `oe_a7320/src/oe_a7320/network/range_extender_network.dart`: `getRangeExtenderSystemsDevicesList` @0x22a385c (`AkNetwork.requestHttp`, path C)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns


## Device-tested by

none
