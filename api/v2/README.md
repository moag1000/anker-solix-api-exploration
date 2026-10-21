> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# v2

Service index for the URL prefix `/v2/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/v2/anka/devmgr/sync`](anka/devmgr/sync.md) | Synced device-manager data of the Anka AI assistant (the fourth branch of the 3.18.0 `RequestModel.data`, with the keys `messageId`, `userId`, `manufacturerName`) (3.18.0 asm for the keys; the meaning is string-only, the request class of this branch was not located). | - | removed |
| [`/v2/anka/history/del_msg`](anka/history/del_msg.md) | Deletes chat messages of the Anka AI assistant history (class `AiChatHomeDeleteChatMsgRequestModel`, sent by `Channel.request`) (string-only: the meaning is taken from the class and URL names). | - | owner |
| [`/v2/anka/history/get_msg`](anka/history/get_msg.md) | Fetches a page of the Anka AI assistant chat history (class `AiChatHomeSyncChatMsgRequestModel`, sent by `Channel.request`) (string-only: the meaning is taken from the class and URL names). | - | owner |
| [`/v2/anka/history/update_msg`](anka/history/update_msg.md) | Updates chat messages of the Anka AI assistant history (class `AiChatHomeUpdateChatMsgRequestModel`, sent by `Channel.request`) (string-only: the meaning is taken from the class and URL names). | - | owner |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
