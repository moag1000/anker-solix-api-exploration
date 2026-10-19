> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# wakeup_oil_machine_bluetooth

## Purpose

Asks the cloud to wake up the Bluetooth of an oil-machine generator (A7320) by serial number; the generator home logic sends it when the generator's Bluetooth must be woken.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /generator/v1/app/wakeup_oil_machine_bluetooth` (asm-traced). Sender: `A7320RequestApi.wakeupOilMachineBluetoothRequest` (`oe_a7320/src/oe_a7320/page/home/a7320_requet_api.dart @0x352af80`); the URL literal (with a leading slash) is loaded at `@0x352afdc` and passed to `AkNetwork.requestHttp` (`@0x352afec`) with the named argument `params` (`@0x352afe4`); the method is fixed to `POST` inside the helper (`base_service/util/ak_util/src/ak_network.dart @0x21c34fc`).

## Encrypted?

Direct SDK call, path C (asm-traced), through the shared helper `AkNetwork.requestHttp` (`a7320_requet_api.dart`, call `@0x352afec`): the helper always sends `POST` and calls `handle` with `akiot.cloud_api` (`base_service/util/ak_util/src/ak_network.dart @0x21c3544`). The inventory row says `encrypted: false` with the note "plain callee; callee default needEncryption=true"; that note does not apply, because `AkNetwork.requestHttp` has no `needEncryption` switch and goes straight to the SDK (mechanics: [sdk_senders.md](../../sdk_senders.md#aknetworkrequesthttp), background: [encryption.md](../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`params`) is a `<String, dynamic>` map of one pair (`r2 = 4`, `@0x352afb0`).

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | String | yes | `<generator sn>` | `a7320_requet_api.dart @0x352afb8`; the argument (the caller passes `""` when no serial is known, `a7320_home_logic.dart @0x352af50`) |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the answer is ignored.

## Response

The sender awaits the result (`@0x352aff8`) and returns nothing; an exception is logged as `wakeupOilMachineBluetoothRequest--...` (`@0x352b030`).

## Example request/response

Request, synthesized

```json
{ "sn": "<generator sn>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `A7320HomeLogic._wakeupOilMachineBluetooth` (`oe_a7320/src/oe_a7320/page/home/a7320_home_logic.dart @0x352af64`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0xab650`). since: 3.24.3.

## Known unknowns

- What the server does (sends a wake-up message to the generator, which then enables its Bluetooth) is inferred from the name; no capture exists.
- Why the app uses the cloud to wake the Bluetooth, and how this relates to the BLE documentation in [../../../ble/README.md](../../../ble/README.md), is not traced.

## Device-tested by

none
