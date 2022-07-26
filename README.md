# Codello’s Dotfiles

These are the dotfiles of @codello, managed with [chezmoi](https://chezmoi.io).

## Quick Start

In order to configure a new macOS system you need to run multiple commands

```shell
# Install Homebrew, see https://brew.sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
# Install chezmoi
brew install chezmoi
# Configure dotfiles
chezmoi init --apply codello
```

The dotfiles configuration does **not** manage Homebrew itself.

## Caveats

- Currently only macOS systems are supported.
