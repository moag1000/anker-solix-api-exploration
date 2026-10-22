> Verified against: App 3.24.3 · Date: 2026-10-21 · Confidence: asm-traced · Owner page: this page

# Native libraries

This page owns the inventory of native shared objects (`.so`) shipped in the APK (`lib/arm64-v8a/`) and what each one is. Library identity is read from the file name and from exported symbols (`nm -D`); the three Anker-written JNI surfaces are cited by their exact exported symbols. Tag: asm-traced. Where a library is a well-known open-source or vendor component, that identity is stated; its internals are out of scope. Transport and at-rest encryption are described at the role level only — this page does not derive any key material, curve, KDF parameter or message layout from the binaries.

## Contents

1. [Anker-written JNI surfaces](#anker-written-jni-surfaces)
1. [Cryptography and storage](#cryptography-and-storage)
1. [Packer](#packer)
1. [Application runtimes](#application-runtimes)
1. [Media, scanning and support](#media-scanning-and-support)

## Anker-written JNI surfaces

Three shipped libraries export `Java_com_anker…` / `Java_com_jni…` symbols, i.e. they are Anker's own JNI, not third-party:

| Library | JNI class | Exported methods | Role |
|---|---|---|---|
| `libecc-encryption.so` | `com.anker.esiotkit.support.crypto.EccEncryption` | `eccEncrypt`, `eccDecrypt`, `generateEccKey` | App-layer transport crypto for the esIoT kit — the native side of the ECDH + AES scheme the Dart code drives (see [../api/encryption.md](../api/encryption.md)) |
| `libUbdt.so` | `com.jni.Ubdt` | `init`, `openLog`, `sendobj`, `sendobjtest` (+ `com.jni.I4test.sendobj`) | Wi-Fi / IoT device debug-log transport |
| `libak_logan.so` | — (registered via `JNI_OnLoad`) | none exported by name | Meituan **Logan** mobile logger (encrypted rolling local logs) |

`libecc-encryption.so` also contains a tiny-AES implementation and HMAC-SHA256; together with the `EccEncryption` class this is the native half of the request-body encryption whose Dart side is documented on [../api/encryption.md](../api/encryption.md). It is transport/payload protection; the scheme (which fields, when) lives on that page.

## Cryptography and storage

All of these are standard components, present for transport security and at-rest storage:

| Library | Identity | Role |
|---|---|---|
| `libcrypto-security.so` | BoringSSL / OpenSSL | TLS and general crypto primitives (large export surface) |
| `libconscrypt_jni.so` | Google Conscrypt | JSSE/TLS provider for the JVM side |
| `libargon2.so` | Signal `org.signal.argon2` (`Argon2Native.hash/verify`) | Argon2 password hashing / key derivation |
| `libsqlcipher.so` | SQLCipher (`sqlite3_key`, `sqlite3_rekey`) | Encrypted local SQLite database (data at rest) |

The presence of Argon2 and SQLCipher means local secrets and the local database are protected at rest; neither is reverse-engineered further here.

## Packer

| Library | Role |
|---|---|
| `libijmDataEncryption*.so` (per ABI, in `base_apk/assets/`) | Ijiami payload decryptor |
| `libijm-emulator.so` | Ijiami anti-emulator check |
| `libijmdetect-drisk.so` | Ijiami tamper / risk detection |

These run the packing layer described on [app_packaging.md](app_packaging.md).

## Application runtimes

The app ships **two** UI runtimes side by side:

| Stack | Libraries | Note |
|---|---|---|
| Flutter (primary) | `libflutter.so`, `libapp.so`, `libdartjni.so`, `libfbjni.so`, `libjsi.so` | `libapp.so` is the Dart AOT snapshot that every other section of this reference is built from |
| React Native (secondary) | `libreactnative.so`, `libhermes.so`, `libhermestooling.so`, `libjsctooling.so`, `libquickjs.so`, `libquickjs-android.so` | Hermes + QuickJS; a subset of screens is React Native, not Flutter |

A third runtime, Unity (`libil2cpp.so`, `libunity.so`, `libdraco_unity.so`, `libAVProMovieCaptureNative.so`), ships for 3D product visualisation only and is out of scope for this reference — it carries no protocol or API logic.

## Media, scanning and support

Stock components, listed for completeness: `libpdfium.cr.so` / `libpdfiumandroid.so` (PDF), `libgifimage.so` / `libimagepipeline.so` / `libnative-imagetranscoder.so` / `libnative-filters.so` / `libimage_processing_util_jni.so` (Fresco image pipeline), `libopus-lib.so` (audio), `libbarhopper_v3.so` / `libscannative.so` (ML Kit barcode / QR), `libsentry.so` / `libsentry-android.so` (Sentry crash reporting), `libc++_shared.so` (NDK runtime), `libdatastore_shared_counter.so` (Jetpack DataStore), `libandroidx.graphics.path.so`, `libsurface_util_jni.so`.
