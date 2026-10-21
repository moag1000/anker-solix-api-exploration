> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# charging_pv_svc

Service index for the URL prefix `/charging_pv_svc/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/charging_pv_svc/getMiStatus`](getmistatus.md) | Reads the current power, status and energy of an A5150 solar micro-inverter for its home page (caller `A5150HomeHttpReposity::getMiStatus`) (string-only: inferred from the function and class names, no caller chain is in `data/endpoints.json`). | - | owner |
| [`/charging_pv_svc/getPvStatus`](getpvstatus.md) | Reads the PV status of one or more A5140 devices for the device home page and the device list (caller chain `A5140HomeLogic::_isOffline`, `DeviceMainLogic::getDeviceList`, `HttpRequestController::getPvStatus`, in `data/endpoints.json`) (asm-traced). | `get_device_pv_status` | owner |
| [`/charging_pv_svc/getPvTotalStatistics`](getpvtotalstatistics.md) | Reads the lifetime PV totals (energy, CO2 reduction, saved money, power config) of an A5140 device for its home page (caller `A5140HttpReposity::getPvTotalStatistics`) (string-only: inferred from the function and class names, no caller chain is in `data/endpoints.json`). | `get_device_pv_total_statistics` | owner |
| [`/charging_pv_svc/selectUserTieredElecPrice`](selectusertieredelecprice.md) | Reads the tiered electricity price (currency and price tiers) a user saved for a PV device (caller chain `HttpRequestController::selectUserTieredElecPrice`, in `data/endpoints.json`) (asm-traced). | `get_device_pv_price` | owner |
| [`/charging_pv_svc/set_aps_power`](set_aps_power.md) | Sets the maximum output power (APS max power) of an A5140 device (caller `A5140HttpReposity::requestApsMaxPower`) (string-only: inferred from the function name, no caller chain is in `data/endpoints.json`). | `set_device_pv_power` | owner |
| [`/charging_pv_svc/statisticsPv`](statisticspv.md) | Loads the PV generation statistics (curve, energy, money) for a period on the A5140, A5150 and green-power chart pages (callers `ChartHttpReposity::getPvStatistics`, `A5150HomeHttpReposity::getPvStatistics`, `A5150SolarDetailsReposity::getSolarStatistics`, `ChartHttpReposity::getGreenPvStatistics`) (string-only: inferred from the function names, no caller chain is in `data/endpoints.json`). | `get_device_pv_statistics` | owner |
| [`/charging_pv_svc/updateUserTieredElecPrice`](updateusertieredelecprice.md) | Saves the tiered electricity price (currency and price tiers) a user entered for a PV device (caller chain `HttpRequestController::updateUserTieredElecPrice`, in `data/endpoints.json`) (asm-traced for the call; the meaning of the tiers is taken from the model field names, string-only). | `set_device_pv_price` | owner |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
