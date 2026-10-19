> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# devicecontrol

Service index for the URL prefix `/devicecontrol/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/devicecontrol/v1/app/get_self_check_record`](app/get_self_check_record.md) | TODO | - | skeleton |
| [`/devicecontrol/v1/app/report_event_data`](app/report_event_data.md) | TODO | - | skeleton |
| [`/devicecontrol/v1/app/self_check_report`](app/self_check_report.md) | TODO | - | skeleton |
| [`/devicecontrol/v1/device/verify_unlock_default_power_code`](device/verify_unlock_default_power_code.md) | Checks an unlock code that the user types into the "DIY legal power limit" prompt before the app sets an output limit above the legal limit. | - | hand-written |
| [`/devicecontrol/v1/get_devices_power_config`](get_devices_power_config.md) | TODO | - | skeleton |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
