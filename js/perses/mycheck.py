import os
import sys

cases = int(sys.argv[1])

import js_oracle

def check():
	filename = 'my.js'
	runc = 'java -jar testjs-n.jar "$(cat ' + filename + ')"'	
	r = os.popen(runc)
	o = r.read()
	r.close()
	return js_oracle.oracle(cases, o)

if check():
	print('0', end="")
else:
	print('1', end="")

