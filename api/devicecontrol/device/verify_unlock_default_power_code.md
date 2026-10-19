> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# verify_unlock_default_power_code

## Purpose

Checks an unlock code that the user types into the "DIY legal power limit" prompt before the app sets an output limit above the legal limit.

## Upstream name

none; our name `verify_unlock_default_power_code` (no upstream name), taken from the URL.

## Method+URL

`POST /devicecontrol/v1/device/verify_unlock_default_power_code` (asm-traced): URL string at `http_request_repository_impl.dart @0x30bc250` (pool entry `pp+0x171ac8`), method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x30bc248`, in `HttpRequestControllerImpl::verifyUnlockDefaultPowerCode` (`http_request_repository_impl.dart @0x30bc0fc`).

## Encrypted?

Yes (asm-traced): sent through `HttpRequestControllerImpl::encryptionRequestHttp` (`http_request_repository_impl.dart @0x30bc278`). The scheme is described in `api/encryption.md`.

## Request

The body starts as a one-pair map literal (2 slots, raw `r2 = 4`, `@0x30bc150`) holding `unlock_code`. Then exactly one of `device_sn` or `site_id` is added: if the device serial argument is a non-empty string, `device_sn` is added and `site_id` is skipped (`@0x30bc19c` to `@0x30bc1c8`, branch to `@0x30bc218`); otherwise `site_id` is added if it is non-empty (`@0x30bc1cc` to `@0x30bc214`).

| field | type | required | example | source |
|---|---|---|---|---|
| `unlock_code` | String | yes | `"<code typed by the user>"` | `http_request_repository_impl.dart @0x30bc158` (value from parameter r7) |
| `device_sn` | String | only if a device serial is passed; then `site_id` is not sent | `"<device_sn>"` | `http_request_repository_impl.dart @0x30bc1b4` (value from parameter r2) |
| `site_id` | String | only if no device serial is passed | `"<site_id>"` | `http_request_repository_impl.dart @0x30bc204` (value from parameter r5) |

In the station power limit page caller no device serial is passed (see Callers in app for the two callers that pass one), so the app sends `unlock_code` and `site_id`: the sheet field that feeds the serial argument (`DiyLegalPowerLimitSheet` field at offset 0x23, read at `diy_legal_power_limit_sheet.dart @0x30b9454`) is not set by `showOutputPowerPicker`'s closure (`station_power_limit_logic.dart @0x43554c4` to `@0x4355520` sets the type, two callbacks, image, content and the site id only).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model class is parsed; the success closure (`diy_legal_power_limit_sheet.dart @0x30bc3bc`) reads one key from the response object.

## Response

| field | type | required | example | source |
|---|---|---|---|---|
| `verify_result` | bool (nullable; `null` is treated as `false`) | no | `true` | `diy_legal_power_limit_sheet.dart @0x30bc3f8` (key), `bool?` check at `@0x30bc448`, null default `false` at `@0x30bc464` |

## Example request/response

Request, synthesized (decrypted body as built for the station power limit page)

```json
{"unlock_code": "<code>", "site_id": "<site_id>"}
```

Response, synthesized (shape only; whether `verify_result` arrives inside a `data` envelope is not traced)

```json
{"code": 0, "msg": "success", "data": {"verify_result": true}}
```

## Errors seen

None recorded. On a transport or server error the app logs `verifyUnlockDefaultPowerCode fail: code=<code>, msg=<msg>` (`diy_legal_power_limit_sheet.dart @0x30bc328`) and shows the translated text `netWorkError` (`@0x30bc374`). A `verify_result` of `false` shows the translated text `passwordError` (`@0x30bc490`). Error codes are catalogued in `api/errors.md`.

## Callers in app

- `_ImagePasswordContentState::_onConfirm` (`diy_legal_power_limit_sheet.dart @0x30bbea4`, call at `@0x30bc02c`), the confirm button of the image-plus-password variant of `DiyLegalPowerLimitSheet`. It returns without a request when the typed code is empty (`@0x30bbef4`). On `verify_result == true` it calls the sheet's success callback (`@0x30bc0ac`), which closes the sheet and sets the output limit; see [../../../flows/system_output_limit.md](../../../flows/system_output_limit.md).
- Two more callers (flow trace, [../../../flows/diy_unlock.md](../../../flows/diy_unlock.md)): the A17C1 settings power picker callback (`a17c1setting_logic.dart @0x3d91bd4`, sheet allocated at `@0x3d91fa8`, serial slot set at `@0x3d92004`) and the grid-connected settings (`grid_connected_settings_controller.dart`, `showBottomLegal` `@0x2aefffc`, serial store at `@0x2af0164` unless the page is in a site context). The A17C1 picker fills the serial slot; the grid-connected settings caller fills it only when the flag tested at @0x2af00d0 is clear, otherwise it stores null and the request carries `site_id` (sheet offset 0x23) and not the site id, so the request carries `device_sn` instead of `site_id` there. The station page remains the caller that sends `site_id`.

## Since/changed

3.18.0: endpoint not present (the URL string is absent from the 3.18.0 object pool). 3.24.3: new.

## Known unknowns

- Where the unlock code comes from for the user (printed on the device, shown in the image `unlock_pop_image`, given by support); the app only forwards what is typed.
- Whether `verify_result` is the only key of the response and whether it is wrapped in `data`.
- Whether a successful verification changes any server state (for example, allowing values above the legal limit for later `set_site_device_param` calls), or only gates the app UI.

## Device-tested by

none
