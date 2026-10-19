> Verified against: App 3.24.3 · Date: 2026-10-19 · Confidence: string-only · Owner page: this page

# App architecture

This page describes how App 3.24.3 is put together as a program, so that a reader of the endpoint, MQTT and BLE pages knows what runs where: the Flutter/Dart layer that the rest of this repository documents, the native libraries around it (compared with 3.18.0), the SDKs that disappeared, the hosts that appear as literals, and which of the three communication channels carries what. It owns only the facts of that overview. Every protocol fact stays on its owner page and is linked, never repeated. Tags and the Smi rule are defined in [../METHODOLOGY.md](../METHODOLOGY.md). The app facts block (version code, package hash, Dart SDK, snapshot id) is in [../README.md](../README.md) and is not repeated here.

Closest template: [templates/model.md](templates/model.md) (Purpose, a fact table per topic, Changed since 3.18.0, Known unknowns). The Fields, Produced and Consumed sections are replaced by the topic sections below, because there is no JSON model. Page type: reference. The status header carries the lowest tag on the page (`string-only`); stronger rows carry their own tag.

Method and scope: the library and manifest lists come from `ls`, `stat`, `file`, `strings` and a byte-level string extraction over the extracted APK directories; the host lists come from the object pool (`pp.txt`) and the asm of the Blutter output. Nothing from those directories was executed. File sizes are plain byte counts from `stat`, not asm immediates, so the Smi rule does not apply to them. Pool offsets (`pp+0x...`) differ between the two versions and are always given for the version named in the row. A row that names `3.18.0` is history, not a current fact.

## Contents

