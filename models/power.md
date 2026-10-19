# Power Limits / SOC — Response Models

> **Numbers under review (2026-10-19):** integers on this page that came from decompiled code were read without Smi decoding and may be 2× too large. Verified values: see docs/audit/models.md; corrected facts live on their owner pages (docs/STRUCTURE.md).

> 2 models

## DevicePowerLimit

Source: `model/soc_model.dart`

```
device_sn, feeder0w, id, ip_region, legal_power_limit, min, power_limit_option,
power_limit_option_real, pv_power_limit, pv_power_limit_option,
region_microinverter_limit, region_power_limit, regulation_code, rssi,
switch_0w, user_power_limit
```

## StationPowerLimitModel

Corrected 2026-10-19 (App 3.24.3): the field list below is outdated; `StationPowerLimitModel`, `PowerLimitOption`, `DeviceInfo` and `Ae100Info` are owned by [`models/station_power_limit.md`](station_power_limit.md).

Source: `ui/page/device/main/sitation_energy_system/station_home_settings/station_power_limit/station_power_limit_model.dart`

```
acInputLimit, ac_input_power_unit, ae100_info, device_img, device_info,
device_name, device_pn, device_sn, exceed_alarm, legal_limit,
legal_power_limit, limit, limit_real, outputPower, parallel_type,
power_limit_option, site_id, status, supportAcLimit
```

## Known unknowns

None recorded beyond the row-level notes above.
