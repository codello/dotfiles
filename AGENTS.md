# AGENTS.md

This file provides guidance to AI coding agents that work in this repository.

## Overview

This is the chezmoi source directory for the user's macOS dotfiles. Currently only macOS is supported.

Commit messages use Conventional Commits with the tool as scope, e.g. `feat(zed): ...`.

## Editing and Verifying Changes

Do not edit or create files in the home directory directly. Make all changes in this source directory. chezmoi then applies them to the home directory.

Do not run `chezmoi apply` unless the user asks. Use read-only commands such as `chezmoi diff` and `chezmoi cat` instead.

Many templates read secrets from a password manager. Rendering them can trigger prompts or fail when the password manager is locked.

## Conventions

- The configuration supports two device types: `work` and `personal`. Templates use `.work` and `.personal` for device-specific content.
- When configuration applies to more than one tool, keep a single source for it, e.g. a shared template in `.chezmoitemplates/`. The global instructions for AI agents use this pattern.
