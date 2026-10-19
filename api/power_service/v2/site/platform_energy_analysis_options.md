> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# platform_energy_analysis_options

## Purpose

Asks for the energy-analysis chart options of a site or device in an AX170 (ATS) system for a date range; the command function exists in the AX170 package, but no caller of it was found in the 3.24.3 asm.

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (docstring list of V2 endpoints, no comment).

## Method+URL

`POST /power_service/v2/site/platform_energy_analysis_options` (asm-traced). Sender: `AKIotAX170Command.getPlatformEnergyAnalysisOptions` (`@0x2334664`) (`ats_ax170/src/sdk/command/ax170_command.dart`). The path literal has no leading slash (`@0x23346d0`), the method is the string `"POST"` (`@0x23346e8`), and the map keys `path`, `method`, `param` are stored at `@0x23346c8`, `@0x23346dc`, `@0x23346f4`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ax170_command.dart @0x23347d4`, call `@0x23347e4`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, String>` map of six pairs (`r2 = 24`, `@0x2334704`); all six arguments are Strings.

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `<site id>` | `ax170_command.dart @0x233470c`; fifth argument |
| `device_sn` | String | yes | `<device sn>` | `ax170_command.dart @0x2334720`; second argument |
| `date_type` | String | yes | `"month"` | `ax170_command.dart @0x2334734`; first argument; the allowed values are not shown (compare the `ChartDateType` names on [get_charge_order_stats](../../app/order/get_charge_order_stats.md#request), not confirmed for this endpoint) |
| `start_time` | String | yes | `2026-10-01` | `ax170_command.dart @0x2334748`; sixth argument |
| `end_time` | String | yes | `2026-10-19` | `ax170_command.dart @0x233475c`; third argument |
| `select_type` | String | yes | `<select type>` | `ax170_command.dart @0x2334770`; fourth argument; meaning not shown |

Compare [energy_options](../device/energy_options.md) (the S1/S2 charger chart start date) and [energy_analysis](../device/energy_analysis.md); how this request differs is not known.

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument (`stp x16, NULL`, `@0x23347d0`); no model is known.

## Response

Not parsed anywhere that was found: there is no caller.

## Example request/response

Request, synthesized

```json
{ "site_id": "<site id>", "device_sn": "<device sn>", "date_type": "month", "start_time": "2026-10-01", "end_time": "2026-10-19", "select_type": "<select type>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- none traced: no `bl` to `AKIotAX170Command::getPlatformEnergyAnalysisOptions` exists in the decoded 3.24.3 asm (searched every decoded call line). A caller inside a mixin region that the Blutter dump omits is possible (UNCONFIRMED).

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x1e650`); the 3.18.0 asm was not searched for a caller. 3.24.3: present, pool `pp+0x20a00`. since: ≤3.18.0.

## Known unknowns

- No caller was found, so it is not known whether the app ever sends this request; the page documents the body the function would send.
- The meaning of `select_type` and the answer layout are unknown.

## Device-tested by

none
