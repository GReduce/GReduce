import os
import time
cnt = 0
outfile = 'all.txt'

r = [
'./delta.js --cmd examples/predicates/cmd-stderr-n.js --errmsg INDEX njs/n1.js',
'./delta.js --cmd examples/predicates/cmd-stderr-n2.js --errmsg REPED njs/n2.js',
'./delta.js --cmd examples/predicates/cmd-stderr-n.js --errmsg NaN njs/n3.js',
'./delta.js --cmd examples/predicates/cmd-stderr-n.js --errmsg k_4 njs/n4.js',
'./delta.js --cmd examples/predicates/cmd-stderr-n5.js --errmsg REPED njs/n5.js',
'./delta.js --cmd examples/predicates/cmd-stderr-n6.js --errmsg REPED njs/n6.js',
'./delta.js --cmd examples/predicates/cmd-stderr-n.js --errmsg undefined njs/n7.js',
'./delta.js --cmd examples/predicates/cmd-stderr-n.js --errmsg NEGATING njs/n8.js',
'./delta.js --cmd examples/predicates/cmd-stderr-n.js --errmsg x_7 njs/n9.js',
'./delta.js --cmd examples/predicates/cmd-stderr-n.js --errmsg i_26 njs/n10.js',
]

def count(x):
	return len(x.replace('\n','').replace(' ','').replace('\t','').replace('\r',''))

def run(runc):

	global cnt
	cnt += 1

	if (cnt != 8):
		return

	st = time.time()
	file = runc.split(' ')[-1].split('/')[-1]
	resf = 'res_%s.txt' % file
	
	r = os.system(runc + ' 2>&1 | tee ' + resf)

	with open(resf) as f:
		out = f.read()
		tt = out.count('Testing candidate')

	out_code = out.split('final version is at')[1].split('(')[0].strip()
	with open(out_code) as f:
		rc = f.read()

	with open(outfile, 'a') as f:
		print(file, ":", "S=", count(rc), "T=", time.time() - st, "P=", tt, file=f)
	with open('ok_%s' % file, 'a') as f:
		print(rc, file=f)

for i in range(10):
	x = r[i]
	run(x)
	
