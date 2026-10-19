> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# Backup report models

## Purpose

Carries the answers of the backup-report endpoints: the popup check (is there a new report, with the report summary) and the report list (new reports and reports grouped by year); a backup report most probably describes a power outage that a backup system bridged (inferred from the key names `outage_start_time` and `backup_duration_hours`).

## Dart class + file

`BackupReportPopupModel` (`charging/ui/page/user/main/backup_report/models/backup_report_popup_model.dart`); `BackupReportPopupItemModel` (`charging/ui/page/user/main/backup_report/models/backup_report_popup_model.dart`); `BackupReportListModel` (`charging/ui/page/user/main/backup_report/models/backup_report_list_model.dart`); `BackupReportGroupModel` (`charging/ui/page/user/main/backup_report/models/backup_report_list_model.dart`); `BackupReportItemModel` (`charging/ui/page/user/main/backup_report/models/backup_report_list_model.dart`). `fromJson` addresses are under each class below.

## Fields

Every `source` address is the string load of the JSON key inside the class `fromJson` and was re-read in the asm. Dart types and nullability come from `tools/model_fields.py` (`data/models.json`); an "of `X`" note is the list element class read from the `<X>` type argument next to the key.

### BackupReportPopupModel

Answer of `popup_check`: whether a popup is due and the report it refers to.

`fromJson` `backup_report_popup_model.dart @0x260f150`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `has_popup` | `bool` | yes | 3.24.3 | `backup_report_popup_model.dart @0x260f17c` |
| `report` | `BackupReportPopupItemModel?` | yes | 3.24.3 | `backup_report_popup_model.dart @0x260f1fc` |

### BackupReportPopupItemModel

The report summary inside `BackupReportPopupModel.report`.

`fromJson` `backup_report_popup_model.dart @0x260f5a4`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `report_id` | `String` | yes | 3.24.3 | `backup_report_popup_model.dart @0x260f5d0` |
| `outage_start_time` | `int` | yes | 3.24.3 | `backup_report_popup_model.dart @0x260f65c` |
| `backup_duration_hours` | `num?` | yes | 3.24.3 | `backup_report_popup_model.dart @0x260f6e4` |
| `total_score` | `int?` | yes | 3.24.3 | `backup_report_popup_model.dart @0x260f7b0` |
| `report_url` | `String` | yes | 3.24.3 | `backup_report_popup_model.dart @0x260f828` |

### BackupReportListModel

Answer of `report_list`: new reports and the year groups.

`fromJson` `backup_report_list_model.dart @0x298c600`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `new_reports` | `List<BackupReportItemModel>` | no | 3.24.3 | `backup_report_list_model.dart @0x298c62c` |
| `report_groups` | `List<BackupReportGroupModel>` | no | 3.24.3 | `backup_report_list_model.dart @0x298c758` |

### BackupReportGroupModel

One year group in `BackupReportListModel.report_groups`.

`fromJson` `backup_report_list_model.dart @0x298cf68`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `year` | `int` | yes | 3.24.3 | `backup_report_list_model.dart @0x298cf94` |
| `reports` | `List<BackupReportItemModel>` | no | 3.24.3 | `backup_report_list_model.dart @0x298d01c` |

### BackupReportItemModel

One report in a group or in `new_reports`.

`fromJson` `backup_report_list_model.dart @0x298d1b4`.

| JSON key | Dart type | nullable | since | source |
|---|---|---|---|---|
| `report_id` | `String` | yes | 3.24.3 | `backup_report_list_model.dart @0x298d1e0` |
| `site_id` | `String` | yes | 3.24.3 | `backup_report_list_model.dart @0x298d26c` |
| `site_name` | `String` | yes | 3.24.3 | `backup_report_list_model.dart @0x298d2f8` |
| `device_sn` | `String` | yes | 3.24.3 | `backup_report_list_model.dart @0x298d384` |
| `status` | `String` | yes | 3.24.3 | `backup_report_list_model.dart @0x298d410` |
| `push_status` | `String` | yes | 3.24.3 | `backup_report_list_model.dart @0x298d49c` |
| `backup_duration_hours` | `num?` | yes | 3.24.3 | `backup_report_list_model.dart @0x298d528` |
| `date` | `String` | yes | 3.24.3 | `backup_report_list_model.dart @0x298d5f0` |
| `data_incomplete` | `bool` | yes | 3.24.3 | `backup_report_list_model.dart @0x298d67c` |
| `report_url` | `String` | yes | 3.24.3 | `backup_report_list_model.dart @0x298d704` |
| `total_score` | `int?` | yes | 3.24.3 | `backup_report_list_model.dart @0x298d790` |

## Produced by

- [`popup_check`](../api/energy/backup_report/popup_check.md): `BackupReportPopupModel` (`BackupReportPopupModel.fromJson` call `charging/http/user/profile/profile_http_request_repository_impl.dart @0x260f110`)
- [`report_list`](../api/energy/backup_report/report_list.md): `BackupReportListModel` (`fromJson` call `profile_http_request_repository_impl.dart @0x298c5c0`)

## Consumed by

The device main page (`_checkBackupReportPopup`) and the monthly/backup report list page (`anker_monthly_report_list_logic.dart`); field-level use is not traced.

## Changed since 3.18.0

All five classes are new in 3.24.3 (every key is marked `3.24.3`).

## Known unknowns

- The values of `status` and `push_status` (strings) and the unit of `outage_start_time` are not decoded.
- `backup_duration_hours` and `total_score` are nullable; how the score is computed is not shown in the app.
- The format of `report_url` (a web page or a file) is not known.
