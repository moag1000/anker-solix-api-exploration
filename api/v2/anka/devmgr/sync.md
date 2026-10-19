> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

Removed in 3.24.3 — present in 3.18.0 only

# sync

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/v2/anka/devmgr/sync`, method: not extracted by the inventory <!-- TODO -->; string-only: `anka_agent/http/request.dart @0x220d27c`

## Encrypted?

encrypted: "unknown (URL literal only, no `*Http*` call)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `url` | ? | ? | ? | `anka_agent/http/request.dart @0x220d1ec` |
| `method` | ? | ? | ? | `anka_agent/http/request.dart @0x220d1ec` |
| `country` | ? | ? | ? | `anka_agent/http/request.dart @0x220d1ec` |
| `cloudVersion` | ? | ? | ? | `anka_agent/http/request.dart @0x220d1ec` |
| `useWebsocket` | ? | ? | ? | `anka_agent/http/request.dart @0x220d1ec` |
| `isAIotEnv` | ? | ? | ? | `anka_agent/http/request.dart @0x220d1ec` |
| `user_id` | ? | ? | ? | `anka_agent/http/request.dart @0x220d1ec` |
| `msg_list` | ? | ? | ? | `anka_agent/http/request.dart @0x220d1ec` |
| `page` | ? | ? | ? | `anka_agent/http/request.dart @0x220d1ec` |
| `num` | ? | ? | ? | `anka_agent/http/request.dart @0x220d1ec` |
| `messageId` | ? | ? | ? | `anka_agent/http/request.dart @0x220d1ec` |
| `userId` | ? | ? | ? | `anka_agent/http/request.dart @0x220d1ec` |
| `manufacturerName` | ? | ? | ? | `anka_agent/http/request.dart @0x220d1ec` |

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

- `anka_agent/http/request.dart`: `data` @0x220d1ec (URL literal only, no `*Http*` call)

## Since/changed

3.18.0: present. 3.24.3: absent (removed). since: ≤3.18.0.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
