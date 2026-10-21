> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_home_load_chart

## Purpose

Reads the home-load chart of a site: `EnergyPlanLogic::getSiteHomeLoadChatDate` (A17C1), `EnergyHomeController::getSiteHomeLoadChatDate` and `MergeSystemEnergyPlanLogic::getSiteHomeLoadChatDate` call `getSiteHomeLoadChat`.

## Upstream name

`home_load_chart` in `API_ENDPOINTS` of `api/apitypes.py` (upstream-confirmed).

## Method+URL

`POST /power_service/v1/site/get_home_load_chart` (asm-traced): URL string at `http_request_repository_impl.dart @0x28cced0`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x28ccec8`, in `HttpRequestControllerImpl::getSiteHomeLoadChat` (`http_request_repository_impl.dart @0x28cce04`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 2-pair map literal typed `<String, String>` (type arguments `@0x28cce84`) built in `getSiteHomeLoadChat` (`http_request_repository_impl.dart @0x28cce04`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | `"<site_id>"` | key `@0x28cce5c`, value store `@0x28cce6c` (parameter at `fp-0x20`) |
| `device_sn` | string | yes | `""` | key `@0x28cce70`, literal empty string `@0x28cce7c`, store `@0x28cce80` |

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::HomeLoadChat` (`data/models.json` key; fields on [`models/other.md`](../../../models/other.md#homeloadchat)), parsed in the success closure `http_request_repository_impl.dart @0x28ccf14` by `HomeLoadChat.fromJson`.

## Response

The model has the single top-level key `data` (`List<ChatData>`). `ChatData` (`charging/ui/page/device/main/sitation_energy_mian/energy_home/state/state.dart`, `ChatData.fromJson` `@0x28cd450`, `data/models.json`, `charging::ChatData`) has the keys `time` (String, nullable) and `load` (declared `unknown`).

## Example request/response

Request, synthesized (decrypted body as built by `getSiteHomeLoadChat`)

```json
{"site_id": "<site_id>", "device_sn": ""}
```

Response keys: see Response; no capture.

## Errors seen

None traced: the builder passes the `postJML` failure template (`charging/http/http_request_repository_impl.dart @0x226824c`); the callers' failure callbacks were not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getSiteHomeLoadChat` @0x28cce04 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::getSiteHomeLoadChat`
- `charging/ui/page/device/a17c1/energy_plan/energy_plan_logic.dart::getSiteHomeLoadChatDate`
- `charging/ui/page/device/main/sitation_energy_mian/energy_home/controller/energy_home_controller.dart::getSiteHomeLoadChatDate`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/merge_system_energy/merge_system_energy_plan_logic.dart::getSiteHomeLoadChatDate`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta. The model `HomeLoadChat` is `≤3.18.0` in `data/models.json`.

## Known unknowns

- Whether the server uses `device_sn` when it is non-empty: the app always sends the empty string.
- Failure handling in the callers was not read. — traced 2026-10-20: the call sites pass no `fail` closure among their named arguments: `EnergyPlanLogic.getSiteHomeLoadChatDate` (`charging/ui/page/device/a17c1/energy_plan/energy_plan_logic.dart @0x28ccd58`): no named argument; `EnergyPlanLogic.getCacheHomeCrossData` (`charging/ui/page/device/a17c1/energy_plan/energy_plan_logic.dart @0x28d1094`): no named argument; `EnergyHomeLogic.getSiteHomeLoadChatDate` (`charging/ui/page/device/main/sitation_energy_mian/energy_home/controller/energy_home_controller.dart @0x34de924`): named arguments `showLoading`; `MergeSystemEnergyPlanLogic.getSiteHomeLoadChatDate` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/merge_system_energy/merge_system_energy_plan_logic.dart @0x28f9b38`): no named argument; `MergeSystemEnergyPlanLogic.getCacheHomeCrossData` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/merge_system_energy/merge_system_energy_plan_logic.dart @0x28fd610`): no named argument. Failure then falls to the callee's default or to the awaiting code, neither of which was read

## Device-tested by

none
