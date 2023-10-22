import numpy as np
from collections import deque

import settings 

rand_record = []
rand_deque = deque()

choosed_node = set()

dec_cnt = 0
dec_level = 0
dec_father = 0
dec_rec = []


print("seed=", settings.SEED)

np.random.seed(settings.SEED)

REPLAY = False

def getargs():
	return settings.args

def ran(x, y):
	# print("Rand[%d,%d]" % (x, y))
	# return np.random.randint(x, y)
	
	if REPLAY:
		global rand_deque
		r = rand_deque.popleft()
		if x + r >= y:
			raise Exception("REPLAY FAIL!")
		# print("REPLAY=", x, y, x + r)
		return x + r

	r = np.random.randint(x, y)
	global rand_record
	rand_record += [r - x]
	# print("rand=", x, y, r)
	# print("rand_record=", rand_record)
	return r

def ran_ord(l):
	x_ord = np.arange(l)
	for x_index in range(l):
		swap_ind = ran(x_index, l)
		x_ord[x_index], x_ord[swap_ind] = x_ord[swap_ind], x_ord[x_index]
	return x_ord

def ran_ord_b(l):
	c = 2
	if l <= c:
		return ran_ord(l)
	tmp = ran_ord(c)
	return [i + l - c for i in tmp] + list(ran_ord(l - c))

def ran_input(shape):
	# ss = [int(x) for x in shape]
	# t = 1
	# for ess in ss:
	# 	t = t * ess
	# ss_value = []
	# for i in range(t):
	# 	ss_value.append(ran(0, 100) / ran(1, 100))
	# return np.array(ss_value).reshape(shape)
	return np.ones(tuple(shape))
	# return np.random.random(tuple(shape))

def clear_rand():
	global rand_record
	rand_record = []

def clear_dec():
	global dec_cnt
	dec_cnt = 0
	global dec_level
	dec_level = 0
	global dec_father
	dec_father = 0
	global dec_rec
	dec_rec = []

def get_rand_record():
	global rand_record
	return rand_record

def get_choosed_node():
	global choosed_node
	return choosed_node

def get_dec_rec():
	global dec_rec
	return dec_rec


import traceback
def dec(*args):
	global dec_cnt
	dec_cnt += 1

	global dec_father
	my_father = 0
	if (args[1] == 2):
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

