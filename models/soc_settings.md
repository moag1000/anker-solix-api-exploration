> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# SocSettings

## Purpose

Carries the SOC limits of a device as reported by the device through the IoT kit (field `soc_data`); it is a device capability class, not a response of the cloud endpoint `get_site_device_param`.

## Dart class + file

`SocSettings`, `ak_iot_contract/src/device/capability/i_soc_command_capability.dart` (package `ak_iot_contract`), fromJson `@0x3b985d0`.

## Fields

The class does not exist in 3.18.0 (no class of this name in the 3.18.0 asm), so every key is `3.24.3`. The keys are camelCase.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `chargeLimit` | `int?` | yes | 3.24.3 | `i_soc_command_capability.dart @0x3b9860c` |
| `dischargeLimit` | `int?` | yes | 3.24.3 | `i_soc_command_capability.dart @0x3b986a4` |
| `backupReserve` | `int?` | yes | 3.24.3 | `i_soc_command_capability.dart @0x3b98738` |

## Produced by

Not an HTTP endpoint. `SocCommandCapability.getSoc` (`device/src/setting/controller/soc_settings/soc_command_capability.dart`, closure `@0x3b982bc`) requests the external field `soc_data` through the handler `akiot.device.get_external_field` (`@0x3b9841c`) and parses the `data` value with `SocSettings.fromJson` (`@0x3b98534`). The push listener `watchSoc` (`@0x46448f8`) parses the same class (`@0x4644b68`). The cloud counterpart is `SocSettingParam` ([soc_setting_param.md](soc_setting_param.md), `param_type` 27).

## Consumed by

The SOC settings controllers of the `device` package; field use is not traced.

## Changed since 3.18.0

New class in 3.24.3.

## Known unknowns

- The transport behind `akiot.device.get_external_field` (BLE, local or cloud) is decided inside the native plugin and is not visible in Dart. This page does not claim any BLE or cloud fallback behaviour — reclassified: native plugin, not in Dart asm, [device test row 156](../docs/DEVICE_TEST_BACKLOG.md#added-2026-10-20-depth-pass).
