import os
for i in range(1, 11):
	os.system('cp run.py ./graph-g%d/' % i)
	os.system('cd ./graph-g%d && python run.py' % i)
