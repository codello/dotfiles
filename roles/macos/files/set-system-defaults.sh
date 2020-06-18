# This file contains unused system default settings that have not yet been
# converted into ansible tasks.

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

# Hide Spotlight tray-icon (and subsequent helper)
# chmod 600 /System/Library/CoreServices/Search.bundle/Contents/MacOS/Search

# Disable Spotlight indexing for any volume that gets mounted and has not yet
# been indexed before.
# Use `mdutil -i off "/Volumes/foo"` to stop indexing any volume.
#defaults write /.Spotlight-V100/VolumeConfiguration Exclusions -array "/Volumes"

# Make sure indexing is enabled for the main volume
# mdutil -i on / > /dev/null
# Rebuild the index from scratch
# mdutil -E / > /dev/null
