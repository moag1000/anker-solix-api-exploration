Hi @thomluther,

quick update — the models still allow this, and the first run on the current APK is done.

**What I did**
- Pulled Anker Power **3.24.3** (versionCode 237, Dart 3.11.0) and decompiled `libapp.so` with Blutter (had to build the Dart 3.11 VM for it).
- Traced the exact code path behind the 10 W slider: `StationPowerLimitLogic::showOutputPowerPicker` → `_setOutputPowerLimit` → `HttpRequestControllerImpl::setSiteDevicePowerLimit`.

**What the app sends for the fine-grained limit (e.g. 790 W)**

```json
POST /power_service/v1/site/set_site_device_param
{
  "site_id": "<site_id>",
  "param_type": "19",
  "cmd": 123,
  "param_data": "{\"display_type\":1,\"power_limit\":{\"limit\":790,\"limit_real\":790}}"
}
```

- `limit` and `limit_real` are the same value (slider value).
- `display_type: 1` is **new since 3.18.0** — the old app (discrete options only) sent the same structure without it. My reading: this is the flag that tells the server "free value, not an entry of `power_limit_option`". That would explain your `10004 ItemNotFoundError` for 790 W and the success for 800 W.
- `cmd` is `123` in the app for this call (your library uses 17 for everything; `setSiteDeviceParam` in the app does use 17, but the power-limit function hardcodes 123). Whether the server cares is unknown.
- The app sends this through its encrypted request path (`x-encryption-info: algo_ecdh`). Since 800 W works for you unencrypted, I don't think encryption is the blocker, but noting it.

**Slider range / DIY unlock**
- Range in the app: 100 W … `legal_power_limit`, step 10 W.
- Values *above* the legal limit go through a new "DIY legal power limit" sheet that can require an unlock code: `POST /devicecontrol/v1/device/verify_unlock_default_power_code` with `{"unlock_code", "device_sn", "site_id"}` → `verify_result`. `get_power_limit` now carries `unlock_default_power_type`, `unlock_pop_content`, `unlock_pop_image` for that. Not relevant for 790 W, but good to know it exists.

**Suggested test on your A17C5 (in this order, raw payloads)**

| # | cmd | param_data | expectation |
|---|-----|------------|-------------|
| 1 | 17 | `{"display_type":1,"power_limit":{"limit":790,"limit_real":790}}` | works → `display_type` is the key |
| 2 | 123 | same | works → either flag or cmd |
| 3 | 123 | `{"power_limit":{"limit":790,"limit_real":790}}` (no display_type) | control |

If you can paste the raw responses (incl. error codes) for the three, I'll record the result as device-tested.

**One honest caveat about the existing docs**
While doing this I found a systematic mistake in my earlier Blutter-based numbers: Blutter prints raw register values, and Dart stores small ints tagged (value × 2). So several integers in this repo are exactly double the real value — e.g. the `cmd: 246` in FLOWS.md is really 123, the MQTT header `cmd 34 / cmd_status 4 / sign_code 2` are really 17 / 2 / 1 (which matches what your library has always used), and `disaster_type 4` is really 2. String-based facts (endpoint paths, field names, `"19"` etc.) are not affected. I'm reworking the whole repo on 3.24.3 with that fixed, plus the ~80 endpoints that are new since 3.18.0 (installer service, Modbus TCP settings, `power_service/v2`, …). Will post here when the power-limit pages are updated.

Cheers,
Michael
