> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# batch_read

## Purpose

Marks guardian journal events of an S1/S2 device as read; the home page sends the id of the top event after showing it.

## Upstream name

`none` (no upstream name).

## Method+URL

`POST /power_service/v2/device/timeline/event/batch_read` (asm-traced): path literal at `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2a09748`, method `"POST"` (`@0x2a09760`), in `S1S2DeviceCommand.markGuardianEventsAsRead` (`@0x2a096ec`, static; `url_provider` row in the inventory).

## Encrypted?

Direct SDK call (asm-traced), path C of [encryption.md](../../../../../encryption.md#which-calls-are-encrypted): ``markGuardianEventsAsRead`` builds the map `path`, `method`, `param` and passes it to `akIoTKitManager.handle` with the identifier `akiot.cloud_api` (`s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2a09810`). The decorator tests are not involved; encryption and headers are native to the SDK. The inventory flag `encrypted: false` only means that no `*Http*` wrapper is called.

## Request

`param` is a map literal with two pairs (`r2 = 8`, `@0x2a0977c`); the outer map has `path`, `method`, `param` (`r2 = 12`, `@0x2a09730`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `"<device sn>"` | `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2a09784`; function argument stored at `@0x2a09794` |
| `event_ids` | list | yes | `[ "<event id>" ]` | `@0x2a09798`; function argument stored at `@0x2a097a8`; the home page builds a one-element growable list (`AllocateGrowableArray`, `s1_s2/src/page/home/s1_s2_home_logic.dart @0x2a0952c`) from the `id` of the top event; the element type is not decoded |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed.

## Response

No response field is read by the traced caller (asm-traced). `S1S2HomeLogic._markGuardianEventAsRead` (`s1_s2/src/page/home/s1_s2_home_logic.dart @0x2a09470`, call `@0x2a09550`) checks only success: on success it logs `Successfully marked event ... as read` (`@0x2a09598`), on failure `Failed to mark as read` (`@0x2a095e8`).

## Example request/response

Request, synthesized

```json
{ "path": "/power_service/v2/device/timeline/event/batch_read", "method": "POST", "param": { "device_sn": "<device sn>", "event_ids": [ "<event id>" ] } }
```

Response: no captured response; no field is read.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../../../../encryption.md#response-handling-and-error-codes). `api/errors.md` does not exist yet (Task 4.2).

## Callers in app

- `S1S2DeviceCommand.markGuardianEventsAsRead` (`s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2a096ec`) called by `S1S2HomeLogic._markGuardianEventAsRead` (`s1_s2/src/page/home/s1_s2_home_logic.dart @0x2a09470`, call `@0x2a09550`) and by the guardian journal detail page (`s1_s2/src/page/guardian/guardian_journal_detail_logic.dart`, call `@0x2ae9db8`). UI: the S1/S2 home page unlock sheet and the guardian journal detail page (package `s1_s2`).

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- The type of the ids (the journal events carry an `id` field, see [event](../event.md#response)) is not decoded.
- Whether the server accepts several ids in one call is likely from the name (`batch_read`) but the app sends one.
- Server behaviour is not known.

## Device-tested by

none
