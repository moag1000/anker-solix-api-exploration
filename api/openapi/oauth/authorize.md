> Verified against: App 3.24.3 · Date: 2026-10-20 · Confidence: string-only · Owner page: this page

# authorize

## Purpose

Not a request the app sends: `AlexaConstants::isAlexaAuthUrl` (`charging/constants/alexa_constants.dart @0x49ce29c`) recognises the link that the Alexa app opens in the Anker app by testing a URL string for the marker `alexaapp_to_ankerpower` (`@0x49ce2c8`) or for the path `/openapi/oauth/authorize` (`@0x49ce2f8`); the query of that link is then read by `AlexaLinkLogic::parseAuthParams` and used for [`app_to_app_access`](app_to_app_access.md) (asm-traced for the string test; the reading of the link's role is string-only).

## Upstream name

`none` (no upstream name)

## Method+URL

No HTTP method and no sender: the string `/openapi/oauth/authorize` (`charging/constants/alexa_constants.dart @0x49ce2f8`) is the argument of a string-matching interface call (`@0x49ce304`, selector not named by Blutter) that `isAlexaAuthUrl` applies to the incoming URL; the same function tests the marker `alexaapp_to_ankerpower` the same way (`@0x49ce2d4`). Nothing in the Dart code calls an `*Http*` wrapper with it (string-only).

## Encrypted?

Not applicable (string-only): the string is matched against an incoming link, not sent by an HTTP wrapper.

## Request

No request: the string is only matched against a URL. The query parameters of the incoming link that the app reads afterwards are `client_id`, `redirect_uri`, `response_type`, `scope` and `state` (`charging/ui/page/account/login/alexa_link_logic.dart @0x3bce4d0`..`@0x3bce5f4`); they are documented under `app_to_app_access`.

## `param_type`/`cmd`

n/a

## Response model (link)

none: there is no response; the function returns a bool (`charging/constants/alexa_constants.dart @0x49ce29c`).

## Response

No response key exists (see Response model).

## Example request/response

None: this is a URL pattern test, not a request.

## Errors seen

none traced: not a request. Code meanings are owned by `api/errors.md`.

## Callers in app

- `charging/constants/alexa_constants.dart`: `isAlexaAuthUrl` @0x49ce29c (URL literal only, no `*Http*` call)

## Since/changed

3.18.0: present. 3.24.3: present. since: <=3.18.0. No parameter delta is recorded for this URL in `tools/out/diff_3.18.0_3.24.3.md` (string-level diff only; it compares literals, not types).

## Known unknowns

- Whether the Alexa app opens a path with this exact prefix on a host of the Anker domain (an app link) or a custom scheme: only the matched strings are visible, not the manifest or associated-domain declarations.
- What the marker `alexaapp_to_ankerpower` stands for (a query value or a scheme part): the string is matched, its position in the link is not visible.
- Why the Anker app tests for `/openapi/oauth/authorize` at all, since the app never requests it: the string is the path of the OAuth authorize endpoint that the Alexa app opens; the server-side endpoint is not part of the app's own request set.

## Device-tested by

none
