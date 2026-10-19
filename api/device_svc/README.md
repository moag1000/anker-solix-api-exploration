> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# device_svc

Service index for the URL prefix `/device_svc/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/device_svc/v1/get_mes_devics_info`](get_mes_devics_info.md) | TODO | - | skeleton |
| [`/device_svc/v1/get_self_check_config`](get_self_check_config.md) | TODO | - | skeleton |
| [`/device_svc/v1/get_url_by_country_code`](get_url_by_country_code.md) | TODO | - | skeleton |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
