> Verified against: App 3.24.3 · Date: 2026-10-21 · Page type: guidance (no API facts) · Owner page: this page

# Platform layer (beyond the Dart snapshot)

Every other section of this reference is built from the Dart AOT snapshot (`libapp.so`, disassembled with Blutter). That snapshot is the Flutter business logic: the cloud API, the MQTT decoders, the BLE protocol. It is not the whole APK. This section documents the parts of `Anker Power 3.24.3` that live **outside** the Dart snapshot and that a client-library author or an integrator still has to reason about: how the app declares itself to Android, which native libraries it ships, the one embedded web view and its bridge, and the packaging layer that wraps the Java/Kotlin half of the app.

Everything here is read directly from the shipped artifacts — the jadx-decoded `AndroidManifest.xml`, `nm -D` / `strings` on the `.so` files, the decoded web view bundle, and file listings of `base_apk/assets`. None of it is runtime analysis. Where a fact about behaviour can only be settled by running the app (anything the packed Java does), the page says so instead of guessing.

| Page | Tag | What it owns |
|---|---|---|
| [android_manifest.md](android_manifest.md) | asm-traced | Package/SDK, the permission set by capability, the exported-component surface, deep links / NFC / OAuth intent filters, embedded third-party SDK keys (by purpose), and the manifest-level packer markers |
| [native_libraries.md](native_libraries.md) | asm-traced | The shipped `.so` inventory as a role table, the three Anker JNI surfaces with their symbols, the crypto/storage libraries at role level, the packer libraries, and the dual Flutter + React Native runtime |
| [webview_bridge.md](webview_bridge.md) | asm-traced | The one bundled web view (`ankerPost` energy-flow editor), the JS→Flutter `callHandler` names and the `postMessage` codes it uses |
| [app_packaging.md](app_packaging.md) | asm-traced | The Ijiami packer finding (stub `classes.dex`, packed payload, loaders) and the two RSA public-key assets |

Not here: anything in the Dart snapshot (see [../api/README.md](../api/README.md), [../mqtt/README.md](../mqtt/README.md), [../ble/README.md](../ble/README.md)); the app-layer request encryption scheme as the Dart side builds it ([../api/encryption.md](../api/encryption.md)).
