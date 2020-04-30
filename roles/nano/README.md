# nano

Configures nano using the `.nanorc` file. The configuration includes:

- Syntax Highlighting

## Configuration

The `nano` role can be configured using the `nano` namespace. Available options and their defaults are:

```yaml
nano:
	syntax_highlighting: yes
```

Available options are:

- `syntax_highlighting`: Enables syntax highlighting. This is incompatible with nano v2 so you might want to disable this option if nano v3 or later is not available.

