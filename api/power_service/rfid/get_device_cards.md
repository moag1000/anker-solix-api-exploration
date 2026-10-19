> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_device_cards

## Purpose

Lists the RFID cards stored for an EV charger (card number and alias); the RFID cards screen of the charger settings uses it.

## Upstream name

`get_device_rfid_cards` (upstream-confirmed, `api/apitypes.py` line 195; upstream comment: "needs owner. get rfid cards (for EV charger?), {\"device_sn\": deviceSn}").

## Method+URL

`POST /power_service/v1/rfid/get_device_cards` (asm-traced). Sender: `AKIotEVChargeCommand.getDeviceCards` (`ev_charger/src/ev_charger/sdk/command/ev_charge_command.dart` `@0x2ab2340`). The path literal has no leading slash (`@0x2ab2398`), the method is the string `"POST"` (`@0x2ab23b0`), and the map keys `path`, `method`, `param` are stored at `@0x2ab2390`, `@0x2ab23a4`, `@0x2ab23bc`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ev_charge_command.dart @0x2ab2440`, call `@0x2ab2450`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#the-common-envelope), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, String>` map of one pair (`r2 = 4`, `@0x2ab23cc`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<device sn>` | `ev_charge_command.dart @0x2ab23d4` |

## `param_type`/`cmd`

n/a

## Response model (link)

`A5190RfidCardModel` ([../../../models/ev_charger_device_models.md](../../../models/ev_charger_device_models.md#a5190rfidcardmodel)), taken from the type argument of `handle<A5190RfidCardModel>` (ev_charge_command.dart `@0x2ab2430`)

## Response

The SDK result is typed `IoTAKResult<A5190RfidCardModel>`; the keys are on the model page. The wrapper `data` of `A5190RfidCardModel.fromJson` is described there. The caller reads the result type before using the data.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) or map | no |  | `a5190_rfid_card_model.dart @0x45b2164` |
| `list` | list of `RfidCardModel` (`card_number`, `alias_name`) | no | `[ { "card_number": "...", "alias_name": "..." } ]` | `a5190_rfid_card_model.dart @0x45b2248`, `@0x45b2420`, `@0x45b24a8`; [models/ev_charger_device_models.md](../../../models/ev_charger_device_models.md#a5190rfidcardmodel) |

## Example request/response

Request, synthesized

```json
{ "device_sn": "<device sn>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `RfidCardsLogic.getCardData` (`ev_charger/src/ev_charger/page/home/setting/rfid_cards/rfid_cards_logic.dart @0x2ab1fa4`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x81c60`); the sender function has no literal difference between 3.18.0 and 3.24.3 (`tools/cmp_since.py`: ordered string, integer and type literals compared; branch logic not compared). Not new in 3.24.3: the inventory learned URL literals without a leading slash, which made the URL visible. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- The card number format (hex, decimal, length) is not shown; the charger reports the number over BLE (`readRfidCardNumber`) when a card is added by reading.

## Device-tested by

none
