# Safari

Configures Safari for macOS using the macOS `defaults`. This role supports:

- Configuring safe downloads
- Configuring Developer Options

This role can only be run on macOS systems.

## Configuration

The `safari` role can be configured using the `safari` namespace. Available options and their defaults are:

```yaml
safari:
	# Do not open safe files after download.
  open_safe_downloads: no
  # Set to `yes` to enable the internal debug menu.
  debug_menu: null
  # Make Safari’s search banners default to Contains instead of Starts With.
  search_starts_with: null
  # Enable the Developer Menu.
  developer: yes
  # Enable warnings about fraudulent websites.
  warn_about_fraudulent_websites: yes
  # Enable "Do not Track".
  do_not_track: yes
  # Automatically update extensions.
  auto_update_extensions: yes
```

Each value can also be set to the `null` value to keep the respective setting untouched.

