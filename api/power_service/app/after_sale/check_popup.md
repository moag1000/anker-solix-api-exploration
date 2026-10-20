> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: asm-traced · Owner page: this page

# check_popup

## Purpose

Asks whether a device pop-up (after-sale notice) has to be shown on the A17C0 energy plan, the A17C1 energy deploy page and the energy home page (callers `A17c0energyPlanLogic::getCheckDevicePopUp`, `EnergyDeployLogic::getCheckDevicePopUp`, `EnergyHomeLogic::getCheckDevicePopUp`) (asm-traced, caller chain in `data/endpoints.json`).

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/app/after_sale/check_popup` (asm-traced): URL string at `charging/http/http_request_repository_impl.dart @0x28c14d4`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x28c14cc`, in `HttpRequestControllerImpl::checkDevicePopUpApi` (`charging/http/http_request_repository_impl.dart @0x28c1464`), sent through `encryptionRequestHttp` (`@0x28c14fc`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

(asm-traced) `HttpRequestControllerImpl::checkDevicePopUpApi` (`charging/http/http_request_repository_impl.dart @0x28c1464`) receives the body map as a parameter (`r5`, `fp-0x18`) and builds none itself. All three callers build the same one-pair literal with type arguments `<String, int>`: `A17c0energyPlanLogic` (`charging/ui/page/device/a17c0/a17c0energyPlan/a17c0energy_plan_logic.dart @0x28c13ac`, value `@0x28c13b8`), `EnergyDeployLogic` (`charging/ui/page/device/a17c1/energy_deploy/energy_deploy_logic.dart @0x28ca5cc`, value `@0x28ca5d8`) and `EnergyHomeLogic` (`charging/ui/page/device/main/sitation_energy_mian/energy_home/controller/energy_home_controller.dart @0x338a938`, value `@0x338a944`). The stored immediate is raw 2 in a tagged slot (`StoreField` of a 32-bit register), so the value is 1 (Smi rule).

| field | type | required | example | source |
|---|---|---|---|---|
| `type_id` | int (Smi, w) | yes | `1` | `charging/ui/page/device/a17c0/a17c0energyPlan/a17c0energy_plan_logic.dart @0x28c13ac`; same key and value in the two other callers |

## `param_type`/`cmd`

n/a

## Response model (link)

no model class (asm-traced): the success closure (`charging/http/http_request_repository_impl.dart @0x28c1518`) reads the key `check_data` (string literal `@0x28c1568`, index call `@0x28c1570`), casts the value to `String` (`@0x28c15b4`), runs `jsonDecode` on it (`@0x28c15bc`) and casts the result to `List?` (`@0x28c15fc`).

## Response

| field | type | required | example | source |
|---|---|---|---|---|
| `check_data` | string holding a JSON list (decoded with `jsonDecode`, cast to `List?`) | yes (non-null `String` cast, `@0x28c15b4`) | `"[...]"` | `charging/http/http_request_repository_impl.dart @0x28c1568` |

## Example request/response

Request, synthesized (decrypted body as built by the sender; `<...>` are placeholders, not captured values)

```json
{
  "type_id": 1
}
```

Response, synthesized (key read by the success closure; the list content is not known)

```json
{
  "data": {
    "check_data": "[...]"
  }
}
```

## Errors seen

none traced: no numeric error code is compared in the sender or the closures read for this page. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `checkDevicePopUpApi` @0x28c1464 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::checkDevicePopUpApi`
- `charging/ui/page/device/a17c0/a17c0energyPlan/a17c0energy_plan_logic.dart::getCheckDevicePopUp`
- `charging/ui/page/device/a17c1/energy_deploy/energy_deploy_logic.dart::getCheckDevicePopUp`
- `charging/ui/page/device/main/sitation_energy_mian/energy_home/controller/energy_home_controller.dart::getCheckDevicePopUp`

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- What the entries of the decoded `check_data` list contain: the closure only casts the result to `List?` (`charging/http/http_request_repository_impl.dart @0x28c15fc`); the consumers in the three callers were not decoded. — traced 2026-10-20: the consumer in the success closure of `A17c0energyPlanLogic.getCheckDevicePopUp` (`charging/ui/page/device/a17c0/a17c0energyPlan/a17c0energy_plan_logic.dart @0x28c163c`) casts the list to `Iterable` (`@0x28c1688`), iterates it, casts each element to `Map<String, dynamic>` (`@0x28c1724`), reads one value through unnamed dispatch-table calls (`@0x28c1738`..`@0x28c17a0`, no key string is loaded there) and casts it to `int` (`@0x28c17e8`) before it calls `getCurrentRegion` (`@0x28c17f4`); the key names inside the elements are not visible there and the other two callers were not read
- What other `type_id` values would select (the three callers all send 1). — reclassified: server
- Whether `check_data` sits under `data` or at the top of the body: the closure indexes the object it receives (`charging/http/http_request_repository_impl.dart @0x28c1570`). — traced 2026-10-20: the success closure receives its argument as the already decoded object of the call (`encryption.md#response-handling-and-error-codes`: the decorator converts the SDK result and JSON-decodes its `data`) and indexes it for `check_data`; whether that object is the `data` member or the whole body is decided in that layer and was not followed per caller

## Device-tested by

none
