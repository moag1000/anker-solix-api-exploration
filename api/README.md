> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# API

This directory holds one page per cloud endpoint, grouped by service (the first URL segment after the host), plus the cross-cutting pages `param_types.md`, `errors.md`, `auth.md` and `encryption.md`. An endpoint page is the single owner of that endpoint's request parameters, response payload and confidence tags.

Planned service sub-directories, named exactly after the URL prefix: `power_service/`, `charging_hes_svc/`, `charging_hes_installer_svc/`, `charging_hes_third_party_service_svc/`, `charging_energy_service/`, `charging_hes_dynamic_price_svc/`, `charging_pv_svc/`, `charging_imsg_svc/`, `charging_common_svc/`, `charging_disaster_prepared/`, `devicecontrol/`, `mini_power/`, `app/`, `passport/`, `openapi/`.

Not here: MQTT or BLE facts (see [../mqtt/README.md](../mqtt/README.md), [../ble/README.md](../ble/README.md)), step-by-step flows ([../flows/README.md](../flows/README.md)); ownership rules are in [../docs/STRUCTURE.md](../docs/STRUCTURE.md).


