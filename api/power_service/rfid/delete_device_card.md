> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# delete_device_card

## Purpose

Deletes one RFID card of an EV charger from the cloud list.

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 251, docstring list of endpoints "neither implemented nor explored"); the comment there (no comment on this entry) is the upstream author's note, not a test result.

## Method+URL

`POST /power_service/v1/rfid/delete_device_card` (asm-traced). Sender: `AKIotEVChargeCommand.deleteDeviceCard` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x397a870`). The path literal has no leading slash (`@0x397a8cc`), the method is the string `"POST"` (`@0x397a8e4`), and the map keys `path`, `method`, `param` are stored at `@0x397a8c4`, `@0x397a8d8`, `@0x397a8f0`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x397a980`, call `@0x397a990`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#the-common-envelope), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, String>` map of two pairs (`r2 = 8`, `@0x397a908`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x397a908` |
| `card_number` | String | yes | `<card number>` | `ev_charge_command.dart @0x397a91c` |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>", "card_number": "<card number>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- an anonymous closure in `RfidDetailLogic` (`ev_charger/src/ev_charger/page/home/setting/rfid_cards/rfid_detail/rfid_detail_logic.dart @0x397a74c`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x81b80`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the inventory learned URL literals without a leading slash, which made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- Whether the card is also removed from the charger by this call or only through a BLE command is not known.

## Device-tested by

none
