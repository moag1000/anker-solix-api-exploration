> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# share_site_report

## Purpose

Sends a site id to the cloud from the station home screens of the AX170 (ATS) and micro-HES (A17E2 and basic station) systems when they load the scene info; the answer is only logged. The name suggests it prepares or triggers sharing of the site report; the app does not read the answer.

## Upstream name

`none` (no upstream name; the URL is not mentioned in `api/apitypes.py`).

## Method+URL

`POST /site/v1/app/share_site_report` (asm-traced). Three senders, all `_shareSiteReport`: `AX170StationController` (`ats_ax170/src/ats_ax170/page/station/ax170_station_controller.dart @0x23594fc`; URL literal `@0x23595c8`), `BasicStationLogic` (`micro_hes/src/common_business/basic_station/station/basic_station_logic.dart @0x2360884`; `@0x2360950`) and `BaseStationLogic` of the A17E2 station (`micro_hes/src/a17e2/station/home/base_station_logic.dart @0x2348b00`; `@0x2348bcc`); each uses `Method.post` (pool entry `pp+0xa7e0`, `@0x23595c0`, `@0x2360948`, `@0x2348bc4`).

## Encrypted?

Yes by wrapper (asm-traced): all three senders call `HttpServiceImpl.encryptionRequestHttp` (`ax170_station_controller.dart @0x23595ec`, `basic_station_logic.dart @0x2360974`, `base_station_logic.dart @0x2348bf0`) with the named arguments `fail` and `success` only and without `needEncryption`, so the default `true` applies ([encryption.md](../../encryption.md#which-calls-are-encrypted)). Whether the call really goes through the SDK is decided at run time ([encryption.md](../../encryption.md)); asm alone does not decide it.

## Request

Body is a one-pair map in each sender (`site_id`, from the controller's site id field).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | String | yes | `<site id>` | `ax170_station_controller.dart @0x2359568`; `basic_station_logic.dart @0x23608f0`; `base_station_logic.dart @0x2348b6c` |

## `param_type`/`cmd`

n/a

## Response model (link)

n/a (asm-traced): the answer is not parsed.

## Response

Each success closure only logs ` shareSiteReport success: <data>` (`ax170_station_controller.dart @0x23596b4` to `@0x23596e4`); the failure closure logs `shareSiteReport failed: code=... msg=...` (`@0x2359638` to `@0x2359674`). Nothing is stored.

## Example request/response

Request, synthesized

```json
{ "site_id": "<site id>" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../encryption.md](../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../errors.md).

## Callers in app

- `AX170StationController.requestSceneInfo` (`ats_ax170/src/ats_ax170/page/station/ax170_station_controller.dart @0x234e9cc`)
- `BasicStationLogic.requestSceneInfo` (`micro_hes/src/common_business/basic_station/station/basic_station_logic.dart @0x235c7ac`)
- `BaseStationLogic.requestSceneInfo` (`micro_hes/src/a17e2/station/home/base_station_logic.dart @0x233c758`)

## Since/changed

3.18.0: absent (the URL string is not in the 3.18.0 object pool). 3.24.3: present (pool `pp+0x239a8`). since: 3.24.3.

## Known unknowns

- The server-side effect of the call is not known; the name and the fact that it is sent when the scene info loads suggest it registers the site for report sharing.
- Which of the three station types send it first on a given system is not traced.

## Device-tested by

none
