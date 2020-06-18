# git

Configures git using the `.gitconfig` file. The configuration includes:

- Git name and email
- Keychain support on macOS
- Global `.gitignore` for common OS files

## Configuration

The `git` role can be configured using the `git` namespace. Available options and their defaults are:

```yaml
git:
	# The name and email to use for git commits.
	name: "{{ full_name }}"
	email: "{{ email }}"
```

