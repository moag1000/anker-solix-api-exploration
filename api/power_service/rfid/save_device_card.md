> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# save_device_card

## Purpose

Stores one RFID card (number and alias) for an EV charger in the cloud; the add-card and edit-card screens call it after the card was written to the charger over BLE.

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (line 250, docstring list of endpoints "neither implemented nor explored"); the comment there (no comment on this entry) is the upstream author's note, not a test result.

## Method+URL

`POST /power_service/v1/rfid/save_device_card` (asm-traced). Sender: `AKIotEVChargeCommand.saveDeviceCard` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x3216c54`). The path literal has no leading slash (`@0x3216cb4`), the method is the string `"POST"` (`@0x3216ccc`), and the map keys `path`, `method`, `param` are stored at `@0x3216cac`, `@0x3216cc0`, `@0x3216cd8`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x3216d7c`, call `@0x3216d8c`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#the-common-envelope), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, String>` map of three pairs (`r2 = 12`, `@0x3216ce8`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x3216cf0` |
| `card_number` | String | yes | `<card number>` | `ev_charge_command.dart @0x3216d04` |
| `alias_name` | String | yes | `Garage card` | `ev_charge_command.dart @0x3216d18` |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument.

## Response

Not parsed by the sender.

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>", "card_number": "<card number>", "alias_name": "Garage card" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `RfidTools.addRfidCard` (`ev_charger/src/ev_charger/page/home/setting/rfid_cards/tools/rfid_tools.dart @0x3216a70`)
- an anonymous closure in `RfidDetailLogic` (`ev_charger/src/ev_charger/page/home/setting/rfid_cards/rfid_detail/rfid_detail_logic.dart @0x397b064`)

Order of the BLE write and this call (asm-traced): `RfidTools.addRfidCard` (`ev_charger/src/ev_charger/page/home/setting/rfid_cards/tools/rfid_tools.dart`) shows the loading indicator (`showLoading` `@0x32169c4`), calls the BLE command `setRfidCard` (`@0x32169d4`), awaits it (`Await` `@0x32169e0`) and only then calls `saveDeviceCard` (`@0x3216a70`), so there the card is written to the charger first and saved to the cloud afterwards. The `RfidDetailLogic` closure (`ev_charger/src/ev_charger/page/home/setting/rfid_cards/rfid_detail/rfid_detail_logic.dart`) calls `showLoading` (`@0x397afa4`), trims a text value (`trim` `@0x397afd0`, `value()` `@0x397b040`) and calls `saveDeviceCard` (`@0x397b064`) without a `setRfidCard` call in that closure.

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x68f60`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the inventory learned URL literals without a leading slash, which made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- Whether the same call renames an existing card (same `card_number`) or creates a duplicate is not known.

## Device-tested by

none
