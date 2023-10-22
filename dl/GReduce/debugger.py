import sys
import json
import time
from collections import deque
import onnx

import gen_random
gen_random.REPLAY = True


DENUM = gen_random.getargs().GN
MODE_D = gen_random.getargs().GMD
MODE_G = gen_random.getargs().GMC

MODE = 'HDD'

if MODE_D == 'S':
	MODE = 'DD'
elif MODE_D == 'T':
	MODE = 'HDD'

if MODE_G == 's3':
	import gl as g
elif MODE_G == 's2':
	import gl_b as g
elif MODE_G == 's1':
	import gl_r as g


bug_file_prefix = 'models/bug%d'

error_message = None

original = None
after_reduce = None
candidates = 0

def graph_data(m):
	return (len(m.graph.node) + len(m.graph.input) + len(m.graph.output),
		sum([len(x.input) for x in m.graph.node]) + len(m.graph.output))

def model_count(model):
	# model = onnx.load(model_file)
	alln = set()
	edge = 0
	for n in model.graph.node:
		edge += len(n.input) + len(n.output)
		alln |= set(n.input)
		alln |= set(n.output)
	return (len(alln), edge)


def propertyTest(model_data):
	global candidates
	candidates += 1

	model, inputs_feed, network_node_num = model_data

	try:
		g.test(model_data, "reduce-test.onnx")
	except Exception as err:
		err_m = str(err)
		print("sim=", g.similarity(error_message, err_m))
		print(err_m)
		if 'ONNXRuntimeError' in err_m:
			return False
		if g.similarity(error_message, err_m) >= 0.8:
			return True
	return False

def graph_reduce():
	global rec_dec_rec
	nl = rec_dec_rec
	def gen_replay(nl):
		global rec_rand_record
		gen_random.rand_deque = deque(rec_rand_record)
		gen_random.choosed_node = set(nl)
		return g.work()

	def criterion(nl):
		if nl == []:
			return False
		try:
			return propertyTest(gen_replay(nl))
		except:
			return False

	import dd
	if MODE == 'DD':
		reduced_nl = dd._ddmin(nl, criterion)
	elif MODE == 'HDD':
		reduced_nl = dd._hddmin(nl, criterion)
	
	print("reduced_nl=", reduced_nl)

	return gen_replay(reduced_nl)


def debug():
	ST_TIME = time.time()
	global bug_file
	bug_file = bug_file_prefix % DENUM

	print("DEBUG for ", bug_file)

	global error_message
	with open(bug_file + '_log.txt') as f:
		error_message = f.read()
	print("bug message=", error_message)

	global candidates
	candidates = 0

	global rec_rand_record
	with open(bug_file + '.onnx_rec.txt', 'r') as f:
		rec_rand_record = json.loads(f.read())
	# print("rand_record=")
	# print(rec_rand_record)
	gen_random.rand_deque = deque(rec_rand_record)


	global rec_dec_rec
	with open(bug_file + '.dec_rec.txt', 'r') as f:
		rec_dec_rec = json.loads(f.read())
	# print("dec_rec=", rec_dec_rec)
	rec_dec_rec = [(x[0], x[1]) for x in rec_dec_rec]
	gen_random.choosed_node = set(rec_dec_rec)

	model, inputs_feed, network_node_num = g.work()
	original = model_count(model)
	#g.test((model, inputs_feed, network_node_num))
	print('----------------------------\n')
	print('----------------------------\n')
	print('----------------------------\n')

	reduced_graph = graph_reduce()

	model, inputs_feed, network_node_num = reduced_graph
	onnx.save(model, bug_file + '.reduce%s%s.onnx' % (MODE_D, MODE_G))
	after_reduce = model_count(model)

	print("---------")
	# print("times = %d" % candidates)
	print(original, '=>', after_reduce)
	with open('all.txt', 'a') as f:
		print(MODE_D, MODE_G, DENUM, ":", "S=", after_reduce, \
			"T= %.6lf" % (time.time() - ST_TIME), \
			"P = %d" % candidates, file=f)

	return reduced_graph



if __name__ == '__main__':

	# if len(sys.argv) > 1:
	# 	MODE_D = str(sys.argv[1])
	# if len(sys.argv) > 2:
	# 	MODE_G = str(sys.argv[2])
	# if len(sys.argv) > 3:
	# 	DENUM = int(sys.argv[3])
	
	debug()
	# for d in range(1, 21):
	# 	DENUM = d
	# 	debug()

	# for d in range(1, 41):
	# 	for m in ['DD', 'HDD']:
	# 		DENUM = d
	# 		MODE = m
	# 		debug()

	
