# homebrew

Installs packages via homebrew. If homebrew is unavailable this role tries to install homebrew itself first. This role features:

- Automatic installation of homebrew
- Support for formulae and casks
- Support for tapping additional taps

## Configuration

The `homebrew` role can be configured using the `homebrew` namespace. Available options and their defaults are:

```yaml
homebrew:
	# If set to true homebrew will update all taps before installing formulae.
  update: yes
  
  # If set to true homebrew will also upgrade all existing formulae and casks.
  upgrade: yes
  
  # List additional taps that should be tapped before installation.
  # Private taps are not currently supported.
  taps: []
  
  # A list of formulae that should be installed.
  formulae: []
  
  # A list of casks that should be installed.
  casks: []
```

