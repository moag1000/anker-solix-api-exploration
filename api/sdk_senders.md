> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# SDK direct senders (path C)

This page owns what the endpoint pages of the EV charger, group-device, installer-sharing and Anka groups say once instead of repeating it: how several Dart helpers send a request straight through the IoT kit SDK, without any `requestHttp` or `encryptionRequestHttp` wrapper. The encryption background is in [encryption.md](encryption.md); the endpoint pages link here for the sender mechanics and keep only their own `param` body.

## Contents

1. [Path C sender list](#path-c-sender-list)
2. [The common envelope](#the-common-envelope)
3. [AKIotEVChargeCommand (EV charger command map)](#akiotevchargecommand-ev-charger-command-map)
4. [AkNetwork.requestHttp](#aknetworkrequesthttp)
5. [ScheduleNetwork._requestHttp](#schedulenetwork_requesthttp)
6. [Response typing and the model registry](#response-typing-and-the-model-registry)
7. [Reading the inventory rows](#reading-the-inventory-rows)
8. [Known unknowns](#known-unknowns)

## Path C sender list

This page owns the list of senders that reach the SDK without a `*Http*` wrapper (path C of [encryption.md](encryption.md#which-calls-are-encrypted)); [encryption.md](encryption.md) keeps the three-path rule and the counts. Tag: asm-traced.

| sender | file `@0xADDR` of the function | `handle` call | section |
|---|---|---|---|
| `AkNetwork.requestHttp` | `base_service/util/ak_util/src/ak_network.dart @0x21c3444` | `@0x21c3544` (`AKIoTKitManagerImpl.handle`) | [below](#aknetworkrequesthttp) |
| `StationApiClient.request` | `station_home/src/http/station_api_client.dart @0x2a4435c` | `@0x2a444c0` (`AkIotKitFlutter.handle`) | not covered further here |
| `ScheduleNetwork._requestHttp` | `ev_charger/src/ev_charger/page/home/schedule_charge/network/ schedule_network.dart @0x284f6d0` | `@0x284f790` | [below](#schedulenetwork_requesthttp) |
| `AKIotEVChargeCommand` static functions | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` (38 sends, one per function) | in the function that holds the URL literal | [below](#akiotevchargecommand-ev-charger-command-map) |
| `AKIotAX170Command` static functions and their closures | `ats_ax170/src/sdk/command/ax170_command.dart` | in the function or closure that holds the URL literal | same envelope |
| direct `handle` calls in UI logic | for example `TextInfoDialogLogic._setElectricianInfo`, `getElectricianInfo` (`base_service/view/text_info_dialog/text_info_dialog_logic.dart`) | next to the URL literal | same envelope |

## The common envelope

All senders on this page call `AKIoTKitManagerImpl.handle<T>` (`base_service/ak_iot_kit/ak_iot_kit_manager_impl.dart @0x21c3a94`, signature `handle<Y0>(manager, String, Map<String, dynamic>, {allowIntercept, openTransaction})`, returns `Future<IoTAKResult<Y0>>`) with the identifier string `"akiot.cloud_api"` and a map of three keys (asm-traced):

| key | value | source |
|---|---|---|
| `path` | the URL path without a leading slash, for example `power_service/v1/app/order/get_charging_order_list`; one literal keeps its slash (`/power_service/v1/app/vehicle/add_vehicle`) | `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart @0x3394790` (no slash), `@0x3983efc` (slash) |
| `method` | the string `"POST"` | `ev_charge_command.dart @0x33947a8` |
| `param` | the request body of the endpoint page (a `Map<String, dynamic>`; the endpoint pages list its keys) | `ev_charge_command.dart @0x33947b4` and following |

`handle` stores `isOpenTransactionLock` and `allowIntercept: true` in a settings map (`ak_iot_kit_manager_impl.dart @0x21c3bc0`, `@0x21c3bd4`), builds the SDK parameters with `_processParams` (`@0x21c3cb4`), and forwards them to `AkIotKitFlutter.handle` (`@0x21c3d4c`); the SDK sends the request natively. Which headers and which body encryption the SDK applies is not visible in Dart (the SDK is native); [encryption.md](encryption.md#which-calls-are-encrypted) lists these senders as "path C" (`AkNetwork`, `ScheduleNetwork`, and the direct `handle` calls). The inventory flag `encrypted: false` on such rows only means that no `*Http*` wrapper is called ([encryption.md](encryption.md#rule-and-resulting-counts)); it does not say the request is plain.

## AKIotEVChargeCommand (EV charger command map)

`AKIotEVChargeCommand` (abstract class, class id 4446, file `ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart`, package `ev_charger`) is a bag of static functions. Of its 62 static functions, 38 call `handle` with `"akiot.cloud_api"` (cloud requests, counted from the string loads, for example `@0x339489c`), one calls `handle` with `"akiot.device.fetch_device_fault_info"` (`getUserFloatingFaultInfo`, `@0x2c67324`) and one with `"akiot.product.fetch_kvconfig"` (`fetchEvChargerKVConfig`, `@0x29e3288`); the other functions write device properties through `writeProperty` with the property name `prop_write_evcharger` (for example `setBrightness`, `@0x2cdd8ec`) and are device commands outside the scope of this page. A cloud function:

1. loads the static `akIoTKitManager` (static field `0x196c`; for example `@0x3394754`),
2. builds the `path`, `method` and `param` map (array length 12 means three pairs, `r2 = 12`, `@0x3394778`),
3. calls `handle<ResponseModel>` and returns the future (for example `@0x33948ac`).

The function does not parse the answer itself; the UI logic that awaits the future reads the `IoTAKResult` (a result-type enum compared with an `AKResultType` instance, and the data). Because the sender is inside the call-map function, the inventory (`data/endpoints.json`) lists these URLs as `url_provider` rows with the pseudo request keys `path`, `method`, `param`; those three keys are the envelope above, not request fields.

The UI callers of a function are the Dart call sites of `AKIotEVChargeCommand::<function>`; each endpoint page lists them under "Callers in app".

## AkNetwork.requestHttp

`AkNetwork.requestHttp` (`base_service/util/ak_util/src/ak_network.dart @0x21c3444`, `static`, named parameter `params`, returns `Future<Map<String, dynamic>?>`) is the generic path-C helper used by several packages. It builds the same envelope with the URL given by the caller, `method` always `"POST"` (`@0x21c34fc`) and `param` = the caller's map (`@0x21c3518`), and calls `handle` (`@0x21c3544`) with `"akiot.cloud_api"` (`@0x21c3534`). It logs the result (`"ToAkNetwork返回+"`, `@0x21c358c`) and compares the result type with the `AKResultType` instance `success` (enum index 0, pool entry `pp+0xa5b0`, `@0x21c3608`; the enum has five instances, among them `requestError` and `responseError`). Any other result type throws through `AkNetworkExceptionExtension.errorToAkNetworkException` (`@0x21c3760`). On success it returns `null` when the result object holds no data (`@0x21c3620` to `@0x21c3628`), reads the key `data` of it (`@0x21c3630`), returns `null` when that is null or the empty string (`@0x21c3654`, `@0x21c3698`), and otherwise returns it as a `Map<String, dynamic>` (return type from `InitAsync`, `@0x21c34a4`). Callers: [get_ocpp_endpoint_list](power_service/app/get_ocpp_endpoint_list.md), [get_ocpp_info](power_service/app/get_ocpp_info.md).

## ScheduleNetwork._requestHttp

`ScheduleNetwork._requestHttp` (`ev_charger/src/ev_charger/page/home/schedule_charge/network/ schedule_network.dart @0x284f6d0`; the file name has a leading space, `%20` in the asm path) builds the same envelope: `path` from its second argument (`@0x284f738`), `"POST"` (`@0x284f74c`), `param` from its first argument (`@0x284f764`), and calls `handle` with `"akiot.cloud_api"` (`@0x284f780`, call `@0x284f790`). It returns the raw `IoTAKResult`; the callers parse it themselves. Caller of record here: `ScheduleNetwork.getVehicleList` ([get_vehicle_list](power_service/app/vehicle/get_vehicle_list.md)).

## Response typing and the model registry

`handle<Y0>` takes the response class as its type argument, and the answer is an `IoTAKResult<Y0>`. The conversion from the SDK result to `Y0` happens in a closure of `handle` (allocated at `ak_iot_kit_manager_impl.dart @0x21c3d24`; its body was not read). The EV charger package registers a `fromJson` factory for every response class in `AnkerJsonUtils.initAnkerModelSerializable` (`ev_charger/src/ev_charger/ev_charger_json_factory.internal.dart @0x45ab020`; for example `A5190ChargeSessionsModel` at `@0x45ab13c`), so the conversion most probably goes through this registry (inferred, not traced). The registered `fromJson` of the A5190 session models first checks whether `json["data"]` is a `String` and, if so, decodes it with `jsonDecode`; it uses the map itself when `data` is absent (for example `a5190_charge_sessions_model.dart @0x45b2b6c` to `@0x45b2c4c`). The model pages record this as the `data` wrapper field.

Closure body (app side, traced 2026-10-20): the closure allocated at `base_service/ak_iot_kit/ak_iot_kit_manager_impl.dart @0x21c3d24` has its body at `@0x221cdf0`; it turns the native event into an `IoTAKResult` with `_ioTAKResultFromNative` (`@0x221ce60`, function `@0x221d2ac`), which converts the payload with `AnkerJson::_parseData` (call `@0x221d380`, `anker_get/src/json/anker_json.dart @0x2208788`; the function loads the static field `0x18a0` at `@0x2208858` and tests the type argument `Y0` at `@0x2208814`), and then runs `_processResult` (`@0x221ce98`, function `@0x221cef0`), which folds the result through the registered `IoTAKInterceptor` objects with `interceptResult` (`fold` `@0x221cfc0`, `@0x221d02c`). So the conversion to `Y0` goes through the `AnkerJson` converter; that the factories of the EV charger registry are the ones it uses is by the shared `Y0` lookup, not traced into the static field.

## Reading the inventory rows

| inventory shape | meaning |
|---|---|
| `role: url_provider`, file `ev_charge_command.dart`, params `path`, `method`, `param.<key>` | a map-building function of `AKIotEVChargeCommand`; the `param.<key>` entries are the real body keys |
| `role: sender`, `function` in `ocpp_network.dart` | a caller of `AkNetwork.requestHttp` |
| `encrypted: false` and a note "plain callee" | the `*Http*` callee is `AkNetwork.requestHttp`; the note text "callee default needEncryption=true" does not apply, because that callee ignores the flag and always uses the SDK |

## Known unknowns

- Which request headers and which body encryption the native SDK applies to a `"akiot.cloud_api"` call is not known from Dart. — reclassified: device test row 153 (2026-10-20: native SDK behaviour, no Dart asm)
- Which factory table the static field `0x18a0` of `AnkerJson::_parseData` holds (the link to `AnkerJsonUtils.initAnkerModelSerializable` of the EV charger package): not traced — traced 2026-10-20 (the closure body is in Response typing).
- The SDK may accept a leading-slash and a no-slash `path` alike (`add_vehicle` is the only literal with a slash); this was not tested.
