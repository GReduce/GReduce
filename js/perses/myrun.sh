#!/bin/bash

path_prefix="MYPATH"

cp ./my.js ${path_prefix}/my.js
cd ${path_prefix}
output=$(python3 ${path_prefix}/mycheck.py REPLACEME)
# echo -e "should exit $output" > ${path_prefix}/output.txt
if [ "$output" == "0" ]; then
  cp ./my.js ./ok.js
fi
exit $output
