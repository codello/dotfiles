# macos

Configures macOS systems. This role features:

- Configuring the computer name
- Configuring the guest account
- Configuring trackpads
- Enabling high quality bluetooth audio
- Much more…

## Configuration

The `macos` role can be configured using the `macos` namespace. Available options and their defaults are:

```yaml
macos:
	# Whether to skip all tasks that require sudo permissions.
  skip_system: no

	# Quit the printer app automatically when printing is finished.
  quit_printer_when_finished: yes
  
  # Enable transparency for the main menu bar.
  transparent_menu_bar: null
  
  # Enable tap to click on trackpads.
  tap_to_click: yes
  
  # Enable high quality bluetooth audio.
  hq_bluetooth_audio: yes
  
  # Enable scroll to zoom using the ctrl (^) modifier.
  display_zoom: yes
  
  # Enable font smoothing on non-Apple LCDs.
  # See: https://github.com/kevinSuttle/macOS-Defaults/issues/17#issuecomment-266633501
  font_smoothing: 1

	# Set the computer name (as done via System Preferences → Sharing)
  computer_name: null
  
  # Disable remote apple events
  remote_apple_events: off
  
  # Disable remote login
  remote_login: off
  
  # Disable the guest account
  guest_account_login: off
  
  # Display information about the host (IP address, hostname, ...) in the login window.
  login_window_host_info: null
  
  # Automatically restart if the computer freezes.
  restart_after_freeze: on
  
  # The delay in minutes until the computer goes to sleep.
  # Set to `off` to prevent the computer from going to sleep.
  computer_sleep: 5
  
  # The delay in minutes until the display goes to sleep.
  # Set to `off` to prevent the display from going to sleep.
  display_sleep: 1
```

Each value can also be set to the `null` value to keep the respective setting untouched.
