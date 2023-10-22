import os
import sys
import json
from collections import deque
import time


generator_cnt = 0
out_set = []

proptest_cnt = 0
all_testmessage = set()

local = "" # user-defined
jar = None


tmpdata = local + "tmpdata.txt"
testres_file = local + "testres.txt"
bugdec = local + "bug.dec_rec.txt"

with open(testres_file, 'w') as f:
	pass
with open(bugdec, 'w') as f:
	pass


ALGO = "HDD"
NUM = 1
PRINT_RES = False

if len(sys.argv) > 1:
	if sys.argv[1] == 'T':
		ALGO = 'HDD'
	else:
		ALGO = 'DD'

if len(sys.argv) > 2:
	if sys.argv[2] == 's3':
		jar = "g-%d-a.jar"
	elif sys.argv[2] == 's2':
		jar = "g-%d-b.jar"
	elif sys.argv[2] == 's1':
		jar = "g-%d-r.jar"

if len(sys.argv) > 3:
	NUM = int(sys.argv[3])

jar = jar % NUM

FINAL_OUT = None


def genAndTest(data):
	global generator_cnt
	generator_cnt += 1

	with open(tmpdata, 'w') as f:
		f.write(data)
	
	if data != "first":
		data = "file"

	runc = 'java -jar %s %s 2>&1' % (jar, data)
	# print(runc)

	r = os.popen(runc)
	out = r.read()
	r.close()

	# print("----------------------------[out]----------------------------")
	if 'edu.berkeley.cs.jqf.examples.MainTest.genGraph' in out:
		return False
	
	if 'GReduce-duplicate.' not in out:
		print(out)
		# print(count(out.splitlines()[1]))

		global proptest_cnt
		proptest_cnt += 1

		if len(out) > 0:
			with open(testres_file, 'a') as f:
				if data == "first":
					out = "\n".join(out.splitlines()[1:])
				code = out.splitlines()[0]
				other = out.splitlines()[1:]
				print(code, file=f)
				print("\t".join(other), file=f)

	res = ('true' in out)
	if res:
		global FINAL_OUT
		FINAL_OUT = out.splitlines()[0]
	return res

def reduce(nl):

	def gen_replay(nl):
		if len(nl[0]) == 1:
			res = ",".join([str(x) for x in nl])
		else:
			res = ",".join(['%d-%d' % (x[0], x[1]) for x in nl])
		return res

	tried_nl = {}

	def criterion(nl):
		# print("try NL=", nl)
		if nl == []:
			return False
		if tried_nl.get(str(nl)) != None:
			return tried_nl[str(nl)]
		res = genAndTest(gen_replay(nl))
		tried_nl[str(nl)] = res
		return res

	import dd

	if ALGO == 'DD':
		reduced_nl = dd._ddmin(nl, criterion)
	elif ALGO == 'HDD':
		reduced_nl = dd._hddmin(nl, criterion)	


def reduce_graph():
	st_time = time.time() 
	genAndTest("first")

	with open(bugdec) as f:
		s = f.read()
	def parseInput(s):
		sarr = s.replace("\n", "").replace(" ", "").replace("-", "=").split(",")
		res = []
		for x in sarr:
			if '=' in x:
				xp = x.replace("[","").replace("]", "").split("=")
			res.append((int(xp[0]),int(xp[1])))
		return res
	
	reduce(parseInput(s))

	global FINAL_OUT
	global proptest_cnt

	nn = FINAL_OUT.split(']')[0]
	n = nn.count(',') + 1
	mm = FINAL_OUT.split(']')[1]
	m = mm.count('{') + mm.count('(')

	print("The result writes into all.txt.")
	with open("all.txt", 'a') as f:
		print(" ".join(sys.argv), ":", "S=", (n, m), "T=", time.time() - st_time, "P=", proptest_cnt, file=f)
		if PRINT_RES:
			print('---------------')
			print(FINAL_OUT, file = f)
			print('---------------')

	with open("graph%d.txt" % NUM, 'w') as f:
		print(FINAL_OUT, file = f)


if __name__ == '__main__':		
	reduce_graph()

