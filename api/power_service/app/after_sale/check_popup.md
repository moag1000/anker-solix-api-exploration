> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# check_popup

## Purpose

<!-- TODO -->

## Upstream name

`none` (no upstream name)

## Method+URL

`/power_service/v1/app/after_sale/check_popup`, method: not extracted by the inventory <!-- TODO -->; string-only: `charging/http/http_request_repository_impl.dart @0x28c14d4`

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

No request keys found by the extractor. <!-- TODO -->

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

- `charging/http/http_request_repository_impl.dart`: `checkDevicePopUpApi` @0x28c1464 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::checkDevicePopUpApi`
- `charging/ui/page/device/a17c0/a17c0energyPlan/a17c0energy_plan_logic.dart::getCheckDevicePopUp`
- `charging/ui/page/device/a17c1/energy_deploy/energy_deploy_logic.dart::getCheckDevicePopUp`
- `charging/ui/page/device/main/sitation_energy_mian/energy_home/controller/energy_home_controller.dart::getCheckDevicePopUp`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. <!-- TODO --> (compare params in `tools/out/diff_3.18.0_3.24.3.md`)

## Known unknowns

- <!-- TODO -->

## Device-tested by

none
