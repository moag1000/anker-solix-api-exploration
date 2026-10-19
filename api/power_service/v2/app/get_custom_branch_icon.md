> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: asm-traced · Owner page: this page

# get_custom_branch_icon

## Purpose

Lists the icon catalogue (categories with named icon URLs) that the AX170 custom-branch editor offers for branch circuits.

## Upstream name

`none` (no upstream name). Upstream lists the URL without a key in `api/apitypes.py` (docstring list of V2 endpoints, comment "get list of branch icons and url").

## Method+URL

`POST /power_service/v2/app/get_custom_branch_icon` (asm-traced). Sender: `AKIotAX170Command.getCustomBranchIcons` (`@0x27d5f64`) (`ats_ax170/src/sdk/command/ax170_command.dart`). The path literal has no leading slash (`@0x27d5fb4`), the method is the string `"POST"` (`@0x27d5fcc`). The map has two pairs, `path` and `method` (`r2 = 8`, `@0x27d5fa0`), and no `param`.

## Encrypted?

Direct SDK call, path C (asm-traced): the command function calls `AKIoTKitManagerImpl.handle` with the identifier `akiot.cloud_api` (`ax170_command.dart @0x27d5fec`, call `@0x27d5ffc`) and no `*Http*` wrapper, so the inventory flag `encrypted: false` only says that no wrapper is called. The SDK sends the request natively; what it encrypts is not visible in Dart (mechanics: [../../../sdk_senders.md](../../../sdk_senders.md#the-common-envelope), background: [../../../encryption.md](../../../encryption.md#rule-and-resulting-counts)).

## Request

No body: the envelope map has only `path` and `method` (`@0x27d5fa0`), there is no `param` key.

## `param_type`/`cmd`

n/a

## Response model (link)

`BranchIconModel` ([../../../../models/branch_icon_models.md](../../../../models/branch_icon_models.md#branchiconmodel)) with its element class `BranchIconInfo`; `handle` itself has no type argument (`stp x16, NULL`, `@0x27d5fe8`), and the caller maps the data with `BranchIconModel.fromJson` (closure `ats_ax170/src/ats_ax170/branch_circuit/pages/custom_branch/custom_branch_controller.dart @0x27d6014`, call `@0x27d604c`).

## Response

`CustomBranchController.getBranchIcons` (`custom_branch_controller.dart @0x27d5b0c`) awaits the result (`@0x27d5b40`), shows the SDK error text when it is non-empty (`@0x27d5ba8`), logs `getBranchIcons接口返回data: ...` (`@0x27d5be0`), checks that the data is a `Map<String, dynamic>` (`@0x27d5c44`), reads its `data` key (`@0x27d5c84`) and maps the list through the closure above.

| field | type | required | example | source |
|---|---|---|---|---|
| `data` | list of `BranchIconModel` | yes | `[ { "icon_category": "...", "icon_infos": [ { "name": "...", "url": "..." } ] } ]` | `custom_branch_controller.dart @0x27d5c84`; keys `icon_category` (`branch_circuit_data.dart @0x27d6090`), `icon_infos` (`@0x27d60ec`), `name` (`@0x27d6540`), `url` (`@0x27d65b0`) |

## Example request/response

Request, synthesized

```json
{ "path": "power_service/v2/app/get_custom_branch_icon", "method": "POST" }
```

## Errors seen

No error code specific to this endpoint was traced; the shared transport codes are in [../../../encryption.md](../../../encryption.md#response-handling-and-error-codes). The code catalog is [errors.md](../../../errors.md).

## Callers in app

- `CustomBranchController._getBranchIcons` (`ats_ax170/src/ats_ax170/branch_circuit/pages/custom_branch/custom_branch_controller.dart @0x27d5b34`)

## Since/changed

3.18.0: present (URL string in the 3.18.0 object pool, `pp+0x77090`); the sender was not compared function by function. 3.24.3: present. since: ≤3.18.0.

## Known unknowns

- The `icon_infos[].url` host and image format are not known.
- No response was captured.

## Device-tested by

none
