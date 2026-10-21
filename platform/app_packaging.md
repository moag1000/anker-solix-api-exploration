> Verified against: App 3.24.3 · Date: 2026-10-21 · Confidence: asm-traced · Owner page: this page

# App packaging and asset keys

This page records two facts about how the APK is assembled that affect anyone trying to reverse the non-Flutter half of the app: the Java/Kotlin code is wrapped by the **Ijiami** (ijm) commercial packer, and the app ships two RSA **public**-key assets. Everything here is read from file listings and `strings` on `base_apk/`; tag: asm-traced. What the packed Java actually does at runtime is explicitly **not** covered — it is not statically readable, and this page does not describe how to unpack it.

## Contents

1. [The Ijiami packer](#the-ijiami-packer)
1. [Consequence for reversing](#consequence-for-reversing)
1. [RSA public-key assets](#rsa-public-key-assets)

## The Ijiami packer

`classes.dex` in the base APK is a **16 KB stub**, not the app. Its strings are the packer bootstrap:

| String in `classes.dex` | Meaning |
|---|---|
| `Ls/h/e/l/l/S;`, `Ls/h/e/l/l/A;`, `Ls/h/e/l/l/C;`, `Ls/h/e/l/l/N;` | The packer shell classes (`s.h.e.l.l.S` is the manifest `Application`, `s.h.e.l.l.A` the `appComponentFactory`) |
| `com.ijm.dataencryption.DETool` | Ijiami data-encryption entry point |
| `com.anker.charging.AnkerApplication` | The **real** app `Application`, reached only after the packer unpacks |
| `assets/ijm_lib/%s/libexec.so`, `assets/ijm_lib/%s/libexecmain.so` | The per-ABI loaders the stub `dlopen`s (`%s` = ABI) |

The packed real code and the native loaders ship as assets:

| Asset | Size | Role |
|---|---|---|
| `base_apk/assets/ijiami.dat` | 8.4 MB | Packed/encrypted payload |
| `base_apk/assets/ijiami.ajm` | 6.8 MB | Packed/encrypted payload |
| `base_apk/assets/ijm_lib/<abi>/libexec.so`, `libexecmain.so` | — | Runtime loaders (one set per ABI) |
| `base_apk/assets/libijmDataEncryption*.so` | — | Payload decryptor, per ABI |
| `base_apk/assets/IJMDal.Data` | — | Packer data file |

The manifest-side markers of the same packer (`IjiamiActivityOfflineAttack`, the isolated `IsolatedService`, and the `s.h.e.l.l.*` application wiring) are on [android_manifest.md](android_manifest.md#packer-markers).

## Consequence for reversing

Running `jadx` or any static DEX decompiler on this APK yields only the ~16 KB stub above — the real Java/Kotlin classes (`com.anker.charging.*`, the account/usercenter UI, the FCM handlers, the RSA loader) are inside the encrypted `ijiami.dat` / `ijiami.ajm` and are only materialised in memory at runtime by `libexecmain.so`. **The Flutter/Dart half of the app (`libapp.so`) is not packed** — that is why every other section of this reference exists. Any fact that lives only in the packed Java is out of reach of the static method used here and is marked "not visible in the app" wherever it comes up.

## RSA public-key assets

Two PEM files ship under `base_apk/assets/flutter_assets/assets/rsa/`:

Tag: untagged by design — the byte counts are file sizes, not decoded immediates.

| File | Bytes | Type |
|---|---|---|
| `public.pem` | 272 | `-----BEGIN PUBLIC KEY-----` (SubjectPublicKeyInfo) |
| `publicMp.pem` | 272 | `-----BEGIN PUBLIC KEY-----` (SubjectPublicKeyInfo) |

Both are **public** keys; no private key ships in the APK (as expected). They are the public half of an RSA scheme the app uses to encrypt something it sends to the server (a public key can only encrypt / verify, so the matching private key lives server-side). In the Dart snapshot only the type (`<RSAPublicKey>`) and the `.pem` extension appear — **no loader that reads these files is traceable in `libapp.so`**, which places the RSA loader in the packed Java half. The `Mp` suffix on the second key is a naming distinction only (a separate key for a second channel, e.g. a mini-program); the app code that selects between them is in the packed Java and not visible here.
