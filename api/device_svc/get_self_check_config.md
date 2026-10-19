> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_self_check_config

## Purpose

Reads the cloud-defined self-check texts (title, text, image, type per check id) for a product, so the self-check and self-check-failure screens of the initial setup can explain a failed check.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /device_svc/v1/get_self_check_config` (asm-traced). Two senders: `SelfCheckController._loadCloudSelfCheckConfig` (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2ad0f98`; URL literal `@0x2ad1184`) and `SelfCheckFailController.loadCloudSelfCheckConfig` (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_fail_controller.dart @0x2ad2054`; URL literal `@0x2ad21b0`); both use `Method.post` (pool entry `pp+0xa7e0`, `@0x2ad117c`, `@0x2ad21a8`).

## Encrypted?

Yes by wrapper (asm-traced): both senders call `HttpServiceImpl.encryptionRequestHttp` (`self_check_controller.dart @0x2ad11a8`; `self_check_fail_controller.dart @0x2ad21d8`) with named arguments `fail` and `success` (and `showLoading` in the second) and without `needEncryption`, so the default `true` applies ([encryption.md](../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time ([encryption.md](../encryption.md)); asm alone does not decide it.

## Request

Body is a map of two pairs; the first key is the same in both senders, the second differs (`r2 = 8`, `@0x2ad1084`; `@0x2ad20d4`).

| field | type | required | example | source |
|---|---|---|---|---|
| `productCode` | String | yes | `A5191` | `self_check_controller.dart @0x2ad1090`; `self_check_fail_controller.dart @0x2ad20e0`; the product code of the device being set up (placeholder PN in the example) |
| `checkIds` | list of int (one element) | yes (first sender) | `[20000004]` | `self_check_controller.dart @0x2ad10a4`; the list holds the integer returned by `failureCode()` (`@0x2ad10b4`, boxed with `BoxInt64Instr` `@0x2ad10d4`) |
| `errorBits` | list of int (one element) | yes (second sender) | `[4]` | `self_check_fail_controller.dart @0x2ad20fc`; the list holds the integer field `0x4b` of the controller (`@0x2ad2108`, boxed `@0x2ad2128`) |

`checkIds` and `errorBits` are alternatives: the self-check screen asks by failure code, the failure screen by error bits. The example values are placeholders (compare the failure codes on [self_check_report](../devicecontrol/app/self_check_report.md)).

## `param_type`/`cmd`

n/a

## Response model (link)

`SelfCheckConfigItem` ([../../models/self_check_config_model.md](../../models/self_check_config_model.md#selfcheckconfigitem)): the success closure calls `SelfCheckConfigModel.fromJson` on the data (`self_check_controller.dart @0x2ad1354`) and adds its items to a list of `SelfCheckConfigItem` (`@0x2ad1324`, `addAll` `@0x2ad1378`).

## Response

Success closure of the first sender: `@0x2ad12fc`; the second sender's closure is `@0x2ad195c` (it first checks that the data is a `List`). Exceptions are logged as ` _loadCloudSelfCheckConfig exception: ...` (`@0x2ad11fc`, `@0x2ad2278`).

| field | type | required | example | source |
|---|---|---|---|---|
| `<list>` | list of `SelfCheckConfigItem` | no | `[ { "checkId": 1, "title": "...", "content": "...", "imageUrl": "...", "checkType": 1 } ]` | [../../models/self_check_config_model.md](../../models/self_check_config_model.md#selfcheckconfigitem); item keys `checkId`, `content`, `imageUrl`, `checkType`, `title` (`self_check_config_model.dart @0x2ad2410` to `@0x2ad262c`) |

## Example request/response

Request, synthesized (self-check screen)

```json
{ "productCode": "<pn>", "checkIds": [20000004] }
```

Request, synthesized (failure screen)

```json
{ "productCode": "<pn>", "errorBits": [4] }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../encryption.md](../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../errors.md).

## Callers in app

- `SelfCheckController.onReady` (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acaf30`)
- an anonymous closure in `SelfCheckController` (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acc5a8`)
- an anonymous closure in `SelfCheckController` (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2acc9cc`)
- an anonymous closure in `SelfCheckController` (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_controller.dart @0x2ad0cfc`)
- an anonymous closure in `SelfCheckFailPage` (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_fail_page.dart @0x39a91c4`)
- `SelfCheckFailController.onReady` (`flutter_charging_beginning/beginning/state_cards/self_check/self_check_fail_controller.dart @0x2ad2f00`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0xad708`). since: 3.24.3.

## Known unknowns

- How the answer reaches the item list (which key, or whether `data` is the list itself) is not decoded; see the model page.
- What `errorBits` encodes (a bit index or a bit mask) is not shown by the sender.

## Device-tested by

none
