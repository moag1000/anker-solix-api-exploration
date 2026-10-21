> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

3.24.3: string present in the object pool, no code reference found (present in 3.18.0 with a sender)

# set_port_protocol_status

## Purpose

Saves the per-port protocol selection of a charger from the custom-protocol manager (callers `saveToAllPorts` in `CustomProtocolManagerLogic` and the A2345 protocol-manage logic) (string-only: the sender body is not in the asm dump; the caller names are read, the meaning comes from names only).

## Upstream name

`none` (no upstream name)

## Method+URL

`/mini_power/v1/app/setting/set_port_protocol_status`, method: not extracted (string-only). The 3.24.3 object pool holds the URL string (`pp+0xa3890`), but no decoded function references it: the senders are mixin-deduplicated functions (`[dart:mixin_deduplication]`) whose bodies Blutter did not write to the asm dump, so neither the method object nor the key stores can be read. Call sites in 3.24.3:

- `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart`: `saveToAllPorts` (`@0x3a7764c`) calls the mixin function at `@0x3a77738`, passing an instance of `PortProtocolSetType` (`@0x3a77730`); a second call is at `@0x3a78360`.
- `charging/ui/page/device/a2345/a2345prococol_manage/a2345protocol_manage_logic.dart`: calls at `@0x3e646c8` and `@0x3e65558`.

## Encrypted?

encrypted: `true` per the 3.18.0 inventory (`encryptionRequestHttp`); not re-read in 3.24.3 because the sender body is not in the asm dump. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

Not re-read in 3.24.3: the sender is a mixin-deduplicated function whose body is not in the asm dump (see Method+URL), so the keys below are the 3.18.0 inventory rows (`data/endpoints.json`); their addresses do not exist in the 3.24.3 asm and are therefore not cited. Types and requiredness in the table are from the 3.18.0 builder read below, not from 3.24.3.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String (3.18.0 builder) | yes (3.18.0) | `<device sn>` | 3.18.0 builder, see below; not present in the 3.24.3 asm |
| `version` | String (3.18.0 builder) | yes (3.18.0) | `"v1.1.1"` | 3.18.0 builder, see below; not present in the 3.24.3 asm |
| `type` | String (3.18.0 builder) | yes (3.18.0) |  | 3.18.0 builder, see below; not present in the 3.24.3 asm |
| `port_list` | list of maps (3.18.0 builder) | yes (3.18.0) |  | 3.18.0 builder, see below; not present in the 3.24.3 asm |

3.18.0 builder read (traced 2026-10-20, 3.18.0 asm tree, not the 3.24.3 app): `setPortProtocolStatus` (`small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart 0x246dd88` in the 3.18.0 tree) fills a `<String, Object>` literal (`0x246ded8`, 16 slots = 4 pairs `0x246de00`) with `device_sn` (parameter, `0x246de0c`), `version` (the constant string `"v1.1.1"`, `0x246de2c`), `type` (`field_13` of the `PortProtocolSetType` argument, `0x246de44`) and `port_list` (the list argument mapped with `map<Map<String, dynamic>>` through `PortInfo::toJson` and `toList`, `0x246de50`..`0x246de9c`), and sends it with `encryptionRequestHttp` (`0x246df50`) and the method object `Obj!Method@2c736e1` (name `post`), so POST in 3.18.0. `type` is a string: the enum `PortProtocolSetType` carries a text value, `"apply_to_all"` for `applyToAll` (index 1) and `"ports"` for `singlePort` (index 0) (`objs.txt Obj!PortProtocolSetType@38f6521`, `Obj!PortProtocolSetType@38f6541`, field `off_14`; the 3.24.3 call site passes an instance of this enum, `custom_protocol_manager_logic.dart @0x3a77730`). The elements of `port_list` are `PortInfo` maps with the keys `title`, `ports`, `protocols` (a list of `Protocol` maps with the keys `name` and `status`) and `tlv` (`small_charging_platform/src/custom_protocol/model/port_protocol_status_model.dart`, `PortInfo::toJson` `@0x285a384`..`@0x285a59c`, `Protocol::toJson` `@0x285aaa4`, `@0x285ab24` in the 3.24.3 tree). The page stays `string-only` because the 3.24.3 sender body is not in the dump.

## `param_type`/`cmd`

n/a

## Response model (link)

not extracted: the sender body is not in the asm dump, so the response handling cannot be read (the callbacks passed at the call site are closures `@0x3a77ae8` and `@0x3a77a0c` of `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart`, not read).

## Response

No response key is confirmed read (see Response model).

## Example request/response

Request: not synthesized (the keys are not re-read in 3.24.3, see Request).

Response: not synthesized (no capture exists for this endpoint).

## Errors seen

none traced: the sender body is not in the asm dump, so the failure path of the request is not readable. Code meanings are owned by `api/errors.md`.

## Callers in app

- `small_charging_platform/src/custom_protocol/page/custom_protocol_manager_logic.dart`: `setPortProtocolStatus` (3.18.0 inventory, encryptionRequestHttp; address not present in the 3.24.3 asm)

## Since/changed

3.18.0: present (with a sender in the inventory). 3.24.3: the URL string is in the object pool (`pp+0xa3890`) and the callers listed under Method+URL still call the sender, but the sender body is not in the asm dump; `tools/out/diff_3.18.0_3.24.3.md` lists the URL under Removed endpoints (string-level). since: <=3.18.0. Treat the URL as still in use (the callers exist) until a capture says otherwise.

## Known unknowns

- The method, request keys and types of the 3.24.3 sender: the 3.18.0 builder is read (see Request), the 3.24.3 mixin-deduplicated body is not in the dump — traced 2026-10-20
- How the answer is used: the callbacks were not read. — traced 2026-10-20 (3.18.0 tree): the builder passes the same shared closures as `get_port_protocol_status` (success `charging/http/http_request_repository_impl.dart 0x19dc8a8`, which forwards its argument to the stored callback unchanged); what the callbacks of `CustomProtocolManagerLogic` do with the value was not decoded
- Header stays `string-only` because Method, request types and response handling are missing. — rechecked 2026-10-20: still true; the typing attempts are recorded on the bullets of this section
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
