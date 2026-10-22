> Verified against: App 3.24.3 · Date: 2026-10-21 · Confidence: asm-traced · Owner page: this page

# Web view bridge

The app bundles exactly one HTML web view: an energy-flow editor at `assets/webview/post/ankerPost.html` (with `index.html` and `404.html`), a compiled Next.js app loaded through the `flutter_inappwebview` plugin. This page owns the bridge between that web view and the Flutter host. The handler and message names are read from the bundled JavaScript (`flutter_assets/assets/webview/post/`); tag: asm-traced. The web view issues **no HTTP of its own** — it receives all its data from the host over the bridge and sends all its actions back the same way.

## JS → Flutter: `callHandler`

The page calls `window.flutter_inappwebview.callHandler("<name>")` to ask the host to act. Confirmed names:

| Handler | When the page calls it |
|---|---|
| `initPost` | Once, on mount |
| `getData` | On mount, then polled on a 10-second interval (`setInterval(…, 1e4)`) |
| `refresh` | The retry button |
| `closePage` | The close button |
| `openStorageDrawer` | Opens the storage-configuration drawer |
| `jumpToPrivacy` | The terms / privacy link |

## Flutter → JS: injected `window.set*` setters

The host pushes the energy-flow configuration into the page by calling globals the page defines. Each setter re-broadcasts its argument as a `window.postMessage({code, args}, "*")` that the page's own `message` listener consumes:

| Global the host calls | `code` broadcast | Flow element it configures |
|---|---|---|
| `window.setSolar(data)` | `setSolar` | Solar / PV source |
| `window.setGrid(data)` | `setGrid` | Grid connection |
| `window.setHome(data)` | `setHome` | Home load |
| `window.setStorage(data)` | `setStorage` | Battery storage |
| `window.setDiesel(data)` | `setDiesel` | Diesel generator |
| `window.setFlows(data)` | `setFlows` | The flow arrows between the elements |

So the data direction is: Flutter computes the live energy picture and calls `window.setSolar` / `setGrid` / `setHome` / `setStorage` / `setDiesel` / `setFlows`; the page renders the diagram; user edits in the page come back to Flutter through `callHandler`. The `message` listener gates on `e.origin`, and the page falls back to a `flutterInAppWebView`-ready event when `window.flutter_inappwebview` is not yet present.
