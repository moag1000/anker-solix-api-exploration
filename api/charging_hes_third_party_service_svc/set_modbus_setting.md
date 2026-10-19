> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# set_modbus_setting

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/charging_hes_third_party_service_svc/set_modbus_setting`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/ui/widget/home_assitent/home_assistant_logic.dart @0x38db248`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

| field | type | required | example | source |
|---|---|---|---|---|
| `sn` | ? | ? | ? | `charging/ui/widget/home_assitent/home_assistant_logic.dart @0x38db0b8` |
| `pn` | ? | ? | ? | `charging/ui/widget/home_assitent/home_assistant_logic.dart @0x38db0b8` |
| `modbusStatus` | ? | ? | ? | `charging/ui/widget/home_assitent/home_assistant_logic.dart @0x38db0b8` |
| `rtuId` | ? | ? | ? | `charging/ui/widget/home_assitent/home_assistant_logic.dart @0x38db0b8` |
| `siteId` | ? | ? | ? | `charging/ui/widget/home_assitent/home_assistant_logic.dart @0x38db0b8` |
| `isBluetooth` | ? | ? | ? | `charging/ui/widget/home_assitent/home_assistant_logic.dart @0x38db0b8` |

## `param_type`/`cmd`

n/a

## Response model (link)

<!-- TODO -->

## Response

<!-- TODO -->

## Example request/response

<!-- TODO -->

## Errors seen

`api/errors.md`: <!-- TODO -->

## Callers in app

- `charging/ui/widget/home_assitent/home_assistant_logic.dart`: `saveSetId` @0x38db0b8 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/ui/widget/home_assitent/home_assistant_logic.dart::openSwichRequest`

## Since/changed

3.18.0: absent. 3.24.3: present (new). since: 3.24.3.

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
