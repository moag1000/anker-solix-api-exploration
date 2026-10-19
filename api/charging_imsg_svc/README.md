> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# charging_imsg_svc

Service index for the URL prefix `/charging_imsg_svc/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/charging_imsg_svc/app/referral/del_red`](app/referral/del_red.md) | Clears the referral red dot on the server after the user has opened the referral entry. | - | hand-written |
| [`/charging_imsg_svc/app/referral/get_red`](app/referral/get_red.md) | Reads whether the referral entry should show a red dot (new referral news); the user main page asks on opening. | - | hand-written |
| [`/charging_imsg_svc/remove_user_floating_fault_info`](remove_user_floating_fault_info.md) | Dismisses ("closes") one or more floating fault messages of an EV charger on the app's home screen by serial number and fault ids. | - | hand-written |
| [`/charging_imsg_svc/user_fault_alarm`](user_fault_alarm.md) | Sends the fault bit array of an EV charger to the message service together with the device serial, product code, a fixed type id and the local time; the fault-info widget of the charger home screen calls it when it parses fault info (the name suggests it raises or records a fault alarm for the user). | - | hand-written |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
