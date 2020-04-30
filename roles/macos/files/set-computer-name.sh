#!/bin/bash

# Set computer name (as done via System Preferences → Sharing)
scutil --set ComputerName "$COMPUTER_NAME"
scutil --set HostName "$COMPUTER_NAME"
scutil --set LocalHostName "$COMPUTER_NAME"
defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string "$COMPUTER_NAME"
