> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# set_user_params

## Purpose

Writes user-level parameters: the personalization options page (`PersonalizationOptionsLogic::setPersonalizationOptionsStatus`) calls `setPersonalizationOptionsApi`; the EV charger code writes the driving plan through `ScheduleNetwork::_setUserParams` (`setDrivingPlan`) and `AKIotEVChargeCommand::setUserParams` (`EvChargerUserParams::setUserParam`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/user/set_user_params` for the first sender (asm-traced): URL string `about_http_request_repository_impl.dart @0x4036440`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x4036438`, in `AboutHttpRequestControllerImpl::setPersonalizationOptionsApi` (`@0x4036308`). `AKIotEVChargeCommand::setUserParams` (`ev_charge_command.dart @0x405be14`) puts the path `"power_service/v1/app/user/set_user_params"` (`@0x405be6c`) and the string literal `"POST"` (`@0x405be84`) into a command map for `akIoTKitManager.handle` (`@0x405bf1c`). `ScheduleNetwork::_setUserParams` (`%20schedule_network.dart @0x39682d4`) calls its own `_requestHttp` helper with the path (`@0x3968388`); its method was not read.

## Encrypted?

encrypted: "default-true (requestHttp) — verify" / `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Three senders, each with a `params` object.

| field | type | required | example | source |
|---|---|---|---|---|
| `params` | object | yes | | `setPersonalizationOptionsApi`: key `@0x403637c`, outer map typed `<String, Map<String, bool>>` (`@0x40363f0`, pool `pp+0x36f90`), value store `@0x40363cc` |
| `params.<code>` | bool | yes | `true` | inner map typed `<String, bool>` (`@0x40363b8`, pool `pp+0x9f90`): the key is `60002.toString()` (`r16 = 60002` `@0x4036388`, tagged Smi, so `"30001"`) and the value is a bool parameter (store `@0x40363b4`) |
| `params.driving_plan` | ? | yes | | `ScheduleNetwork::_setUserParams`: inner map typed `<String, Map<String, dynamic>>` (`@0x396833c`), key `@0x3968328`, value store `@0x3968338` (parameter at `fp-0x10`) |
| `params` | object | yes | | `AKIotEVChargeCommand::setUserParams`: key `@0x405bea8` inside the `param` map typed `<String, Map<String, dynamic>>` (`@0x405bebc`) |

Method of the schedule sender (asm-traced): `ScheduleNetwork::_requestHttp` (`schedule_network.dart @0x284f6d0`, the same helper for both schedule calls) stores the String literal `"POST"` as `method` (`@0x284f74c`, key `@0x284f740`) next to `path` (`@0x284f730`) and `param` (`@0x284f758`) and calls `handle` with `akiot.cloud_api` (`@0x284f780`, call `@0x284f790`); see [sdk_senders.md](../../../sdk_senders.md#schedulenetwork_requesthttp).

## `param_type`/`cmd`

n/a

## Response model (link)

None for the first sender: the response body is not parsed there. Its success callback is the forwarding template `http_request_repository_impl.dart @0x261b9a0` (a constant `true`) and its failure callback the template `@0x226824c`. Not read for the other two senders.

## Response

No response key is read by the first sender.

## Example request/response

Request, synthesized (first sender)

```json
{"params": {"30001": "<bool>"}}
```

Response: none parsed by the first sender.

## Errors seen

None traced for the first sender (no compare in its callbacks). The other senders' callbacks were not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/user/about/about_http_request_repository_impl.dart`: `setPersonalizationOptionsApi` @0x4036308 (encryptionRequestHttp; encrypted: true)
- `ev_charger/src/ev_charger/page/home/schedule_charge/network/%20schedule_network.dart`: `_setUserParams` (`schedule_network.dart @0x39682d4`; _requestHttp; encrypted: default-true (requestHttp) — verify)
- `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`: `setUserParams` @0x405be14 (URL literal only, no `*Http*` call; sends in the same function (`AKIoTKitManagerImpl::handle`); resolved from the URL literal at `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x405be6c` (string-only: the sender was found by following callers; it may send other URLs too — see tools/README.md))

Called from:

- `charging/ui/page/user/about/personalizationOptions/personalization_options_logic.dart::setPersonalizationOptionsStatus`
- `ev_charger/src/ev_charger/base/ev_charger_user_params.dart::setUserParam`
- `ev_charger/src/ev_charger/page/home/schedule_charge/network/%20schedule_network.dart::setDrivingPlan`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- The `driving_plan` value and the IoT-kit `params` content (parameters). Header stays string-only. — traced 2026-10-20: not decoded in this pass (`driving_plan` value and IoT-kit `params`); the reason given in the bullet stands
- What option code 30001 means (see [get_user_params](get_user_params.md)). — reclassified: server (the option code meaning is defined by the server)
- The callers' handling of the answer of `ScheduleNetwork::_setUserParams` (`schedule_network.dart @0x39682d4`) — traced 2026-10-20: the method is `"POST"` (see Request); the callers were not read for the answer

## Device-tested by

none
