> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# device_svc

Service index for the URL prefix `/device_svc/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/device_svc/v1/get_mes_devics_info`](get_mes_devics_info.md) | Converts device serial numbers to their laser-engraved (MES) serial numbers for a small set of product codes; the apps use it for sub-package serial lists (A17E2 and A17C1 home screens, the add-device flow) and for floating fault messages. The URL spells `devics` (sic). | - | owner |
| [`/device_svc/v1/get_self_check_config`](get_self_check_config.md) | Reads the cloud-defined self-check texts (title, text, image, type per check id) for a product, so the self-check and self-check-failure screens of the initial setup can explain a failed check. | - | owner |
| [`/device_svc/v1/get_url_by_country_code`](get_url_by_country_code.md) | Returns the URL of the device shop (mall) for a country code; the user main page uses it to show the shop entry. | - | owner |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
