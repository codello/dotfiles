# Mail

Configures Mail for macOS using the macOS `defaults`. This role supports:

- Configuration of address copying
- Viewing of inline attachments

This role can only be run on macOS systems.

## Configuration

The `mail` role can be configured using the `mail` namespace. Available options and their defaults are:

```yaml
mail:
  # Copying email addresses with names results in strings like `Foo Bar <foo@example.com>`.
  # Without names only the address `foo@example.com` will be copied.
  copy_with_names: no
  # Disable inline attachments and only show the attachment icons instead.
  no_inline_attachments: yes
```

Each value can also be set to the `null` value to keep the respective setting untouched.

