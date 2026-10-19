> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# list

## Purpose

Lists the third-party device platforms (for example Shelly) with their products that can be added to a system; in the installer flow the app asks the installer service instead of the consumer service and sends `app_id` `anker_pros`.

## Upstream name

`none` for the installer URL (no upstream name). The consumer twin `/power_service/v1/app/third/platform/list` is the upstream key `get_third_platforms` (`api/apitypes.py` line 143, upstream-confirmed; `apibase.py` `get_third_platforms_list` sends no body and reads `data.data`).

## Method+URL

`POST /charging_hes_installer_svc/v2/app/third/platform/list` (asm-traced). `PlatformAppointAddDeviceController.getThirdPartyPlatformList` (`flutter_charging_beginning/beginning/state_cards/add_devices/platform_appoint_add_device/platform_appoint_add_device_controller.dart @0x24e60d8`) chooses between two literal paths: the consumer path `/power_service/v1/app/third/platform/list` (`@0x24e610c`) with `app_id` `"anker_power"` (`@0x24e611c`) and, when the route argument `systemId` of the page is non-null (the object field at offset 0x5f is filled from the argument `systemId` in `onInit`, `@0x350b238` to `@0x350b28c`; the test is `cmp w1, NULL` at `@0x24e6134`), the installer path `/charging_hes_installer_svc/v2/app/third/platform/list` (`@0x24e613c`, pool `pp+0x135258`) with `app_id` `"anker_pros"` (`@0x24e6144`). The method string is the literal `"POST"` (`@0x24e6c58`). This selector is not the `isProApp` flag of [the variant selector](../../../../README.md#variant-selector-installer-app-versus-consumer-app); it is a page argument.

## Encrypted?

Direct SDK call (asm-traced), path C of [../../../../../encryption.md](../../../../../encryption.md#which-calls-are-encrypted): the closure `@0x24e6bd8` builds the map `path`, `method`, `param` and passes it to `akIoTKitManager.handle` with the identifier `akiot.cloud_api` (`@0x24e6ce8` to `@0x24e6cf8`), wrapped in `startCommand` (`@0x24e616c`). The decorator tests are not involved; encryption and headers are native to the SDK. The inventory flag `encrypted: false` only means that no `*Http*` wrapper is called.

## Request

Map literal passed as `param` (`<String, String>`, one pair, `r2 = 4`, `@0x24e6c78`).

| field | type | required | example | source |
|---|---|---|---|---|
| `app_id` | String | yes | `"anker_pros"` | `flutter_charging_beginning/beginning/state_cards/add_devices/platform_appoint_add_device/platform_appoint_add_device_controller.dart @0x24e6c7c`; value `anker_pros` when `systemId` is set, else `anker_power` (field at offset 0x13 of the closure context, `@0x24e6c8c`) |

The path and the method are not body keys; they sit next to `param` in the outer map (`path` `@0x24e6c34`, `method` `@0x24e6c4c`, `param` `@0x24e6c64`). Upstream sends no body to the consumer twin (upstream-confirmed), so `app_id` is an app addition that already exists in 3.18.0.

## `param_type`/`cmd`

n/a

## Response model (link)

`ThirdPartyPlatformInfoModel` (legacy page [../../../../../../models/other.md](../../../../../../models/other.md#thirdpartyplatforminfomodel)): `ThirdPartyPlatformInfoModel.fromJson` is called for each list element at `flutter_charging_beginning/beginning/state_cards/add_devices/platform_appoint_add_device/platform_appoint_add_device_controller.dart @0x24e63f0` (`third_party_platform_info_model.dart`, `fromJson @0x24e6544`).

## Response

The SDK result must be of the success type (`Instance_AKResultType` compare, `@0x24e6194`); its payload is cast to `Map<String, dynamic>?` and read as follows.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | list of maps | yes | `[ { "name": "Shelly", ... } ]` | `flutter_charging_beginning/beginning/state_cards/add_devices/platform_appoint_add_device/platform_appoint_add_device_controller.dart @0x24e61e8`; each element is cast to `Map<String, dynamic>` (`@0x24e63e4`) and parsed by `ThirdPartyPlatformInfoModel.fromJson` (`@0x24e63f0`) |

Element keys (from `fromJson`, `base_service/bean/model/third_party/shelly/third_party_platform_info_model.dart`): `index`, `name`, `content`, `logo`, `tag`, `url`, `callback_url`, `tag_code`, `products` (key addresses `@0x24e6570`, `@0x24e65cc`, `@0x24e6628`, `@0x24e6688`, `@0x24e66e8`, `@0x24e6744`, `@0x24e67a4`, `@0x24e6804`, `@0x24e6860`). The upstream example for the consumer twin shows the same keys plus `countries` (upstream-confirmed, `apibase.py` docstring of `get_third_platforms_list`); `countries` is not read by the 3.24.3 model.

## Example request/response

Request, synthesized

```json
{ "path": "/charging_hes_installer_svc/v2/app/third/platform/list", "method": "POST", "param": { "app_id": "anker_pros" } }
```

Response: no captured response from the installer path. The consumer twin's response is documented upstream (`apibase.py`), not copied here.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or shows a toast; the shared transport codes are in [../../../../../encryption.md](../../../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../../../errors.md).

## Callers in app

- `PlatformAppointAddDeviceController.getThirdPartyPlatformList` (`flutter_charging_beginning/beginning/state_cards/add_devices/platform_appoint_add_device/platform_appoint_add_device_controller.dart @0x24e60d8`), called from `afterPermissionEnable` (`@0x24e04dc`, call `@0x24e0548`) and `onInit` (call `@0x350b6d8`). UI: the platform appoint add-device page (route `/platformAppointAddDevicePage`, string `@0x24e0524`) of the `flutter_charging_beginning` package (the installer commissioning flow).

## Since/changed

3.18.0: the consumer path `/power_service/v1/app/third/platform/list` with `app_id` is present (sender in `charging/http/http_request_repository_impl.dart`); the installer path is absent (no `installer_svc` string in the 3.18.0 pool). 3.24.3: the installer path is present (new). since: 3.24.3 for the installer path.

## Known unknowns

- Server behaviour of the installer service (whether the list differs from the consumer list) is not known.
- The meaning of `systemId` (an installer system id) is inferred from the route argument name.
- Whether the installer answer carries `countries` is not known.

## Device-tested by

none
