# TextEdit

Configures TextEdit for MacOS using the macOS `defaults`. This role supports:

- Configuring the default format for new documents (rich or plain text)
- UTF-8 support

This role can only be run on macOS systems.

## Configuration

The `textedit` role can be configured using the `textedit` namespace. Available options and their defaults are:

```yaml
textedit:
	# Whether new documents should be created as rich text or plain text documents.
  rich_text: no
  # Set the default open and save format to UTF-8.
  utf8: yes
```

Each value can also be set to the `null` value to keep the respective setting untouched.

