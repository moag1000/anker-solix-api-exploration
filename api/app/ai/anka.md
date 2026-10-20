> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# anka

## Purpose

Not an HTTP request: `AiChatController::getHomePageInitData` (`anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48`) builds the init data map of the Anka agent kit, and `AiChatController::initAnkaAgentKit` (`anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9a0c`) logs it and hands it to the native side with `sendDataToNative` under the event name `aiChatHomePageInit` (`@0x35c9ae8`, call `@0x35c9af8`). The string `/app/ai/anka` is the value of the map key `path` (`@0x35ca73c`), not a URL passed to a `*Http*` wrapper (string-only for the reading of `path` as a route of the native agent).

## Upstream name

`none` (no upstream name)

## Method+URL

No HTTP method and no sender: the string `/app/ai/anka` (`anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca734`) is stored as the value of the key `path` in a `Map<String, dynamic>` literal (type arguments `@0x35c9fb0`) that the app passes to the native agent kit (see Purpose). Nothing in the Dart code calls an `*Http*` wrapper with it (string-only).

## Encrypted?

Not applicable (string-only): the map is not sent by an HTTP wrapper from Dart. Whether the native agent kit encrypts its own requests was not examined.

## Request

Keys of the init data map (not a request body of an HTTP call). The sources are the key literal and the value store in `getHomePageInitData`; the value types of the keys that are read from services are not typed in the asm (`?`). Several values are credentials or identifiers of the session (`userToken`, `userId`, `touristId`, `iotPublicKey`, `openUdid`, `deviceSn`); only their role is documented here, never a value.

| field | type | required | example | source |
|---|---|---|---|---|
| `domain` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca6ac` (value store `@0x35ca6c4`) |
| `exchangeKeyDomain` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca6ec` (value store `@0x35ca704`) |
| `path` | string | yes | `"/app/ai/anka"` | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca72c` (value store `@0x35ca73c`) |
| `appName` | string | yes | `"anker_power"` | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca740` (value store `@0x35ca754`) |
| `userId` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca758` (value store `@0x35ca76c`) |
| `userToken` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca790` (value store `@0x35ca7a4`) |
| `touristId` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca7c8` (value store `@0x35ca7dc`) |
| `iotPublicKey` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca800` (value store `@0x35ca814`) |
| `openUdid` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca838` (value store `@0x35ca84c`) |
| `modelType` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca870` (value store `@0x35ca884`) |
| `appVersion` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca8a8` (value store `@0x35ca8bc`) |
| `osVersion` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca8e0` (value store `@0x35ca8f4`) |
| `osType` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca918` (value store `@0x35ca92c`) |
| `phoneModel` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca950` (value store `@0x35ca964`) |
| `presetKey` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca988` (value store `@0x35ca99c`) |
| `language` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca9c0` (value store `@0x35ca9d4`) |
| `country` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca9f8` (value store `@0x35caa0c`) |
| `timezone` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35caa30` (value store `@0x35caa44`) |
| `deviceSn` | string | yes | `""` | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35caa68` (value store `@0x35caa78`) |
| `isLogined` | ? | yes | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35caa7c` (value store `@0x35caab0`) |

## `param_type`/`cmd`

n/a

## Response model (link)

none: there is no response; the map is delivered to the native side (`sendDataToNative`, `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9af8`).

## Response

No response key exists: the call returns nothing that the code reads (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "domain": "<domain>",
  "exchangeKeyDomain": "<exchangeKeyDomain>",
  "path": "/app/ai/anka",
  "appName": "anker_power",
  "userId": "<userId>",
  "userToken": "<userToken>",
  "touristId": "<touristId>",
  "iotPublicKey": "<iotPublicKey>",
  "openUdid": "<openUdid>",
  "modelType": "<modelType>",
  "appVersion": "<appVersion>",
  "osVersion": "<osVersion>",
  "osType": "<osType>",
  "phoneModel": "<phoneModel>",
  "presetKey": "<presetKey>",
  "language": "<language>",
  "country": "<country>",
  "timezone": "<timezone>",
  "deviceSn": "",
  "isLogined": "<isLogined>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `anka_agent/pages/home/controller/ai_chat_controller.dart`: `getHomePageInitData` @0x35c9f48 (URL literal only, no `*Http*` call)

Called from:

- `anka_agent/pages/home/controller/ai_chat_controller.dart::initAnkaAgentKit`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the native Anka agent kit does with the map and which network requests it makes: the Dart side only passes the data (`sendDataToNative`, `@0x35c9af8`).
- Whether `/app/ai/anka` is a route in the agent's own protocol or an HTTP path the native kit calls: the string is only a map value here. — reclassified: device test row 153 (2026-10-20: the native agent kit is outside the Dart asm)
- Types of the keys that come from services (`userId`, `userToken`, `touristId`, `iotPublicKey`, `openUdid`, `modelType`, `appVersion`, `osVersion`, `osType`, `phoneModel`, `presetKey`, `language`, `country`, `timezone`, `isLogined`): the values are returned by calls whose result types the asm does not show. — attempted 2026-10-20 (two-hop not readable: `initAnkaAgentKit` (`anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9a40`) pass slots or fields of their own frames; no literal or declared type in the argument setups)
- The constants are `appName` (`"anker_power"`), `path` and `deviceSn` (the empty string, `@0x35caa78`).
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
