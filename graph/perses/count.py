import json
import sys
import re

for i in range(1, 11):
	t = 'graph-g%d/ok.json' % i
	with open(t) as f:
		d = json.load(f)

	# with open('models/bug%d.perses.cnt.txt' % i) as f:
	# 	t = len(f.readlines())

	ti = 3600
	with open('graph-g%d/res.txt' % i) as f:
		pp = f.readlines()[-10:]
		for p in pp:
			if ('Elapsed time' in p):
				ti = int(re.findall("is(.+?)seconds", p)[0])
			if ('execution count:' in p):
				t = int(p.split("execution count:")[1])


	with open('all.txt', 'a') as f:
		print("Perses", i, ":", "S=", (len(d['nodes']), len(d['edges'])), "T=", ti, "P = ", t, file=f)

	with open('reduced_graphs.txt', 'a') as f:
		print(d['nodes'], [(x['from'], x['to']) for x in d['edges']], file=f)