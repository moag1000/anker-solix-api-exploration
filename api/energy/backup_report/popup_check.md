> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# popup_check

## Purpose

Asks whether a new backup report popup is due for the account (a report about a power outage that a backup system bridged) and returns the report summary; the device main page calls it when it opens.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /energy/v1/backup_report/popup_check` (asm-traced). Sender: `ProfileHttpRequestControllerImpl.checkBackupReportPopup` (`charging/http/user/profile/profile_http_request_repository_impl.dart @0x260eff0`); the URL literal is loaded at `@0x260f094` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x260f08c`).

## Encrypted?

Yes by wrapper (asm-traced): `checkBackupReportPopup` calls `HttpRequestControllerImpl.encryptionRequestHttp` (`charging/http/user/profile/profile_http_request_repository_impl.dart @0x260f0c4`) without passing `needEncryption`, so the default `true` applies ([encryption.md](../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../encryption.md)); asm alone does not decide it.

## Request

Body is an empty `<String, dynamic>` map (a `Map._fromLiteral` call with no pairs, `@0x260f054`).

## `param_type`/`cmd`

n/a

## Response model (link)

`BackupReportPopupModel` ([../../../models/backup_report_models.md](../../../models/backup_report_models.md#backupreportpopupmodel)): the success closure (`charging/http/user/profile/profile_http_request_repository_impl.dart @0x260f0e0`) calls `BackupReportPopupModel.fromJson` on the data (`@0x260f110`) and passes the result to the caller's callback (`@0x260f12c`).

## Response

The caller is `DeviceMainLogic._checkBackupReportPopup` (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x260efbc`).

| field | type | required | example | source |
|---|---|---|---|---|
| `has_popup` | bool | no | `true` | `backup_report_popup_model.dart @0x260f17c` |
| `report` | object (`BackupReportPopupItemModel`) | no | `{ "report_id": "...", "outage_start_time": 1760000000, "backup_duration_hours": 2.5, "total_score": 90, "report_url": "..." }` | `backup_report_popup_model.dart @0x260f1fc`; item keys on the [model page](../../../models/backup_report_models.md#backupreportpopupitemmodel) |

## Example request/response

Request, synthesized

```json
{}
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `DeviceMainLogic._checkBackupReportPopup` (`charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart @0x260efbc`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x1215f0`). since: 3.24.3.

## Known unknowns

- The wire shape of the empty request (`{}` versus no body) is not shown here.
- What makes a popup due (a new report since the last one) is decided by the server; the unit of `outage_start_time` is not known.

## Device-tested by

none
