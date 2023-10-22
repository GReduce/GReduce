import os

ABS_PATH = os.path.abspath(os.path.join(os.getcwd(), ".."))

with open('myrun.sh') as f:
	t = f.read()
	t = t.replace('MYPATH', ABS_PATH)
	t = t.replace('output=', "echo 2 >> ${path_prefix}/cnt.txt\n\noutput=")
	t = t.replace('output1=', "echo 2 >> ${path_prefix}/cnt.txt\n\noutput1=")
	
	with open('run.sh', 'w') as f2:
		f2.write(t)
	os.system('chmod +x run.sh')

os.system('cp create_graph.py.orig ./create_graph.py')
os.system("rm cnt.txt")
os.system("timeout 3600 java -jar perses_deploy.jar --test-script ./run.sh --input-file ./create_graph.py --threads 1 2>&1 | tee res.txt")
