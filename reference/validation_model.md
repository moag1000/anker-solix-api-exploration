> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Page type: reference · Owner page: this page

# Validation model (App 3.24.3)

Closest template: [../docs/templates/flow.md](../docs/templates/flow.md) (Preconditions, Failure paths, Known unknowns); the sections below are grouped by the question "where does the limit of this value come from", because that is the question a library author asks before sending a value. The page is `Page type: reference`.

It replaces the 3.18.0 root page [../VALIDATION_MODEL.md](../VALIDATION_MODEL.md). It does not copy `api/param_types.md`: the `param_type` list, the `cmd` values and the `param_data` keys stay on [../api/param_types.md](../api/param_types.md); this page only says which read comes before which write and which limits the app itself applies. Timing, gates and polling are on [business_rules.md](business_rules.md).

## Contents

1. [Where a limit comes from](#where-a-limit-comes-from)
2. [Read before write: verified pairs](#read-before-write-verified-pairs)
3. [Client-side limits hardcoded in the app](#client-side-limits-hardcoded-in-the-app)
4. [Settings whose limits come from the device](#settings-whose-limits-come-from-the-device)
5. [Checks on received data](#checks-on-received-data)
6. [Corrections to the 3.18.0 root page](#corrections-to-the-3180-root-page)
7. [Known unknowns](#known-unknowns)

## Where a limit comes from

Tag: `asm-traced` for the structure below (the decoded senders and getters named in the next section); the claim per setting is only as strong as the row that carries it.

`VM-n` is row n (counting table rows from the top) of [../docs/audit/VALIDATION_MODEL.md](../docs/audit/VALIDATION_MODEL.md) (36 rows: 11 OK, 3 WRONG, 22 NOT-FROM-ASM); `BR-n` is the same for [business_rules.md](business_rules.md). The audit has no row numbers of its own; they were assigned in table order.

A value that the app lets the user change has one of four limit sources:

| source | meaning | where documented |
|---|---|---|
| server response | a GET returns the range or the option list and the UI is built from it | the endpoint page and the model page of the GET, linked in [Read before write](#read-before-write-verified-pairs) |
| device status | the value or option set arrives in a status message of the device | the `mqtt/<pn>.md` page of the device, see [Settings whose limits come from the device](#settings-whose-limits-come-from-the-device) |
| hardcoded in the app | a constant in the Dart code (maximum per product number, minimum of a text field, default when the value is null) | [Client-side limits](#client-side-limits-hardcoded-in-the-app) |
| none found | the app sends what the user typed or picked without a range check that was found | [Known unknowns](#known-unknowns) |

The 3.18.0 page opened with "the app does NOT hardcode validation ranges". That is too strong: 3.24.3 has hardcoded limits (the next sections list them), although the main ranges of the site-level settings do come from the server. The 3.18.0 general pattern (read the limits first, build the control from them, then write) is also the structure of the owner pages, but it was not re-verified setting by setting (see [Known unknowns](#known-unknowns)).

## Read before write: verified pairs

Tag: `asm-traced`. All functions are in `charging/http/http_request_repository_impl.dart`; the `param_type` values are string literals in the request map (so the Smi rule does not apply to them). The decoded rows of [../api/param_types.md](../api/param_types.md) (rows for the listed values) agree with these pairs (VM-4 to VM-13).

| setting | read (GET) | write (SET) | param_type | sites | rows |
|---|---|---|---|---|---|
| site output power limit | [`get_power_limit`](../api/power_service/site/get_power_limit.md), `getSitePowerLimit @0x2378fb4`: builds `{site_id, app_ability}` only, no `param_type`; response model [StationPowerLimitModel](../models/station_power_limit.md) | [`set_site_device_param`](../api/power_service/site/set_site_device_param.md), `setSiteDevicePowerLimit @0x4355750` (literal `@0x43558ac`) | 19 for the SET, none for the GET (the app has no GET for 19) | the old page paired the GET with 16; 16 belongs to the power-dock config `getCombineBoxListData` | VM-1, VM-2, VM-4 |
| safety SOC reserve | `getSafetySocParams @0x2377e5c` | `setSafetySocParams @0x23a0220` (literal `@0x23a0348`) | 18 | same literal for both | VM-5 |
| green mode | `getSiteGreenModeDeviceParam @0x28f2c2c` | wrapper `setSiteDeviceParam @0x24043b4` | 1 | literal at the caller sites listed on param_types | VM-6 |
| peak/valley time | `getSitePeakTimeDeviceParam @0x28f1538` | `setSiteDeviceParam` | 2 | same | VM-7 |
| peak shaving enable | `getSiteEnablePeakDeviceParam @0x28f215c` | `setSiteDeviceParam` | 3 | same | VM-8, VM-13 |
| lower limit | `getSiteLowerLimitDeviceParam @0x28f2674` | `setSiteDeviceParam` | 5 | same | VM-9 |
| usage-mode family | a getter exists for each of the first six values (the sixth is the Solarbank 2 schedule); the first is `getSiteGreenModeDeviceParam @0x28f2c2c` | `setSiteDeviceParam` / the 17C1 variants | 1, 2, 3, 4, 5, 6 | the first six rows of `param_types.md` | VM-10 |
| grid / country code | `getStationCountryCode @0x237eed8` | `setStationCountryCode @0x28d3d4c` (literal `@0x28d3ec4`) | 20 | | VM-11 |
| third-party PV | `getThreePvParam @0x237dc80` | `setThreePvInstallSwitch @0x42fd430` (literal `@0x42fd518`) | 26 | | VM-12 |

Where the `cmd` of each SET is a different value (the generic wrapper and the dedicated senders differ), the values and the sender addresses are on [../api/param_types.md](../api/param_types.md); they are not repeated here. The sequence "read the limit, pick a value, write it" for the output limit is [../flows/system_output_limit.md](../flows/system_output_limit.md).

Other GET to SET pairs of the old page (home load, device attributes, dynamic price options, disaster preparedness check, A7320 maintenance and range extender endpoints, EV charger, generator) have endpoint pages for the HTTP side: [`get_device_home_load`](../api/power_service/app/device/get_device_home_load.md), [`set_device_home_load`](../api/power_service/app/device/set_device_home_load.md), [`get_device_attrs`](../api/power_service/app/device/get_device_attrs.md), [`set_device_attrs`](../api/power_service/app/device/set_device_attrs.md), [`check_function`](../api/charging_hes_svc/check_function.md). The field lists of their responses are owned by those pages and the model pages; the old page's field tables were not audit rows and are not repeated.

## Client-side limits hardcoded in the app

Tag: `asm-traced`. Each limit is a constant in the Dart code. The values live in [business_rules.md](business_rules.md) and only the pointer is here (single source).

| limit | what it constrains | value and site | rows |
|---|---|---|---|
| maximum peak-shaving power per product number | the upper bound of the A5101 / A5102 / A5103 / A5341 peak-shaving input; 0 for any other product | [business_rules.md](business_rules.md#peak-shaving-maxima-and-input-range), `getPeakShavingMaxPower` in `system_policy_logic.dart` | BR-40 to BR-44 |
| text-input range | `RangeTextInputFormatter` rejects values below the minimum of 1 or above the maximum it is given | same section | BR-50 |
| second range for the A5341 | the peak-shaving controller bounds `_inputPowerChanged` independently | same section | BR-43 |
| output-power picker | the station power-limit picker is configured with hardcoded numbers; the roles are undecided | [business_rules.md](business_rules.md#station-power-limit-picker-new-read) | new read |
| defaults of the A17C1 power cutoff | three percentages used when a parameter is null | [business_rules.md](business_rules.md#power-cutoff-led-power-limit-list) | BR-14 |
| maximum number of plug schedules | default when the server attribute is null | [business_rules.md](business_rules.md#a17x8-smart-plug) | BR-21 |
| plug countdown | duration encoded in a fixed-size field (size in business_rules), a negative remaining time is clamped to zero | same section | BR-24, BR-25 |
| schedule slots of the A17C1 | a fixed maximum number of slots | [business_rules.md](business_rules.md#schedule-settacticstime-and-backup-power) | BR-8 |
| seasonal time-of-use default mode | a constant mode value | [business_rules.md](business_rules.md#counts-defaults-and-catalogs) | BR-57 |

Not found in 3.24.3: a client-side comparison of a typed power value with the server's `power_limit_option` list before the SET of the output limit; the app builds the picker from the response and sends the picked value (the picker configuration above is the only constant found on that path). This is a negative search result, not proof that the app does not check.

## Settings whose limits come from the device

Tag: untagged by design (pointer table; the facts and their tags are on the owner pages).

The MQTT-only settings of the Solarbank and the smart plug take their current values and option sets from the device's status messages. Opcodes, tags, value meanings, option sets and the device-tested sessions are owned by the 3.6a pages; this page does not repeat them. Old rows and where their content went:

| old rows | setting | owner |
|---|---|---|
| VM-14, VM-23 | LED / light mode | [../mqtt/a17c1.md](../mqtt/a17c1.md) |
| VM-15, VM-24 | temperature unit | [../mqtt/a17c1.md](../mqtt/a17c1.md) |
| VM-16, VM-25 | power cutoff thresholds and their option sets | [../mqtt/a17c1.md](../mqtt/a17c1.md) |
| VM-17, VM-26, VM-30 | max load, grid export | [../mqtt/a17c1.md](../mqtt/a17c1.md), [../mqtt/a17c1_status.md](../mqtt/a17c1_status.md) |
| VM-18, VM-27, VM-29 | usage mode and schedule | [../mqtt/a17c1.md](../mqtt/a17c1.md) |
| VM-19, VM-20, VM-21, VM-31, VM-32 | plug switch, schedule, timer | [../mqtt/a17x8.md](../mqtt/a17x8.md) |
| VM-22 | status message types and field names | [../mqtt/envelope.md](../mqtt/envelope.md), the `mqtt/<pn>.md` pages |
| VM-34 | SOC option list `soc_list` | [../models/get_site_device_param_response.md](../models/get_site_device_param_response.md) |

The hex-string MQTT opcodes of the old page (`0068`, `0050`, `0067`, `0080`, `005e`, `007a`, `007c`, `007e`) are strings from the upstream library and from device captures; their BLE counterparts are asm-traced pool lists on the 3.6a pages. The opcode `005a` has no pool list in 3.24.3 and is a Known unknown on those pages.

## Checks on received data

Tag: `asm-traced`.

| check | rule | site | rows |
|---|---|---|---|
| plug countdown status (`ad`) | the parser compares the length with 8, then reads bytes 0 to 2 (delay), 3 (setting), 4 (status) and 5 to 7 (elapsed) | `a17x8_device_commands.dart` `parseCountDownInfo @0x3b634c4` (`cmp x1,#8`, unboxed length), `sublist` end `r16 = 6` `@0x3b63508` (tagged, 6 / 2 = 3), index `r16 = 6` `@0x3b6354c`, `r16 = 8` `@0x3b63588` (8 / 2 = 4), `r2 = 5` `@0x3b635f0` | VM-33 |
| response signature | an HTTP 200 body whose `Result` carries a `signature` is verified; a mismatch becomes failure code 463 | [../api/encryption.md](../api/encryption.md#request-signing) (`http_manager.dart` `validateSignature @0x486c99c`) | link only |

The status code values 0 (off), 2 (paused) and 3 (running) of the `ad` field come from device captures (A17X8 FW 0.0.2.7), not from asm; they are on [../mqtt/a17x8.md](../mqtt/a17x8.md).

## Corrections to the 3.18.0 root page

Tag: untagged by design (pointers; old values are history).

| old claim | status in 3.24.3 | where |
|---|---|---|
| `get_power_limit` takes `param_type` 16 (VM-1, VM-2) | it takes none; 16 is the power-dock config | [Read before write](#read-before-write-verified-pairs) |
| the app does not hardcode validation ranges | it hardcodes several | [Client-side limits](#client-side-limits-hardcoded-in-the-app) |
| the A17C1 schedule occupies a4 to be (VM-28) | the range is a3 to be or a4 to be depending on the role of a3; the 3.6a page decided the data tags a2 to be | [../mqtt/a17c1.md](../mqtt/a17c1.md); role of a3 in [Known unknowns](#known-unknowns) |
| the summary table pairs the output limit with `get_power_limit`(16) and `set_site_device_param`(19) | the GET has no `param_type`; the SET is 19 | [Read before write](#read-before-write-verified-pairs) |

The `cmd` correction for the output-limit SET (the app and the upstream library send different values; acceptance of each is unverified) is owned by [../api/param_types.md](../api/param_types.md) and [../api/power_service/site/set_site_device_param.md](../api/power_service/site/set_site_device_param.md).

## Known unknowns

Tag: untagged by design (no API fact). Rules of the old page that are not carried as facts.

- **Per-setting GET-before-write behavior.** The statement "always query the limits first, then validate input against the response" and the old summary table (about 38 rows) were prose and were not audit rows except where listed above. The 3.6a and API pages own the individual settings; no new trace of "the UI is built from the response" was made for this page.
- **Role of tag a3 in the A17C1 schedule frame** (VM-28): a slot tag or a separate flag; the audit left it undecided and the 3.6a page lists the upstream name with a question mark.
- **Whether the server accepts the upstream value for the output-limit SET** (the app and upstream send different command values): not tested; see [../api/param_types.md](../api/param_types.md#known-unknowns).
- **Field lists of the old page** (`min`, `max`, `step`, `init_step`, `legal_limit`, ... of `StationPowerLimitModel`, VM-3): owned by [../models/station_power_limit.md](../models/station_power_limit.md); the old list is not what the app's model reads.
- **Numbers in labels**: "A7320: 22 commands and 18 endpoints" (VM-35) are prose counts that do not match the tables below them; the firmware and session labels (A17C1 FW 1.0.6.10, A17X8 FW 0.0.2.7, "4 sessions", VM-36) are device-test provenance without client version, tester and date, so no `device-tested` tag is claimed.
- **A7320, AS200, A5190 and PPS BLE settings** of the old page (action names and parameter keys): not audit rows; owned by the future `ble/<pn>.md` pages.

## Related pages

- [business_rules.md](business_rules.md): gates, polling, timeouts and the hardcoded values.
- [../api/param_types.md](../api/param_types.md), [../api/power_service/site/get_power_limit.md](../api/power_service/site/get_power_limit.md), [../api/power_service/site/set_site_device_param.md](../api/power_service/site/set_site_device_param.md), [../api/power_service/site/get_site_device_param.md](../api/power_service/site/get_site_device_param.md).
- [../flows/system_output_limit.md](../flows/system_output_limit.md).
- [../METHODOLOGY.md](../METHODOLOGY.md): Smi rule and tags.
