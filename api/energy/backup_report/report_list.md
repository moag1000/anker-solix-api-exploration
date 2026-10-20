> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# report_list

## Purpose

Lists the backup reports of the account (new reports and reports grouped by year) for the backup report list page.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /energy/v1/backup_report/report_list` (asm-traced). Sender: `ProfileHttpRequestControllerImpl.getBackupReportList` (`charging/http/user/profile/profile_http_request_repository_impl.dart @0x298c4b4`); the URL literal is loaded at `@0x298c548` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x298c540`).

## Encrypted?

Yes by wrapper (asm-traced): `getBackupReportList` calls `HttpRequestControllerImpl.encryptionRequestHttp` (`charging/http/user/profile/profile_http_request_repository_impl.dart @0x298c574`) without passing `needEncryption`, so the default `true` applies ([encryption.md](../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../encryption.md)); asm alone does not decide it.

## Request

No body: the sender builds no parameter map. It passes `showLoading: true` (`@0x298c564`).

## `param_type`/`cmd`

n/a

## Response model (link)

`BackupReportListModel` ([../../../models/backup_report_models.md](../../../models/backup_report_models.md#backupreportlistmodel)): the success closure (`charging/http/user/profile/profile_http_request_repository_impl.dart @0x298c590`) calls `BackupReportListModel.fromJson` on the data (`@0x298c5c0`) and passes the result to the caller's callback (`@0x298c5dc`).

## Response

The caller is `AnkerMonthlyReportListLogic.getBackupReportList` (`charging/ui/page/anker_post/anker_monthly_report_list_logic.dart @0x298c48c`).

| field | type | required | example | source |
|---|---|---|---|---|
| `new_reports` | list of `BackupReportItemModel` | no | `[ { "report_id": "...", "site_id": "...", "site_name": "...", "device_sn": "...", "status": "...", "date": "...", "report_url": "..." } ]` | `backup_report_list_model.dart @0x298c62c` |
| `report_groups` | list of `BackupReportGroupModel` (`year`, `reports`) | no | `[ { "year": 2026, "reports": [ ... ] } ]` | `backup_report_list_model.dart @0x298c758`; keys on the [model page](../../../models/backup_report_models.md#backupreportlistmodel) |

## Example request/response

Request, synthesized

```json
{}
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `AnkerMonthlyReportListLogic.getBackupReportList` (`charging/ui/page/anker_post/anker_monthly_report_list_logic.dart @0x298c48c`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x1161a0`). since: 3.24.3.

## Known unknowns

- Paging is not visible: no page parameters are sent, so the answer is presumably the full list.
- The values of `status` and `push_status` per report are not decoded. — reclassified: server (2026-10-20: status values are server data)

## Device-tested by

none
