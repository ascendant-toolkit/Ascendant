#!/bin/bash
# usage: struct.sh <kitname>  -> outline of body and js with line numbers (used when splitting a chapter)
n=$1
echo "== BODY"; grep -n '<section\|<h2>\|id="[a-zA-Z0-9]*"\|<details class="eq">\|</details>\|class="rw"' $n.body.html | grep -v 'class="readout"' | sed -E 's/<div class="readout">.*//' | cut -c1-150
echo "== JS"; grep -n '^/\* ---\|^Lib\.\|^function \|^const [A-Za-z0-9_]* = (' $n.js | cut -c1-130
