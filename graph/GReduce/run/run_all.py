import os
for i in range(1, 11):
	if i in [2, 4, 9]:	# compare results from two versions
		os.system('python debuggerc.py T s3 %d' % i)
	else:
		os.system('python debugger.py T s3 %d' % i)
		