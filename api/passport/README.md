> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# passport

Service index for the URL prefix `/passport/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/passport/change_password`](change_password.md) | TODO | - | skeleton |
| [`/passport/discount_desc`](discount_desc.md) | TODO | - | skeleton |
| [`/passport/estimate_domain`](estimate_domain.md) | TODO | - | skeleton |
| [`/passport/external_login`](external_login.md) | A login URL the app knows by name but never sends in 3.24.3: the string is only compared against the URL of a failed request to decide whether the login screen must be started again after a forced logout. | - | owner, not in `data/endpoints.json` |
| [`/passport/forget_password`](forget_password.md) | TODO | - | skeleton |
| [`/passport/freeze_account`](freeze_account.md) | TODO | - | skeleton |
| [`/passport/get_profile`](get_profile.md) | TODO | - | skeleton |
| [`/passport/get_subscriptions`](get_subscriptions.md) | TODO | - | skeleton |
| [`/passport/get_user_param`](get_user_param.md) | TODO | - | skeleton |
| [`/passport/login`](login.md) | Logs a user in with e-mail and password: the app sends the e-mail, the encrypted password and its client public key, and the response carries the session token (`auth_token`) with the user profile. | - | owner |
| [`/passport/logout`](logout.md) | Tells the server that the session of the current user ends; the app sends an empty body and then clears its stored encryption information and all local user data. | - | owner |
| [`/passport/phone_bind_account`](phone_bind_account.md) | TODO | - | skeleton |
| [`/passport/phone_code_list`](phone_code_list.md) | TODO | - | skeleton |
| [`/passport/phone_reset_password`](phone_reset_password.md) | TODO | - | skeleton |
| [`/passport/phone_verification_code`](phone_verification_code.md) | TODO | - | skeleton |
| [`/passport/phone_verification_login`](phone_verification_login.md) | TODO | - | skeleton |
| [`/passport/phone_verification_regist`](phone_verification_regist.md) | TODO | - | skeleton |
| [`/passport/register`](register.md) | TODO | - | skeleton |
| [`/passport/resend_active_email`](resend_active_email.md) | TODO | - | skeleton |
| [`/passport/set_account_password`](set_account_password.md) | TODO | - | skeleton |
| [`/passport/set_subscriptions`](set_subscriptions.md) | TODO | - | skeleton |
| [`/passport/subscription_configs`](subscription_configs.md) | TODO | - | skeleton |
| [`/passport/terminal_id`](terminal_id.md) | Asks the server for a terminal id (the app's anonymous client identity before login); the app stores it and sends it later as the `Openudid` header, as `X-Terminal-ID`, and to the IoT SDK as `terminalId`. | - | owner, not in `data/endpoints.json` |
| [`/passport/third_party_login`](third_party_login.md) | Logs a user in with an access token from a third-party identity provider (the only provider the app sends is Amazon) instead of e-mail and password; the response is the same session data as for [login](login.md). | - | owner |
| [`/passport/update_profile`](update_profile.md) | TODO | - | skeleton |
| [`/passport/update_user_param`](update_user_param.md) | TODO | - | skeleton |
| [`/passport/validate_email`](validate_email.md) | TODO | - | skeleton |
| [`/passport/validate_pass`](validate_pass.md) | TODO | - | skeleton |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
