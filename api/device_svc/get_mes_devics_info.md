> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_mes_devics_info

## Purpose

Converts device serial numbers to their laser-engraved (MES) serial numbers for a small set of product codes; the apps use it for sub-package serial lists (A17E2 and A17C1 home screens, the add-device flow) and for floating fault messages. The URL spells `devics` (sic).

## Upstream name

`none` (no upstream name). Upstream lists a related URL `power_service/v1/app/device/get_mes_device_info` in `api/apitypes.py` (comment: "shows laser_sn field but no more info"); the 3.24.3 URL is a different one in `device_svc`.

## Method+URL

`POST /device_svc/v1/get_mes_devics_info` (asm-traced). Sender: `AkSnConverter.convertSns` (`base_service/util/ak_util/src/ak_sn_converter.dart @0x23009b8`); the URL literal is loaded at `@0x2300b98` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x2300b90`).

## Encrypted?

Yes by wrapper (asm-traced): `convertSns` calls `HttpServiceImpl.encryptionRequestHttp` (`base_service/util/ak_util/src/ak_sn_converter.dart @0x2300bbc`) with named arguments `fail` and `success` only (`@0x2300bb4`) and without `needEncryption`, so the default `true` applies ([encryption.md](../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../encryption.md)); asm alone does not decide it.

## Request

The function first checks that the product code is in a constant set of six strings (`AE103`, `A17E2`, `A17C1`, `A17C2`, `A17C3`, `A17C5`; pool `pp+0x14e30`, `@0x23009f8`) and otherwise logs `不支持的 PN` (unsupported PN) and returns without a request (`@0x2300a18`). It filters the serial list with a closure (`where`, `@0x2300a68`) and returns when the list is empty (`SN 列表为空`, `@0x2300a88`). Body is a `<String, List<String>>` map of one pair (`@0x2300b4c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sns` | list of String | yes | `["<device sn>"]` | `base_service/util/ak_util/src/ak_sn_converter.dart @0x2300b38`; the filtered serial list |

The product-code argument is not a body key (traced 2026-10-20): the six-element set check and the "unsupported PN" return (`base_service/util/ak_util/src/ak_sn_converter.dart @0x23009f8`, `@0x2300a18`) are the only uses of the product code in `convertSns`; the body map holds `device_sns` only (`@0x2300b38`).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the response is parsed by `_parseResponse` into a `Map<String, String>`.

## Response

`_parseResponse` (`base_service/util/ak_util/src/ak_sn_converter.dart @0x2300d8c`) reads the key `list` (`@0x2300dac`); if it is not a non-empty list it logs `接口返回数据为空` (empty answer, `@0x2300eb0`) and returns null; otherwise it builds a `<String, String>` map from each element's `device_sn` (`@0x2300fec`) to its `laser_sn` (`@0x2301018`), skipping empty values. The failure closure logs `SN 转换请求失败: code=...` and completes the future with null (`@0x2300c90`).

| field | type | required | example | source |
|---|---|---|---|---|
| `list` | list of map | yes | `[ { "device_sn": "...", "laser_sn": "..." } ]` | `base_service/util/ak_util/src/ak_sn_converter.dart @0x2300dac` |
| `list[].device_sn` | String | yes | `<device sn>` | `base_service/util/ak_util/src/ak_sn_converter.dart @0x2300fec` |
| `list[].laser_sn` | String | no | `<laser sn>` | `base_service/util/ak_util/src/ak_sn_converter.dart @0x2301018`; entries with an empty value are dropped |

## Example request/response

Request, synthesized

```json
{ "device_sns": ["<device sn>"] }
```

Response, synthesized

```json
{ "list": [ { "device_sn": "<device sn>", "laser_sn": "<laser sn>" } ] }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../errors.md).

## Callers in app

- `A17E2HomeController._convertSubPackageSns` (`micro_hes/src/a17e2/home/a17e2_home_controller.dart @0x355dde0`)
- `SubDeviceDataFetcher._applySnConversion` (`flutter_charging_beginning/beginning/state_cards/add_devices/select_power_device/sub_device_data_fetcher.dart @0x2abab00`)
- `A17C1homeLogic._convertSubPackageSns` (`charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x2626594`)
- `DeviceFaultManager.void _getUserFloatingFaultInfo` (`business_common/msg/device_fault_manager.dart @0x230a458`)
- `SiteMsgBannerController.getUserFloatingFaultInfo` (`business_common/msg/site_msg_banner_controller.dart @0x22fdab8`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x14e70`). since: 3.24.3.

## Known unknowns

- What the laser serial is used for in the UI (display of the printed serial, matching of sub-package serials) is not traced. — traced 2026-10-20: the only visible user is `A17E2HomeController::_convertSubPackageSns` (`micro_hes/src/a17e2/home/a17e2_home_controller.dart @0x355dde0`, call `convertSns`), which merges the answer map into a cache field of the controller (`addAll`, `@0x355de0c`) and then, for each sub-package device entry, replaces the raw serial with the converted one (log text `_convertSubPackageSns: apply sn, rawSn=... -> convertedSn=...`, `@0x355df7c`, store `@0x355dfe8`); so the laser serial replaces the sub-package serial in the A17E2 home device list. Where that list is shown was not followed
- No response was captured.

## Device-tested by

none
