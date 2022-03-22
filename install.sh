#!/bin/bash

# Backup the current sudoers.so
mkdir -p ~/.cache/sudo
cp /usr/lib/sudo/sudoers.so "$HOME/.cache/sudo/sudoers.so.bak.$(date +%s)"
ln -fs "$HOME/.cache/sudo/sudoers.so.bak.$(date +%s)" "$HOME/.cache/sudo/sudoers.so.bak"

./suwudo.py

# This wierd construction silences the segfault error
# https://stackoverflow.com/a/28522034
sudo cp ./sudoers.so /usr/lib/sudo/sudoers.so &>/dev/null | cat

# Remove the lectured file so the uwu-lecture prompt will appear again
sudo rm -f /var/db/sudo/lectured/$USER

echo "Successfully installed!"