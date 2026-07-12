import { LIB_NAME } from "./env";

// Canonical Waybar snippets shown in the install docs. Single source of truth
// for the web app so the landing page and any other consumer stay in sync.
//
// Keep these aligned with what packages/lib/install.sh generates. The image
// module runs the `logo` command, which prints the PNG path (line 1) and the
// tooltip (line 2) — so hovering the logo shows the same breakdown as the text.
// `interval` is required for the image to render; `signal` refreshes it on
// provider/data changes. Logos are rasterised to opaque RGB PNGs (a grayscale
// or alpha PNG makes Waybar blank the bar).

export const WAYBAR_CUSTOM_MODULE = `"custom/${LIB_NAME}": {
    "exec": "~/.local/bin/${LIB_NAME} daemon",
    "restart-interval": 1,
    "return-type": "json",
    "format": "{}",
    "tooltip": true,
    "on-click": "~/.local/bin/${LIB_NAME} refresh",
    "on-click-right": "~/.local/bin/${LIB_NAME} config",
    "on-scroll-up": "~/.local/bin/${LIB_NAME} scroll-up",
    "on-scroll-down": "~/.local/bin/${LIB_NAME} scroll-down",
    "on-click-middle": "~/.local/bin/${LIB_NAME} cycle-metric"
}`;

export const WAYBAR_LOGO_MODULE = `"image#${LIB_NAME}": {
    "exec": "~/.local/bin/${LIB_NAME} logo",
    "size": 14,
    "interval": 3,
    "signal": 11,
    "on-click": "~/.local/bin/${LIB_NAME} refresh",
    "on-click-right": "~/.local/bin/${LIB_NAME} config",
    "on-scroll-up": "~/.local/bin/${LIB_NAME} scroll-up",
    "on-scroll-down": "~/.local/bin/${LIB_NAME} scroll-down",
    "on-click-middle": "~/.local/bin/${LIB_NAME} cycle-metric",
    "tooltip": true
}`;

export const WAYBAR_LAYOUT = `{
    // ...
    "modules-right": [
        "image#${LIB_NAME}",
        "custom/${LIB_NAME}",
        "network",
        "cpu",
        "memory",
        "clock",
        "tray"
    ],
    // ...
}`;
