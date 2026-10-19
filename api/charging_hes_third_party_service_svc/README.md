> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# charging_hes_third_party_service_svc

Service index for the URL prefix `/charging_hes_third_party_service_svc/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/charging_hes_third_party_service_svc/query_modbus_setting`](query_modbus_setting.md) | Reads the Modbus (third-party control) configuration of one device or site: which Modbus variants the device supports (TCP, RTU), which one is enabled, the RTU slave id, the device IP address and port, and links to the Home Assistant and Homey guides. | - | owner |
| [`/charging_hes_third_party_service_svc/set_modbus_setting`](set_modbus_setting.md) | Sends the Modbus (third-party control) setting of a device to the cloud: which variant is enabled (off, Modbus TCP or Modbus RTU), the RTU slave id, and whether the device was already configured over Bluetooth; what the server does with it is not verified. | - | owner |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
