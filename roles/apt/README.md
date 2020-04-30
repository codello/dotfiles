# apt

Installs packages via apt or apt-get. This role features:

- Update and installation of packages
- Autoremove unused packages

## Configuration

The `apt` role can be configured using the `apt` namespace. Available options and their defaults are:

```yaml
apt:
	# Update the package index before installation.
  update: yes
  
  # Upgrade all existing packages.
  upgrade: yes
  
  # Autoremove unused packages.
  autoremove: yes
  
  # A list of packages to be installed.
  packages: []
```

