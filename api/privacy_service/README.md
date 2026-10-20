> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# privacy_service

Service index for the URL prefix `/privacy_service/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/privacy_service/v1/export_account_data`](export_account_data.md) | Requests an export of the user's account data and optionally mails it; sent by `DataExportReposity::exportAccountData` (`charging/ui/page/user/dataExport/data_export_reposity.dart @0x29854bc`) (asm-traced for the sender; the inventory lists no caller, so the screen is not in the chain, string-only). | - | owner |
| [`/privacy_service/v1/export_record_list`](export_record_list.md) | Lists the user's earlier data export requests; sent by `DataExportListReposity::getExportRecordList` (`charging/ui/page/user/dataExport/export_list/data_export_list_reposity.dart @0x2985374`) (asm-traced for the sender; the inventory lists no caller, so the screen is not in the chain, string-only). | - | owner |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
