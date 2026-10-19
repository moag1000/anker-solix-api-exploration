> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# anka

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/app/ai/anka`, method: not extracted by the inventory <!-- TODO -->; string-only: `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35ca734`

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `domain` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `exchangeKeyDomain` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `path` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `appName` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `userId` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `userToken` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `touristId` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `iotPublicKey` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `openUdid` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `modelType` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `appVersion` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `osVersion` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `osType` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `phoneModel` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `presetKey` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `language` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `country` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `timezone` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `deviceSn` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |
| `isLogined` | ? | ? | ? | `anka_agent/pages/home/controller/ai_chat_controller.dart @0x35c9f48` |

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `anka_agent/pages/home/controller/ai_chat_controller.dart`: `getHomePageInitData` @0x35c9f48 (URL literal only, no `*Http*` call)

Called from:

- `anka_agent/pages/home/controller/ai_chat_controller.dart::initAnkaAgentKit`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
