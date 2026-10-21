> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# EV charger device-sharing models

## Purpose

Carries the answers of the device-sharing endpoints of the EV charger app: the members a charger is shared with, and the installers that were invited to a charger.

## Dart class + file

`DeviceShareListResponse` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/models/src/device_share_list_model.dart`); `DeviceShareListModel` (`ev_charger/src/ev_charger/page/home/setting/device_share_members/models/src/device_share_list_model.dart`); `DeviceShareInstallerListModel` (`ev_charger/src/ev_charger/page/home/setting/device_share_installer/model/device_share_installer_list_model.dart`); `DeviceShareInstallerItem` (`ev_charger/src/ev_charger/page/home/setting/device_share_installer/model/device_share_installer_list_model.dart`). `fromJson` addresses are under each class below.

## Fields

Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Dart types and nullability come from `tools/model_fields.py` (`data/models.json`); an "of `X`" note is the list element class read from the `<X>` type argument next to the key.

### DeviceShareListResponse

Answer of `get_shared_device`: the share entries and the maximum number of members.

`fromJson` `device_share_list_model.dart @0x21c2744`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `device_list` | `List<DeviceShareListModel>` | no | ≤3.18.0 | `device_share_list_model.dart @0x21c2770` |
| `max_invite_members_count` | `int?` | yes | ≤3.18.0 | `device_share_list_model.dart @0x21c2884` |

### DeviceShareListModel

One share entry (member) in `DeviceShareListResponse.device_list`.

`fromJson` `device_share_list_model.dart @0x21c2e08`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `user_id` | `String?` | yes | ≤3.18.0 | `device_share_list_model.dart @0x21c2e34` |
| `member_id` | `String?` | yes | ≤3.18.0 | `device_share_list_model.dart @0x21c2eb0` |
| `device_sn` | `String?` | yes | ≤3.18.0 | `device_share_list_model.dart @0x21c2f2c` |
| `email` | `String?` | yes | ≤3.18.0 | `device_share_list_model.dart @0x21c2fa8` |
| `phone` | `String?` | yes | ≤3.18.0 | `device_share_list_model.dart @0x21c3024` |
| `status` | `int?`, converted with `DeviceShareStatus.fromValue` (`@0x21c3110`): 1 inviting, 2 joined, 3 rejected, 4 expired, other 0, see [enums](../reference/enums.md#devicesharestatus-and-devicesharemembertype) | yes | ≤3.18.0 | `device_share_list_model.dart @0x21c30a0` |
| `member_type` | `int?`, converted with `DeviceShareMemberType.fromValue` (`@0x21c31ac`): 1 normal, 2 owner, 10 installer, 11 other, see [enums](../reference/enums.md#devicesharestatus-and-devicesharemembertype) | yes | ≤3.18.0 | `device_share_list_model.dart @0x21c3128` |

### DeviceShareInstallerListModel

Answer of `get_installer_invited_list`: the invited installers.

`fromJson` `device_share_installer_list_model.dart @0x2aaf4c0`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `installerList` | `List<DeviceShareInstallerItem>` (type argument `<DeviceShareInstallerItem>` `@0x2aaf52c`, mapping closure `@0x2aaf594`) | yes | ≤3.18.0 | `device_share_installer_list_model.dart @0x2aaf4fc` |

### DeviceShareInstallerItem

One invited installer in `DeviceShareInstallerListModel.installerList`.

`fromJson` `device_share_installer_list_model.dart @0x2aaf984`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `installerUserId` | `String?` | yes | ≤3.18.0 | `device_share_installer_list_model.dart @0x2aaf9a4` |
| `deviceSn` | `String?` | yes | ≤3.18.0 | `device_share_installer_list_model.dart @0x2aafa2c` |
| `installerMaskedEmail` | `String?` | yes | ≤3.18.0 | `device_share_installer_list_model.dart @0x2aafab4` |
| `sourceType` | `int?` | yes | ≤3.18.0 | `device_share_installer_list_model.dart @0x2aafb3c` |

## Produced by

- [`get_shared_device`](../api/app/devicerelation/get_shared_device.md): `DeviceShareListResponse` (`DeviceShareListResponse.fromJson` called at `ev_charger/src/ev_charger/page/home/setting/device_share_members/network/device_share_network.dart @0x21a4bdc`)
- [`get_installer_invited_list`](../api/charging_hes_svc/share_device/get_installer_invited_list.md): `DeviceShareInstallerListModel` (`fromJson` call `device_share_network.dart @0x2aaf43c`)

## Consumed by

The device sharing screens of the EV charger settings (`DeviceShareListLogic`, `DeviceShareInstallerListLogic`); field-level use is not traced.

## Changed since 3.18.0

All classes are present in 3.18.0 (`since` column); no key is new in 3.24.3.

## Known unknowns

- `sourceType` of an installer item is not decoded — traced 2026-10-20: the key string `sourceType` occurs in the model and in unrelated OTA, load-balancing and station files, none of them a reader of this model; reads by field offset in the installer pages were not followed.
