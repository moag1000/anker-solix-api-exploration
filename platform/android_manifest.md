> Verified against: App 3.24.3 · Date: 2026-10-21 · Confidence: asm-traced · Owner page: this page

# Android manifest

This page owns the facts read from the app's `AndroidManifest.xml`. The manifest in the shipped APK is binary; the values below are from the jadx-decoded copy (`jadx -s` on the base APK). Cited as `AndroidManifest.xml`. Tag: asm-traced — every value here is a literal attribute in that file, not an inference. What a component *does* at runtime is a separate question and is only answered here where the Dart snapshot or another page already settles it.

## Contents

1. [Identity and SDK](#identity-and-sdk)
1. [Application flags](#application-flags)
1. [Permissions by capability](#permissions-by-capability)
1. [Exported components](#exported-components)
1. [Deep links, NFC and OAuth](#deep-links-nfc-and-oauth)
1. [Embedded third-party SDK keys](#embedded-third-party-sdk-keys)
1. [Packer markers](#packer-markers)

## Identity and SDK

Tag: untagged by design — these are verbatim manifest attribute values, not decoded immediates, so the Smi rule and `@0x` citations do not apply.

| Attribute | Value |
|---|---|
| `package` | `com.anker.charging` |
| `versionName` | `3.24.3` |
| `versionCode` | `237` |
| `minSdkVersion` | `26` (Android 8.0) |
| `targetSdkVersion` | `35` (Android 15) |
| `compileSdkVersion` | `36` |

## Application flags

From the `<application>` element (`AndroidManifest.xml`):

| Flag | Value | Note |
|---|---|---|
| `android:name` | `s.h.e.l.l.S` | Not an app class — the Ijiami packer's `Application` shell (see [Packer markers](#packer-markers)) |
| `android:appComponentFactory` | `s.h.e.l.l.A` | Ijiami component factory; intercepts class instantiation |
| `android:allowBackup` | `false` | No `adb backup` of app data |
| `android:usesCleartextTraffic` | `true` | Cleartext HTTP is permitted by the platform; the app still uses HTTPS for the cloud (see [../api/auth.md](../api/auth.md)) |
| `android:extractNativeLibs` | `false` | `.so` files are loaded straight from the APK, not unpacked to disk |
| `firebase_crashlytics_collection_enabled` | `false` | Crashlytics auto-collection off |
| `firebase_messaging_auto_init_enabled` | `false` | FCM auto-init off (initialised in code instead) |
| `io.flutter.embedding.android.EnableImpeller` | `false` | Flutter renders with Skia, not Impeller |

## Permissions by capability

Tag: untagged by design — the `maxSdkVersion` numbers are verbatim manifest attributes.

| Capability | Permissions |
|---|---|
| Network | `INTERNET`, `ACCESS_NETWORK_STATE`, `ACCESS_WIFI_STATE`, `CHANGE_WIFI_STATE` |
| Bluetooth | `BLUETOOTH` / `BLUETOOTH_ADMIN` (`maxSdkVersion=30`), `BLUETOOTH_SCAN` (`neverForLocation`), `BLUETOOTH_CONNECT` |
| Wi-Fi provisioning | `NEARBY_WIFI_DEVICES` (`neverForLocation`) |
| Location | `ACCESS_COARSE_LOCATION`, `ACCESS_FINE_LOCATION`, `ACCESS_BACKGROUND_LOCATION`, `FOREGROUND_SERVICE_LOCATION` |
| Foreground services | `FOREGROUND_SERVICE`, `FOREGROUND_SERVICE_DATA_SYNC` |
| Camera / audio | `CAMERA`, `RECORD_AUDIO` |
| NFC | `NFC` (+ `uses-feature android.hardware.nfc required=false`) |
| Biometric | `USE_BIOMETRIC`, `USE_FINGERPRINT` |
| Notifications / push | `POST_NOTIFICATIONS`, `com.google.android.c2dm.permission.RECEIVE` (FCM) |
| Device / ads | `READ_PHONE_STATE`, `com.google.android.gms.permission.AD_ID`, `ACCESS_ADSERVICES_AD_ID`, `ACCESS_ADSERVICES_ATTRIBUTION`, install-referrer |
| Misc | `WAKE_LOCK`, `VIBRATE`, `REORDER_TASKS`, legacy storage (`WRITE_EXTERNAL_STORAGE`, `READ_EXTERNAL_STORAGE` `maxSdkVersion=32`) |

Both `BLUETOOTH_SCAN` and `NEARBY_WIFI_DEVICES` carry `neverForLocation`, so neither is used to derive location. The location permissions exist because Wi-Fi provisioning of a new device needs them on Android, and `ACCESS_BACKGROUND_LOCATION` backs the geolocator plugin.

## Exported components

Seven components carry `android:exported="true"`. Only two are Anker's own; the rest are framework boilerplate that is exported by the library that ships them.

| Component | Owner | Why exported |
|---|---|---|
| `com.anker.charging.MainActivity` | Anker | The single Flutter activity; launcher + all deep links, NFC and OAuth redirects (below) |
| `com.amazon.identity.auth.device.workflow.WorkflowActivity` | Amazon LWA | Login-with-Amazon / Alexa account linking redirect (`amzn://com.anker.charging`) |
| `FlutterFirebaseMessagingReceiver` | Firebase | Receives `com.google.android.c2dm.intent.RECEIVE` (push) |
| `FirebaseInstanceIdReceiver` | Firebase | FCM token events |
| `com.google.android.gms.common.api.GoogleApiActivity` | Google GMS | GMS result shuttle |
| `com.google.android.gms.auth.api.signin.RevocationBoundService` | Google GMS | Google sign-out |
| `androidx.profileinstaller.ProfileInstallReceiver` | AndroidX | Baseline-profile install |

The security-relevant takeaway: `MainActivity` is the only app-written exported surface. Everything an external app can reach is funnelled through it and through the Amazon redirect activity.

## Deep links, NFC and OAuth

All intent filters below are on `MainActivity`. `flutter_deeplinking_enabled` is `false`, so Flutter's own router does not claim them — native code dispatches. Hosts match the China-region cloud (see [../api/README.md](../api/README.md) and [../mqtt/envelope.md](../mqtt/envelope.md) for the per-region host tables).

| Scheme / host | Path | Flags | Purpose |
|---|---|---|---|
| `ankerApp://product` | — | BROWSABLE | In-app product deep link |
| `https://aiot-api-cn.anker.com.cn` | `/ankerApp/` | `autoVerify` | App Link (China aIoT host) |
| `https://charging-api-cn.anker.com.cn` | `/ankerApp/` | `autoVerify` | App Link (China charging host) |
| `https://charging-smart.anker.com` | `/openapi/oauth/authorize` | `autoVerify` | OAuth authorize redirect (prod) |
| `https://charging-smart-qa.anker.com` | `/openapi/oauth/authorize` | `autoVerify` | OAuth authorize redirect (QA — a test host left in the shipped manifest) |
| NFC `NDEF_DISCOVERED` | mime `application/com.anker.charging` | — | Tap-to-open an Anker NFC tag |
| NFC `NDEF_DISCOVERED` | the two `.anker.com.cn` hosts + `/ankerApp/` | — | NFC tag carrying an App Link URL |
| `amzn://com.anker.charging` | — | BROWSABLE | Amazon LWA redirect (on `WorkflowActivity`) |

The QA OAuth host shipping in the production manifest is noted as-is; it is a smaller attack-surface observation, not a claim that it resolves.

## Embedded third-party SDK keys

Three third-party SDK keys are embedded as `<meta-data>` in the manifest. They are client keys (present in any copy of the APK); their literal values are **not reproduced here**. They identify which SDKs are wired in:

| `meta-data` name | SDK | Role |
|---|---|---|
| `com.google.android.geo.API_KEY` | Google Maps | Maps / geo outside China |
| `com.amap.api.v2.apikey` | AMap (Gaode) | Maps inside China |
| `com.tencent.mm.sdk.openapi.WX_APP_ID` | WeChat SDK | WeChat login / share (China) |

The pair of map SDKs and the WeChat app id confirm the app ships a China-region build path alongside the global one, consistent with the `.com.cn` hosts above and the Huawei HMS `<queries>` entries.

## Packer markers

Four manifest entries are the Ijiami packer, not Anker code. They are the manifest-visible half of the finding detailed on [app_packaging.md](app_packaging.md):

| Entry | Meaning |
|---|---|
| `<application android:name="s.h.e.l.l.S">` | Packer `Application` subclass; bootstraps unpacking before any app code runs |
| `android:appComponentFactory="s.h.e.l.l.A"` | Packer `AppComponentFactory`; hooks component class loading |
| `com.ijm.detect.drisk.IjiamiActivityOfflineAttack` | Packer anti-tamper activity |
| `com.ijm.detect.drisk.IsolatedService` (`:tmpIService`, `isolatedProcess`) | Packer integrity check in an isolated process |

Because `s.h.e.l.l.S` is the real `Application`, the Anker application class named in the stub dex (`com.anker.charging.AnkerApplication`) is only reached after the packer has unpacked the real code at runtime.
