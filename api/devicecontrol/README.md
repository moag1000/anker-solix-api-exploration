> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# devicecontrol

Service index for the URL prefix `/devicecontrol/`. All five endpoints of this service are new in App 3.24.3: none of the URL strings exists in the 3.18.0 object pool. Each endpoint gets its own page, named after the last URL segment; until a page exists the endpoint is listed here with its tag.

| endpoint | method + path | page | tag | source |
|---|---|---|---|---|
| `verify_unlock_default_power_code` | `POST /devicecontrol/v1/device/verify_unlock_default_power_code` | [verify_unlock_default_power_code.md](verify_unlock_default_power_code.md) | `asm-traced` | `http_request_repository_impl.dart @0x30bc0fc` |
| `get_devices_power_config` | `/devicecontrol/v1/get_devices_power_config` | not yet | `string-only` | `pp.txt` entry `pp+0xa57c0` |
| `get_self_check_record` | `/devicecontrol/v1/app/get_self_check_record` | not yet | `string-only` | `pp.txt` entry `pp+0x134840` |
| `self_check_report` | `/devicecontrol/v1/app/self_check_report` | not yet | `string-only` | `pp.txt` entry `pp+0x134bd8` |
| `report_event_data` | `/devicecontrol/v1/app/report_event_data` | not yet | `string-only` | `pp.txt` entry `pp+0x14920` |

For the four `string-only` rows only the path string is known; method, body and callers are not traced yet, so no method is stated.

Not here: request and response details, which live on each endpoint page; ownership rules are in [../../docs/STRUCTURE.md](../../docs/STRUCTURE.md).
