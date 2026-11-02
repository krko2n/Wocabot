WOCA BEE CONTROL - PORTABLE
============================

Start:
  Double-click Start-WocaBee-Control.cmd
  (or WocaBee-Control.exe directly).

This folder contains its own Chromium browser and does not need Python or
Playwright to be installed on a Windows 11 PC. Keep every file and folder
together when copying it to a USB flash drive.

Important:
  config.toml is your local account configuration and contains your saved login
  details. Keep the USB drive private. Do not upload or share config.toml.

The panel offers checkpoint, current-part, full-package and all-package modes.
It waits between actions, handles the vocabulary-introduction screen, spelling
choices, and the fast pexeso double-click. Logs and diagnostic screenshots are
saved under diagnostics.

If WocaBee changes an exercise screen, the run stops and writes a screenshot
instead of continuing blindly.
