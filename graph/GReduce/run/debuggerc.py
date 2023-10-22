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
NUM = 2
PRINT_RES = False

if len(sys.argv) > 1:
	if sys.argv[1] == 'T':
		ALGO = 'HDD'
	else:
		ALGO = 'DD'

if len(sys.argv) > 2:
	if sys.argv[2] == 's3':
		jar1 = "g-%dA-a.jar"
		jar2 = "g-%dB-a.jar"
	elif sys.argv[2] == 's2':
		jar1 = "g-%dA-b.jar"
		jar2 = "g-%dB-b.jar"
	elif sys.argv[2] == 's1':
		jar1 = "g-%dA-r.jar"
		jar2 = "g-%dB-r.jar"


if len(sys.argv) > 3:
	NUM = int(sys.argv[3])

jar1 = jar1 % NUM
jar2 = jar2 % NUM

FINAL_OUT = None


def genAndTest(data):
	global generator_cnt
	generator_cnt += 1

	with open(tmpdata, 'w') as f:
		f.write(data)
	
	if data != "first":
		data = "file"

	runc = 'java -jar %s %s 2>&1' % (jar1, data)
	r = os.popen(runc)
	out1 = r.read()
	r.close()
	# print(out1)

	runc = 'java -jar %s %s 2>&1' % (jar2, data)
	r = os.popen(runc)
	out2 = r.read()
	r.close()
	# print(out2)

	# print("----------------------------[out]----------------------------")
	# print(out1)

	if ('edu.berkeley.cs.jqf.examples.MainTest.genGraph' in out1) or ('edu.berkeley.cs.jqf.examples.MainTest.genGraph' in out2):
		return False

	if 'GReduce-duplicate.' not in out1:
		global proptest_cnt
		proptest_cnt += 1

		if len(out1) > 0:
			if data == "first":
				out1 = "\n".join(out1.splitlines()[1:])

			with open(testres_file, 'a') as f:
				code = out1.splitlines()[0]
				other = out1.splitlines()[1:]
				print(code, file=f)
				print("\t".join(other), file=f)

		if len(out2) > 0:
			if data == "first":
				out2 = "\n".join(out2.splitlines()[1:])

			with open(testres_file, 'a') as f:
				code = out2.splitlines()[0]
				other = out2.splitlines()[1:]
				print(code, file=f)
				print("\t".join(other), file=f)

	out1 = out1[1:]
	out2 = out2[1:]
	res = (out1 != out2)

	# print("out1:", out1)
	# print("out2:", out2)
	# print("res:", res, len(out1), len(out2))
	
	if res:
		global FINAL_OUT
		FINAL_OUT = out1.splitlines()[0]
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

