> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# set_standby_exercise_plan

## Purpose

Saves the standby exercise plan of a third-party (oil-machine) generator attached to an AX170 (ATS) system: when the next maintenance run is due, the interval in weeks, the maintenance time and the plan status.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /generator/v1/app/set_standby_exercise_plan` (asm-traced). Sender: the anonymous closure at `@0x3823588` inside `AKIotAX170Command.setStandbyExercise` (`@0x38234bc`), which hands the closure to `CommandErrorHandler.startCommand` (`base_service/ak_iot_kit/business/basic/command/command_error_handler.dart @0x2283a30`) (`@0x3823570`) (`ats_ax170/src/sdk/command/ax170_command.dart`). The path literal has no leading slash (`@0x38235ec`), the method is the string `"POST"` (`@0x3823604`), and the map keys `path`, `method`, `param` are stored at `@0x38235e4`, `@0x38235f8`, `@0x3823610`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command closure calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ax170_command.dart @0x38236f0`, call `@0x3823700`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../sdk_senders.md](../../sdk_senders.md#the-common-envelope), background: [../../encryption.md](../../encryption.md#rule-and-resulting-counts)).

## Request

Body (`param`) is a `<String, Object>` map of five pairs (`r2 = 20`, `@0x3823620`). `setStandbyExercise` takes five arguments and stores them in the closure context; the three integers are boxed with `BoxInt64Instr` (`@0x3823500`, `@0x382351c`, `@0x3823538`, unboxed int64) and the fifth is Smi-tagged (`lsl x1, x0, #1`, `@0x3823554`), so all four numbers are integers.

| field | type | required | example | source |
|---|---|---|---|---|
| `device_sn` | String | yes | `<generator sn>` | `ax170_command.dart @0x3823628`; context field read at `@0x3823638` |
| `next_maintenance_time` | int | yes | `1760000000` | `ax170_command.dart @0x3823644`; context field `0x1b` (`@0x3823650`), the fourth argument |
| `interval_period_week` | int | yes | `4` | `ax170_command.dart @0x382365c`; context slot 0 (`@0x3823668`), the third argument |
| `maintenance_time` | int | yes | `3600` | `ax170_command.dart @0x3823674`; context field `0x13` (`@0x3823680`), the second argument |
| `status` | int | yes | `1` | `ax170_command.dart @0x382368c`; context field `0x1f` (`@0x3823698`), the Smi-tagged fifth argument |

The example values are placeholders: the units (seconds or milliseconds for the times, the meaning of `maintenance_time` and of the `status` values) are not shown in the sender. The caller `Thirdpatygeneratorlogic.syncExerciseDataToCloud` (`ats_ax170/src/ats_ax170/third_generator/third_paty_generator_logic.dart @0x3823290`) takes the values from observables (`value()` calls, `@0x38231e8` to `@0x382325c`) after it computed the next maintenance time with `_calculateNextMaintenanceTime` (`@0x38231c8`) and wrote the generator settings with `updateThirdOilSetting` (`@0x38230d0`).

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): `handle` is called without a type argument (`stp x16, NULL`, `@0x38236ec`).

## Response

The caller awaits the result (`@0x382329c`) and shows `setupSuccessful` or `settingFailed` toasts (`@0x382342c`, `@0x3823474`); the answer body is not read.

Order of device and cloud write (traced 2026-10-20, app side): `Thirdpatygeneratorlogic::assertAndSync` (`ats_ax170/src/ats_ax170/third_generator/third_paty_generator_logic.dart @0x3823030`) first calls `updateThirdOilSetting` (`@0x38230d0`, device-side update) and awaits it; only when the result type equals the stored `AKResultType` instance (`@0x38230e8`, `@0x38230f0`, `b.eq` to `@0x3823170`) does it compute the next maintenance time (`_calculateNextMaintenanceTime` `@0x38231c8`) and call `setStandbyExercise` (`@0x3823290`); otherwise it shows the `settingFailed` toast (`@0x3823148`) and returns. So the cloud plan is written after a successful device update, not instead of it. Whether the device update also carries the same plan values was not compared.

## Example request/response

Request, synthesized

```json
{ "device_sn": "<generator sn>", "next_maintenance_time": 1760000000, "interval_period_week": 4, "maintenance_time": 3600, "status": 1 }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `Thirdpatygeneratorlogic.syncExerciseDataToCloud` (`ats_ax170/src/ats_ax170/third_generator/third_paty_generator_logic.dart @0x3823290`), through `AKIotAX170Command.setStandbyExercise`

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x119b18`). since: 3.24.3.

## Known unknowns

- The units of `next_maintenance_time` and `maintenance_time` and the values of `status` are not decoded. — reclassified: server (2026-10-20: the app writes the numbers as given (see Request); their units and the status values are not derivable from the app)
- Whether the device update carries the same plan values as the cloud call (the order is on the Response section) was not compared — traced 2026-10-20

## Device-tested by

none
