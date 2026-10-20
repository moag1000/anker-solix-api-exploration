> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Page type: reference · Owner page: this page

# Business rules (App 3.24.3)

Closest template: [../docs/templates/flow.md](../docs/templates/flow.md) (Preconditions, Timing, Failure paths, Known unknowns), but the sections here are grouped by topic instead of by one flow, because a rule belongs to a topic and not to one UI action. The page is `Page type: reference`; its header carries the lowest tag among its rows (`string-only`, because some rules are log or localization strings without a decoded caller).

This page owns the client-side rules of the 3.24.3 app: when it polls, how long it waits, when it refuses to send, which hardcoded limits it applies. It replaces the deleted 3.18.0 root page `BUSINESS_RULES.md`. Protocol facts stay with their owners: opcodes and TLV tags on the [mqtt pages](../mqtt/README.md), `param_type` and `cmd` on [../api/param_types.md](../api/param_types.md), signing and the 461/463 headers on [../api/encryption.md](../api/encryption.md), sequences on [../flows/README.md](../flows/README.md). What the app checks before it sends a value is on [validation_model.md](validation_model.md).

## Contents

1. [How to read this page](#how-to-read-this-page)
2. [Polling facts for library authors](#polling-facts-for-library-authors)
3. [Timeouts and timing constants](#timeouts-and-timing-constants)
4. [Retry and backoff](#retry-and-backoff)
5. [A17C1 Solarbank: gates and pre-flight checks](#a17c1-solarbank-gates-and-pre-flight-checks)
6. [A17X8 smart plug](#a17x8-smart-plug)
7. [A5101 HES and station-level limits](#a5101-hes-and-station-level-limits)
8. [A1790 expansion battery guards](#a1790-expansion-battery-guards)
9. [BLE rules](#ble-rules)
10. [Counts, defaults and catalogs](#counts-defaults-and-catalogs)
11. [Corrections to the 3.18.0 root page](#corrections-to-the-3180-root-page)
12. [Changed since 3.18.0](#changed-since-3180)
13. [Known unknowns](#known-unknowns)

## How to read this page

- **Row references.** `BR-n` is row n (counting table rows from the top) of [../docs/audit/BUSINESS_RULES.md](../docs/audit/BUSINESS_RULES.md), the Smi sweep of the old page (66 rows: 27 OK, 16 WRONG, 15 NOT-FROM-ASM, 5 CHANGED-IN-3.24.3, 3 UNVERIFIABLE). The audit has no row numbers of its own; they are assigned here and repeated on [validation_model.md](validation_model.md). `new read` marks a rule that is not an audit row and was read from the 3.24.3 asm for this page (grep and sed only).
- **Integers** follow the Smi rule in [../METHODOLOGY.md](../METHODOLOGY.md#smi-rule-reading-numbers-from-blutter-output). Every interval below is given with its store width: a `Duration` built in code is `AllocateDurationStub` plus a 64-bit `stur x0,[x3,#7]` (unboxed microseconds, so the raw immediate is the real value); a `Duration` loaded from the object pool is an untagged microsecond value printed by `pp.txt`.
- **Tags.** `asm-traced` = cited 3.24.3 site; `string-only` = string in the binary without a decoded caller; `upstream-confirmed` = upstream file named. No `device-tested` fact is on this page.
- **"Not found in 3.24.3"** means: searched in the 3.24.3 asm with the stated names or strings and nothing matched. It does not say the rule is false on the server or on the device.
- **Bool tests.** Blutter shows Dart booleans as `tbz`/`tbnz w0,#4`. In every gate on this page the branch targets only make sense if `tbnz w0,#4` jumps when the value is `false` (for example `canEditEquipmentFeedNetwork` would otherwise be false whenever `isSettingsEnable` is true). The gates are described with that polarity; the field names are not in the dump (see the notes per gate).

## Polling facts for library authors

Tag: `asm-traced` unless a row says otherwise. This section is the input of the safe-usage guidance ([docs/SAFE_USAGE.md](../docs/SAFE_USAGE.md)). All timer rows were produced by one scan of the `Timer.periodic` call sites of the app files in the 3.24.3 dump (124 files, after excluding the Flutter framework, third-party packages, a few UI-only widgets; the `ota_kit` package was in the scan, but its timer bodies were not read) and then reading the owning function; the same timers with the same values exist in 3.18.0 (see [Changed since 3.18.0](#changed-since-3180)).

### The short version

1. There is no `RefreshManager` timer. `RefreshManager` (`charging/feature/common_location/common_location.dart`, class id 6044; a second `RefreshManager` in `ak_soft_ems/common_location/common_location.dart`, class id 8025, also has no timer or `Duration`) only keeps a list of reload closures: `refreshData` (`@0x2409b20`) runs all registered closures with `Future.wait` (`wait()` `@0x2409b8c`) and `registerReload` (`@0x2409cfc`) appends one. It holds no `Duration`, `Timer` or retry counter. Mentions of "RefreshManager intervals" (the rework plan, the CHANGELOG entry about the disaster-preparedness initialization) have nothing to point at: the class has no interval.
2. The repeated HTTP data fetches found are the 59 s statistics call of the A5140 home page (P6) and the 60 s `check_function` request of the A5101 system policy page (P14, found by reading the P14 closure). The 30 s timers send an MQTT request (a site heartbeat or a device-list heartbeat, P1 to P4); the 60 s device timer (P5) is armed only while the device status is `wifiConnected` and asks the device controller for all device info through the per-call transport gate. The OTA result polling (P11) is a kit channel poll. The closures of P7, P9, P10, P12, P13 and P15 call the functions named in the table; the bodies of those functions were not read.
3. The 1 s, 100 ms and 120 ms timers found are UI countdowns, slider long-press repeat and progress animation (see the list after the table).
4. The plain HTTP path has no retry. The only `RetryInterceptor` in the app is on the OTA file download, with one retry (see [Retry and backoff](#retry-and-backoff)).
5. HTTP 461 and 463 are reported to the caller and not retried; 401 and the SDK codes 401/26085/26084 force a logout (see [Failure codes](#what-the-app-does-on-461-463-and-401)).

### Timer inventory

| id | timer (file, function) | interval | store | what the callback does | tag |
|---|---|---|---|---|---|
| P1 | `charging/ui/page/home/home_base_logic.dart` `HomeBaseLogic.startRefreshTimer` | 30 s (30,000,000 us) | `Duration` alloc `@0x2359cf8`, `mov x0,#0xc380` + `movk #0x1c9,lsl#16` `@0x2359d00`, `stur x0,[x3,#7]` `@0x2359d0c` (64-bit), `Timer.periodic` `@0x2359d2c` | closure `@0x2359d6c` calls `sendPowerSiteHeartBeatMsg` (`@0x2359dbc`): builds an `MqttServe` request and calls `siteSendMsg`; log string `e1电站发送mqtt心跳 ` (my translation: "e1 station sends MQTT heartbeat") `@0x2359e10`, debounce key `home_mqtt_heartbeat_` `@0x2359e48`; the same message is also sent once, 1 s after `stationSubscribeTopic` (`@0x2359bb0`, `Future.delayed` `@0x2359c0c` with pool `[pp+0x1458]`, untagged 1,000,000 us), call `@0x2359c60`, which then arms the timer `@0x2359c78` | asm-traced |
| P2 | `charging/ui/page/device/main/station_device_home/station_main_page/station_main_page_logic.dart` `StationMainPageLogic.startRefreshTimer` | 30 s (30,000,000 us) | `mov x0,#0xc380` `@0x2403b00`, `stur x0,[x3,#7]` `@0x2403b0c` (64-bit), `Timer.periodic` `@0x2403b2c` | closure `@0x2403b68` calls `sendPowerSiteHeartBeatMsg` (`@0x2403bb8`, same `MqttServe.siteSendMsg` shape); the timer is armed by the call at `@0x2403a80` | asm-traced |
| P3 | `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart` `StationEnergySystemLogic.startRefreshTimer` | 30 s (30,000,000 us) | `mov x0,#0xc380` `@0x2389a70`, `stur x0,[x3,#7]` `@0x2389a7c` (64-bit), `Timer.periodic` `@0x2389a9c` | closure `@0x2389adc` calls `sendPowerSiteHeartBeatMsg` `@0x2389b10` | asm-traced |
| P4 | `charging/ui/page/device/main/station_device_home/device_main_page/device_main_logic.dart` `DeviceMainLogic.startRefreshTimer` | 30 s (pool `Obj!Duration` `[pp+0x29af0]`, untagged 30,000,000 us) | `Timer.periodic` `@0x244f84c` | closure `@0x244f88c` calls `sendDeviceListHeartBeatMsg` (`@0x244f8dc`): same `MqttServe.siteSendMsg` request, built by `setCmdRequest` (`@0x244f93c`, keys `user_id`, `site_id`, `head`, `payload`); one immediate call `@0x244f794` before the timer is armed `@0x244f7ac` | asm-traced |
| P5 | `charging/ble/device/A17C1/a17c1_anker_device.dart` `A17C1AnkerDevice.startIotTimer` (the same function exists in six more device classes, `Timer.periodic` sites: `a17C0_anker_device.dart @0x36b6844`, `a172x_anker_device.dart @0x36b6644`, `a1771_anker_device.dart @0x36b6a78`, `a17a3_anker_device.dart @0x36b6ed4`, `a17x7_anker_device.dart @0x36b7304`, `a17x8_anker_device.dart @0x36b7104`) | 60 s (pool `[pp+0x1d8e0]`, untagged 60,000,000 us) | `Timer.periodic` `@0x36b6cb4` | starts only when `_getCurrentStatus()` equals `wifiConnected` (pool object `[pp+0xca50]`, enum index 0, compared at `@0x36b6c5c` to `@0x36b6c68`; object dump `objs.txt Obj!DeviceConnectionStatus@4212b21`), so the timer is armed only for a device that the app sees on WiFi, and each tick's `getDeviceAllMessage` goes through the per-call transport gate of the device controller (BLE for `bleBusinessConnected`, MQTT-wrapped for `wifiConnected`, nothing otherwise); closure `@0x36b6dbc` logs `[能源上报定时] 定时60s 发送能源数据上报` (my translation: "energy report timer, every 60 s send energy data report") `@0x36b6e0c` and calls `getDeviceAllMessage` `@0x36b6e28` (the function also calls `getDeviceAllMessage` once at `@0x36b6c90` before arming the timer, so the first poll is at t=0), which calls `setDeviceUpdateEnergy` `@0x36b6d20` and, after a one-shot delay, `getAllDeviceInfo` `@0x36b6d90`; the timer is re-armed from `@0x371d2ac` only while the connected status holds | asm-traced |
| P6 | `charging/ui/page/device/a5140/a5140home/a5140home_logic.dart` `A5140homeController._startPollingTimer` | 59 s (pool `[pp+0x106d90]`, untagged 59,000,000 us) | log string `====开启A5140首页轮询timer-间隔:59s--` (my translation: "start A5140 home polling timer, interval 59 s") `@0x34d06dc`, `Timer.periodic` `@0x34d070c` | closure `@0x34d0740` calls `_pollingTimerCallback` (`@0x34d0798`): `getPvTotalData` `@0x34d07bc`, `_isOffline` `@0x34d07c4`; `getPvTotalStatistics` `@0x34d0914` is the statistics call. This is the one home page found that repeats a data fetch by itself | asm-traced |
| P7 | `charging/ui/page/device/a2345/a2345home/a2345home_logic.dart` `_startDCPortHeartbeatTimer` (and `a91b2home_logic.dart`, `@0x279363c`) | 9 s (pool `[pp+0xe2138]`, untagged 9,000,000 us) | `Timer.periodic` `@0x2771ac0` | DC-port heartbeat of the charger home page; closure `@0x2772218` calls `_sendDCPortHeartSchedule` (`@0x2772244`), a command send of the charger page (its body was not read) | asm-traced |
| P8 | `charging/aiot/iot_logic.dart` `IoTLogicManager.createTimer` | 2 s (pool `[pp+0x18ac0]`, untagged 2,000,000 us) | `Timer.periodic` `@0x419df98`, started by `onResumed` `@0x419df0c` | closure `@0x419e038` logs `轮询获取列表状态` (my translation: "poll list status") `@0x419e060` and then continues into code the AOT compiler removed (`Attempt to execute code removed by Dart AOT compiler (TFA)` `@0x419e090`, `Throw`): the timer exists but its body does nothing | asm-traced |
| P9 | `charging/ui/page/station/A5101/a5101_station_logic.dart` `A5101StationWithA5150Logic.onInitStation` | 2 s (pool `[pp+0x18ac0]`, untagged 2,000,000 us) | `Timer.periodic` `@0x47acf30` | closure `@0x47ad564` calls `onTestConnecting` (`@0x47ad590`; its body was not read) | asm-traced |
| P10 | `charging/ui/page/device/a5101/device_home_page/device_home_logic.dart` closure after `getDeviceSoc` | 150 s (pool `[pp+0x115ce8]`, untagged 150,000,000 us) | `Timer.periodic` `@0x33c5ac4` | closure `@0x33c6710` calls `getDeviceSoc` (`@0x33c6798`), a repeated read of the device SoC (its transport was not read) | asm-traced |
| P11 | `ota_kit/src/controllers/resume/ota_remote_observer.dart` `OTARemoteObserver._startResultPolling` | 60 s (pool `[pp+0x1d8e0]`, untagged 60,000,000 us; pool constant, no register store) | `Timer.periodic` `@0x2ecee9c` | calls `_pollResult` (`@0x2ecef04`, function `@0x2ecef1c`); `_pollResult` asks `isDeviceOTAInProgress`, which sends the kit channel `akiot.device.is_ota_in_progress` and then reads the firmware version ([../flows/ota_monitor.md](../flows/ota_monitor.md#steps), step 8), so it is a kit channel poll, not a plain HTTP fetch | asm-traced |
| P12 | `charging/ui/page/device/a1340/a1340real_time_chart/a1340real_time_chart_logic.dart` `startTimer` | 60 s (pool `[pp+0x1d8e0]`, untagged microseconds: a pool constant, no register store, so the Smi rule does not enter) | `Timer.periodic` `@0x33e677c` | closure `@0x33e67b8` logs the current time (`当前时间是：`) and works on `DateTime` parts (`_parts` at `@0x33e682c`); the rest of the body was not read | asm-traced |
| P13 | `charging/ui/page/device/a1782/station/station_main_page/chart/a1782_chart_logic.dart` `_startTimer` | 60 s (pool `[pp+0x1d8e0]`, untagged microseconds: a pool constant, no register store, so the Smi rule does not enter) | `Timer.periodic` `@0x34cc6f0` | closure `@0x34cc730` checks that a registered controller exists and calls `refreshChart` (`@0x34cc7cc`; the body of `refreshChart` was not read) | asm-traced |
| P14 | `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_logic.dart` `startCheckFunctionTimer` | 60 s (pool `[pp+0x1d8e0]`, untagged microseconds: a pool constant, no register store, so the Smi rule does not enter) | `Timer.periodic` `@0x28e7ce4` | closure `@0x28e7d20` calls `getLatestSystemFunction` (`@0x28e7d4c`), which calls `HttpRequestRepositoryImpl.checkFunction` (call `@0x28e7ddc`, function `http_request_repository_impl.dart @0x28e7e58`, key `station_id`, URL literal `/charging_hes_svc/check_function` at `@0x28e7f0c`; owner [check_function](../api/charging_hes_svc/check_function.md)): a repeated HTTP request every 60 s while the timer runs | asm-traced |
| P15 | `small_charging_platform/src/mobile_temperature/strategy/mobile_temperature_utils.dart` `_startTimer` | 60 s (pool `[pp+0x1d8e0]`, untagged microseconds: a pool constant, no register store, so the Smi rule does not enter) | `Timer.periodic` `@0x466752c` | closure `@0x4667568` calls `_collectPhoneTemperature` (`@0x4667594`; a local sensor read, the body was not read) | asm-traced |

Intervals that exist in the pool but are not data polls (listed so nobody mistakes them for polls): 1 s countdowns (`[pp+0x1458]`, 1,000,000 us; login, OTP, wizard screens), 100 ms slider long-press repeat (`[pp+0x68e8]`, `energy_deploy_logic.dart` `@0x42ddf80`, `@0x42de3bc`), 120 ms progress animation (`[pp+0x9f4c8]`), 600 s weather refresh (`[pp+0x1bca8]`, `station_home/src/weather/weather_service.dart @0x2badb24`), 300 s Anka agent proactive polling (`[pp+0x1f438]`, `anka_agent_entry_logic.dart @0x2e0b138`). Timers named `startCountDown` or `_startOTA` use the 5 s pool value (`[pp+0x13850]`, 5,000,000 us, for example `a17c1home_logic.dart @0x262ee30`, `a1770ota_logic.dart @0x46eeb1c`); their bodies were not read.

### Heartbeat message content (new read)

Tag: asm-traced. The command map that P1 to P4 hand to `MqttServe.siteSendMsg` is built by `setCmdRequest` (`station_energy_system_logic.dart @0x235a094`, size 0x1a8; `device_main_logic.dart @0x244f93c` for P4): a JSON object with the keys `head` and `payload`. `payload` is the JSON text of `{"user_id": <SpUtil.getUserId()>, "site_id": <site id>}` (`@0x235a0dc` to `@0x235a168`, `jsonEncode` at `@0x235a1dc`). `head` is `HttpCommandTransformer.getPowerSiteCommandHeader` (`http_command_transformer.dart @0x235a254` to `@0x235a3fc`), a map of nine pairs: `version` `"1.0.0.1"`, `client_id` (value from a call, not read), `sess_id` `"1"`, `msg_seq` 1, the command code (decimal ten, raw immediate 20 at `@0x235a35c`), `cmd_status` 2, `sign_code` 1, `seed` `"1"`, `timestamp` (the UTC time in seconds: microseconds divided by 1000 twice, `@0x235a29c` to `@0x235a2ac`). The Smi values are stored with `StoreField` into the array (raw 2, 20, 4, 2, so 1, 10, 2, 1). Fact belongs on [../mqtt/envelope.md](../mqtt/envelope.md) (the head fields `cmd_status` 2, `sign_code` 1 and `msg_seq` 1 agree with the upstream-tested head).

### Minimum spacing

- The app defines no minimum spacing between two HTTP requests to the same endpoint. The only client-side spacing found is `AnkerDebounceThrottle` with a default delay of 300 ms (`base_service/util/anker_debounce_throttle.dart @0x267d9e4`, pool `[pp+0x93f0]`, untagged 300,000 us; BR-29) and a per-key debounce on the heartbeat (`debounceKey` `home_mqtt_heartbeat_`, the `debounceMs` value is a static field that was not decoded).
- Nothing in the HTTP status handler reacts to HTTP 429 or to a rate-limit header; the handler tests 463, 461 and 401 only ([../api/encryption.md](../api/encryption.md#response-handling-and-error-codes)). Whether the server throttles is outside the app. The upstream library documents server-side limits; this repository has not verified them (see [Known unknowns](#known-unknowns)).
- Transaction lock for commands to one device: see [Timeouts and timing constants](#timeouts-and-timing-constants), row T7.

### What the app does on 461, 463 and 401

Tag: `asm-traced`. Full tables and addresses live on [../api/encryption.md](../api/encryption.md#response-handling-and-error-codes) and [../api/auth.md](../api/auth.md#token-lifecycle); this is the rule for library authors.

- **461** (request timestamp rejected, device clock): reported to the caller as a failure with a "device time may be wrong" hint; no retry, no clock correction in the app. Author's recommendation, not an app behavior: resynchronize the clock and resend once.
- **463**, or a failed response signature check: reported as a failure; the log says the key must be renegotiated, but no renegotiation is started in that function. Author's recommendation, not an app behavior: renegotiate the session key before the next request.
- **401** (HTTP status with body code 401 or 26085) and SDK code 26084: forced logout through `_handler401` (`HttpEncryptionDecorator.dart @0x486b2bc`, `performLogout` `@0x486b3c8`), not an automatic re-login. The 3.18.0 root page said "HTTP 401 triggers `_reLogInIoTSDK()` transparently" (BR new read): in 3.24.3 `_reLogInIoTSDK` (`http_request_repository_impl.dart @0x273cd20`) is called from `updateRegionDomain` (`@0x273c954`, call `@0x273ccf8`), the region-switch path, and not from the 401 handler.

## Timeouts and timing constants

Tag: `asm-traced`. All durations are pool objects (untagged microseconds) unless the store column says otherwise.

| id | constant | value | site | store | rows |
|---|---|---|---|---|---|
| T1 | default debounce of `AnkerDebounceThrottle` | 300 ms | `base_service/util/anker_debounce_throttle.dart @0x267d9e4` | pool `[pp+0x93f0]` | BR-29 |
| T2 | BLE connect timeout | 30 s | `base_service/util/simple_ble_connector.dart @0x43181c8` (string `Connection timeout (30s)`) | pool `[pp+0x29af0]` | BR-33, BR-62 |
| T3 | default BLE command response wait | 5 s | `charging/communication/command_controller/ble_command_controller.dart` `sendCommand @0x226fc88` (default `delay` null gives `Instance_Duration`) | pool `[pp+0x13850]` | BR-19, BR-34 |
| T4 | background disconnect threshold | 30 min | `charging/base/app_life_cycle_delegate.dart @0x2856970`; also the `Timer.periodic` of `a17c1home_logic.dart @0x262d53c` and `a17c0home_logic.dart @0x26749d0` | pool `[pp+0xd7e8]`, untagged 1,800,000,000 us | BR-37, BR-63 |
| T5 | plain-HTTP connect and send timeout | owned by [flows/encrypted_request.md](../flows/encrypted_request.md#timing-delayspolling); not repeated here | | | |
| T6 | plain-HTTP receive timeout | owned by [flows/encrypted_request.md](../flows/encrypted_request.md#timing-delayspolling); not repeated here | | | |
| T7 | transaction lock timeout per device command | 6 s when a transaction config exists, 15 s default | `base_service/ak_iot_kit/transaction/transactionlock_interceptor.dart @0x221b1f0`; `transaction_manager.dart` `lockPropertiesForCommand @0x221bf30` | `r5 = 12` boxed argument (Smi, 12 / 2 = 6 s); `mov x0,#0xf` merged into `mul x3,x0,#1000000` (unboxed 15 s) | BR-52 |
| T8 | pool Duration 900 ms | 900 ms | exists in pool (`[pp+0x27d80]`); users found: the unity three-dot indicator and the anka_agent banner only; no safety-SOC use found | pool `[pp+0x27d80]` (no decoded consumer; string-only) | BR-30 |
| T9 | pool Duration 2 s | 2 s | `[pp+0x18ac0]`: users are P8 (`iot_logic.dart @0x419df98`), P9 (`a5101_station_logic.dart @0x47acf30`) and the A2345/A91B2 get-all-info timeout timers; the "MQTT message listener" closure at `[pp+0x18ac8]` belongs to a mixin-deduplicated function whose asm is not in the dump | pool | BR-31 |
| T10 | pool Duration 60 s | 60 s | `[pp+0x1d8e0]`: users are P5 (seven device classes, for example `a17c1_anker_device.dart @0x36b6cb4`) and P11 to P15 (bodies not read) | pool | BR-35 |
| T11 | pool Duration 5 min | 5 min | `[pp+0x1f438]` is used by the Anka agent proactive polling (`anka_agent_entry_logic.dart @0x2e0b138`); the "every 5 minutes" of the A17C1 error-10 text is text inside the localization string only | pool | BR-36 |
| T12 | pool Duration 5 s | 5 s | `[pp+0x13850]` is the BLE command wait (T3) and the interval of the `startCountDown` (`a17c1home_logic.dart @0x262ee30`), OTA and screen-timeout timers; it is not a generic API polling interval | pool | BR-32 |

The 3.18.0 root page called the 30 s value "BLE command timeout" and the 5 s value "API polling interval". Both attributions are wrong in 3.24.3 (BR-34, BR-32); see [Corrections](#corrections-to-the-3180-root-page).

## Retry and backoff

Tag: `asm-traced`.

| fact | site | detail |
|---|---|---|
| The app never retries a normal API request | `http_request_repository_impl.dart` (grep: `RetryInterceptor()` appears only in `downloadOta`) | `HttpRequestControllerImpl.downloadOta` (`@0x2694384`) creates a Dio (`createDio` `@0x2694408`), adds a `RetryInterceptor` (`@0x2694410`, constructor `@0x2694420`) and calls `download` |
| Retry count of that interceptor | `dio_smart_retry/src/retry_interceptor.dart` constructor `@0x26be40c`: `mov x3,#1` then `stur x3,[x6,#0xf]` `@0x26be460` (64-bit, unboxed) | 1 retry. `onError` compares `attempt + 1` with the constant: `add x4,x0,#1` `@0x4766398`, `cmp x4,#1` `@0x47663a0`, `b.gt` `@0x47663a4` skips the retry when the attempt counter is above 1 |
| Delay list | constructor `@0x26be41c` (`List<Duration>(3)` `[pp+0x9f580]`) | 1 s, 3 s, 5 s (pool durations `[pp+0x1458]`, `[pp+0x13660]`, `[pp+0x13850]`, untagged 1,000,000, 3,000,000 and 5,000,000 us); with one retry only the first delay applies; the wait is `Future.delayed` `@0x476650c` |
| Retried statuses | `Set<int>(18)` `[pp+0x9f588]` copied into a `DefaultRetryEvaluator` `@0x26be490` | the 18 pool values 0x198, 0x1ad, 0x1f4, 0x1f6, 0x1f7, 0x1f8, 0x1b8, 0x1f3, 0x1cc, 0x256, 0x257, 0x208 to 0x20d and 0x20f (untagged, decimal 408, 429, 500, 502, 503, 504, 440, 499, 460, 598, 599, 520 to 525 and 527), the dio_smart_retry default list. Applies to the OTA download only |
| No exponential backoff | same | the delays are a fixed list, not a computed backoff |
| Duplicate-request cancel | see [flows/encrypted_request.md](../flows/encrypted_request.md#timing-delayspolling) | owned by that page |
| SDK path | inside the native SDK | whether the SDK retries is unknown ([../api/encryption.md](../api/encryption.md#known-unknowns)) |

Not found in 3.24.3: any retry loop, backoff or reconnect timer around the HTTP calls of the Dart code, and any app-level rate-limit table. The A17C1 and similar `startIotTimer` loops are re-armed only while the device reports the connected status (P5); they are not backoff.

## A17C1 Solarbank: gates and pre-flight checks

Tag: `asm-traced`. The field names used by the 3.18.0 page (`device_online`, `feeder_power`, `fc_enabled`, `mode_type`, `charge_priority`) are not in the dump, which prints byte offsets only; where a name appears below it is the old page's name for that offset and is not re-verified (BR-5, BR-10).

### isCurDeviceConnected (new read)

`A17C1homeLogic.isCurDeviceConnected` (`charging/ui/page/device/a17c1/a17c1home/a17c1home_logic.dart @0x2634660`) is called 14 times in this file in 3.24.3 (12 in 3.18.0; BR-2 gave "5 call sites", which was a prose count). Structure, in order:

1. A boolean flag of the device holder (offset 419, `@0x2634688`) must be set; if not, the app logs `device变量还未初始化` ("device variable not yet initialized", my translation) `@0x2634698` and returns false.
2. If the flag at offset 0x43 of the device object (`@0x26346b8`) is false, the result is `_getCurrentStatus() == connected` (`@0x26347c8`, compare `@0x26347d4`).
3. If that flag is true and the flag at offset 0x47 (`@0x26346d8`) is false, the result is false (`@0x2634790`).
4. If both are true, the result is the comparison of `getUnifiedMac` of the device with the MAC of the connected BLE device (`@0x2634718`, `@0x2634788`).

The 3.18.0 page said "all 4 conditions must pass" (BR-1). The asm shows an either-or structure; the two flags are not named, so which of them means BLE and which means cloud is not decided here. A caller that is not connected is skipped silently; no error is shown by this function.

### Settings gates (new read)

| gate | site | condition in 3.24.3 |
|---|---|---|
| `isSettingsEnable` | `a17c1/a17c1setting/a17c1setting_logic.dart @0x2756218` | false when the integer field at offset 0xd3 of the device model is non-zero (`cbnz` `@0x2756248`); otherwise the value of the boolean at offset 0x37 (`@0x2756250`). The old page named these `isUpdating` and `isOnline` |
| `canEditEquipmentFeedNetwork` | same file `@0x3d8ff80` | `isSettingsEnable` and the flag at offset 0xdb is false and the flag at 0x43 is true and the flag at 0x53 is false (`@0x3d8ffa4` to `@0x3d8fff0`) |
| `canEditSafetySoC` | same file `@0x3d90e40` | `isSettingsEnable` and the flag at offset 0xdb is false and `isDeviceInStation()` is false (`@0x3d90e64` to `@0x3d90eac`) |

Both editing gates read offset 0xdb of the same object and both require it to be false. The 3.18.0 page named it `grid_connected` and required true for the feed-in gate and false for the SOC gate; that cannot both hold for one field, so the old names are unreliable. What the asm supports: the SOC gate also excludes devices that are part of a station, and the feed-in gate needs the 0x43 flag set and the 0x53 flag clear. OTA blocking is part of `isSettingsEnable` only through the offset 0xd3 value (that it is the OTA flag is the old page's reading).

### setDevicePowerLimit: code paths, guards, offsets

The BLE opcode is the pool list `[0, 0x80]` (`charging/ble/device/A17C1/a17c1_device_controller.dart @0x2277580`, BR-3); TLV tags are on [../mqtt/a17c1.md](../mqtt/a17c1.md). The sender has four code paths depending on which parameters are non-null (the old page's table; the tag lists were wrong, BR-4, see [Corrections](#corrections-to-the-3180-root-page)). Guards in `a17c1home_logic.dart` (`checkDeviceEnableStatus`, power-limit handling):

| guard | 3.24.3 offset | 3.18.0 offset | compare in 3.24.3 | rows |
|---|---|---|---|---|
| device online (old name) | 1255 (`r17` load `@0x33d0f00`) | 1231 | boolean test | BR-5, BR-10 |
| unchanged cached value (old name `feeder_power`) | 675 (`@0x33d0e7c`) | 663 | not re-read | BR-5 |
| capability flag (old name `fc_enabled`) | 663 (`@0x33d1508`) | 651 | not re-read | BR-5 |
| mode flag (old name `mode_type`) | 667 (`@0x33d107c`) | 655 | `cmp w3,#2` `@0x33d1088` on a tagged field = equals 1 | BR-5, BR-6 |
| charge priority after send | n/a | n/a | `cmp w,#4` `@0x33d160c` and `cmp w,#2` `@0x33d1658` on tagged fields = equals 2 and equals 1 | BR-7 |
| priority flags for the schedule gate (`is_charge_priority`, `secondary_charge_priority`, `0x4CF + 0x2CB`) | 719, 723, 663, 1255, 727 | 707, 711, 651, 1231, 715 | `cmp w1,#4` `@0x2625d78` = power-limit enable needs `charge_priority_value` equal to 2 | BR-10, BR-11 |
| `error_code` read after a refresh | 999 (0x3E7), `a17c1home_logic.dart @0x2629bf0` | 987 (0x3DB) | `r17 = 999` | BR-17 |

Offsets are byte offsets (real values, not Smi). Tag: `asm-traced` (offsets and compares at the cited sites); the names are the old page's and are not decoded.

### Schedule (`setTacticsTime`) and backup power

| rule | value | site | rows |
|---|---|---|---|
| maximum schedule slots | 7; the data tags are 29 = 1 mode tag plus 7 slots x 4 values (start, end, power, charging percentage) and the frame ends with a CRC tag, not a timestamp | `a17c1_device_controller.dart setTacticsTime @0x288ac88` (`r2 = 116` before `AllocateArray`: 116 / 2 = 58 array slots = 29 key/value pairs), CRC tag store `@0x288b238` | BR-8, BR-9 |
| mode value of `setBackPower` | 4, hardcoded | `a17c1_device_controller.dart setBackPower @0x281a5bc` (`r1 = 4`, an unboxed argument of `intToList`) | BR-12 |
| schedule UI disabled when both charge-priority flags are set | boolean rule, implemented in `checkDeviceEnableStatus` | `a17c1home_logic.dart @0x2625d78` region (offsets above) | BR-10 |

The tag list of both commands is on [../mqtt/a17c1.md](../mqtt/a17c1.md); the 3.18.0 tag letters were wrong and are not repeated here (BR-9, BR-13).

### Power cutoff, LED, power-limit list

| rule | value | site | rows |
|---|---|---|---|
| defaults of `setSoc` when a parameter is null | 10, 5, 10 (output cutoff, low-power input, input cutoff in the order of the old page; the roles are not decoded) | `a17c1setting_logic.dart @0x3d94f1c`, `@0x3d94f44`, `@0x3d94f6c` (unboxed merge registers, real values) | BR-14 |
| event after the cloud call succeeds | `MessageEvent` with id 2214 and data 1 (not 2) | `a17c1setting_logic.dart @0x3d94ec8` (`stur x`, id unboxed), `@0x3d94ed0` (`stur w`, raw 2 / 2 = 1) | BR-15 |
| LED command | two TLV pairs (4 slots), no precondition on the app side | `a17c1_device_controller.dart setDeviceLightMode @0x3d84ab0` (`r2 = 8`, 8 / 2 = 4 slots), opcode list `@0x3d84b64` | BR-16 |
| attributes fetched by `getPowerLimitList` | 14 (11 in 3.18.0) | `a17c1setting_logic.dart @0x26d2f4c` (`r2 = 28`, 28 / 2) | BR-18 |

The app also calls the cloud (`set_power_cutoff` family) and then sends the same value locally; that sequence is a flow and is owned by [../flows/README.md](../flows/README.md).

### A17C1 error code to message key (new read)

Tag: asm-traced for the code to key map, string-only for the texts (English titles from the pool localization map, `pp.txt` lines 51934 to 51943, 52015, 52209, 57866 and 58967). The message model builds a map literal of 48 pairs (`AllocateArray` `r2 = 192`, 96 slots, `base_service/msg/msg_model.dart @0x2396f5c` to `@0x2397434`); the key of each pair is a Smi stored with `StoreField` (raw value / 2) and the value a `messageA17C1Error<n>` key. The displayed text carries the device error code through its `%s`. This replaces the "twelve rows" of the old BR-26, which could not be compared.

| device error code (decoded Smi) | message key | English title | first pair |
|---|---|---|---|
| 23, 28, 113, 209, 215, 218, 224, 227, 233, 236, 254, 281, 284, 287, 290, 300, 329 | `messageA17C1Error1` | System failure (wait a few minutes, then contact customer service) | `@0x2396f68` |
| 75, 76 | `messageA17C1Error2` | System failure (disconnect PV and the on-grid load, hold the power button) | `@0x2396f90` |
| 91 | `messageA17C1Error3` | Off-grid overload | `@0x2397134` |
| 92 | `messageA17C1Error4` | Grid connection lost | `@0x2397148` |
| 93 to 100 | `messageA17C1Error5` | Power grid exception | `@0x239715c` |
| 14, 15, 16, 17 | `messageA17C1Error6` | PV input overvoltage (module voltage not above 60 V) | `@0x239722c` |
| 25, 26, 126, 132 | `messageA17C1Error7` | Device overheating | `@0x2397370` |
| 32 | `messageA17C1Error8` | Meter abnormality (meter communication lost, self-use mode exited) | `@0x23972bc` |
| 33 | `messageA17C1Error9` | Software version incompatible | `@0x23972e0` |
| 35 | `messageA17C1Error10` | Meter connection error (check the CT position and direction) | `@0x2397304` |
| 40 | `messageA17C1Error11` | Device sleep (some data unavailable until PV charging) | `@0x239734c` |
| 129, 135 | `messageA17C1Error12` | Low device temperature | `@0x2397400` |
| 36 | `messageA17C1Error36` | Smart plug not communicating with the host (unbind and re-add the plug) | `@0x2397328` |
| 212, 222, 223, 230 | `messageA17CXError<code>` | System error (disconnect the PV cable first and wait 5 minutes before the grid cable) | `@0x2397080` |

The keys `messageA17C1Error13` and `messageA17C1Error14` ("System Fault") exist in the pool but are not values of this map. Error 10's "5 minutes" and the CX texts' "5 minutes" are text, not timers (see T11). Fact belongs on [../api/errors.md](../api/errors.md) as a device error list (Task 10).

## A17X8 smart plug

Tag: `asm-traced`.

| rule | value | site | rows |
|---|---|---|---|
| connection check before every command | `_getCurrentStatus()` must equal the connected status; the log line names it `mqtt连接状态` ("MQTT connection status", my translation) and the command log line says `发送蓝牙命令` ("send Bluetooth command"), so the transport of this path is not decided here | `charging/ble/device/A17X8/a17x8_device_controller.dart sendCommandWithParam @0x2418e9c` (status read `@0x2419034`, compare `@0x2419088`, `b.ne` `@0x241908c`) | BR-19 |
| response wait of that path | 5 s, not 30 s; the Smi 30 at `a17x8_device_controller.dart @0x24190c0` is the named argument `functionType` (30 / 2 = 15), not a timeout | same function; wait in `ble_command_controller.dart @0x226fc88` | BR-19, BR-34 |
| maximum number of schedules | default 24 when the server attribute is null (the attribute name `timing_limit` and `getDeviceAttrsInfo` are the old page's and were not re-read) | `charging/ui/page/device/a17x8/a17x8home/a17x8home_logic.dart @0x3463920` (`mov x4,#0x18`, unboxed) | BR-21 |
| weekday tag of the schedule | tag byte 0xA7 (key 334 / 2), added only when the weekday list is not empty (length load `a17x8_device_controller.dart @0x3de1e74`, `cbz` skips the store at `@0x3de1e90`; [flows](../flows/smart_plug_schedule.md#failure-paths)) | `a17x8_device_controller.dart setTimingCmd @0x3de1e8c` | BR-22 |
| countdown cancel | there is no separate cancel opcode: delete sends the same `007e` frame with state 0 ([flows](../flows/smart_plug_countdown_timer.md)) | `a17x8countdown_logic.dart @0x3dcf9c4` | (old page) |
| device error codes shown by the app | a `Map<int, String>` of 5 entries in the pool (`[pp+0x18be0]`): 1 `messageA17X8Error1` (overcurrent fault: load above the socket's rated input current, socket shut off), 2 `messageA17X8Error2` (over-temperature fault), 3 `messageA17X8Error3` (overcurrent and overtemperature fault), 4 a Chinese literal meaning over-temperature warning (not a message key), 22 `messageA17X8Error1`; the old page named only the codes 1 and 2 | `pp.txt` lines 16542 to 16548; texts `pp.txt` lines 52229, 57246, 57247 (string-only) | BR-28 |
| countdown duration | 3 bytes; if the asm reading (one little-endian integer in seconds) holds, the maximum is 16,777,215 s (about 194 days) — upstream reads the same bytes as s:m:h, conflict recorded on [mqtt/README.md](../mqtt/README.md#source-conflicts-two-sided-app-side-re-checked-2026-10); a negative remaining time is clamped to 0 | `setCountdownCmd @0x3dcfbe4` (`intToList3`), clamp `@0x3dcfbfc` to `@0x3dcfc08` (`tbnz x1,#0x3f`) | BR-24, BR-25 |
| switch debounce | the 2 s delayed future of 3.18.0 is gone; 3.24.3 counts pending switch commands (offset 1231) and resets a flag at offset 1211 | `a17x8_anker_device.dart onSwitchCommandSent @0x3073964`; `a17x8home_logic.dart changeSwitch @0x3dd6fdc` | BR-20 (CHANGED-IN-3.24.3) |

The 3.18.0 claim that the schedule enabled flag is inverted was disproved by a device test and is not carried over (BR-23). Timer and schedule are independent pages and commands; the 3.18.0 statement that they can run at the same time was not re-read (see [Known unknowns](#known-unknowns)).

## A5101 HES and station-level limits

### Guard messages per control

Tag: `string-only` (the log literals are at the cited addresses; the conditions that select each log are not decoded). `charging/ui/page/device/a5101/setting/systemPolicy/system_policy_view.dart` logs which check blocked an action, prefixed `SystemPolicyPage========<control>--->`. Meaning (my translation): EMS = `禁用ems策略` "EMS strategy disabled", OFF = `离网状态` "off-grid state", BLE = `蓝牙未连接` "Bluetooth not connected", MAN = `近场手动离网状态` "near-field manual off-grid state".

| control | EMS | OFF | BLE | MAN | first sites |
|---|---|---|---|---|---|
| control `a5101ManualBackupPower` | yes | yes | yes | yes | `@0x3ebbb4c`, `@0x3ebbc4c`, `@0x3ebbc88`, `@0x3ebbd04` (and a second copy from `@0x3ebc888`) |
| control `AutoDisasterPreparednessSupport` | yes | yes | yes | yes | `@0x3ebd0bc`, `@0x3ebd18c`, `@0x3ebd1c8`, `@0x3ebd244` |
| control `gridRecharging` | yes | yes | yes | yes | `@0x3ec0d2c`, `@0x3ec0dfc`, `@0x3ec0e38`, `@0x3ec0eb4` |
| `a5101PeakShaving1`, `a5101PeakShaving2` | no | yes | yes | yes | `@0x3ec0680`, `@0x3ec06bc`, `@0x3ec0738`; `@0x3ebf870`, `@0x3ebf8ac`, `@0x3ebf928` |
| `offGridPowerConsumption`, `SmartShiftMode`, `selfPowered` | yes | yes | yes | no | `@0x3ec4408`, `@0x3ec45d0`, `@0x3ec4618`; `offGridPowerConsumption` also logs two state-of-charge guards, `远场电量小与等于10不允许点击手动离网` (my translation: "far-field charge at or below 10 does not allow tapping manual off-grid") `@0x3ec4510` and the near-field variant `@0x3ec46e8`; `@0x3ec74f8`, `@0x3ec759c`, `@0x3ec75d8`; `@0x3ec9c2c`, `@0x3ec9cd0`, `@0x3ec9d0c` |
| control `billSavingOptimization` | yes | no | no | no | `@0x3ec3ca0` (other logs of this control concern the Nem 3.0 switch) |

The 3.18.0 page said four guard conditions block every setting (BR-39). In 3.24.3 the guards appear per control in the log strings (the per-control reading is inferred from which strings exist, not from decoded conditions); the old rule "all HES settings need EMS enabled, grid connected, BLE connected and not manually off-grid" is therefore too broad. The AI EMS control logs three other reasons (`realOffGrid`, `isDisable`, `has never enableAiEms`, `@0x3eca480`, `@0x3eca4cc`, `@0x3eca500`). A library that sends A5101 settings should still check these conditions, because the server may refuse them; this page does not say what the device or server does without them.

### Battery reserve initial value (new read)

Tag: asm-traced. BR-45's "default 20 %" is not an app default: the page state `SystemPolicyState` creates the reserve value as `IntExtension.obs` of the immediate 0x14 (`system_policy_state.dart @0x3eb087c`), a Smi argument, so 10; the slider shows 100 minus the value (maximum 100, `system_policy_view.dart @0x3eb8cb4`, `d0 = 100.0`) and therefore starts at 90 (derived: 100 minus 10 from the view's `d0 = 100.0`; the inversion in the view was not re-read) until the device state arrives. The old 20 is the raw immediate. This is a placeholder before the first device read, not a device or server default. Trace: [../flows/a5101_battery_reserve.md](../flows/a5101_battery_reserve.md#preconditions).

### Peak shaving maxima and input range

Tag: `asm-traced`. `getPeakShavingMaxPower` (`system_policy_logic.dart`) returns a hardcoded maximum per product number; the caller stores it with a 64-bit `stur x0,[x3,#0xf]`, so the raw value is real. The minimum is 1 (`stur x0,[x3,#7]` `@0x3ebfba8`, `RangeTextInputFormatter`, BR-50).

| product number | maximum (W) | site | rows |
|---|---|---|---|
| A5101 | 60,000 | `getPeakShavingMaxPower @0x3ebfd3c` | BR-40 |
| A5102 | 60,000 | `@0x3ebfd8c` | BR-41 |
| A5103 | 180,000 | `@0x3ebfdb4` (`0x2bf20`) | BR-42 |
| A5341 | 38,400 | `system_policy_logic.dart @0x3ebfd64` (`0x9600`); the same function also bounds `station_peak_shaving_controller.dart _inputPowerChanged @0x361a568` (`cmp x1,x17`, valid range 3000 to 38400) | BR-43 |
| any other | 0 | `system_policy_logic.dart @0x3ebfdc8` (`r0 = 0`) | BR-44 |

The text input rejects values below 1 or above the maximum; the old page's "invalid input reverts silently" was not re-read.

### HES work modes (wire value to enum)

Tag: `asm-traced`. `grid_dispatch_logic.dart` (WorkMode switch `@0x27c7724` to `@0x27c7810`) maps the API value as follows: 0 gives standby, 1 to 8 give working, 255 gives gridOff, anything else gives unKnown (`cmp x2,#0` to `cmp x2,#0xff` on an unboxed integer; `cmp w0,#0x1fe` is the boxed 255). The enum indices (unKnown 0, standby 1, gridOff 2, working 3) are not wire values (BR-46). The old table (0 standBy, 2 gridOff, 6 working) was wrong. Enum owner: [enums.md](enums.md).

### Station power-limit picker (new read)

`StationPowerLimitLogic.showOutputPowerPicker` (`charging/ui/page/device/main/sitation_energy_system/station_home_settings/station_power_limit/station_power_limit_logic.dart @0x4354f94`) fills a picker configuration with unboxed 64-bit stores: 100 (`mov x0,#0x64`, `stur x0,[x3,#0x13]` `@0x43550bc` and `stur x0,[x3,#0x2f]` `@0x43550d0`), a default of 100 when the text field parses to null (`@0x435505c`), and 10 (`mov x1,#0xa`, `stur x1,[x3,#0x23]` `@0x43550cc`). The roles follow from the widget `NewPowerSliderView` (`widget/new_power_slider_view.dart`, store sequence `@0x43550a4` to `@0x43550d0`): the first 100 is the minimum (`field_13`), the last option of the server list is the maximum (`field_1b`), 10 is the step (`field_23`), and the second 100 (`field_2f`) is the minimum label that the widget prints as text (`_interpolateSingle` at `@0x30bd1c8`). The start value (`field_b`, the displayed limit or the default 100) is clamped between 100 (the Smi 200 argument of `clamp`) and the maximum in `initState` (`@0x2c1f3f4`). The field names are not in the dump; the roles come from the uses. The accepted values are validated on the server list in [validation_model.md](validation_model.md#client-side-limits-hardcoded-in-the-app).

## A1790 expansion battery guards

Tag: asm-traced. The two predicates that guard the A1790 home page live on `A1790AnkerDevice` (`charging/ble/device/A1790/a1790_anker_device.dart`); the page logic only forwards to them (`a1790home_logic.dart isSubBatteryEqualing @0x2649780`). There are 12 call sites of `isSubBatteryEqualing` in 3.24.3 (13 in 3.18.0): 3 in `a1790home_logic.dart`, 2 in `a1790home_view.dart`, 2 in `a1790_device_info_widget.dart`, 1 in `a1790_generator_input_wiget.dart` and 4 in `a1782/home/handler/device_home_ui_handler.dart`. The A1782 handler has its own functions of the same names (`isSubBatteryOverError` at asm line 1547 and `isSubBatteryEqualing` at line 1703 of that file); they were not decoded here, so the rules below are the A1790 ones.

| predicate | rule | site |
|---|---|---|
| `isSubBatteryOverError` | false when the sub-battery list (device offset 1199, elements `A1790SubBatteryInfoModel`) is empty; otherwise true when at least one element has the status field at offset 0x3b equal to 4 or 5 (compares `cmp w2, #8` and `cmp w2, #0xa` on the tagged value, so 4 and 5) | `@0x2640d00`, closure `@0x2640da8` |
| `isSubBatteryEqualing` | false when `isSubBatteryOverError` is true; otherwise true when the device field at offset 1227 equals 1 (`cmp w1, #2` tagged); otherwise true when at least one list element has the field at offset 0x3f equal to 1 (`cmp w2, #2` tagged), false for an empty list | `@0x2644d10`, `@0x2644d34`, `@0x2644d5c`, closure `@0x2644e04` |

The names of the model fields at 0x3b and 0x3f and of the device field at 1227 are not in the dump; the predicate names say "over error" and "equalizing" (the app's wording).

## BLE rules

Tag: untagged by design (the BLE/WiFi exclusion is a community finding, not an asm fact; see [ble/protocol.md](../ble/protocol.md#connection-routing-and-the-wifi-exclusion-rule)). BLE is not a live fallback for the cloud: the community finding is that BLE is unavailable while the device is on WiFi; the rule rows below are asm-traced.

| rule | value | site | rows |
|---|---|---|---|
| BLE command status codes of the password lockout | the response codes are 10 (wrong password) and 11 (retry count exceeded); 15 and 16 are enum indices | `BleCmdStatus` map `[pp+0xe480]` (`Map<int, BleCmdStatus>(17)`, untagged keys 0xa and 0xb), enum objects `[pp+0x50be8]`, `[pp+0x50bf8]` | string-only (pool objects, caller not decoded) |  (BR-61) 
| MTU overhead | 10 bytes, then one more byte is subtracted, so the usable size is mtu - 11 | `charging/ble_zx/base/assemble_command_util.dart @0x2272270` (`sub x1,x0,#0xa`, then `sub x2,x1,#1`; unboxed arithmetic) | BR-64 |
| A17C5 PV-limit support gate | `data.length >= 12` and `data[11] == 1` (an equality on one byte, not `>= 2`) | `charging/ble/device/A17C5/a17c5_device_commands.dart @0x4863624` (`cmp x1,#0xc` unboxed length; element index `r16 = 22` tagged = 11; `cmp w0,#2` tagged = 1); debug string `固件是否支持pv设置光伏上限 isSupportPvLimit:` | BR-60 |
| connect timeout, background disconnect | see T2 and T4 | | BR-62, BR-63 |

The lockout needing a power cycle of the device (old page) and the OS limit of concurrent BLE connections are not app facts (BR-65, [Known unknowns](#known-unknowns)).

## Counts, defaults and catalogs

| rule | value | site | tag | rows |
|---|---|---|---|---|
| device categories of the site-creation payload | 10 list names (`solar_list` to `home_backup_system_list`), present in 3.18.0 and 3.24.3 | pool strings | string-only | BR-53 |
| product-number enum size | at least 26 members (highest pool index 25 in 3.24.3; 3.18.0 had 14 pool objects with highest index 17); the member list is owned by [enums.md](enums.md) | `Obj!PN` pool objects | string-only | BR-54 |
| price-provider support by product | `isFlatpeakSupported` and `isTibberSupported`: the same nine products, `A5102`, `A5103`, `A5191`, `A17C5`, `AE100`, `AE103`, `A17E2`, `AE111`, `AE113` (two separate `Set<PN>` constants); `isTouV2Supported`: five products, `A17E1`, `AX170`, `AS510`, `AS520`, `AS521`; `isAIEmsSupported`: two products, `A17C5`, `AE100`; `supportSlitScheduleMode` is Flatpeak or Tibber. The old BR-56 counts (Flatpeak 5, Tibber 5, AI EMS 2) are replaced: 9, 9, 2 and a five-member TOU v2 set | `electricity_price/components/electricity_price_common/electricity_providers_pn_supported.dart` (`isFlatpeakSupported @0x27b9474`, `isTouV2Supported @0x289b998`, `supportSlitScheduleMode @0x28a42e4`, `isTibberSupported @0x28a4334`, `isAIEmsSupported @0x29aa620`; sets `[pp+0x66870]`, `[pp+0x8aa08]`, `[pp+0x66860]`, `[pp+0x67608]`, members decoded from the object dump `objs.txt`) | asm-traced | BR-56 |
| currency decimals | 5 for products A5143 and A1903, 2 for every other product (not by market) | `charging_pn.dart @0x29af0dc` (Smi results untagged by `LoadInt32Instr`, raw 10 and 4) | asm-traced | BR-55 |
| default `mode_type` of a seasonal time-of-use plan | 5 (`EmsModeType.timeOfUse`) | `electricity_price/components/electricity_price_common/view/tou_plan_logic.dart getParamData @0x31b9f74` (`r3 = 10`, boxed value of `[]=`, 10 / 2) | asm-traced | BR-57 |
| single-device max-load options | 350, 600, 800, 1000 W (the multi-device list is not in the asm: the options come from the server attribute `power_limit_option`) | upstream `api/mqttmap.py` `VALUE_OPTIONS` | upstream-confirmed | BR-59 |
| two-state A17C1 error texts with behavior | error 8 text says the meter communication is lost and self-use mode has been exited; error 10 text says the system re-checks every 5 minutes | pool strings `messageA17C1Error8` (`base_service/msg/msg_model.dart @0x23972cc`) and `messageA17C1Error10` | string-only | BR-26 |
| WiFi band note | every bind flow shows the `selectWifi5GTips` string (2.4 GHz only); present in 6 asm files | pool string | string-only | BR-48 |
| freeze and forced-update fields | `freeze_status` and the `force_upgrade` / `is_forced` keys exist in 3.24.3; their effect was not traced | pool strings | string-only | (old page) |

## Corrections to the 3.18.0 root page

Tag: untagged by design (pointers; the current values and their sites are in the section named in the last column, and the old values are history).

| old claim | status in 3.24.3 | where |
|---|---|---|
| "All 4 conditions must pass" in `isCurDeviceConnected`, "5 call sites" (BR-1, BR-2) | wrong structure and count | [isCurDeviceConnected](#iscurdeviceconnected-new-read) |
| four TLV path tag lists a2 to ac, setBackPower tags (BR-4, BR-13) | wrong tag letters | [../mqtt/a17c1.md](../mqtt/a17c1.md) |
| `mode_type == 2`, `charge_priority == 4` and `== 2`, power limit enable on `charge_priority_value == 4` (BR-6, BR-7, BR-11) | all three compares halved | [setDevicePowerLimit](#setdevicepowerlimit-code-paths-guards-offsets) |
| schedule command "30 TLV tags (a2 to bb) plus timestamp" (BR-9) | different tag count, CRC instead of timestamp | [Schedule and backup power](#schedule-settacticstime-and-backup-power) |
| `MessageEvent(id=2214, data=2)`, "22 attributes fetched" (BR-15, BR-18) | data and count halved | [Power cutoff, LED, power-limit list](#power-cutoff-led-power-limit-list) |
| 30 s "command timeout" of the A17X8 path (BR-19, BR-34) | 30 s is the connect timeout | [A17X8](#a17x8-smart-plug), T2, T3 |
| weekday tag `0x14E` (BR-22) | tagged value, real tag byte differs | [A17X8](#a17x8-smart-plug) |
| `5000ms` "API polling interval" (BR-32) | not an API poll | T12 |
| HES work modes 0, 2, 6 (BR-46) | wrong wire values | [HES work modes](#hes-work-modes-wire-value-to-enum) |
| transaction lock default 12 s (BR-52) | halved or 15 s | T7 |
| currency decimals 5 or 4 by market (BR-55) | by product, other values | [Counts](#counts-defaults-and-catalogs) |
| A17C5 PV-limit gate "`>= 2`" (BR-60) | equality on one byte | [BLE rules](#ble-rules) |
| BLE lockout statuses 15 and 16 (BR-61) | enum indices, not response codes | [BLE rules](#ble-rules) |
| "4 universal guard conditions" of A5101 (BR-39) | per-control guards, as far as the log strings show (the conditions behind them were not decoded) | [Guard messages per control](#guard-messages-per-control) |
| HTTP 401 triggers an automatic re-login (new read) | forced logout | [On 461, 463 and 401](#what-the-app-does-on-461-463-and-401) |
| `sendDeviceCommandWithDebounce` wraps all slider sets and sends only the last value (new read) | the function exists once, in `a5101/setting/systemPolicy/system_policy_logic.dart @0x24a1258`; it starts a per-key cancel-and-restart one-shot timer (the map lookup and `cancel` at `@0x24a12d0` to `@0x24a1310`; pool `[pp+0x12208]`, 10 s, `Timer` `@0x24a1344`) and calls `sendDeviceCommand` with the `evcharger_enable` setting (`@0x24a13d0`) on every call; no last-value-only behavior was found | this row |
| `isOtaInProgress()` guards the A1790 and A1782 home pages (new read) | the name is only a string key in `ota_kit/src/services/ota_remote_status_service.dart @0x2ecf95c`; no such guard on those pages was found | this row |

## Changed since 3.18.0

Tag: `asm-traced` (3.24.3 side; the 3.18.0 side is history).

- The polling timers P1 to P6 and P8 have the same values in 3.18.0 (3.18.0 `Timer.periodic` sites `0x1a31808`, `0x1ae28f8`, `0x1a67118`, `0x1b81738`, `0x1d53fb8`, `0x2cf1408`, `0x265d594` in the same functions); only the addresses and pool offsets changed. The `RetryInterceptor` with the same constant retry count is in 3.18.0 at `0x1e722f8`.
- Guard offsets, error-code offset, relay-flag handling and the PN enum size changed as listed in the A17C1, A17X8 and counts sections.
- New in 3.24.3: the 461 branch of the status handler (see [../api/encryption.md](../api/encryption.md#changed-since-3180)).

## Known unknowns

Tag: untagged by design (no API fact). Rules that the 3.18.0 page stated and that this page does not carry as facts, with the reason.

- **A5190 fault table** (BR-27, 23 codes with "stops charging" column) and the 6 A fallback, five scenarios and 80 % main-breaker rules (BR-38): the pool key family `evChargeErrorCode0x..` has 12 keys, 0x21 to 0x28 and 0x30 to 0x33, and they are the toast texts for failed charger commands, selected by `parseControllerCommandResult` (`ev_charge_command_error_code_parser.dart @0x3944478`; mapping and English texts in [../flows/ev_charger_start_charging.md](../flows/ev_charger_start_charging.md#failure-paths)); 0x21 is "EV charger is preparing to charge.", not "internal fault". The old table's codes 0x01 to 0x1D are not under it and no such key exists (grep of the prefixes `evChargeErrorCode0x0` and `evChargeErrorCode0x1` in `pp.txt`: 0 hits), and the charger rules (6 A fallback, scenarios, 80 %) are help-text content, not code. Not carried over; owner pages would be the future `devices/a5190.md` and `api/errors.md`.
- **Temperature protection zones** (BR-49) and **chart periods** (BR-58): string-derived prose counts, not re-read — traced 2026-10-20: the pool has the four zone strings `outHightTemperatureProtection`, `outLowTemperatureProtection`, `inHightTemperatureProtection`, `inLowTemperatureProtection` (`[pp+0xd060]` to `[pp+0xd078]`), but no zone boundary values were bound to them; the chart periods were not looked at. The A17X8 error codes of BR-28 are in the A17X8 table above.
- **HES state machine values 0 to 9 and 20** (BR-51): no integer-to-enum switch with value 20 in `mode_state_definition.dart` or `device_mode_tips_logic.dart`; the 11-member enum has `forcedRecharge` at index 10 and different names for indices 4, 6 and 8 (`automaticBackupState`, `manualGridOutage`, `physicalOffGrid`). The "hardware override, read-only" claim is therefore unverified.
- **Multi-device parallel option list** `1200, 2400, 3600, 4800 W` (BR-59): not in the asm; the server attribute `power_limit_option` supplies options.
- **Slider debounce and OTA blocking**: see the corrections table. The guard behaviour of `isSubBatteryEqualing` and `isSubBatteryOverError` is in the A1790 expansion battery guards section.
- **`isEffective` inversion** (BR-23): disproved by a device test and by the audit; nothing to carry.
- **Library facts** (BR-65 OS-limited concurrent BLE connections, BR-66 server-side ban rule): not app facts. The ban rule is described in the upstream project; no upstream file was checked for this page, so no `upstream-confirmed` tag is claimed.
- **Server-side rate limits** and whether the server accepts the polling spacing of the app: unknown; no device or server test is recorded.
- **Heartbeat details**: the topic the heartbeat is published on, the `debounceMs` value and the source of `client_id` in the head — traced 2026-10-20: the message content is in the Heartbeat message content section; `MqttServe.siteSendMsg` was not found as a function in the dump (grep `_ siteSendMsg`: 0 hits), so the topic and debounce stay open.
- **Bodies of the functions the P7, P9, P10, P12, P13 and P15 closures call** (`_sendDCPortHeartSchedule`, `onTestConnecting`, `getDeviceSoc`, the A1340 chart clock, `refreshChart`, `_collectPhoneTemperature`) and the `startCountDown` bodies were not read — traced 2026-10-20: the closures themselves are read and named in the Timer inventory table; P11 and P14 are resolved there.
- **Mixin-deduplicated code**: functions inside `_MixinApplication...` classes (for example the MQTT message listener closure at `[pp+0x18ac8]`) have no asm file in the dump; their timing cannot be read. — traced 2026-10-20: grep of the asm root for `addr: 0x2431914` and `addr: 0x24317c0` (the closure and its function): 0 hits, and no `dart:mixin_deduplication` directory exists.
- **Names of the gate fields** (offsets 0x37, 0x43, 0x47, 0x53, 0xd3, 0xdb, 419 and the charge-priority fields): not in the dump; the old names are unverified.
- **Timer and schedule coexistence** of the plug is device behaviour — reclassified: device, [device test row 129](../docs/DEVICE_TEST_BACKLOG.md#added-2026-10-20-depth-pass); the **debounce of the relay switch beyond the pending-count mechanism** is on [../flows/smart_plug_relay_toggle.md](../flows/smart_plug_relay_toggle.md#failure-paths); countdown cancel and the weekday tag are in the A17X8 table.
- **Weather and agent timers** (600 s, 300 s) are not part of device control.

## Related pages

- [validation_model.md](validation_model.md): what is validated before a value is sent.
- [../api/encryption.md](../api/encryption.md), [../api/auth.md](../api/auth.md): 461, 463, 401.
- [../api/param_types.md](../api/param_types.md): `param_type` and `cmd`.
- [../mqtt/envelope.md](../mqtt/envelope.md), [../mqtt/a17c1.md](../mqtt/a17c1.md), [../mqtt/a17x8.md](../mqtt/a17x8.md), [../mqtt/a5101.md](../mqtt/a5101.md): payloads and tags.
- [../flows/encrypted_request.md](../flows/encrypted_request.md): timeouts of the plain path.
- [../METHODOLOGY.md](../METHODOLOGY.md): Smi rule and tags.
