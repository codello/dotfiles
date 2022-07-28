#!/usr/bin/env zsh
##############################################################################
# ZSH Custom Aliases
##############################################################################

if command -v bat > /dev/null; then
    alias cat='bat --paging=never'
fi

if command -v gls >/dev/null; then
    alias ls="gls --color"
fi

alias la='ls -lAh'
alias ll='ls -lah'
