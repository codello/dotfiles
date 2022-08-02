#!/usr/bin/env zsh
##############################################################################
# ZSH History Configuration
##############################################################################

# How many lines of history to keep in memory
HISTSIZE=5000
# Where to save history to disk
HISTFILE="$XDG_STATE_HOME/zsh/history"
#Number of history entries to save to disk
SAVEHIST=5000
#Erase duplicates in the history file
HISTDUP=erase
#Append history to the history file (no overwriting)
setopt    appendhistory
#Save each command's beginning timestamp and the duration to the history file
setopt    extendedhistory
#Share history across terminals
setopt    sharehistory
#Immediately append to the history file, not just when a term is killed
setopt    incappendhistory
#Remove duplicates from history
setopt    histignorealldups
#Remove superflous blanks from history
setopt    histreduceblanks

# no c-s/c-q output freezing
setopt noflowcontrol
# display PID when suspending processes as well
setopt longlistjobs
# report the status of backgrounds jobs immediately
setopt notify
# allow use of comments in interactive code
setopt interactivecomments

setopt csh_null_glob
setopt hist_verify
setopt auto_cd
setopt multios
# No "Beep"ing
setopt nobeep
# Don't push the same dir twice
setopt pushd_ignore_dups
