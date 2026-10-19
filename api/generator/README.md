> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# generator

Service index for the URL prefix `/generator/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/generator/v1/app/get_standby_exercise_plan`](app/get_standby_exercise_plan.md) | Reads the standby exercise plan of a third-party (oil-machine) generator that is attached to an AX170 (ATS) system: the schedule on which the generator is exercised while in standby. | - | hand-written |
| [`/generator/v1/app/set_standby_exercise_plan`](app/set_standby_exercise_plan.md) | Saves the standby exercise plan of a third-party (oil-machine) generator attached to an AX170 (ATS) system: when the next maintenance run is due, the interval in weeks, the maintenance time and the plan status. | - | hand-written |
| [`/generator/v1/app/wakeup_oil_machine_bluetooth`](app/wakeup_oil_machine_bluetooth.md) | TODO | - | skeleton |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
