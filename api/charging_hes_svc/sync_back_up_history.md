> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# sync_back_up_history

## Purpose

Uploads the locally recorded backup-power entries of an A5102 station to the cloud (`BackupHistoryLogic::syncBackUpHistory`, called from `onMessageDispatch`); the success closure logs `备份历史记录 进场备电记录同步到云端成功` ("backup history: entering backup-power records synchronised to the cloud, success", my translation) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/sync_back_up_history` (asm-traced): URL string at `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x2791630`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x2791628`, in `BackupHistoryLogic::syncBackUpHistory` (`charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x2791310`), sent through `requestHttp` (`@0x2791654`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `BackupHistoryLogic::syncBackUpHistory` (`charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart`, call `@0x2791654`, argument list `@0x279164c`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

`BackupHistoryLogic::syncBackUpHistory` (`charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x2791310`) stores 3 keys in a map literal with type arguments `<String, Object>` (`@0x27915e4`), which do not type the values. `syncBackUpHistory` is a growable list with element type `Map<String, dynamic>` (`@0x2791374`), so it is a list; its element maps `{start, end}` come from a `<String, dynamic>` literal (`@0x2791460`) with the values stored as received (`@0x2791448`, `@0x279145c`) and are added only inside a loop guarded at `@0x27913f8`, so the list can be empty. `station_id` is stored as received (`@0x279157c`) and `sn` falls back to the empty string when null (`@0x27915c0`).

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | yes | ? | `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x279156c` |
| `sn` | ? | yes | empty string when the source is null (`charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x27915c0`) | `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x2791580` |
| `syncBackUpHistory` | list | yes | a list of maps with `start` and `end` | `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x27915d4`; `@0x2791374` |
| `syncBackUpHistory[].start` | ? | yes | ? | `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x2791434` |
| `syncBackUpHistory[].end` | ? | yes | ? | `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x279144c` |

## `param_type`/`cmd`

n/a

## Response model (link)

not parsed by the sender (asm-traced): the success closure (`charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x27916f8`) only logs a fixed text (`exeSuccess` `@0x2791718`); the failure closure (`@0x2791678`) logs the code and message (`exeError` `@0x27916dc`).

## Response

No response key is read by the app (see Response model).

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "sn": "<sn>",
  "syncBackUpHistory": "<syncBackUpHistory>",
  "syncBackUpHistory[].start": "<syncBackUpHistory[].start>",
  "syncBackUpHistory[].end": "<syncBackUpHistory[].end>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart`: `syncBackUpHistory` @0x2791310 (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart::onMessageDispatch`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The types of `station_id`, `sn`, `start` and `end`: all are stored as received into `<String, Object>` or `<String, dynamic>` maps.
- The format of `start` and `end` (time stamps or text): the fields of the source object (`field_7`, `field_f`, `charging/ui/page/device/a5102/setting/backup_history/backup_history_logic.dart @0x2791434`, `@0x279144c`) were not resolved.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
