> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# set_modbus_setting

## Purpose

Stores the Modbus (third-party control) state of a device in the cloud: which variant is enabled (off, Modbus TCP or Modbus RTU), the RTU slave id, and whether the device was already configured over Bluetooth.

## Upstream name

`none` (no upstream name): `api/apitypes.py` has no key for this URL.

## Method+URL

`POST /charging_hes_third_party_service_svc/set_modbus_setting` (asm-traced): URL string `pp+0xb75b8` at `home_assistant_logic.dart @0x38db248`, method object `Method.post` (pool entry `pp+0xa7e0`, `off_10: "post"`) at `@0x38db240`, in `HomeAssistantLogic::saveSetId` (`home_assistant_logic.dart @0x38db0b8`).

## Encrypted?

Yes (asm-traced): `saveSetId` calls `HttpServiceImpl::encryptionRequestHttp` (`home_assistant_logic.dart @0x38db270`) with the loading overlay on (`showLoading: true`, `@0x38db258`). The scheme is described in `api/encryption.md`.

## Request

The body is a map literal with six key/value pairs (raw `r2 = 24`, i.e. 12 slots, `home_assistant_logic.dart @0x38db148`). Values come from the route arguments of the third-party control page (`HomeAssistantLogic::onInit`, `home_assistant_logic.dart @0x35eaa34`) and from the switches on that page.

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | String | yes | `"<device_sn>"` | `home_assistant_logic.dart @0x38db150`; route argument `deviceSn` (`@0x35eab50`) |
| `pn` | String | yes | `"A17X8"` | `home_assistant_logic.dart @0x38db164`; route argument `productCode` (`@0x35eabf0`); the smart plug page passes the string literal `"A17X8"` (`a17x8setting_logic.dart @0x3ddeb50`) |
| `modbusStatus` | int | yes | `1` | `home_assistant_logic.dart @0x38db178`; value of `modbusState()` (`@0x38db538`), tagged with `lsl x2, x1, #1` before the 32-bit store (`@0x38db188`), so the stored number is the function's plain return value: 1 when the Modbus TCP switch is on (`mov x0, #1`, `@0x38db568`, unboxed return), 2 when the Modbus RTU switch is on (`mov x0, #2`, `@0x38db58c`, unboxed), 0 when both are off (`mov x0, #0`, `@0x38db59c`, unboxed). |
| `rtuId` | int or null | no (null for TCP) | `1` | `home_assistant_logic.dart @0x38db190`; named argument, default `null` (`@0x38db0c4`). Only the RTU path passes it: `int.parse` of the RTU id text field (`openSwichRequest`, `@0x38db040`), boxed at `@0x38db06c`. The TCP path calls `saveSetId` without it (`@0x38db018`), so `rtuId` is sent as `null`. Accepted input range 1 to 255 (see the note below the table). |
| `siteId` | String | yes (may be empty) | `"<site_id>"` or `""` | `home_assistant_logic.dart @0x38db1a4`; `StationDeviceManager::getSiteIdByDeviceSn(deviceSn)` when the route argument `isSite` is `true` (`@0x38dae38`, `@0x38dae54`), otherwise the empty string literal `""` (`@0x38dae60`) |
| `isBluetooth` | bool | yes | `false` | `home_assistant_logic.dart @0x38db1b8`; field set by `checkConnectionEnvironment` (`@0x38dbf30`): `true` only on the RTU path when the device Wi-Fi is offline and the local (Bluetooth) connection is up (`@0x38dc090`), `false` otherwise (`@0x38dbfb4`, `@0x38dc054`). When it is `true` the app has already sent the same setting to the device through the IoT kit before this request (`@0x38daeb0`), see [../../devices/modbus.md](../../devices/modbus.md#bluetooth-path-iot-kit-action). |

RTU id input rule (`checkIdLength`, `home_assistant_logic.dart @0x38dabc0`): the field only accepts digits (`FilteringTextInputFormatter.digitsOnly`, `@0x38da9e8`); a value with more than one character that starts with `"0"` is rejected (length compare `cmp x2, #1` on the untagged length, `@0x38dac1c`, so 1; `startsWith("0")`, `@0x38dac30`); the parsed value must be at most 255 (`cmp x0, #0xff` on the result of `int.parse`, unboxed, `@0x38dac80`) and at least 1 (`cmp x0, #1`, unboxed, `@0x38dac88`). Otherwise the dialog shows the key `exceedTheLimit` and the save button stays disabled.

`modbusStatus` uses the same numbers that [query_modbus_setting](query_modbus_setting.md#response) returns. TCP and RTU are mutually exclusive in the app: switching one on switches the other off before the request (`home_assistant_page.dart @0x38dca30` to `@0x38dcaa0`).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed. The success closure (`home_assistant_logic.dart @0x38db384`) only checks that the payload is a `Map`.

## Response

No response field is read (asm-traced, `home_assistant_logic.dart @0x38db384`). If the payload is a `Map`, the app copies the RTU id text into its display value, reports success to the page, and logs `setCommunicationSetting success:<payload>` (`@0x38db4f8`). The failure closure receives an int code and a String message (`@0x38db290`).

| field | type | required | example | source |
|---|---|---|---|---|
| (none read) | | | | `home_assistant_logic.dart @0x38db384` |

## Example request/response

Request, synthesized (decrypted body as built by `saveSetId` when the user enables Modbus RTU with id 1 over the cloud path; `modbusStatus` and the id range are cited in the Request table)

```json
{
  "sn": "<device_sn>",
  "pn": "<product_code>",
  "modbusStatus": 2,
  "rtuId": 1,
  "siteId": "",
  "isBluetooth": false
}
```

Response, synthesized (shape only; no captured response exists)

```json
{"code": 0, "msg": "success", "data": {}}
```

## Errors seen

None recorded. On any failure the app shows the toast key `requestTimeout` (`home_assistant_logic.dart @0x38db2dc`), reports failure to the page, which puts the switch back (see [../../flows/modbus_setup.md](../../flows/modbus_setup.md#failure-paths)), and logs `setCommunicationSetting fail:<code> ---- <msg>` (`@0x38db32c`). Error codes are catalogued in `api/errors.md`.

## Callers in app

- `HomeAssistantLogic::saveSetId` (`home_assistant_logic.dart @0x38db0b8`) is the only sender. It is called twice in `openSwichRequest` (`@0x38dadc4`): without `rtuId` for Modbus TCP (`@0x38db018`) and with `rtuId` for Modbus RTU (`@0x38db0a0`).
- `openSwichRequest` is reached from the TCP and RTU switches on the third-party control page (closure `home_assistant_page.dart @0x38dc9cc`, call at `@0x38dcb00`) and from the RTU id edit dialog (closures `home_assistant_logic.dart @0x38dace0`, `@0x38dc360`). The whole sequence is on [../../flows/modbus_setup.md](../../flows/modbus_setup.md).

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool). 3.24.3: new.

## Known unknowns

- What the server does with the setting: whether it forwards it to the device (for example over MQTT) or only records it. The app sends the cloud request also after a successful Bluetooth write (`isBluetooth: true`), which suggests the record is kept in the cloud, but this is not verified.
- Whether the server validates `rtuId` (1 to 255 is enforced only by the app) and how it treats `rtuId: null` on the TCP path.
- Whether `modbusStatus` values other than 0, 1 and 2 exist.
- Whether `siteId` may stay empty for devices that belong to a site.

## Device-tested by

none
