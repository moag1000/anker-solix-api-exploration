> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# site

Service index for the URL prefix `/site/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/site/v1/app/share_site_report`](app/share_site_report.md) | Sends a site id to the cloud from the station home screens of the AX170 (ATS) and micro-HES (A17E2 and basic station) systems when they load the scene info; the answer is only logged. The name suggests it prepares or triggers sharing of the site report; the app does not read the answer. | - | owner |
| [`/site/v1/get_user_site_param`](get_user_site_param.md) | Reads the account's site-level user parameters (`/site/v1/get_user_site_param`); the generic `getUserParams` function of the HTTP repository sends it. The only caller candidate is the AE100 custom-mode usage scenario page, through a mixin function that the dump omits (UNCONFIRMED). | - | owner |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
