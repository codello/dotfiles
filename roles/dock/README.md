# Dock

Configures the macOS Dock using the macOS `defaults`. This role supports:

- Translucent icons for hidden apps
- Indicator for Running applications

This role can only be run on macOS systems.

## Configuration

The `dock` role can be configured using the `dock` namespace. Available options and their defaults are:

```yaml
dock:
	# Make icons of hidden applications translucent.
  show_hidden: yes
  # Show indicator lights for running applications.
  indicators: yes
```

Each value can also be set to the `null` value to keep the respective setting untouched.