1. [Process and layer layout](#process-and-layer-layout)
2. [Native libraries: 3.24.3 against 3.18.0](#native-libraries-3243-against-3180)
3. [What each new library is for](#what-each-new-library-is-for)
4. [Removed SDKs](#removed-sdks)
5. [Hosts](#hosts)
6. [The three communication channels](#the-three-communication-channels)
7. [Changed since 3.18.0](#changed-since-3180)
8. [Known unknowns](#known-unknowns)

## Process and layer layout

Tag: `string-only` unless a row cites an asm address.

The app is one Flutter application. Its Dart code is the AOT snapshot in `libapp.so`; around it the package carries a Unity player for the 3D station view, a React Native runtime (Hermes), a native IoT-Kit SDK that Dart reaches over platform channels, and a code-protection layer that hides the Java code. No asm shows how these are started; the table is what the files and strings show.

| layer | what is there | evidence |
|---|---|---|
| Flutter engine and Dart snapshot | `libflutter.so` (11316480 bytes in 3.24.3, 10602168 in 3.18.0) and `libapp.so` (77923248 bytes in 3.24.3, 58590128 in 3.18.0: 19333120 bytes or 33 percent larger). Dart SDK and snapshot id: [../README.md](../README.md) | `stat` on `v3.24.3/arm64/lib/arm64-v8a` and `arm64/lib/arm64-v8a`; string-only |
| Launcher activity | `com.anker.charging.MainActivity`; the manifest also lists the `com.anker.akiotkit...AKBackgroundTaskService$AKIoTForegroundService` and `com.example.anka_agent.service.AnkaReplyForegroundService` foreground services, both new in 3.24.3 | string extraction of `AndroidManifest.xml`; string-only (class names only, no call site) |
| Java layer | hidden: `classes.dex` is a stub (13892 bytes in 3.24.3, 13612 in 3.18.0) next to the protection libraries `libijm-emulator.so`, `libijmdetect-drisk.so` and `assets/ijm_lib/arm64-v8a/libexec.so` and `libexecmain.so`; the manifest names `com.ijm.detect.drisk.IsolatedService` and `IjiamiActivityOfflineAttack`. The real Java classes are not in the extracted files | `stat`; manifest strings; string-only |
| Unity player | `libunity.so`, `libil2cpp.so` (the Unity IL2CPP game code), `libmain.so` (names `libunity.so` and `com/unity3d/player/NativeLoader` in its strings); manifest meta-data keys `unity.*` | `strings`; string-only |
| Dart to Unity bridge | Dart package `unity` (absent from the 3.18.0 asm tree): a `MethodChannel` named `anker_flutter_channel` (pool object `pp+0x1b980`) with `invokeMethod` calls in `unity/src/main/channel/unity_channel_helper.dart @0x22c9a44` and `@0x2bae264`; the helper dispatches Unity events by name (`onReady`, `onClickDevice`, `chargingMapLoaded`, `onHouseLoaded`, `consoleLog`) under the module name `U3DModule` | asm-traced for the channel and the call sites; the event names are pool strings read at `unity_channel_helper.dart @0x34bd8fc` onward |
| React Native | `libreactnative.so`, `libhermes.so`, `libjsi.so`, present in both versions; Dart package `ak_flutter_rn_extension` with the channels `com.anker.charging/flutter_rn_method` and `com.anker.charging/flutter_rn_event` (pool `pp+0x36888`, `pp+0x36890`) and `com.charging.ak_flutter_rn_bridge/method_channel` (`pp+0x75d58`) | string-only; what runs in the RN part is not documented in this repository |
| IoT-Kit SDK | one method channel `ak_iot_kit_flutter` plus three event channels; the Dart side only passes identifiers and maps | [../reference/iot_kit_channels.md](../reference/iot_kit_channels.md#transport-one-method-channel-three-event-channels) owns the transport and the `akiot.*` list |
| Log layer | `libak_logan.so` driven from Dart through `dart:ffi` (see [below](#what-each-new-library-is-for)) | asm-traced |

The manifest strings of 3.24.3 contain no process-name string (a name starting with `:` or a `process=` value), so the app is most likely a single process plus the isolated protection service. The manifest attribute values themselves were not decoded, so this stays an inference, not a trace.

## Native libraries: 3.24.3 against 3.18.0

Tag: `string-only` (a directory listing is a fact about the package, but no call site is traced for most rows).

The listing covers `lib/arm64-v8a` of both packages (the extracted directories `arm64/lib/arm64-v8a` for 3.18.0 and `v3.24.3/arm64/lib/arm64-v8a` for 3.24.3), 34 and 41 files. 31 names are in both, 3 only in 3.18.0 (removed), 10 only in 3.24.3 (added). Of the 31 common files 4 differ in size: `libapp.so`, `libflutter.so`, `libc++_shared.so` (1292904 to 1253544 bytes) and `libijmdetect-drisk.so` (680496 to 680592 bytes); the other 27 have identical sizes. The two protection helper libraries in `assets/ijm_lib/arm64-v8a` (`libexec.so` 778k to 792k, `libexecmain.so` 36k in both, `ls` rounded) are in both packages.

| change | library | size in 3.24.3 (bytes) | note |
|---|---|---|---|
| added | `libunity.so` | 23694336 | Unity player, see [below](#what-each-new-library-is-for); string-only |
| added | `libil2cpp.so` | 43043600 | Unity IL2CPP game code; string-only |
| added | `libmain.so` | 6.7k (`ls`) | Unity loader stub |
| added | `libdraco_unity.so` | 2.1M (`ls`) | Draco mesh decoder for Unity |
| added | `libAVProMovieCaptureNative.so` | 957k (`ls`) | Unity plugin (AVPro Movie Capture) |
| added | `libUbdt.so` | 13k (`ls`) | JNI names `com.jni.Ubdt`, origin not identified |
| added | `libdartjni.so` | 131432 | Dart/Java bridge of the `jni` Dart package; string-only here, the load site is asm-traced below |
| added | `libak_logan.so` | 623872 | the app's Logan log writer, loaded by Dart; string-only here, the load site is asm-traced below |
| added | `libpdfium.cr.so`, `libpdfiumandroid.so` | 4.7M and 369k (`ls`) | PDF rendering; Dart package `flutter_pdfview` is also new |
| removed | `libalicomphonenumberauthsdk_core.so` | (3.18.0: 5.8k, `ls`) | Alibaba phone-number authentication, see [Removed SDKs](#removed-sdks) |
| removed | `libbdpush_V3_5.so` | (3.18.0: 66k, `ls`) | Baidu push |
| removed | `libpns-2.14.12-LogOnlineStandardCuumRelease_alijtca_plus.so` | (3.18.0: 474k, `ls`) | Alibaba PNS (phone-number service) core |

The task brief for this page listed `libquickjs` and `libsqlcipher` among the new libraries. They are not new: `libquickjs.so` (1030104 bytes), `libquickjs-android.so` and `libsqlcipher.so` (5797528 bytes) are in both packages with identical sizes. They are listed in [What each new library is for](#what-each-new-library-is-for) only to say what is known about them.

## What each new library is for

Tag per row. "Loaded by" means a Dart call site that opens the library by name; only two libraries have one.

| library | purpose | loaded by | tag |
|---|---|---|---|
| `libak_logan.so` | Logan-style log writer. Exported symbols (`strings`) include `clogan_*` and `aes_encrypt_clogan`, i.e. the log is encrypted natively. The Dart package `ak_logan` (new in 3.24.3) wraps it | `LoganBindings._workerEntry`, `ak_logan/src/logan_bindings.dart @0x49d3afc`: the pool string `libak_logan.so` (`pp+0x362d0`) goes to `dart:ffi ::_open` at `@0x49d3b24`; symbols `clogan_init_bridge` (`pp+0x362e0`) and the other `clogan_*_bridge` names are then looked up with `DynamicLibrary::lookup` (first at `@0x49d3b48`) | asm-traced |
| `libdartjni.so` | native half of the Dart `jni` package (JNI environment access; exports `GetJniEnv`, `GetJniContextPtr`, `Java_com_github_dart_1lang_jni_JniPlugin_setClassLoader`). Its Dart consumers include `path_provider_android` (calls `JObject`/`JString` helpers) | `Jni._loadDartJniLibrary`, `jni/src/jni.dart @0x2a6e0ec`: the pool string `libdartjni.so` (`pp+0x59c58`) goes to `::_open` at `@0x2a6e140` | asm-traced |
| `libunity.so`, `libil2cpp.so`, `libmain.so` | the Unity 3D viewer of the station page (Dart package `unity`, new). `libmain.so` names `libunity.so`; `libil2cpp.so` exports `UnityAdsEngine*` symbols as part of the engine | no `DynamicLibrary` call in Dart; the Java loader `com/unity3d/player/NativeLoader` (a string in `libmain.so`) loads them, and Dart talks to Unity over the method channel `anker_flutter_channel` (see [layout](#process-and-layer-layout)) | string-only for the libraries; asm-traced for the channel |
| `libdraco_unity.so` | Draco mesh decoding for Unity (exports `DecodeMeshForUnity`, `ReleaseUnityMesh`) | not found in Dart | string-only |
| `libAVProMovieCaptureNative.so` | Unity plugin (exports `UnityPluginLoad`, `AVPMC_*`) | not found in Dart | string-only |
| `libpdfium.cr.so`, `libpdfiumandroid.so` | PDF engine for the Android PDF view; Dart package `flutter_pdfview` is new in 3.24.3 | not found in Dart | string-only; the link to `flutter_pdfview` is an inference from the package list |
| `libUbdt.so` | JNI entry points `Java_com_jni_Ubdt_init`, `Java_com_jni_Ubdt_openLog`, `Java_com_jni_Ubdt_sendobj` | not found in Dart | string-only; purpose not identified |
| `libquickjs.so` (both versions) | QuickJS engine with the Java binding `com.quickjs.QuickJSNativeImpl` (strings of `libquickjs.so` and `libquickjs-android.so`) | no reference in the pool or asm of either version | string-only; purpose not identified |
| `libsqlcipher.so` (both versions) | SQLCipher; the Dart package `sqflite_sqlcipher` (pool string `sqflite_sqlcipher`, channel `com.davidmartos96.sqflite_sqlcipher`) is in both asm trees | loaded on the Java side by the plugin, not by Dart | string-only; the link between plugin and library is an inference |

One library that is not new but matters for the protocol pages: `libecc-encryption.so` (307k, both versions) exports `Java_com_anker_esiotkit_support_crypto_EccEncryption_generateEccKey`, `..._eccEncrypt` and `..._eccDecrypt` (strings). It is the likely native home of the ECDH primitives that [../api/encryption.md](../api/encryption.md) says Dart never executes itself; that mapping is not traced.

## Removed SDKs

Tag: `string-only`. The honest result of the pool-string check differs between the two SDKs.

| SDK | what disappeared | what stayed |
|---|---|---|
| Alibaba phone-number authentication | the libraries `libalicomphonenumberauthsdk_core.so` and `libpns-2.14.12-...alijtca_plus.so` (see the table above) | nothing to show by absence in Dart: a `grep -i` for `alicom`, `PhoneNumberAuth`, `phone_number_auth`, `AliAuth` over `pp.txt` and over the asm tree gives 0 hits in both 3.18.0 and 3.24.3. The Dart code never referenced it, so the removal is visible only in the native libraries (the manifests of both versions carry no `alicom` or `mobile.auth` component string either) |
| Baidu push | the library `libbdpush_V3_5.so`; 31 extracted manifest strings containing `baidu` or `bdpush` in 3.18.0 (services, receivers, provider, the `:bdservice_v1` process name, the `baidu.push.permission.WRITE_PUSHINFOPROVIDER...` permission) against 0 in 3.24.3. The vendor push entries of the same family (Xiaomi, Vivo, Meizu, Huawei, Honor, Heytap) and the `BOOT_COMPLETED` receiver permission also left the manifest | Dart residue: `HttpBusinessImpl.clearBaiDuPushBadge` (`charging/http/http_business_impl.dart @0x296d444`) is still in the pool (2 closures, `pp+0x58b68` and `pp+0x58b70`) and is still called from `third_party_service.dart @0x296d410` and `app_life_cycle_delegate.dart @0x3714bdc`; it posts to `/app/push/clear_count` when the user is logged in and `isChinaRegion` is true (`@0x296d47c`, `@0x296d484`, URL literal `pp+0x58b78`). Endpoint page: [../api/app/push/clear_count.md](../api/app/push/clear_count.md). The Dart push stack that remains is Firebase Messaging (package `firebase_messaging`, in both versions) |

So "Baidu push removed" holds for the native SDK and the manifest, not for the Dart code; the app still sends the badge-clear request for China-region accounts. The counts of manifest strings are counts of extracted strings (length-prefix noise stripped), not of manifest elements.

## Hosts

Tag: `string-only` for the pool lists; asm-traced where a site is cited.

The host inventory is every distinct `https://` or `http://` host prefix in `pp.txt` of each version (grep, then unique). 3.24.3 has 53 and 3.18.0 has 51 distinct prefixes including the bare schemes `http://` and `https://` and the partial `https://anker-webview-` (built by string concatenation); the common core is 46 prefixes. Hosts that appear only inside code strings (for example the MQTT broker) are not enumerated here; see [Known unknowns](#known-unknowns).

Core hosts, present in both versions:

| group | hosts (pool strings) | note |
|---|---|---|
| Anker Power API, per region and stage | `https://ankerpower-api.anker.com`, `https://ankerpower-api-eu.anker.com` (stored by `charging/util/save/sp_util_impl.dart @0x226580c` and `@0x2265800`), `https://aiot-api-cn.anker.com.cn` (`sp_util_impl.dart @0x22655b8`), plus the beta, qa and qa2 variants `ankerpower-api-beta`, `-eu-beta`, `-eu-qa`, `-eu-qa2`, `-qa`, `-qa2` and the China beta `charging-api-cn-beta.anker.com.cn` | which host a call goes to is decided by the base-URL selection in the app; the auth and header side is [../api/auth.md](../api/auth.md) |
| Passport, web and tutorial pages | `https://passport.anker.com`, `https://www.anker.com`, `https://www.ankersolix.com`, `https://charging-tutorial.anker.com`, `https://tutorial.anker.com.cn`, `https://tutorial-qa.anker.com.cn`, `https://security-tutorial-qa.eufylife.com` | in-app web views and links |
| Logging | `https://charging-log.eufylife.com`, `https://eufy-log.anker-in.com`, `https://eufy-log-ci.anker-in.com`, `https://log-ci.eufylife.com` | log upload targets; purpose by name only |
| Object storage and CDN | `https://d2htfo7ft368vg.cloudfront.net`, `https://d7p3a6aivdrwg.cloudfront.net`, `https://public-aiot-ore-ci.s3.dualstack.us-west-2.amazonaws.com`, `https://public-aiot-ore-qa...`, `https://test-jpfile1.oss-cn-shenzhen.aliyuncs.com` | the Aliyun OSS entry is a test PDF path; it is a data URL, not an SDK |
| Third party | `https://maps.googleapis.com`, `https://places.googleapis.com`, `https://bing.com`, `https://github.com`, `https://play.google.com`, `https://docs.google.com`, `https://firebase.google.com`, `https://view.officeapps.live.com` and framework documentation links | Google Maps and place APIs belong to the map widgets, the rest are links or library messages |
| Local device | `http://10.10.100.254` | a private-network address literal; its use was not traced |

Hosts only in 3.24.3 (added):

| host | where it is used | note |
|---|---|---|
| `https://openweathermap.org/` | `ak_soft_ems/ems_list/disaster_description_page.dart @0x42000e8` (pool `pp+0x99a50`): the page opens it with `GetNavigation.toNamed` on the route `/commonWebView` (`@0x42000fc`) | an attribution link opened in the in-app web view; no API call to this host was found |
| `https://openai.com/policies/api-data-usage-policies/` | `anka_agent/pages/home/widgets/memory_privacy_sheet.dart @0x2c01254` (pool `pp+0x11a838`): opened on the route `/commonWebViewPlus` with a `WebViewModel` | a privacy link shown with the Anka assistant (the localization keys `ankaAgentBillAnalysisFunctionFaqOpenAILink` name it as OpenAI's API data usage policy). It is a page the user opens; the app does not call an OpenAI host. The Anka endpoints are on [../api/app/ai/anka.md](../api/app/ai/anka.md) and the models on [../models/anka_agent_models.md](../models/anka_agent_models.md) |
| `https://anker-webview-us-qa.anker.com/over-power.html?country=` | `charging/ui/page/device/main/sitation_energy_system/station_home_settings/station_power_limit/widget/diy_legal_power_limit_sheet.dart @0x43583b0` (pool `pp+0x163a40`) | a QA web-view host in a release build; same page name as the 3.18.0 CloudFront `h5-over-power.html` URL below |
| `https://support.ankersolix.com/s/articlemanual?pn=` | `micro_hes/src/a17e2/station/system_flow/system_a17e2_flow_chart_logic.dart @0x3298e48` and `charging/ui/page/device/main/sitation_energy_system/station_energy_system_logic.dart @0x308cb90` (pool `pp+0xf9078`) | a manual link built from the product number |
| `https://maps.google.com` | pool `pp+0x15b998` | no direct asm reference found |
| `https://pub.dev`, `https://docs.flutter.dev` | inside Flutter framework error messages | no app use |

Hosts only in 3.18.0 (removed, history): `https://beta.ankersolix.com` (`?appName=anker_power`, per-country variants), `https://d38dd6169df8my.cloudfront.net/overall/h5-over-power.html?country=`, `https://public-aiot-ohi-prod.s3.dualstack.us-east-2.amazonaws.com/.../privacy_notice_en.html`, `https://www.weather.gov/`, `https://flutter.dev` (framework messages). The 3.18.0 call sites of the first four were not traced. The 3.24.3 manifest also holds the string `charging-api-cn.anker.com.cn` (a China API host, not in the 3.24.3 pool as an `https://` string); its role in the manifest was not decoded.

## The three communication channels

Tag: `asm-traced` for the cited routing facts; the facts themselves live on the owner pages named in each row.

The Dart layer talks to the cloud and to the devices over three channels. This section says what each is and where it is documented; it adds no protocol detail.

| channel | what it carries | who performs it | owner pages |
|---|---|---|---|
| Cloud HTTP | account, site and device REST calls. Three call paths: a decorator that hands the call to the native SDK (`akiot.cloud_api`) or sends it as a plain Dio request, and direct SDK senders that bypass the decorator. Encrypted calls are signed and encrypted natively; Dart only passes the request and the primitives' inputs | Dart (Dio, plain path) or the native IoT-Kit SDK (SDK path) | [../api/README.md](../api/README.md) (endpoints), [../api/auth.md](../api/auth.md) (login, headers), [../api/encryption.md](../api/encryption.md#which-calls-are-encrypted) (the three paths and the encrypted-body rule), [../api/sdk_senders.md](../api/sdk_senders.md#path-c-sender-list) (direct senders) |
| MQTT | device telemetry and commands through the cloud broker: the `head` and `payload` envelope, command types, topics, the binary frame and TLV | Dart (`mqtt_client`, `charging/mqtt/...`) | [../mqtt/envelope.md](../mqtt/envelope.md) (envelope, topics, connection), [../mqtt/README.md](../mqtt/README.md) (per-product maps) |
| BLE | direct Bluetooth LE access to a nearby device with the same binary frame as MQTT plus flag bits, fragmentation and a session key from a handshake | Dart controllers and the IoT-Kit SDK (`akiot.ble.*` identifiers) | [../ble/protocol.md](../ble/protocol.md), [../ble/handshake.md](../ble/handshake.md), [../ble/README.md](../ble/README.md) |

The identifiers the Dart side hands to the native SDK (cloud calls, BLE, OTA and more) are inventoried on [../reference/iot_kit_channels.md](../reference/iot_kit_channels.md). The SDK itself is native and is a known unknown below.

A device is either in a WiFi state or in a BLE state in the app's routing; BLE is not a fallback when the cloud or WiFi path is down. The rule, its asm evidence and the community statement are on [../ble/protocol.md](../ble/protocol.md#connection-routing-and-the-wifi-exclusion-rule); this page does not restate them.

## Changed since 3.18.0

Tag: `string-only` for lists, asm-traced where an address is given.

- Native libraries: 3 removed, 10 added, 31 common (4 resized); details and sizes in [the library table](#native-libraries-3243-against-3180).
- `libapp.so` grew from 58590128 to 77923248 bytes (`stat`); the new Dart packages in the asm tree account for part of it. The asm tree has 216 top-level Dart package directories in 3.24.3 against 195 in 3.18.0 (16 only in 3.18.0, 37 only in 3.24.3; for example `unity`, `ak_logan`, `jni`, `jni_flutter`, `station_home`, `settings`, `ota_kit`, `flutter_pdfview` are new, `flutter_reactive_ble`, `reactive_ble_mobile`, `location`, `protobuf` are gone). The BLE side of that change, `ReactiveBleManager` delegating to the IoT kit, is in [../ble/protocol.md](../ble/protocol.md#stacks-and-send-routing).
- Manifest: the Baidu and vendor push entries left; foreground services `AKIoTForegroundService` and `AnkaReplyForegroundService` and the `unity.*` and `EnableImpeller` meta-data entries arrived; the in-app browser classes moved from `flutter_inappwebview` to `flutter_inappwebview_android`.
- Hosts: 5 removed, 7 added (of which 3 are framework or generic links: `pub.dev`, `docs.flutter.dev`, `maps.google.com`), see [Hosts](#hosts).
- Removed SDKs: Alibaba phone-number authentication and Baidu push at the native level, see [Removed SDKs](#removed-sdks).

## Known unknowns

Tag: untagged by design (no API fact).

- The Java layer is hidden behind the protection stub, so which Java class loads `libquickjs.so`, `libsqlcipher.so`, `libecc-encryption.so`, `libUbdt.so` and the Unity libraries is not known; the attributions above rest on library symbol names only.
- What the native IoT-Kit SDK does with `akiot.*` identifiers (signing, ECDH, request sending, BLE I/O) is not in the Dart dump; see [../reference/iot_kit_channels.md](../reference/iot_kit_channels.md#known-unknowns).
- Whether the app runs in a single OS process (the manifest attribute values were not decoded) and how the Unity player and the React Native runtime are hosted next to the Flutter engine.
- The purpose of `libquickjs.so` and `libUbdt.so`, and what the React Native part of the app shows.
- The MQTT broker host and the cloud host selection logic are not enumerated here (the broker is not an `https://` literal); see [../mqtt/envelope.md](../mqtt/envelope.md#connection-details).
- Whether the 3.18.0 hosts that left the pool are served by other URLs built at run time.
