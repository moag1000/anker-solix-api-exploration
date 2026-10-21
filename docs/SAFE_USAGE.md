> Verified against: App 3.24.3 · Date: 2026-10-19 · Page type: guidance (no API facts) · Owner page: this page

# Safe usage for library authors and home-automation users

This page is guidance for people who call the Anker cloud from their own code: authors of client libraries such as [thomluther/anker-solix-api](https://github.com/thomluther/anker-solix-api) and users who poll the cloud from Home Assistant or a script. It owns no API fact. Every number below is a link to the page that owns it, and nothing is restated here, so if a number changes on its owner page this page does not drift. The one thing this page does own is the recommendations in section 2 and the do-not list in section 3; those are the author's judgement, not app behavior and not `asm-traced`. The reasoning behind them is the app's own behavior in section 1, and where that evidence stops is listed in section 4.

The reverse engineering was heavily AI-assisted and has not been tested against the server for rate limits (see the disclaimer in [../README.md](../README.md)). You use this at your own risk. The upstream project describes a ban behavior (see [Known unknowns](../reference/business_rules.md#known-unknowns), library facts row); it is not verified here, and this repository cannot tell you where any limit is.

## Contents

1. [What the app itself does](#1-what-the-app-itself-does)
2. [Recommended polling for a library](#2-recommended-polling-for-a-library-recommendation)
3. [Do-not-do list](#3-do-not-do-list-recommendation)
4. [What is not known](#4-what-is-not-known)

## 1. What the app itself does

Facts only, each with its owner. Tag on the owner pages: `asm-traced` unless that page says otherwise.

- **Heartbeats and timers.** The site and device-list pages send an MQTT heartbeat request on a repeating timer, and the A5140 home page repeats one statistics call on its own timer; the device controllers also run a periodic device-info request. The intervals, call sites and what each timer does are in the [timer inventory](../reference/business_rules.md#timer-inventory); the short version is at [polling facts for library authors](../reference/business_rules.md#the-short-version). The heartbeat timers send MQTT requests, not HTTP calls. Several timer bodies were not read, so that inventory is a lower bound on what the app sends, not a complete list.
- **No refresh manager.** There is no app-wide refresh timer; `RefreshManager` only runs registered reload closures, see item 1 of [the short version](../reference/business_rules.md#the-short-version).
- **No spacing rule, no 429 handling.** The app defines no minimum spacing between two requests to one endpoint and does not react to a rate-limit status or header; see [minimum spacing](../reference/business_rules.md#minimum-spacing).
- **No retry or backoff on API calls.** The normal HTTP path is never retried and has no backoff; the only retry is on the OTA file download, see [retry and backoff](../reference/business_rules.md#retry-and-backoff).
- **461 and 463 are surfaced, not handled.** A timestamp rejection (461) and a key or signature failure (463) are reported to the caller as failures, with no automatic retry, clock correction or key renegotiation; see [what the app does on 461, 463 and 401](../reference/business_rules.md#what-the-app-does-on-461-463-and-401) and the code table in [api/encryption.md](../api/encryption.md#response-handling-and-error-codes).
- **401 means logout.** A 401 (and the related token-expired code) forces a logout; it is not an automatic re-login. A "logged in elsewhere" code also logs the session out. Owners: [business_rules.md](../reference/business_rules.md#what-the-app-does-on-461-463-and-401) and [auth.md, token lifecycle](../api/auth.md#token-lifecycle).
- **BLE and WiFi.** The app puts a device in either a WiFi state or a BLE state, and routes each command by that state; see [connection routing and the WiFi exclusion rule](../ble/protocol.md#connection-routing-and-the-wifi-exclusion-rule).

## 2. Recommended polling for a library (recommendation)

> Author's recommendation, derived from section 1. Not an app behavior, not `asm-traced`, not `device-tested`, and no server-side limit has been checked.

1. **Floor for state reads: not faster than once per minute per site (the author's conservative choice).** The app has no minimum-spacing rule for HTTP requests to copy. The heartbeat timers (P1 to P4) are MQTT requests and say nothing about HTTP load. The repeated HTTP fetches among the timer bodies that were read are the A5140 statistics call every 59 s (P6) and the A5101 system policy `check_function` request every 60 s (P14, `getLatestSystemFunction`); the device-info timer (P5) is armed only while the device is seen on WiFi, and its transport is undecided; the fast timers (P7 to P9) have unread or empty bodies and are not evidence of fast polling. All of this is in the [timer inventory](../reference/business_rules.md#timer-inventory) and [the short version](../reference/business_rules.md#the-short-version) (owner: [business_rules.md](../reference/business_rules.md)). The once-per-minute figure is chosen to be at least as slow as the slowest repeated HTTP fetch of the app (60 s), not derived from a measured limit.
2. **One site refresh per interval, shared.** Fetch the site data once per cycle and serve every entity from that result; do not let each entity or each automation trigger its own request.
3. **Do not copy the heartbeat timers into an HTTP loop.** The heartbeat is an MQTT request whose payload is not decoded (see [section 4](#4-what-is-not-known)); it is not an HTTP poll, so recommendation 1 does not rest on it.
4. **Back off on failures instead of retrying.** The app has no backoff, so there is no app behavior to copy. Make a failed cycle skip to the next interval and lengthen the interval after repeated failures.
5. **461 (clock):** the app does nothing; a library may resynchronize its clock and resend once, as suggested in [business_rules.md](../reference/business_rules.md#what-the-app-does-on-461-463-and-401). If it fails again, stop for that cycle.
6. **463 (key or signature):** renegotiate the session key once before the next request, per the same page and [api/encryption.md](../api/encryption.md#for-library-implementers). Do not renegotiate on every failure; see the do-not list.
7. **401:** treat the session as ended. Re-authenticate once, with a delay, and surface an error to the user if it fails; never loop on login. The app itself logs out rather than re-logging in ([auth.md](../api/auth.md#token-lifecycle)).
8. **Writes are not polls.** Send a control command once, wait for its result, and do not repeat it to "make sure". The app serializes commands to one device with a transaction lock, see row T7 in [timeouts and timing constants](../reference/business_rules.md#timeouts-and-timing-constants).

## 3. Do-not-do list (recommendation)

> Author's recommendations. The reasons point at app behavior or at documented unknowns; none of them is a measured server limit.

- **No tight loops.** Never poll in a loop without a sleep, and never retry a failed request immediately. The app does neither (see [retry and backoff](../reference/business_rules.md#retry-and-backoff)).
- **Warning:** `legal_limit` is the regulatory feed-in limit of the site's region; the server not enforcing it is not permission — exceeding it may be unlawful or void the installation's certification, and this reference does not endorse it.
- **No fuzzing of `set_*` or `verify_*` endpoints.** These change device state or check secrets. Do not probe them with guessed or generated values. [verify_unlock_default_power_code](../api/devicecontrol/device/verify_unlock_default_power_code.md) is the example: it checks a code that gates an output limit above the legal limit, so repeated guesses look like code guessing, and what the server does about that is not recorded there. Send only values the app itself can send, and see [validation_model.md](../reference/validation_model.md) for what the app checks first.
- **No key-exchange storms.** Do not call the key exchange on every request or every failure. One exchange per session, renegotiate after 463, see [api/encryption.md](../api/encryption.md#key-exchange-endpoint).
- **No parallel sessions from one account.** The server has a "logged in elsewhere" code that the app answers with a forced logout ([auth.md](../api/auth.md#token-lifecycle), code table in [api/encryption.md](../api/encryption.md#response-handling-and-error-codes)). Two clients logging in alternately with the same account may log each other out, and if both clients re-login automatically that could turn into a login loop (an assumption, not tested). Use one process per account, or a dedicated account that you share the system with.
- **No retry loop on 401.** See recommendation 7.
- **No BLE while the device is on WiFi, and no BLE as a cloud fallback.** The community finding is that BLE is unavailable while the device is on WiFi. It is an external statement, not verified here; see [the WiFi exclusion rule](../ble/protocol.md#connection-routing-and-the-wifi-exclusion-rule). Do not design a library that switches to BLE when the cloud is down.
- **No unattended writes above what the app allows.** Power limits and similar settings have app-side guards; see [business_rules.md](../reference/business_rules.md#a17c1-solarbank-gates-and-pre-flight-checks) and do not bypass them from automation.
- **Do not publish your credentials, tokens, or the key exchange material** in issues or logs. This page and the rest of the repository use placeholders for a reason.

## 4. What is not known

These are the limits of the evidence behind sections 2 and 3. The owner list is [Known unknowns](../reference/business_rules.md#known-unknowns) in business_rules.md.

- **Server-side rate limits** and whether the server accepts the spacing the app uses are unknown; no device or server test is recorded. The upstream project describes a ban behavior; this repository has not checked it.
- **Unread timers.** Several timer bodies, including the OTA result polling (P11 in the [timer inventory](../reference/business_rules.md#timer-inventory)), were not read, and mixin-deduplicated functions have no asm in the dump, so the app may send more than the inventory shows.
- **Heartbeat details.** Content, topic and the debounce value of the MQTT heartbeat are not decoded, and whether the periodic device-info request travels over BLE or the cloud is undecided.
- **SDK retries.** Whether the native SDK retries or backs off is not known ([api/encryption.md known unknowns](../api/encryption.md#known-unknowns)).
- **Whether `verify_*` endpoints lock out repeated wrong codes** is this page's own open question; the endpoint page records no lockout ([verify_unlock_default_power_code](../api/devicecontrol/device/verify_unlock_default_power_code.md#known-unknowns)).
- **Firmware and BLE.** The WiFi/BLE exclusion rule comes from the community, not from firmware reading ([ble/protocol.md known unknowns](../ble/protocol.md#known-unknowns)).

If you measure any of these against your own account, report it as a `device-tested` finding with your method; see [CONTRIBUTING.md](../CONTRIBUTING.md).
