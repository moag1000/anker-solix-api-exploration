> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_back_up_history

## Purpose

Loads the backup history list of an A5102 station (`BackupHistoryLogic::getBackupHistoryListFromNet`, called from `BackupHistoryLogic::onReady`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_back_up_history` (asm-traced): URL string at `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x28ef610`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x28ef608`, in `BackupHistoryLogic::getBackupHistoryListFromNet` (`charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x28ef504`), sent through `requestHttp` (`@0x28ef634`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `BackupHistoryLogic::getBackupHistoryListFromNet` (`charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart`, call `@0x28ef634`, argument list `@0x28ef62c`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) Each sender stores its keys in one map literal with type arguments `<String, String>` read at the cited address, so every value is a String: `BackupHistoryLogic::getBackupHistoryListFromNet` (`charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x28ef5c4`, 1 key). No key is behind a null guard.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | string | yes | `"<station_id>"` | `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x28ef5b0` |

## `param_type`/`cmd`

n/a

## Response model (link)

- `charging::BackupHistoryModel`, parsed by `BackupHistoryModel.fromJson` at `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x28ef760` (success closure `@0x28ef6f4`, `bl` target `[package:charging/model/a5101/backup_history_model.dart]`). A second `BackupHistoryModel` exists in package `micro_hes` (`data/models.json`); the `bl` target here is the `charging` one.

## Response

(asm-traced) Top-level keys of the model (`data/models.json`, `charging::BackupHistoryModel`): `events` (int?), `total` (int?), `backUpHistory` (unknown).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`. The failure closure logs `备份历史记录 接口获取 error code=` ("backup history interface error code", my translation) with the code (`charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x28ef698`) and does not compare it.

## Callers in app

- `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart`: `getBackupHistoryListFromNet` @0x28ef504 (requestHttp; encrypted: default-true (requestHttp) — verify)
- `charging/util/demosite_util_impl.dart`: `DemoSiteUtilImpl` @0x4a33a6c (URL literal only, no `*Http*` call)

Called from:

- `charging/boostrap_impl.dart::DIInit`
- `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart::onReady`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- How the entries are sorted and shown: `sortList` is called on the parsed list (`charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x28ef88c`) but the sort key was not read.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
