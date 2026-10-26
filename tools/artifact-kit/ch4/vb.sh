#!/bin/bash
# usage: vb.sh <mk_script_without_ext> <slug>  -- build, smoke test, headless overlap check
cd ~/Documents/GitHub/Ascendant; python3 tools/artifact-kit/$1.py 2>&1 | tail -3
bash tools/artifact-kit/ch4/smoke.sh $2 | grep -o "ERRS=[0-9]* NAN=[0-9]*"; bash tools/artifact-kit/ch4/chkh.sh $2
