> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# shift_power_site_type

## Purpose

Converts a site between power site types: `RemoveStationDevicesLogic::shiftC1toC0`, `StationEnergySystemLogic::checkC1ToC0Station` and `ManageDevicesLogic::checkC1ToC0Station` call `shiftPowerSite`; the function names say C1 to C0.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/shift_power_site_type` (asm-traced): URL string at `http_request_repository_impl.dart @0x238c88c`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x238c884`, in `HttpRequestControllerImpl::shiftPowerSite` (`http_request_repository_impl.dart @0x238c7c4`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 2-pair map literal typed `<String, Object>` (type arguments `@0x238c840`) built in `shiftPowerSite` (`http_request_repository_impl.dart @0x238c7c4`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | string | yes | | key `@0x238c818`, value store `@0x238c828` (parameter at `fp-0x18`; typed at a caller, see the typing paragraph) |
| `power_site_type` | int (Smi, w) | yes | `2` | key `@0x238c82c`, `mov x16, #4` `@0x238c838` + `stur w16` `@0x238c83c`, tagged, so 2 |

Typing (two-hop, asm-traced): in `charging/http/http_request_repository_impl.dart` the builder `shiftPowerSite` takes `site_id` as an untyped parameter. The caller `RemoveStationDevicesLogic.shiftC1toC0` (`charging/ui/page/device/a17c0/remove_station_devices/remove_station_devices_logic.dart @0x3d68b94`) reads `field_1b` of an object and replaces a null value by the String literal `""` (`r3 = ""` `@0x3d68b58`), so `site_id` is a string. The constant 2 of `power_site_type` is the upstream `SolixSiteType.t_2` (A17C0 SB1 by the upstream comment): [reference/enums.md](../../../reference/enums.md#power_site_type-upstream-solixsitetype).

## `param_type`/`cmd`

n/a

## Response model (link)

None: the response body is not parsed. The callers' success callbacks `remove_station_devices_logic.dart @0x3d68bb0`, `station_energy_system_logic.dart @0x238cfa4` and `manage_devices_logic.dart @0x3fbe144` load no argument and call no `fromJson` (they refresh the site list and show a toast).

## Response

No response key is read by the app.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders)

```json
{"site_id": "<site_id>", "power_site_type": 2}
```

Response: none parsed.

## Errors seen

None traced. The shared failure callback `station_energy_system_logic.dart @0x238c8d0` shows a message; no code is compared. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `shiftPowerSite` @0x238c7c4 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::shiftPowerSite`
- `charging/ui/page/device/a17c0/remove_station_devices/remove_station_devices_logic.dart::shiftC1toC0`
- `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart::checkC1ToC0Station`
- `charging/ui/page/device/main/sitation_energy_system/station_home_settings/manage_devices/manage_devices_logic.dart::checkC1ToC0Station`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- The response body: not read by the app. — reclassified: server (not visible in the app: the app does not read the body)

## Device-tested by

none
