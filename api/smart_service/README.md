> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# smart_service

Service index for the URL prefix `/smart_service/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/smart_service/v1/app/anka/delete_all_memory`](app/anka/delete_all_memory.md) | Deletes everything the Anka assistant remembers about the user (the "delete all memory" action of the assistant settings). | - | owner |
| [`/smart_service/v1/app/anka/get_all_config`](app/anka/get_all_config.md) | Reads the Anka AI assistant's entry configuration for the account: whether the entry is shown, the agent domain, the switches (proactive messages, memory, bill analysis, power outage), the setting images and the current bubble. This is the 3.24.3 name of the 3.18.0 call `get_entry_config`. | - | owner |
| [`/smart_service/v1/app/anka/get_entry_config`](app/anka/get_entry_config.md) | Read the entry configuration of the Anka AI assistant for the account (3.18.0 only). 3.24.3 replaced it with `get_all_config`, which reads the same configuration under the new name (the wording of what it carries is taken from that page; the 3.18.0 sender could not be re-read here, string-only). | - | removed |
| [`/smart_service/v1/app/anka/get_entry_show`](app/anka/get_entry_show.md) | Asks whether the Anka assistant entry button should be shown for a site on the AI EMS screens (the button's support check). | - | owner |
| [`/smart_service/v1/app/anka/get_menu_config`](app/anka/get_menu_config.md) | Reads the Anka assistant's menu configuration (menu items with sub items) and, new in 3.24.3, the bill-analysis entry state. | - | owner |
| [`/smart_service/app/anka/get_question_bank`](app/anka/get_question_bank.md) | Reads the recommended questions of the Anka assistant for the AI EMS source (the chat controller fetches them in `_fetchAiEmsRecommendQuestions`). The URL literal has a double slash after `v1`. | - | owner, not in `data/endpoints.json` |
| [`/smart_service/v1/app/anka/proactive_cta`](app/anka/proactive_cta.md) | Reads the suggested questions (call-to-action chips) for a proactive scene of the Anka assistant, such as a reminder; the chat controller refreshes them when a proactive message is shown. | - | owner |
| [`/smart_service/v1/app/anka/set_bubble_status`](app/anka/set_bubble_status.md) | Reports the state of the bubble shown on the Anka entry button (for example that the user consumed it) with the bubble id and type and the time. | - | owner |
| [`/smart_service/v1/app/anka/set_entry_switch`](app/anka/set_entry_switch.md) | Turns the Anka assistant entry (the AI entry on the user page) on or off for the account. | - | owner |
| [`/smart_service/v1/app/anka/set_memory_switch`](app/anka/set_memory_switch.md) | Turns the Anka assistant's memory (remembering conversation facts) on or off. | - | owner |
| [`/smart_service/v1/app/anka/set_push_switch`](app/anka/set_push_switch.md) | Turns one of the Anka push notification switches on or off: proactive messages, power-outage messages or bill analysis. | - | owner |
| [`/smart_service/v1/app/anka/setting`](app/anka/setting.md) | Reads the user's Anka assistant settings: the proactive and power-outage push switches, the memory switch and whether the assistant holds memory. | - | owner |
| [`/smart_service/v1/app/anka/welcome`](app/anka/welcome.md) | Reads the Anka assistant's welcome greeting for a session: the greeting text and the site selection data; the chat controller calls it when the chat opens and when it resyncs the cloud history. | - | owner |
| [`/smart_service/v1/app/anka/welcome_cta`](app/anka/welcome_cta.md) | Reads the suggested questions (call-to-action chips) that go with the welcome greeting of the Anka assistant. | - | owner |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).

<!-- hand-written below: kept by tools/service_index.py -->

## Anka AI assistant: bodies at a glance

`smart_service` is the backend of the Anka AI assistant (Dart package `anka_agent`, plus the entry button in `ak_soft_ems`). All calls are `POST`; the `anka_agent` senders go through `HttpServiceImpl.encryptionRequestHttpByGHttpRequest`, the `ak_soft_ems` entry button through `HttpServiceImpl.encryptionRequestHttp`, both with the default `needEncryption: true` ([../encryption.md](../encryption.md#which-calls-are-encrypted)). The tables below only index the pages; each page owns its body and response ([models/anka_agent_models.md](../../models/anka_agent_models.md) owns the response classes).

| endpoint | request body (keys) | response | state |
|---|---|---|---|
| [`get_all_config`](app/anka/get_all_config.md) | none | `AnkaAgentEntryConfigModel` | 3.24.3 name of `get_entry_config` |
| [`get_entry_config`](app/anka/get_entry_config.md) | none | `AnkaAgentEntryConfigModel` | 3.18.0 name only (skeleton), absent from the 3.24.3 pool |
| [`get_entry_show`](app/anka/get_entry_show.md) | `site_id`, `source` (`"aiems"`) | `show` (bool) | new in 3.24.3 |
| [`get_menu_config`](app/anka/get_menu_config.md) | none | `AnkaAgentMenuConfigModel` | in 3.18.0, model extended |
| [`proactive_cta`](app/anka/proactive_cta.md) | `scene_type` (optional) | `ProactiveCtaResponse` | new in 3.24.3 |
| [`set_bubble_status`](app/anka/set_bubble_status.md) | `status`, `bubble_type`, `bubble_id`, `consume_time` (seconds) | none read | new in 3.24.3 |
| [`set_entry_switch`](app/anka/set_entry_switch.md) | `setting_switch` (bool) | none read | in 3.18.0 |
| [`set_memory_switch`](app/anka/set_memory_switch.md) | `enabled` | none read | new in 3.24.3 |
| [`set_push_switch`](app/anka/set_push_switch.md) | `switch_name` (`proactive_message`, `power_outage`, `bill_analysis`), `enabled` | none read | new in 3.24.3 |
| [`setting`](app/anka/setting.md) | none | `GetSettingResponse` | new in 3.24.3 |
| [`welcome`](app/anka/welcome.md) | `current_time`, `source`, `bubble_id`, `bubble_type` (last three optional) | `WelcomeGreetingModel` | new in 3.24.3 |
| [`welcome_cta`](app/anka/welcome_cta.md) | `current_time`, `welcome_type`, `site_count` (int) | `QuestionBankResponse` | new in 3.24.3 |
| [`delete_all_memory`](app/anka/delete_all_memory.md) | none | none read | new in 3.24.3 |
| [`get_question_bank`](app/anka/get_question_bank.md) | `source` (`"aiems"`) | `QuestionBankResponse` | new in 3.24.3; not in `data/endpoints.json` (the URL literal is `/smart_service/v1//app/anka/get_question_bank`, with a double slash) |

The chat transport itself (`/v2/anka/*` history and device-manager URLs built in `anka_agent/http/request.dart`, with a `useWebsocket` flag) is not part of `smart_service` and not documented here.
