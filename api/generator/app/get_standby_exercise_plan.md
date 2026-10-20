> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_standby_exercise_plan

## Purpose

Reads the standby exercise plan of a third-party (oil-machine) generator that is attached to an AX170 (ATS) system: the schedule on which the generator is exercised while in standby.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /generator/v1/app/get_standby_exercise_plan` (asm-traced). Sender: the anonymous closure at `@0x35e1f50` inside `AKIotAX170Command.getStandbyExercise` (`@0x35e1ef0`), which hands the closure to `CommandErrorHandler.startCommand` (`base_service/ak_iot_kit/business/basic/command/command_error_handler.dart @0x2283a30`) (`@0x35e1f38`) (`ats_ax170/src/sdk/command/ax170_command.dart`). The path literal has no leading slash (`@0x35e1fb4`), the method is the string `"POST"` (`@0x35e1fcc`), and the map keys `path`, `method`, `param` are stored at `@0x35e1fac`, `@0x35e1fc0`, `@0x35e1fd8`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command closure calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ax170_command.dart @0x35e205c`, call `@0x35e206c`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#the-common-envelope), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, String>` map of one pair (`r2 = 4`, `@0x35e1fe8`); the value is the serial passed to `getStandbyExercise` (field of the closure context, `@0x35e2000`).

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<generator sn>` | `ax170_command.dart @0x35e1ff0`; value from the closure context `@0x35e2000` |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument (`stp x16, NULL`, `@0x35e2058`).

## Response

The caller `Thirdpatygeneratorlogic._getStandbyExerciseData` (`ats_ax170/src/ats_ax170/third_generator/third_paty_generator_logic.dart @0x35e1c98`) awaits the result (`@0x35e1cf8`), reads the key `data` (`@0x35e1dcc`) and, when it is a String, decodes it with `jsonDecode` (`@0x35e1e20`). The keys of the decoded plan were not read.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | String (JSON text) | yes | `"{...}"` | `third_paty_generator_logic.dart @0x35e1dcc`, `jsonDecode` `@0x35e1e20` |

Keys of the decoded plan (traced 2026-10-20, app side): `Thirdpatygeneratorlogic::_refreshStandbyOilData` (`ats_ax170/src/ats_ax170/third_generator/third_paty_generator_logic.dart @0x35e0188` awaits `_getStandbyExerciseData`) reads the decoded map with `[]` and casts every value to `int?`: `next_maintenance_time` (key `@0x35e01d4`, cast `@0x35e0210`), `interval_period_week` (`@0x35e0230`, cast `@0x35e026c`), `maintenance_time` (`@0x35e028c`, cast `@0x35e02c8`) and `status` (`@0x35e02e4`, cast `@0x35e0320`): the same four keys as the set page.

## Example request/response

Request, synthesized

```json
{ "device_sn": "<generator sn>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `Thirdpatygeneratorlogic._getStandbyExerciseData` (`ats_ax170/src/ats_ax170/third_generator/third_paty_generator_logic.dart @0x35e1cec`), through `AKIotAX170Command.getStandbyExercise`

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0xe1d28`). since: 3.24.3.

## Known unknowns

- The caller passes the serial as `""` when none is known (`r1 = ""`, `@0x35e1ce0`); what the server answers to an empty serial is not known.

## Device-tested by

none
