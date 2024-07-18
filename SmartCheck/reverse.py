import random
import binheap_check
import ast
import numpy as np
import time

def size_python(value):
	return len(value)

REPLAY = False

choosed_node = set()

dec_cnt = 0
dec_level = 0
dec_father = 0
dec_rec = []

def clear_dec():
	global dec_cnt
	dec_cnt = 0
	global dec_level
	dec_level = 0
	global dec_father
	dec_father = 0
	global dec_rec
	dec_rec = []

def get_choosed_node():
	global choosed_node
	return choosed_node

def get_dec_rec():
	global dec_rec
	return dec_rec

def dec(*args):
	global dec_cnt
	dec_cnt += 1

	global dec_father
	my_father = 0
	if (args[0] == 1):
		my_father = dec_father
	else:
		dec_father = dec_cnt

	# cur_dec_key = dec_cnt # DD
	cur_dec_key = (my_father, dec_cnt) # HDD

	if not REPLAY:
		dec_rec.append(cur_dec_key) 
		return True
	else:
		return (cur_dec_key in choosed_node)


def gen():
	res = []
	for i in range(random.randint(0, 50)):
		if dec(0):
			res.append(random.randint(-100, 100))
	return res


# res = ('/', 1, ('+', 3, -3))
# print(calculator_check.test(res))

tot_size, tot_ti, tot = 0, 0, 0
totmyt, totspeed = 0, 0

def mycheck(ls):
	try:
		rev = list(reversed(ls))
		assert ls == rev
	except Exception as e:
		# print(e)
		return True
	return False

for i in range(111111111):
	REPLAY = False
	random.seed(i)
	clear_dec()
	res = gen()
	# if size_python(res) > 50:
	# 	continue
	if not mycheck(res):
		continue
		# print(e)
		# print(res)
		# print(dec_rec)

	#print("find=", res)
	s1 = size_python(res)
	# binheap_check.test(res)

	l = [x for x in dec_rec]
	ti = 0
	final = None

	import dd
	def f(ls):
		time.sleep(0.005)
		global ti
		ti += 1
		global choosed_node
		choosed_node = set(ls)
		global REPLAY
		REPLAY = True
		random.seed(i)
		clear_dec()
		res = gen()
		if mycheck(res):
			global final
			final = res
			return True
		return False

	# t = dd._ddmin(l, f)
	st = time.time()
	t = dd._ddmin(l, f)
	ed = time.time()
	totmyt += ed-st


	# print(t)
	tot_ti += ti
	f(t)
	# print("time=", ti)
	#print("final=", final)
	s2 = size_python(final)

	tot_size += size_python(final)
	tot += 1

	totspeed += (s1-s2)/(ed-st)

	if tot >= 1000:
		break

with open('all.txt', 'a') as f:
	print('reverse',file=f)
	print(tot,file=f)
	print(1.0 * tot_size / tot, 1.0 * tot_ti / tot,file=f)
	print(1.0 * totmyt / tot, 1.0 * totspeed / tot,file=f)
