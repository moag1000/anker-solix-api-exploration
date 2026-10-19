> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# API

This directory holds one page per cloud endpoint, grouped by service (the first URL segment after the host), plus the cross-cutting pages `param_types.md`, `errors.md`, `auth.md` and `encryption.md`. An endpoint page is the single owner of that endpoint's request parameters, response payload and confidence tags. Paths follow the naming rule in [../docs/STRUCTURE.md](../docs/STRUCTURE.md#naming-conventions): `v1` is dropped from the path, any other version segment is kept.

## Service index

One directory per URL prefix: 406 distinct URLs (394 in 3.24.3, 12 only in 3.18.0). Counts include hand-written pages; all other pages are skeletons rendered from `data/endpoints.json` by `tools/render_pages.py`.

| service | pages | index |
|---|---|---|
| `app/` | 29 | [app/README.md](app/README.md) |
| `charging_common_svc/` | 3 | [charging_common_svc/README.md](charging_common_svc/README.md) |
| `charging_disaster_prepared/` | 5 | [charging_disaster_prepared/README.md](charging_disaster_prepared/README.md) |
| `charging_energy_service/` | 18 | [charging_energy_service/README.md](charging_energy_service/README.md) |
| `charging_hes_dynamic_price_svc/` | 6 | [charging_hes_dynamic_price_svc/README.md](charging_hes_dynamic_price_svc/README.md) |
| `charging_hes_installer_svc/` | 18 | [charging_hes_installer_svc/README.md](charging_hes_installer_svc/README.md) |
| `charging_hes_svc/` | 61 | [charging_hes_svc/README.md](charging_hes_svc/README.md) |
| `charging_hes_third_party_service_svc/` | 2 | [charging_hes_third_party_service_svc/README.md](charging_hes_third_party_service_svc/README.md) |
| `charging_imsg_svc/` | 2 | [charging_imsg_svc/README.md](charging_imsg_svc/README.md) |
| `charging_pv_svc/` | 7 | [charging_pv_svc/README.md](charging_pv_svc/README.md) |
| `device_svc/` | 3 | [device_svc/README.md](device_svc/README.md) |
| `devicecontrol/` | 5 | [devicecontrol/README.md](devicecontrol/README.md) |
| `ems/` | 1 | [ems/README.md](ems/README.md) |
| `energy/` | 4 | [energy/README.md](energy/README.md) |
| `generator/` | 1 | [generator/README.md](generator/README.md) |
| `marketing/` | 1 | [marketing/README.md](marketing/README.md) |
| `mini_power/` | 34 | [mini_power/README.md](mini_power/README.md) |
| `openapi/` | 3 | [openapi/README.md](openapi/README.md) |
| `passport/` | 26 | [passport/README.md](passport/README.md) |
| `power_service/` | 156 | [power_service/README.md](power_service/README.md) |
| `privacy_service/` | 2 | [privacy_service/README.md](privacy_service/README.md) |
| `site/` | 2 | [site/README.md](site/README.md) |
| `smart_service/` | 13 | [smart_service/README.md](smart_service/README.md) |
| `v2/` | 4 | [v2/README.md](v2/README.md) |

## Ambiguous prefixes (resolved: all five are real services)

Checked on 2026-10-19 against the 3.24.3 asm (`blutter_output/asm`, grep only). Five prefixes looked ambiguous in the object-pool strings:

| prefix | URL literals (`"/<prefix>/...`) | Dart package paths | verdict |
|---|---|---|---|
| `smart_service` | 13 | none | real service: 13 endpoints, sent through `encryptionRequestHttp`/`encryptionRequestHttpByGHttpRequest` in `anka_agent/http/` |
| `device_svc` | 3 | none | real service: 3 endpoints, sent via `encryptionRequestHttp` |
| `privacy_service` | 2 | none | real service: 2 endpoints (data export), sent via `encryptionRequestHttp` |
| `energy` | 4 | 6 (`.../src/energy/model/...`) | real service: 4 endpoints (`/energy/v1/...`). The package paths are unrelated Dart directories and are not endpoints |
| `site` | 2 | 12 (`.../family/site/...`) | real service: 2 endpoints (`/site/v1/...`). The package paths are unrelated Dart directories and are not endpoints |

Result: none of the five is only a Dart package path; every one has URL literals with a leading `/` that a `*Http*` sender uses, so all five are inventoried and have their own directory above. Related oddities, not errors: `v2/` holds four `/v2/anka/...` URLs (the version segment comes first, so the URL prefix rule makes `v2` the service directory; the four rows are URL literals with no traced sender, one of them removed in 3.24.3), and `ems/`, `generator/` and `marketing/` hold one endpoint each.

Not here: MQTT or BLE facts (see [../mqtt/README.md](../mqtt/README.md), [../ble/README.md](../ble/README.md)), step-by-step flows ([../flows/README.md](../flows/README.md)); ownership rules are in [../docs/STRUCTURE.md](../docs/STRUCTURE.md).
