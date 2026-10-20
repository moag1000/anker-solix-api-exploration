> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# event

## Purpose

Reads the guardian journal (timeline) of an S1/S2 device: statistics with the number of stable days, the list of events and the current top event; the home page shows the top event as an unlock sheet when it is unread.

## Upstream name

`none` (no upstream name).

## Method+URL

`POST /power_service/v2/device/timeline/event` (asm-traced): path literal `"/power_service/v2/device/timeline/event"` at `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2a0b814`, method `"POST"` (`@0x2a0b82c`), in `S1S2DeviceCommand.getGuardianJournalEvents` (`@0x2a0b7bc`, static; `url_provider` row in the inventory because no `*Http*` wrapper is called).

## Encrypted?

Direct SDK call (asm-traced), path C of [encryption.md](../../../../encryption.md#which-calls-are-encrypted): ``getGuardianJournalEvents`` builds the map `path`, `method`, `param` and passes it to `akIoTKitManager.handle` with the identifier `akiot.cloud_api` (`s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2a0b8c8`). The decorator tests are not involved; encryption and headers are native to the SDK. The inventory flag `encrypted: false` only means that no `*Http*` wrapper is called.

## Request

`param` is a map literal with one string pair (`r2 = 4`, `@0x2a0b848`); the outer map has `path`, `method`, `param` (`r2 = 12`, `@0x2a0b7fc`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `"<device sn>"` | `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2a0b850`; value is the function argument stored at `@0x2a0b860` |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model class is parsed; the callers read keys from the decoded map. The element layout of `list` and `top_event` is not decoded (keys read: `id`, `is_read`, `type`, `eventLevel`).

## Response

Read by `S1S2HomeLogic._fetchAndShowGuardianUnlockSheet` (`s1_s2/src/page/home/s1_s2_home_logic.dart @0x2a08aa8`, call `@0x2a08b24`). The SDK result `data` is accepted as a JSON text (decoded, log `Parsed data field from JSON string`, `@0x2a08c90`) or as a map; an unexpected type logs `Unexpected data field type` (`@0x2a09320`).

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) or map | yes | `{ ... }` | `s1_s2/src/page/home/s1_s2_home_logic.dart @0x2a08c38` |
| `data.statistics` | map | no | `{ "stable_days": 12 }` | `@0x2a08d84` |
| `data.statistics.stable_days` | not decoded | no | not decoded | `@0x2a08ddc` |
| `data.list` | list | no | `[ ... ]` | `@0x2a08e64` |
| `data.top_event` | map | no | `{ "id": ..., "is_read": false }` | `@0x2a08ec8`; when missing the app logs `No top_event found` (`@0x2a08eec`) |
| `data.top_event.is_read` | bool | no | `false` | `@0x2a08fc4`; when true the sheet is skipped (`top_event already read - skip`, `@0x2a09194`) |
| `data.top_event.id` | not decoded | yes | not decoded | `@0x2a091dc`; a missing `id` logs `top_event missing id field` (`@0x2a09244`); the app then marks the event read with [batch_read](event/batch_read.md) |

The log texts at `@0x2a09270` and `@0x2a0929c` name the fields `type` and `eventLevel` of the top event (parsed by the journal service, not in this function).

## Example request/response

Request, synthesized

```json
{ "path": "/power_service/v2/device/timeline/event", "method": "POST", "param": { "device_sn": "<device sn>" } }
```

Response: no captured response; the layout is from the reading code.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../../errors.md).

## Callers in app

- `S1S2DeviceCommand.getGuardianJournalEvents` (`s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2a0b7bc`) called by `S1S2HomeLogic._fetchAndShowGuardianUnlockSheet` (`s1_s2/src/page/home/s1_s2_home_logic.dart @0x2a08aa8`, call `@0x2a08b24`), by the charge sessions page logic (`s1_s2/src/page/charge_sessions/charge_sessions_logic.dart`, call `@0x2ae89e8`) and by the guardian journal detail page (`s1_s2/src/page/guardian/guardian_journal_detail_logic.dart`, call `@0x2ae9378`). UI: the S1/S2 home page, the charge sessions page and the guardian journal detail page of package `s1_s2`.

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- The element layout of `list` and `top_event` (event types, levels) is not decoded; "guardian" is the app's name for the feature, its meaning (a protection feature of the S1/S2 charger) is inferred. — reclassified: server (the layouts and event types are defined by the server)
- Paging or limits (the request has no such key) are not known.
- Server behaviour is not known.

## Device-tested by

none
