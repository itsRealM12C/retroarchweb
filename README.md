# RetroArch Web Port (Fullscreen)

A browser-based RetroArch build that boots straight into fullscreen with no
menu chrome, no click-to-start — just load the page and play. Built for both
desktop and mobile.

## Goal

- **Fullscreen by default** — canvas fills the viewport, all UI (navbar,
  core selector, preview image) hidden.
- **Auto-start** — `autoStart = true` in `libretro.js`, so RetroArch boots
  immediately on page load instead of waiting for a Run click.
- **Mobile + desktop support** — works with on-screen touch overlays on
  mobile and keyboard input on desktop, same build.
- **Optimize Performance** — should be less laggy, and not more laggy.

## Features

- Fullscreen canvas, scaled via CSS `object-fit: contain` to preserve
  aspect ratio (no stretching).
- Drag & drop ROM loading — drop a compatible ROM file anywhere on the
  page to load it into the running core.
- Quick menu access via a small invisible tap-zone at the top-center of
  the screen (double-finger-free — doesn't interfere with on-screen
  overlay controls or button mashing during gameplay).
- Default core: `gambatte` (Game Boy / Color). Other libretro cores
  included in this build can be swapped via the (hidden) core selector
  logic in `libretro.js`.

## Structure

```
index.html          fullscreen shell + drag-drop + quick-menu tap zone
libretro.js          core loader / RetroArch <-> browser bridge
browserfs.min.js      in-browser filesystem
core_list.js          list of available libretro cores
<core>_libretro.js    per-core Emscripten glue (one per core)
<core>_libretro.wasm  per-core compiled binary
assets/frontend/      RetroArch assets bundle (split zip, bundle.zip.aa-ae)
assets/cores/         optional XHR-served core assets
```

## Known limitations

- ROM files are not bundled — bring your own compatible/legal content.
- Some cores may have their own emulation quirks (audio timing, timing
  edge cases) independent of this wrapper.

## License

This wrapper (`index.html`, tap-zone/drag-drop additions) — MIT.
RetroArch, libretro cores, and BrowserFS retain their own original
licenses (GPL/MIT variants) — see each component's own LICENSE file.
