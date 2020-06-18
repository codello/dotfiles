# Finder

Configures the macOS Finder using the macOS `defaults`. This role supports:

- Configuring what to show on the desktop
- Configuring searches
- Configuring the Icon Arrangement

This role can only be run on macOS systems.

## Configuration

The `finder` role can be configured using the `finder` namespace. Available options and their defaults are:

```yaml
finder:
  # Show internal drives (e.g. Macintosh HD) on the Desktop.
  hds_on_desktop: yes
  # Show external drives on the desktop.
  external_hds_on_desktop: yes
  # Show connected servers on the desktop.
  servers_on_desktop: yes
  # Show removable media on the desktop.
  removable_media_on_desktop: yes
  # When searching, search the current folder by default.
  current_folder_search: yes
  # Do not show a warning when changing the extension of a file.
  file_extension_warning: no
  # If enabled no .DS_Store files will be created on network shares.
  no_network_stores: null
  # If enabled no .DS_Store files will be created on USB drives.
  no_usb_stores: null
  # The default arrangement of icons in folder. Set to `none` to not arrange icons.
  default_item_arrangement: grid
  # The icon arrangement on the desktop. If stacks are used this may not be set to `none`.
  desktop_item_arrangement: name
  # How to group stacks. Set to `None` to disable stacks.
  stacks: Kind
```

Each value can also be set to the `null` value to keep the respective setting untouched.

