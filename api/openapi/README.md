> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# openapi

Service index for the URL prefix `/openapi/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/openapi/oauth/app_to_app_access`](oauth/app_to_app_access.md) | Asks the account server for the authorization code of the Alexa account link (OAuth app-to-app flow); sent by `AlexaLinkLogic::getAlexaLinkCode` (`charging/ui/page/account/login/alexa_link_logic.dart`) (asm-traced, caller chain in `data/endpoints.json`). | - | owner |
| [`/openapi/oauth/authorize`](oauth/authorize.md) | Not a request the app sends: `AlexaConstants::isAlexaAuthUrl` (`charging/constants/alexa_constants.dart @0x49ce29c`) recognises the link that the Alexa app opens in the Anker app by testing a URL string for the marker `alexaapp_to_ankerpower` (`@0x49ce2c8`) or for the path `/openapi/oauth/authorize` (`@0x49ce2f8`); the query of that link is then read by `AlexaLinkLogic::parseAuthParams` and used for `app_to_app_access` (asm-traced for the string test; the reading of the link's role is string-only). | - | owner |
| [`/openapi/oauth/key/exchange`](oauth/key/exchange.md) | Starts the session-key negotiation for encrypted requests: the app posts its client public key material and the server answers with its own public key, from which the app derives and stores the session key and its identifier. | - | owner |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
