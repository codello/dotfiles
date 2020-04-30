# opkg

Installs packages via opkg/OpenWrt.

## Configuration

The `opkg` role can be configured using the `opkg` namespace. Available options and their defaults are:

```yaml
opkg:
	# Update the package index before installation.
  update: yes
  
  # A list of packages that should be installed.
  packages: []
```

