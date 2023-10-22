import os
for i in range(1, 21):
	os.system('python debugger.py --GMD T --GMC s3 --GN %d' % i)
