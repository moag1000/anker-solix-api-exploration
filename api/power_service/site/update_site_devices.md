> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# update_site_devices

## Purpose

Replaces the PPS list of a site: `SelectPPSLogic::updateSelectPPSDevice` (`device/greenpower/recharge/select_pps/select_pps_logic.dart`) calls `updateSiteDevices`.

## Upstream name

`none` (no upstream name)

## Method+URL

`POST /power_service/v1/site/update_site_devices` (asm-traced): URL string at `http_request_repository_impl.dart @0x278e740`, method object `Method.post` (pool entry `pp+0xa7e0`) at `@0x278e738`, in `HttpRequestControllerImpl::updateSiteDevices` (`http_request_repository_impl.dart @0x278e680`).

## Encrypted?

encrypted: `true`. Scheme and header rules: `api/encryption.md`; per-sender values are in "Callers in app".

## Request

The body is a 2-pair map literal typed `<String, Object>` (type arguments `@0x278e6f4`) built in `updateSiteDevices` (`http_request_repository_impl.dart @0x278e680`).

| field | type | required | example | source |
|---|---|---|---|---|
| `site_id` | ? | yes | | key `@0x278e6cc`, value store `@0x278e6dc` (parameter at `fp-0x18`) |
| `pps_list` | ? | yes | | key `@0x278e6e0`, value store `@0x278e6f0` (parameter at `fp-0x10`) |

## `param_type`/`cmd`

n/a

## Response model (link)

Not determined. The builder passes the forwarding template `rx_workers.dart @0x228e574` as success callback and its failure template to the caller's callbacks; the caller `SelectPPSLogic::updateSelectPPSDevice` was not read.

## Response

Not determined (see Response model).

## Example request/response

Request, synthesized (types unresolved)

```json
{"site_id": "<site_id>", "pps_list": "<pps_list>"}
```

Response: not determined.

## Errors seen

None traced. The caller's failure callback was not read. Error codes are catalogued in `api/errors.md`.

## Callers in app

- `charging/http/http_request_repository_impl.dart`: `updateSiteDevices` @0x278e680 (encryptionRequestHttp; encrypted: true)

Called from:

- `charging/http/http_request_repository.dart::updateSiteDevices`
- `charging/ui/page/device/greenpower/recharge/select_pps/select_pps_logic.dart::updateSelectPPSDevice`

## Since/changed

3.18.0: present. 3.24.3: present. since: ≤3.18.0. The endpoint is in none of the added, removed or changed-params lists of `tools/out/diff_3.18.0_3.24.3.md`, so there is no string-level parameter delta.

## Known unknowns

- Types of `site_id` and `pps_list` (parameters; the caller was not followed). Header stays string-only. — attempted 2026-10-20 (two-hop not readable: the only caller, `SelectPpsLogic.updateSelectPPSDevice` (`charging/ui/page/device/greenpower/recharge/select_pps/select_pps_logic.dart @0x278e600`), passes values read from fields; no declared types. Header stays string-only)
- Whether the answer is read: the caller's callbacks were not read. — traced 2026-10-20: not decoded in this pass (caller callbacks); the reason given in the bullet stands

## Device-tested by

none
