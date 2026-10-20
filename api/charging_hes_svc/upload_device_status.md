> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# upload_device_status

## Purpose

Reported the device state (station id, serial number, local time, time stamp, status) from the family main page in 3.18.0 (builder `reportDeviceState`); string-only: no 3.24.3 code references the URL and no caller chain is recorded (string-only: no caller chain in `data/endpoints.json`, inferred from the builder name).

## Upstream name

`none` (no upstream name)

## Method+URL

string-only: `/charging_hes_svc/upload_device_status` exists in 3.24.3 only as a string in the object pool (`blutter_output/pp.txt`, entry `[pp+0x2c858]`); no file of the 3.24.3 asm tree references it, so the Method cannot be read. The 3.18.0 sender was `reportDeviceState` in `charging/ui/page/family/family_main_page_logic.dart` (3.18.0 address 0x1aa2cb4, not present in the 3.24.3 tree).

## Encrypted?

encrypted: not determinable in 3.24.3 (no sender). The 3.18.0 inventory recorded a `requestHttp` call; see `api/encryption.md` for what that wrapper does.

## Request

Not readable in 3.24.3. The five keys come from the 3.18.0 inventory of the builder `reportDeviceState`; their types and required-ness were not read.

| field | type | required | example | source |
|---|---|---|---|---|
| `station_id` | ? | ? | ? | 3.18.0 builder, address 0x1aa2cb4 |
| `sn` | ? | ? | ? | 3.18.0 builder, address 0x1aa2cb4 |
| `local_time` | ? | ? | ? | 3.18.0 builder, address 0x1aa2cb4 |
| `time_stamp` | ? | ? | ? | 3.18.0 builder, address 0x1aa2cb4 |
| `status` | ? | ? | ? | 3.18.0 builder, address 0x1aa2cb4 |

3.18.0 builder read (traced 2026-10-20, 3.18.0 asm tree, not the 3.24.3 app): `reportDeviceState` (`charging/ui/page/family/family_main_page_logic.dart @0x1aa2cb4` in the 3.18.0 tree) builds a `<String, Object>` literal (`@0x1aa2ddc`, array length raw 20 = 10 slots, five pairs, `@0x1aa2cf0`) and sends it with `requestHttp` (`@0x1aa2e50`) and the method object `Obj!Method@2c736e1` (3.18.0 `pp.txt` `[pp+0x9b18]`, `objs.txt` of the 3.18.0 tree, name `post`), so the method was POST in 3.18.0. `station_id` and `status` are stored as received from the parameters (`@0x1aa2d0c`, `@0x1aa2db8`, no conversion), `sn` and `local_time` are strings with the fallback `""` for null (`@0x1aa2d28`, `@0x1aa2d50`), and `time_stamp` is an integer boxed from an unboxed 64-bit value (`BoxInt64Instr` `@0x1aa2d68`). The only 3.18.0 caller is a message-event closure of the same file (`@0x1aa2aa4`) that builds an `A5101DeviceStatusModel` from a map (`fromJson` `@0x1aa29f4`), takes the time as `_getCurrentMicros` divided twice by 1000 (`sdiv` `@0x1aa2a0c`, `@0x1aa2a10`, i.e. seconds) and loads `station_id` from a logic field with the fallback `""` (`@0x1aa2a48`). The page stays string-only because the 3.24.3 app has no sender.

## `param_type`/`cmd`

n/a

## Response model (link)

unknown: no 3.24.3 code references the URL.

## Response

Not stated: no 3.24.3 code references the URL.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "station_id": "<station_id>",
  "sn": "<sn>",
  "local_time": "<local_time>",
  "time_stamp": "<time_stamp>",
  "status": "<status>"
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no 3.24.3 code references the URL.

## Callers in app

- `charging/ui/page/family/family_main_page_logic.dart`: `reportDeviceState` 3.18.0 address 0x1aa2cb4 (requestHttp; encrypted: default-true (requestHttp) — verify)

## Since/changed

3.18.0: present (sender `reportDeviceState`). 3.24.3: string present in the object pool, no code reference found (`tools/out/diff_3.18.0_3.24.3.md` lists the endpoint as removed). since: <=3.18.0; last seen in 3.18.0.

## Known unknowns

- The response handling of the 3.18.0 sender (its success closure) and whether the 3.24.3 app sends the call through another builder: the request side of the 3.18.0 builder is read (see Request); no 3.24.3 code references the URL — traced 2026-10-20
- Whether the server still accepts the endpoint: the 3.24.3 app no longer calls it.
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
