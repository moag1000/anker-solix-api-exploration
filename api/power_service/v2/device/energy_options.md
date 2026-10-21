> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# energy_options

## Purpose

Asks for the chart options of a device; the only field the app reads is `earliest_date`, the date from which the S1/S2 charge-session chart may start (the app calls it the start-use time).

## Upstream name

`none` (no upstream name).

## Method+URL

`POST /power_service/v2/device/energy_options` (asm-traced): path literal `"/power_service/v2/device/energy_options"` at `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2998ed4`, method literal `"POST"` (`@0x2998eec`), in `S1S2DeviceCommand.getStartUseTime` (`@0x2998e7c`, a static function; the inventory lists it as a `url_provider` row because no `*Http*` wrapper is called).

## Encrypted?

Direct SDK call (asm-traced), path C of [encryption.md](../../../encryption.md#which-calls-are-encrypted): ``getStartUseTime`` builds the map `path`, `method`, `param` and passes it to `akIoTKitManager.handle` with the identifier `akiot.cloud_api` (`s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2998f88`). The decorator tests are not involved; encryption and headers are native to the SDK. The inventory flag `encrypted: false` only means that no `*Http*` wrapper is called.

## Request

`param` is a map literal with one string pair (`<String, String>`, `r2 = 4`, `@0x2998f08`); the outer map has the three keys `path`, `method`, `param` (`r2 = 12`, `@0x2998ebc`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `"<device sn>"` | `s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2998f10`; value is the function argument stored at `@0x2998f20` |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed; the caller reads one key from a decoded map.

## Response

The caller `fetchs1s2StartUseTime` (`s1_s2/src/page/charge_sessions/repository/charger_chart_http_repository.dart @0x2998a9c`, call `@0x2998adc`) reads the SDK result as follows.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) or already a map | yes | `"{\"earliest_date\": \"2024-08-01\"}"` | `s1_s2/src/page/charge_sessions/repository/charger_chart_http_repository.dart @0x2998b6c`; the closure accepts a `String` and runs `jsonDecode` (`@0x2998ba0`), then casts to `Map<String, dynamic>` (`@0x2998bc0`) |
| `data.earliest_date` | String | no | `"2024-08-01"` | `@0x2998bd4`; the string is passed to `DateTime.parse` (`@0x2998c4c`) only when it is a non-empty String (class-id test `@0x2998c34` to `@0x2998c3c`, length test `cbz` `@0x2998c44`), so the app accepts every format that `DateTime.parse` accepts and the example is of that form but not captured; when the key is missing the app logs `No earliest_date from server, using today as startUseTime` (`@0x2998d28`) and uses the current time |

## Example request/response

Request, synthesized

```json
{ "path": "/power_service/v2/device/energy_options", "method": "POST", "param": { "device_sn": "<device sn>" } }
```

Response: no captured response; the `data` layout above is from the reading code.

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `S1S2DeviceCommand.getStartUseTime` (`s1_s2/src/sdk/command/s1_s2_device_command.dart @0x2998e7c`) called by `fetchs1s2StartUseTime` (`s1_s2/src/page/charge_sessions/repository/charger_chart_http_repository.dart @0x2998a9c`, call `@0x2998adc`): the charge-session chart page of the S1/S2 device module (package `s1_s2`).

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- Whether other chart options besides `earliest_date` exist in the answer is not known; the endpoint name (`energy_options`) suggests more.
- Server behaviour is not known.

## Device-tested by

none
