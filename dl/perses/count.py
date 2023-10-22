import onnx
import re

def model_count(model_file):
	model = onnx.load(model_file)
	alln = set()
	edge = 0
	for n in model.graph.node:
		edge += len(n.input) + len(n.output)
		alln |= set(n.input)
		alln |= set(n.output)
	return (len(alln), edge)

def graph_data(m):
	return (len(m.graph.node) + len(m.graph.input) + len(m.graph.output),
		sum([len(x.input) for x in m.graph.node]) + len(m.graph.output))


def count(i):
	ms = model_count('models/bug%d.perses.reduce.onnx' % i)

	with open('models/bug%d.perses.cnt.txt' % i) as f:
		t = len(f.readlines())

	ti = 3600
	with open('models/bug%d.perses.res.txt' % i) as f:
		pp = f.readlines()[-10:]
		for p in pp:
			if ('Elapsed time' in p):
				ti = int(re.findall("is(.+?)seconds", p)[0])

	with open('all.txt', 'a') as f:
		print("Perses", i, ":", "S=", ms, "T=", ti, "P = ", t, file=f)

def mycount():
	for i in range(1, 21):
		count(i)

mycount()



