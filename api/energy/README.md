> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# energy

Service index for the URL prefix `/energy/`. Each endpoint page is the single owner of its request, response and tags; a skeleton page (status "skeleton", purpose TODO) carries only what `data/endpoints.json` knows and has `Confidence: string-only` until a human reads the asm. Upstream keys are `API_ENDPOINTS` keys of `api/apitypes.py`.

| endpoint | purpose | upstream key | status |
|---|---|---|---|
| [`/energy/v1/backup_report/popup_check`](backup_report/popup_check.md) | Asks whether a new backup report popup is due for the account (a report about a power outage that a backup system bridged) and returns the report summary; the device main page calls it when it opens. | - | hand-written |
| [`/energy/v1/backup_report/report_list`](backup_report/report_list.md) | Lists the backup reports of the account (new reports and reports grouped by year) for the backup report list page. | - | hand-written |
| [`/energy/v1/daily_revenue_card/status`](daily_revenue_card/status.md) | Reads the state of the "yesterday earnings" card of a micro-HES station (status, revenue with currency, link, dynamic-price and abnormal flags). | - | hand-written |
| [`/energy/v1/daily_revenue_card/update_status`](daily_revenue_card/update_status.md) | Tells the cloud that the user has seen or completed the "yesterday earnings" card of a station (the card's tap flow calls it once), so the card status moves on. | - | hand-written |

Not here: MQTT or BLE facts (see [../../mqtt/README.md](../../mqtt/README.md), [../../ble/README.md](../../ble/README.md)), step-by-step flows ([../../flows/README.md](../../flows/README.md)); ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
