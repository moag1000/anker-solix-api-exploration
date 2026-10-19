> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# bind

## Purpose

Binds an everHome (third-party smart meter platform) account to the Anker account: after the user logs in on the everHome page, the page returns an authorization code that the app sends; the answer lists the serial numbers of the bound devices.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /power_service/v1/everhome/bind` (asm-traced): URL literal `@0x3f29df8` in `bind2Cloud` (`charging/ui/page/device/connect/third_party_platform_list/strategy/ever_home_navigation_strategy.dart @0x3f29d24`), method object `Method.post` (pool entry `pp+0xa7e0`, `@0x3f29df0`).

## Encrypted?

Yes by wrapper (asm-traced): ``bind2Cloud`` calls `encryptionRequestHttp` (`charging/ui/page/device/connect/third_party_platform_list/strategy/ever_home_navigation_strategy.dart @0x3f29e20`) without passing `needEncryption`, so the default `true` applies (`api/encryption.md`, [which calls are encrypted](../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time (SDK login state and a base-URL test, [encryption.md](../../encryption.md)); asm alone does not decide it. The loading overlay is on (`r30 = true`, `@0x3f29e08`).

## Request

Map literal with one string pair, `<String, String>` (`r2 = 4`, `@0x3f29d94`).

| field | type | required | example | source |
|---|---|---|---|---|
| `code` | String | yes | `"<authorization code>"` | `charging/ui/page/device/connect/third_party_platform_list/strategy/ever_home_navigation_strategy.dart @0x3f29d9c`; value is the function argument stored at `@0x3f29da8`, passed by the JavaScript handler of the platform web page (`addJsCallHandler`, `@0x3f29b3c`, handler name `clickEvent`, `@0x3f29b98`) |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): no model is parsed; the success closure reads one key from the raw map.

## Response

Success closure `charging/ui/page/device/connect/third_party_platform_list/strategy/ever_home_navigation_strategy.dart @0x3f29f38` (logs `[everHome] bind2Cloud success -> ...`, `@0x3f29f84`):

| field | type | required | example | source |
|---|---|---|---|---|
| `sns` | list of String | no | `[ "<device sn>" ]` | `@0x3f2a000`, `@0x3f2a02c`; the list is mapped to strings (`@0x3f2a0b0`) and `toList` (`@0x3f2a0dc`); if empty the app logs `[everHome] 响应中未找到设备 sn` ("no device sn found in the response", `@0x3f2a138`) |

## Example request/response

Request, synthesized

```json
{ "code": "<authorization code>" }
```

Response, synthesized

```json
{ "sns": [ "<device sn>" ] }
```

## Errors seen

No error code specific to this endpoint was traced. The failure closure of each sender passes the code and message to the caller or logs it; the shared transport codes are in [encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `bind2Cloud` (`charging/ui/page/device/connect/third_party_platform_list/strategy/ever_home_navigation_strategy.dart @0x3f29d24`), called from the JS call handler registered by `addJsCallHandler` (`@0x3f29b3c`) of the `EverHomeNavigationStrategy`: the third-party platform list page (`charging/ui/page/device/connect/third_party_platform_list/`), the everHome connection flow.

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 pool as a code-referenced URL; see the inventory row `since`). 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- What the server does with the code (OAuth exchange with everHome) is not known.
- Whether `sns` is the list of devices that were newly bound or of all everHome devices is not known.

## Device-tested by

none
