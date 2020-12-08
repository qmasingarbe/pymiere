#!/usr/bin/env bash
# Auto install PymiereLink extension to Premiere on mac

# Get temp path
tempdir=$(mktemp -d)

# Download zxp (extension) file
echo "Download .zxp file"
url="https://raw.githubusercontent.com/qmasingarbe/pymiere/master/pymiere_link.zxp"
fname_zxp=$(basename "$url")
path_zxp="$tempdir/$fname_zxp"
curl "$url" --output "$path_zxp"

# Download ExManCmd (extension manager)
echo "Download ExManCmd"
url="https://download.macromedia.com/pub/extensionmanager/ExManCmd_mac.dmg"
fname_exman=$(basename "$url")
path_exman="$tempdir/$fname_exman"
curl "$url" --output "$path_exman"

# Mount ExManCmd DMG
mount_path="$tempdir/ExManCmdMount"
echo "Mount ExManCmd DMG: $path_exman to $mount_path"
hdiutil attach "$path_exman" -mountpoint $mount_path

# Install the .zxp file
exmancmd="$mount_path/Contents/MacOS/ExManCmd"
echo "Install zxp"
"$exmancmd" --install "$path_zxp"
# For debugging
# "$exmancmd" --list all

# Clean up
echo "Unmount ExManCmd DMG"
hdiutil detach "$mount_path"
rm -rf "$tempdir"