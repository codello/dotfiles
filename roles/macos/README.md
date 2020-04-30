# macos

Configures macOS systems. This role features:

- Configuring default macOS apps like Finder, Safari and System Preferences
- Disables the gues account
- Restarts affected apps after applying the changes
- Much more…

## Configuration

The `macos` role supports the following customizations:

```yaml
macos:
	# The name of the computer as configured via System Preferences > Sharing.
  computer_name: "{{ omit }}"
```

Additionally it does however respect the `sudo` and `server` variables:

- If `sudo=no` no system configuration will be applied.
- If `server=yes` some server-specific settings will be applied such as automatically restarting when the system freezes.

