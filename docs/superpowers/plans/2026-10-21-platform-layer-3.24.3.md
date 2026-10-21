# Platform Layer (beyond the Dart snapshot) — 3.24.3

**Goal:** Document the parts of the APK that are not in the Dart AOT snapshot — the Android manifest, the native libraries (role level), the embedded web view bridge, and the app-packaging layer (Ijiami packer + RSA assets) — as a new `platform/` section, and close two leftover tooling gaps.

**Architecture:** One new top-level `platform/` directory, one page per layer, linked from the README repo map and from `reference/README.md`. Facts come from jadx-decoded resources (manifest), `nm -D`/`strings` on the shipped `.so` files (symbol/role level only), the decoded web view JS bundle, and file listings of `base_apk/assets`. No runtime analysis, no unpacking of the Ijiami payload, no extraction of key-derivation internals from any crypto library — those are named at the level of "which library does what / which JNI class exists", consistent with the transport/at-rest crypto already described from the Dart side.

**Scope guard:** Transport and at-rest encryption are documented at the functional/role level (TLS, ECDH+AES app-layer transport, Argon2 KDF, SQLCipher at-rest). We do not derive curve constants, KDF parameters, IV construction or message layout from the binaries. The packer is documented as a *finding* (what is packed, which loaders run it, that the Java is not statically readable), not as an unpacking recipe.

## Pages

- `platform/README.md` — section index + the "not in the Dart snapshot" framing.
- `platform/android_manifest.md` — package/version/SDK, permission set grouped by capability, the exported-component surface (only MainActivity + Amazon LWA are app-specific; rest is framework), deep links / NFC / OAuth intent filters, embedded third-party API keys **by name and purpose only (no literal key values)**, and the manifest-level packer markers (`s.h.e.l.l.S`, `s.h.e.l.l.A`, Ijiami components).
- `platform/native_libraries.md` — the `.so` inventory as a role table; the three Anker JNI surfaces (`EccEncryption`, `com.jni.Ubdt`, Logan) with their confirmed symbols; the crypto/storage libs (BoringSSL, Conscrypt, Signal Argon2, SQLCipher) at role level; the packer libs; the dual Flutter+React-Native runtime observation; Unity marked out of scope.
- `platform/webview_bridge.md` — the `assets/webview/post/ankerPost.html` energy-flow editor, the JS→Flutter `callHandler(...)` names and the `postMessage({code:"set*"})` codes, and that it issues no HTTP of its own.
- `platform/app_packaging.md` — the Ijiami packer finding (16 KB stub `classes.dex`, `ijiami.dat`/`ijiami.ajm` payload sizes, per-ABI `libexec*.so` loaders) with the explicit consequence that the Java/Kotlin code is not statically readable without runtime unpacking; and the two RSA **public**-key assets (`public.pem`, `publicMp.pem`) — type, that no private key ships, and that no Dart-side loader is traceable (loader is in the packed Java).

## Tooling gaps (from the r2 depth pass)

- `endpoint_inventory`: add the `getDataFromService` senders that load the URL as `r1 = "/..."` (currently missed by the caller scan).
- One-hop typing pass was never run on request-field batches 3a/3b — run it and promote what types cleanly.

## Wiring

- README section 6 repo-map: add a `platform/` row.
- `reference/README.md`: add a pointer to `platform/`.
- Lint clean (`tools/lint_docs.py`), tests green (`python3 -I -m unittest discover -s tools/tests -t .`).

## Confidence

Manifest, native symbols, web view bundle and asset listings are all directly extracted → `asm-traced`-equivalent (call it `extracted`/`asm-traced` per page, lowest-tag-on-page rule). Anything about what the packed Java *does* at runtime is explicitly out of reach and labelled as not visible in the app.
