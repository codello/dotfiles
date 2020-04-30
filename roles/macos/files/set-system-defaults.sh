#!/usr/bin/env sh

##############################################################################
# Configuring Security Settings
##############################################################################
# Disable remote apple events
systemsetup -setremoteappleevents off

# Disable remote login
if [[ $SERVER = true ]]; then
    yes 'yes' | systemsetup -setremotelogin on
else
    yes 'yes' | systemsetup -setremotelogin off
fi

##############################################################################
# "Configuring System Settings"
##############################################################################

# Disable guest account login
defaults write /Library/Preferences/com.apple.loginwindow GuestEnabled -bool false

# TODO: Incorporate this somehow
# Set computer name (as done via System Preferences → Sharing)
#scutil --set ComputerName "0x6D746873"
#scutil --set HostName "0x6D746873"
#scutil --set LocalHostName "0x6D746873"
#defaults write /Library/Preferences/SystemConfiguration/com.apple.smb.server NetBIOSName -string "0x6D746873"

if [[ $SERVER = true ]]; then
    # Reveal IP address, hostname, OS version, etc. when clicking the clock
    # in the login window
    defaults write /Library/Preferences/com.apple.loginwindow AdminHostInfo HostName

    # Restart automatically if the computer freezes
    systemsetup -setrestartfreeze on

    # Never go into computer sleep mode
    systemsetup -setcomputersleep Off > /dev/null
fi

###############################################################################
# SSD-specific tweaks                                                         #
###############################################################################

# Disable hibernation (speeds up entering sleep mode)
# pmset -a hibernatemode 0

# Remove the sleep image file to save disk space
# rm /private/var/vm/sleepimage
# Create a zero-byte file instead…
# touch /private/var/vm/sleepimage
# …and make sure it can’t be rewritten
# chflags uchg /private/var/vm/sleepimage


###############################################################################
# running "Configuring Spotlight"
###############################################################################

if [[ $SERVER = true ]]; then
    # Hide Spotlight tray-icon (and subsequent helper)
    chmod 600 /System/Library/CoreServices/Search.bundle/Contents/MacOS/Search
    # Disable Spotlight indexing for any volume that gets mounted and has not yet
    # been indexed before.
    # Use `mdutil -i off "/Volumes/foo"` to stop indexing any volume.
    #defaults write /.Spotlight-V100/VolumeConfiguration Exclusions -array "/Volumes"
fi

# Make sure indexing is enabled for the main volume
# mdutil -i on / > /dev/null
# Rebuild the index from scratch
# mdutil -E / > /dev/null
