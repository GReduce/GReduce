import os

ABS_PATH = os.getcwd()

with open('myrun.sh') as f:
	t = f.read()
	t = t.replace('MYPATH', ABS_PATH)
	with open('run.sh', 'w') as f2:
		f2.write(t)
	os.system('chmod +x run.sh')

for i in range(1, 20 + 1):
	os.system("rm mycnt.txt")
	os.system("cp models/bug%d_log.txt ./bug1_log.txt" % i)
	os.system("cp models/bug%d_inputs.npy ./bug1_inputs.npy" % i)
	os.system("cp models/bug%d.py ./myonnx.py" % i)
	os.system("timeout 3600 java -jar perses_deploy.jar --test-script ./run.sh --input-file ./myonnx.py --threads 1 2>&1 | tee models/bug%d.perses.res.txt" % i)
	os.system("mv ok.onnx models/bug%d.perses.reduce.onnx" % i)
	os.system("mv mycnt.txt models/bug%d.perses.cnt.txt" % i)
