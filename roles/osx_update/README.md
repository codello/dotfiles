# OS X Update

Configures Software Updates for macOS Systems using the macOS `defaults`. This role supports:

- Configuring Automatic Download of Updates
- Configuring Automatic Installation of Updates
- Configuring System and App Updates

This role can only be run on macOS systems.

## Configuration

The `osx_update` role can be configured using the `osx_update` namespace. Available options and their defaults are:

```yaml
software_update:
	# Automatically check for updates.
  auto_check: yes
  # How often to check for new updates (in days).
  check_frequency: 1
  # Automatically download new updates.
  auto_download: yes
  # Automatically install critical updates.
  install_critical: yes
  # Automatically install software updates.
  auto_update: yes
  # Allow automatic installation of updates that require a reboot.
  allow_reboot: yes
```

Each value can also be set to the `null` value to keep the respective setting untouched.

