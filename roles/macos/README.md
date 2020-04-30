# macos

Configures macOS systems. This role features:

- Configuring default macOS apps like Finder, Safari and System Preferences
- Disables the gues account
- Restarts affected apps after applying the changes
- Much more…

## Configuration

The `macos` role cannot be customized. It does however respect the `sudo` and `server` variables:

- If `sudo=no` no system configuration will be applied.
- If `server=yes` some server-specific settings will be applied such as automatically restarting when the system freezes.