# Contributing to Omarchy AI Status

Thank you for your interest in improving Omarchy AI Status.

Currently, this module is heavily optimized for **Linux** and **Waybar**. However, thanks to its modular design, the core logic in `src/core/` and the data-fetching mechanisms in `src/providers/` are independent and can be adapted easily.

## Adding Support for a New OS or Status Bar

If you use macOS, Windows, or another status bar (like Polybar, eww, or sketchybar), you can help us support it.

1. **Fork this repository** on GitHub.
2. **Abstract the UI**: The visual formatting is currently handled in `src/core/render.py` using Pango markup (Waybar's standard). You can modify this file to support standard text or other formatting syntaxes based on environment variables or config flags.
3. **Update Installation**: Modify the `install.sh` and `check.sh` scripts to recognize the new environment and configure it appropriately.
4. **Submit a Pull Request (PR)**. We would love to merge your work to support users across all platforms.

## Developing New Providers

To add a new AI API to the list:

1. Create a folder in `src/providers/<name>`.
2. Write a `query.sh` that makes the HTTP request to the API.
3. Write a `parse.py` (in the same folder) to format the raw output into a standardized JSON array. (Check `src/providers/claude` for an example).
4. Open a Pull Request.
