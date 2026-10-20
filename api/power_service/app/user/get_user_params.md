> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# get_user_params

## Purpose

Reads user-level parameters: the personalization options page (`PersonalizationOptionsLogic::requestPersonalizationOptionsStatus`) calls `getPersonalizationOptionsApi`; the EV charger code reads the same URL from the schedule network (`ScheduleNetwork::_getUserParams`, called by `getDrivingPlan`) and from the IoT-kit command `AKIotEVChargeCommand::getUserParams` (`EvChargerUserParams::getUserParamFromServer`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/user/get_user_params` for the first sender (asm-traced): URL string `about_http_request_repository_impl.dart @0x298e914`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x298e90c`, in `AboutHttpRequestControllerImpl::getPersonalizationOptionsApi` (`@0x298e7d8`). The IoT-kit sender `AKIotEVChargeCommand::getUserParams` (`ev_charge_command.dart @0x2700a98`) puts the path `"power_service/v1/app/user/get_user_params"` (`@0x2700b20`, no leading slash) and the string literal `"POST"` (`@0x2700b38`) into a command map for `akIoTKitManager.handle` (`@0x2700b7c`). `ScheduleNetwork::_getUserParams` (`%20schedule_network.dart @0x2850430`) calls its own `_requestHttp` helper with the path `"power_service/v1/app/user/get_user_params"` (`@0x28504c8`); the method it uses was not read.

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Three senders.

| field | type | required | example | source |
|---|---|---|---|---|
| `params` | list | yes | `["30001"]` | `getPersonalizationOptionsApi`: key `@0x298e844`, map typed `<String, List<String>>` (`@0x298e8c4`), one element `60002.toString()` (`r16 = 60002` `@0x298e850`, tagged Smi, so 30001, `toString` `@0x298e858`) in a `<String>` list (`@0x298e87c`), list store `@0x298e8a0` |
| `params` | ? | yes | | `ScheduleNetwork::_getUserParams`: `<String, dynamic>` map, key `@0x2850470`, store `@0x2850480` (parameter at `fp-0x10`) |
| `device_sn` | ? | optional | | `ScheduleNetwork::_getUserParams`: key `@0x28504b0`, `[]=` `@0x28504b8`; added when the parameter at `fp-0x18` is non-null (`cmp w3, NULL` `@0x285049c`) |
| `params` | object | yes | | `AKIotEVChargeCommand::getUserParams`: key `@0x2700ac4` inside the `param` map; its value type was not read |

Method of the schedule sender (asm-traced): `ScheduleNetwork::_requestHttp` (`schedule_network.dart @0x284f6d0`, the same helper for both schedule calls) stores the String literal `"POST"` as `method` (`@0x284f74c`, key `@0x284f740`) next to `path` (`@0x284f730`) and `param` (`@0x284f758`) and calls `handle` with `akiot.cloud_api` (`@0x284f780`, call `@0x284f790`); see [sdk_senders.md](../../../sdk_senders.md#schedulenetwork_requesthttp).

## `param_type`/`cmd`

n/a

## Response model (link)

`charging::ParamsModel` for the first sender (`data/models.json` key, no model page), parsed in the success closure `about_http_request_repository_impl.dart @0x298e960` by `ParamsModel.fromJson` (resolves to `charging/model/about/param_model.dart`). Not read for the other two senders.

## Response

Top-level key of `ParamsModel` (from `data/models.json`): `params` (Map).

Option 30001 (asm-traced): the sender `getPersonalizationOptionsApi` is called from `PersonalizationOptionsLogic.requestPersonalizationOptionsStatus` (`charging/ui/page/user/about/personalizationOptions/personalization_options_logic.dart @0x298e7b0`). Its success closure (`@0x298eb98`, parameter type `ParamsModel`) reads the field at offset 0x7 of the parameter (`@0x298ebc4`) and looks up the key `60002.toString()` (`r16 = 60002` `@0x298ebd0`, tagged, so `"30001"`; `_getValueOrData` `@0x298ebe4`), takes `false` when the key is missing (`cmp w0, NULL` `@0x298ec0c`, `r4 = false` `@0x298ec14`), checks the value is a `bool` (`@0x298ec4c` to `@0x298ec58`) and passes `"true"` or `"false"` (`@0x298ec70`, `@0x298ec78`) to `updateSwitch` (`@0x298ec7c`). Option 30001 is therefore the one switch of the personalization options page, whose title string is `personalizationOptionsTitle` (`charging/ui/page/user/about/personalizationOptions/personalization_options_page.dart @0x4035b28`); the answer is a map from option code to bool.

## Example request/response

Request, synthesized (first sender)

```json
{"params": ["30001"]}
```

Response keys: see Response; no capture.

## Errors seen

None traced. The first sender's failure callback is the forwarding template `http_request_repository_impl.dart @0x226824c`; the other senders' callbacks were not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/user/about/about_http_request_repository_impl.dart`: `getPersonalizationOptionsApi` @0x298e7d8 (encryptionRequestHttp; encrypted: true)
- `ev_charger/src/ev_charger/page/home/schedule_charge/network/%20schedule_network.dart`: `_getUserParams` (`schedule_network.dart @0x2850430`; _requestHttp; encrypted: default-true (requestHttp) — verify)
- `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`: `getUserParams` @0x2700a98 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x2700b20` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

Called from:

- `charging/ui/page/user/about/personalizationOptions/personalization_options_logic.dart::requestPersonalizationOptionsStatus`
- `ev_charger/src/ev_charger/base/ev_charger_user_params.dart::getUserParamFromServer`
- `ev_charger/src/ev_charger/page/home/schedule_charge/network/%20schedule_network.dart::getDrivingPlan`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- The `params` and `device_sn` types of the schedule sender and the `param` map of the IoT-kit sender (parameters). Header stays string-only. — attempted 2026-10-20 (two-hop not readable: `ScheduleNetwork::_getUserParams` receives `params` and `device_sn` as untyped parameters (`schedule_network.dart @0x2850430`); its callers were not followed. Header stays string-only)

## Device-tested by

none
