# zsh

Configures the Z-Shell using the `.zshrc` and related files. The configuration includes:

- A custom ZSH theme
- A couple of aliases
- Package management via [Antibody](https://getantibody.github.io).

By default the ZSH configuration will install Antibody and matching terminal fonts. This can be configured (see below).

## Configuration

The `zsh` role can be configured using the `zsh` namespace. Available options and their defaults are:

```yaml
zsh:
  # Manually set the location of the ZSH executable. This value is not
  # validated. If the specified executable does not exist, it will be set as
  # the default shell anyway.
  location: null
  
  # Set ZSH as the default shell for the user.
  default: true
  
  # Do not set ZSH as the default shell via chsh but include a bash profile
  # that immediately executes ZSH. This is useful if chsh cannot be used to
  # switch to ZSH for some reason.
  shell_exec: false
  
  # Sets the LANG environment variable
  language: de_DE.UTF-8
  
  # Enable subversion support in the ZSH theme.
  enable_svn: false
  
  # Wether to install antibody if it is absent. Set this to "manual" to not
  # install antibody via Homebrew on macOS.
  antibody: true
  
  # A path to a directory in which to install antibody.
  # The default value is undefined but by default antibody will be installed
  # into ~/.local/bin for a user installation and into /usr/local/bin for a
  # system installation.
  #
  # On macOS the default is to install antibody via Homebrew unless this path
  # is specified.
  antibody_path: null
  
  # Whether antibody should be installed in a system wide directory (by default
  # /usr/local/bin). This causes antibody to be installed in priviliged mode if
  # even if you set antibody_path.
  #
  # On macOS this value is ignored unless you set antibody_path.
  antibody_system_install: false
  
  # Whether to install fonts that work well with the ZSH theme automatically.
  # The fonts are installed via Homebrew on macOS unless this variable is set to
  # a string indicating the target directory for the fonts. On other operating
  # systems fonts are installed into ~/.local/share/fonts by default (or
  # /usr/local/share/fonts if zsh.fonts_system_install is true).
  fonts: true
  
  # Whether to install the fonts system wide. Ignored if zsh.fonts is false.
  fonts_system_install: false
  
  # Additional environemnt variables to be exported.
  env: {}
```

