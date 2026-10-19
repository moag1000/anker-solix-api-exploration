> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_hardware_relation

## Purpose

Reads which sites a list of device serials belongs to (site id, site name, product code, serial, and whether the site is the main one); the app uses it for device relations and for the sub-package (OTA) info of devices.

## Upstream name

`none` for the key; upstream lists the URL without a key in `api/apitypes.py` (line 345, comment "shows empty list", body `{"sn_list": [deviceSn]}`; upstream-confirmed for the key name).

## Method+URL

`POST /power_service/v2/app/get_hardware_relation` (asm-traced). Two senders: `DeviceRelationMgr.requestHardwareRelation` (`base_service/ak_iot_kit/business/basic/model/station_device_relation.dart @0x22a4864`; URL literal `@0x22a49c4`, `Method.post` pool entry `pp+0xa7e0`, `@0x22a49bc`) and `SubPackageInfoProvider.getHardwareRelation` (`ota_kit/src/providers/sub_package_info_provider.dart @0x2b0b4ec`; path literal `@0x2b0b5bc`, method `"POST"` `@0x2b0b5d4`).

## Encrypted?

Two paths. `requestHardwareRelation`: `encryptionRequestHttp` (`base_service/ak_iot_kit/business/basic/model/station_device_relation.dart @0x22a49e8`) without `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)); whether it goes through the SDK is decided at run time. `getHardwareRelation`: direct SDK call, path C (`ota_kit/src/providers/sub_package_info_provider.dart @0x2b0b670`, identifier `akiot.cloud_api`). The inventory flag `encrypted: false` on the `ota_kit` row only means that no `*Http*` wrapper is called.

## Request

The two senders build different value types for the same key.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn_list` (`requestHttp` sender) | String (JSON text) | yes | `"[\"<device sn>\"]"` | `base_service/ak_iot_kit/business/basic/model/station_device_relation.dart @0x22a48f4`; the value is `jsonEncode` of a copy of the serial list (`List.from`, `@0x22a4890`; `jsonEncode` `@0x22a4908`), stored in a `<String, String>` map (`@0x22a4934`): a JSON array **as a string** |
| `sn_list` (SDK sender) | list of String | yes | `[ "<device sn>" ]` | `ota_kit/src/providers/sub_package_info_provider.dart @0x2b0b5f8`; the list is stored directly in a `<String, List<String>>` map (`@0x2b0b60c`); an empty list is not sent (`snList 为空`, "snList is empty", `@0x2b0b52c`) |

Upstream documents the list form (`{"sn_list": [deviceSn]}`); whether the server accepts the string form of the first sender is not tested. The 3.18.0 file holds the same key (`"sn_list"`).

## `param_type`/`cmd`

n/a

## Response model (link)

`SiteSnRelationList` ([../../../../models/site_sn_relation_list.md](../../../../models/site_sn_relation_list.md)), `fromJson` called at `base_service/ak_iot_kit/business/basic/model/station_device_relation.dart @0x22a4bcc` (`requestHardwareRelation` success closure `@0x22a4ab8`).

## Response

`requestHardwareRelation` success closure (`base_service/ak_iot_kit/business/basic/model/station_device_relation.dart @0x22a4ab8`): the payload must be a map; the key `list` (`@0x22a4ba8`) is passed to `SiteSnRelationList.fromJson` and stored in `relationInfoList` (`@0x22a4bd8`). A non-map payload logs `fail reason format error with response` (`@0x22a4bf8`). The SDK sender (`ota_kit/src/providers/sub_package_info_provider.dart`) forwards the SDK result to its caller; its parse was not read.

| field | type | required | example | source |
|---|---|---|---|---|
| `list` | list | yes | `[ { "sn_site_infos": [ ... ] } ]` | `base_service/ak_iot_kit/business/basic/model/station_device_relation.dart @0x22a4ba8`; element keys on the model page |

## Example request/response

Request, synthesized (`requestHttp` sender)

```json
{ "sn_list": "[\"<device sn>\"]" }
```

Request, synthesized (SDK sender)

```json
{ "path": "/power_service/v2/app/get_hardware_relation", "method": "POST", "param": { "sn_list": [ "<device sn>" ] } }
```

Response: no captured response; upstream notes an empty list for its test account.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `DeviceRelationMgr.requestHardwareRelation` (`base_service/ak_iot_kit/business/basic/model/station_device_relation.dart @0x22a4864`, static): the device relation manager of the IoT kit (package `base_service`); the caller was not traced.
- `SubPackageInfoProvider.getHardwareRelation` (`ota_kit/src/providers/sub_package_info_provider.dart @0x2b0b4ec`): the sub-package info of the OTA kit (package `ota_kit`).

## Since/changed

3.18.0: present (the sender file holds the URL string and the key `sn_list` in the 3.18.0 asm). 3.24.3: present, with the second sender in `ota_kit`. since: ≤3.18.0.

## Known unknowns

- Whether the server accepts both the string form and the list form of `sn_list` is not tested.
- The caller of `requestHardwareRelation` and the reading of the SDK sender's result are not traced.
- Server behaviour is not known (upstream saw an empty list).

## Device-tested by

none
