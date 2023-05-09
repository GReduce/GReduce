import os
import time

def count(x):
	return len(x.replace('\n','').replace(' ','').replace('\t','').replace('\r',''))

ABS_PATH = os.getcwd()

def e(c):
	file = 'n%s.js' % str(c) # change
	with open('myrun.sh') as f:
		t = f.read()
		t = t.replace('REPLACEME', str(c)).replace('MYPATH', ABS_PATH)
		with open('run.sh', 'w') as f2:
			f2.write(t)
		os.system('chmod +x run.sh')

	os.system('cp ./njs/%s ./my.js' % file)
	res = 'res_%s.txt' % file

	st = time.time()

	algo = 'Perses'
	runc = 'java -jar perses_deploy.jar --test-script ./run.sh --input-file ./my.js --threads 1 2>&1 | tee ' + res
	os.system(runc)

	ed = time.time()

	with open(res) as f:
		t = f.read()
		tt = int(t.split('Test script execution count: ')[1])

	with open('ok.js') as f:
		code = f.read()

	with open('all.txt', 'a') as f:
		print(file,algo, ":", "S=", count(code), "T=", "%.5lf" % (ed - st), "P=", tt, file=f)

	os.system('cat ok.js')
	os.system('mv ok.js ok_%s' % file)

for i in range(1, 11):
	e(i)
