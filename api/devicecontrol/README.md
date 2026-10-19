> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# devicecontrol

Service index for the URL prefix `/devicecontrol/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/devicecontrol/v1/app/get_self_check_record`](app/get_self_check_record.md) | Reads the last self-check record of a device in a system (status, start and end time); the self-check result and failure cards of the initial setup flow use it. | - | hand-written |
| [`/devicecontrol/v1/app/record_device_command`](app/record_device_command.md) | Records a command that the app sent to an AX170 (ATS) device so that the cloud keeps a history; the traced sender records the update of a branch circuit record with the device serial, a command type and the command data. | - | hand-written |
| [`/devicecontrol/v1/app/report_event_data`](app/report_event_data.md) | Reports a device event to the cloud (the app log calls it the "425 event"): the app sends the device serial, the product code, the field `pn_payload` of the event object and the report time. | - | hand-written |
| [`/devicecontrol/v1/app/self_check_report`](app/self_check_report.md) | Reports the result of a system self-check to the cloud: site, device, a status, a failure code, a capability flag and the start and end time of the check. | - | hand-written |
| [`/devicecontrol/v1/device/verify_unlock_default_power_code`](device/verify_unlock_default_power_code.md) | Checks an unlock code that the user types into the "DIY legal power limit" prompt before the app sets an output limit above the legal limit. | - | hand-written |
| [`/devicecontrol/v1/get_devices_power_config`](get_devices_power_config.md) | Reads the power configuration (input and output power settings) of several devices in one call; the grid connection settings use it to show and set the default output power of devices. | - | hand-written |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
