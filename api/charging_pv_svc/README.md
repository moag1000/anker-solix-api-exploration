> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# charging_pv_svc

Service index for the URL prefix `/charging_pv_svc/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/charging_pv_svc/getMiStatus`](getmistatus.md) | TODO | - | skeleton |
| [`/charging_pv_svc/getPvStatus`](getpvstatus.md) | TODO | `get_device_pv_status` | skeleton |
| [`/charging_pv_svc/getPvTotalStatistics`](getpvtotalstatistics.md) | TODO | `get_device_pv_total_statistics` | skeleton |
| [`/charging_pv_svc/selectUserTieredElecPrice`](selectusertieredelecprice.md) | TODO | `get_device_pv_price` | skeleton |
| [`/charging_pv_svc/set_aps_power`](set_aps_power.md) | TODO | `set_device_pv_power` | skeleton |
| [`/charging_pv_svc/statisticsPv`](statisticspv.md) | TODO | `get_device_pv_statistics` | skeleton |
| [`/charging_pv_svc/updateUserTieredElecPrice`](updateusertieredelecprice.md) | TODO | `set_device_pv_price` | skeleton |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
