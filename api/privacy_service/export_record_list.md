> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# export_record_list

## Purpose

Lists the user's earlier data export requests; sent by `DataExportListReposity::getExportRecordList` (`charging/ui/page/user/dataExport/export_list/data_export_list_reposity.dart @0x2985374`) (asm-traced for the sender; the inventory lists no caller, so the screen is not in the chain, string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /privacy_service/v1/export_record_list` (asm-traced): URL string at `charging/ui/page/user/dataExport/export_list/data_export_list_reposity.dart @0x29853fc`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x29853f4`, in `DataExportListReposity::getExportRecordList` (`charging/ui/page/user/dataExport/export_list/data_export_list_reposity.dart @0x2985374`), sent through `encryptionRequestHttp` (`@0x2985424`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No body field: the sender builds an empty map literal (`Map._fromLiteral` `charging/ui/page/user/dataExport/export_list/data_export_list_reposity.dart @0x29853c0`, no key store before it).

## `param_type`/`cmd`

n/a

## Response model (link)

no top-level model: the success closure (`charging/ui/page/user/dataExport/export_list/data_export_list_reposity.dart @0x29856c4`) reads the key `record_list` (key string `@0x2985700`, lookup `@0x2985720`), tests it for `List` (`@0x29857c8`) and maps each element with `DataExportListItemModel.fromJson` (`@0x2985954`, element closure `@0x298591c`, call target `#0x298596c`, `charging/model/privacy_policy/data_export_list_item_model.dart`) to a `List<DataExportListItemModel>` for the callback (`ClosureCall` `@0x2985884`). A missing list gives an empty list (`@0x29858cc`); a value that is not a list calls the failure callback with the client-side code raw 20004 (a tagged Smi, so 10002, `@0x29858e4`) and the text `data is not List`.

## Response

(asm-traced) One key is read from the top level of the response: `record_list` (list). Keys of `charging::DataExportListItemModel` (`data/models.json`, no page under `models/`): `account` (unknown), `send_status` (int?), `send_email` (unknown), `apply_time` (int?).

## Example request/response

Request: no body fields are built (see Request). Response: not synthesized; no capture exists for this endpoint.

## Errors seen

No server code is compared. The closure itself raises the client-side code 10002 (raw 20004 in a tagged slot, `charging/ui/page/user/dataExport/export_list/data_export_list_reposity.dart @0x29858e4`) with the text `data is not List` when `record_list` is not a list. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/ui/page/user/dataExport/export_list/data_export_list_reposity.dart`: `getExportRecordList` @0x2985374 (encryptionRequestHttp; encrypted: true)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The types of `account` and `send_email` in the item model (`unknown` in `data/models.json`).
- What `send_status` values mean (sent, pending, failed): the model key is typed `int?`; the table of values is not visible. — reclassified: server (2026-10-20: the app only forwards `send_status`; the value table is not derivable here)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
