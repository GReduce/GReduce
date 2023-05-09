#!/bin/bash
path_prefix="MYPATH/graph-g9"
file_input="create_graph.py"

cp ./${file_input} ${path_prefix}/${file_input}
cd ${path_prefix}
python3 ${path_prefix}/proxy.py

echo 1 >> ${path_prefix}/cnt.txt

# Using test command
if test -f "graph.json"; then
    echo 'file exist'
else
    echo "File file.txt does not exist"
    exit 1
fi

output1=$(java -jar jqf-examples-1.9-fat-tests-A.jar 0)
output2=$(java -jar jqf-examples-1.9-fat-tests-B.jar 0)

mv graph.json graph2.json

# if [ "$output" -eq 0 ]; then
#     mv graph2.json ok.json
# fi
substring="true"
out=1
if [[ "$output1" != "$output2" ]]; then
	mv graph2.json ok.json
	mv create_graph.py ok_create_graph.py
	out=0
fi

echo $out

exit $out

