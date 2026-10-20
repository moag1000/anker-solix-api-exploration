> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# get_heat_pump_plan_json

## Purpose

Reads the heat-pump time plan of the device manager as a JSON text (`TimerSettingLogic::getJsonData` through `HttpRequestControllerImpl::getHeatPumpTimePlan`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /charging_hes_svc/get_heat_pump_plan_json` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x3e8b810`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x3e8b808`, in `HttpRequestControllerImpl::getHeatPumpTimePlan` (`charging/http/http_request_repository_impl.dart @0x3e8b75c`), sent through `requestHttp` (`@0x3e8b838`).

## Encrypted?

encrypted: "default-true (requestHttp)". Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

- No named argument `needEncryption` is passed by `HttpRequestControllerImpl::getHeatPumpTimePlan` (`charging/http/http_request_repository_impl.dart`, call `@0x3e8b838`, argument list `@0x3e8b830`); `requestHttp` declares `needEncryption = true` as default (`charging/http/http_request_repository_impl.dart @0x2264944`).

## Request

(asm-traced) `HttpRequestControllerImpl::getHeatPumpTimePlan` (`charging/http/http_request_repository_impl.dart @0x3e8b75c`) stores one key in a map literal with the type arguments `<String, List<Map<String, dynamic>>>` (`@0x3e8b7c4`), so the value is a list of maps; the key is stored unconditionally. The element maps are built by the caller.

| field | type | required | example | source |
|---|---|---|---|---|
| `heat_pump_plan` | list | yes | a list of maps (element keys not read) | `charging/http/http_request_repository_impl.dart @0x3e8b7b0` |

## `param_type`/`cmd`

n/a

## Response model (link)

read key by key, no `fromJson`: the success closure (`charging/http/http_request_repository_impl.dart @0x3e8b854`) reads the key `heat_pump_plan_json` (`@0x3e8b880`, lookup `@0x3e8b8a0`, cast to `String?` `@0x3e8b8dc`) and passes the string to the stored callback (`ClosureCall` `@0x3e8b8f8`).

## Response

(asm-traced) One key is read by the app: `heat_pump_plan_json` (String?), a JSON text that the caller decodes.

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "heat_pump_plan": [
    {
      "<element keys not read>": "<?>"
    }
  ]
}
```

Response: not synthesized; the keys are listed under Response (no capture exists for this endpoint).

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `getHeatPumpTimePlan` @0x3e8b75c (requestHttp; encrypted: default-true (requestHttp) — verify)

Called from:

- `charging/http/http_request_repository.dart::getHeatPumpTimePlan`
- `charging/ui/page/device/a5101/setting/device_manager/heat_pump/timer_setting/timer_setting_logic.dart::getJsonData`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- The element keys of `heat_pump_plan`: the maps are built in `TimerSettingLogic` and were not read for this page.
- The structure of the JSON text in `heat_pump_plan_json`: the app passes it on as a string.
- Whether the transport really encrypts the `requestHttp` call(s): `needEncryption` keeps its default true, the later predicates (login state, base URL) are described in `api/encryption.md` and were not evaluated per call. — reclassified: device test row 150 (traced 2026-10-20: per call the SDK login state `AkIotKitFlutter::isLogin` and the base-URL predicate decide, `HttpEncryptionDecorator.dart @0x4869504`, `@0x4869544`; the predicate is a GDT dispatch whose selector the asm does not name, and the login state is runtime data)
- Server behaviour is not known from the app: this page states what the app builds and parses.

## Device-tested by

none
