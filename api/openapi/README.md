> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# openapi

Service index for the URL prefix `/openapi/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/openapi/oauth/app_to_app_access`](oauth/app_to_app_access.md) | TODO | - | skeleton |
| [`/openapi/oauth/authorize`](oauth/authorize.md) | TODO | - | skeleton |
| [`/openapi/oauth/key/exchange`](oauth/key/exchange.md) | TODO | - | skeleton |

Not here: MQTT or BLE facts ([../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
