#!/bin/bash

path_prefix="MYPATH"

cp ./myonnx.py ${path_prefix}/myonnx.py
cd ${path_prefix}
output=$(python3 ${path_prefix}/myonnx_check.py)

echo "1" >> ${path_prefix}/mycnt.txt

exit ${output: -1}
