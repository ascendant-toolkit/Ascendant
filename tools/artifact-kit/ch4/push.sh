#!/bin/bash
# push main with the ascendant-toolkit account, then switch back to whichever account was active
cd ~/Documents/GitHub/Ascendant
prev=$(gh auth status 2>&1 | grep -B3 "Active account: true" | grep -o "account [A-Za-z-]*" | head -1 | cut -d' ' -f2)
gh auth switch --hostname github.com --user ascendant-toolkit >/dev/null 2>&1
git push -q origin main 2>&1 | tail -1
[ -n "$prev" ] && gh auth switch --hostname github.com --user "$prev" >/dev/null 2>&1
git status -sb | head -1
