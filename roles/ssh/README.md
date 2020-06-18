# ssh

Configures SSH using the `.ssh` folder. The configuration includes:

- Generation of SSH keys.
- Setup `.ssh/authorized_keys` using your GitHub account.
- Configuration of hosts in `.ssh/config`.

## Configuration

The `ssh` role can be configured using the `ssh` namespace. Available options and their defaults are:

```yaml
ssh:
	# The filename of the SSH key to generate. The key will be generated as an
  # ed25519 key.
  # 
  # Optionally you can set a key passphrase. key_passphrase is undefined by default.
  # The passphrase is only required if the key does not already exist. If the key
  # exists the passphrase is not required. Changing the passphrase on an existing key
  # is not supported.
  # To generate a key without passphrase set the key_passphrase to the empty string.
	key: ~/.ssh/id_ed25519
  #key_passphrase:
	
	# If set to true all SSH keys from your GitHub account will be added to the
  # authorized_keys. You can specify your GitHub account using the github_user
  # variable.
	github_keys: no
	
	# A comment that should be applied to all GitHub SSH keys. Using the
  # authorized_keys below this comment can be overridden on a per-key basis.
	github_keys_comment: GitHub
	
	# Specify a list of public SSH keys that should be added to the
  # authorized_keys. You can specify either a public key or a mapping
  # containing a `key` and a `comment`.
	authorized_keys: []
	
	# Specify a list of hosts that should be added to the SSH config. The key of
  # each item is the name in the SSH config. The value is a dictionary of
  # options that are added verbatim to the config file.
	hosts: {}
```

