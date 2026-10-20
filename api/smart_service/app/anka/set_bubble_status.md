> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# set_bubble_status

## Purpose

Reports the state of the bubble shown on the Anka entry button (for example that the user consumed it) with the bubble id and type and the time.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /smart_service/v1/app/anka/set_bubble_status` (asm-traced). Sender: `AnkaAgentHttp.setBubbleStatus` (`anka_agent/http/bubble_http.dart @0x2bc1558`); the URL literal is loaded at `@0x2bc1764` and the method is `Method.post` (pool entry `pp+0xa7e0`, `@0x2bc175c`).

## Encrypted?

Yes by wrapper (asm-traced): `setBubbleStatus` calls `HttpServiceImpl.encryptionRequestHttpByGHttpRequest` (`anka_agent/http/bubble_http.dart @0x2bc178c`) without passing `needEncryption`, so the default `true` applies ([encryption.md](../../../encryption.md#which-calls-are-encrypted)). The wrapper sends through the global `HttpRequest` object (`gHttpRequest`). Whether the call really goes through the SDK is decided at run time ([encryption.md](../../../encryption.md)); asm alone does not decide it.

## Request

Body is a `<String, dynamic>` map of four pairs (`r2 = 16`, `@0x2bc15ac`); the function logs `[Bubble] setBubbleStatus REQUEST: status=..., bubble_type=..., bubble_id=...` first (`@0x2bc16a0`).

| field | type | required | example | source |
|---|---|---|---|---|
| `status` | String or int (not shown) | yes | `<status>` | `bubble_http.dart @0x2bc15b8`; first argument |
| `bubble_type` | String | yes | `<bubble type>` | `bubble_http.dart @0x2bc15cc`; field `0xb` of the second argument (`@0x2bc15dc`), the bubble object |
| `bubble_id` | String | yes | `<bubble id>` | `bubble_http.dart @0x2bc15e8`; field `0x7` of the second argument (`@0x2bc15f4`) |
| `consume_time` | int | yes | `1760000000` | `bubble_http.dart @0x2bc1600`; the current time in whole seconds: `_getCurrentMicros` (`@0x2bc160c`) divided by 1000 twice (`sdiv`, `@0x2bc163c`, `@0x2bc1640`), boxed with `BoxInt64Instr` (`@0x2bc1644`) |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the answer is passed to the caller's callbacks, no model.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "status": "<status>", "bubble_type": "<bubble type>", "bubble_id": "<bubble id>", "consume_time": 1760000000 }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `BubbleStatusService._retrySingle` (`anka_agent/services/bubble_status_service.dart @0x2bc1544`)
- `BubbleStatusService.report` (`anka_agent/services/bubble_status_service.dart @0x2e0b3b8`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x14c070`). since: 3.24.3.

## Known unknowns

- The values of `status` are not decoded; `BubbleStatusService` (`report`, `_retrySingle`) retries failed reports. — traced 2026-10-20: `BubbleStatusService::report` (`anka_agent/services/bubble_status_service.dart @0x2e0b3b8`) is called with enum constants of `BubbleStatus`: `exposed` (index 0, `bubble_entry_coordinator.dart @0x3580e0c`), `click` (index 1, `bubble_chat_helper.dart @0x35c9380`, `@0x35cc8e0`) and `close` (index 2, `bubble_entry_coordinator.dart @0x2e0af98`); whether the sender puts the enum value strings or an index on the wire is not shown by the page

## Device-tested by

none
