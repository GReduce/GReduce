import random
import binheap_check
import ast
import time

def size_python(value):
    def w(x):
        if x is None:
            return 1
        return w(x[1]) + w(x[2]) + 1
    return w(value)


REPLAY = False

choosed_node = set()

dec_cnt = 0
dec_level = 0
dec_father = 0
dec_rec = []
level = 0
dec_fa_level = {}

def clear_dec():
	global dec_cnt
	dec_cnt = 0
	global dec_level
	dec_level = 0
	global dec_father
	dec_father = 0
	global dec_rec
	dec_rec = []
	global level
	level = 0
	global dec_fa_level
	dec_fa_level = {}

def down():
	global level
	level += 1

def up():
	global level
	level -= 1

def get_choosed_node():
	global choosed_node
	return choosed_node

def get_dec_rec():
	global dec_rec
	return dec_rec

def dec():
	global dec_cnt
	dec_cnt += 1

	global dec_father
	my_father = 0
	if (level - 1) in dec_fa_level:
		my_father = dec_fa_level[level - 1]
	dec_fa_level[level] = dec_cnt

	# cur_dec_key = dec_cnt # DD
	cur_dec_key = (my_father, dec_cnt) # HDD

	if not REPLAY:
		dec_rec.append(cur_dec_key) 
		return True
	else:
		return (cur_dec_key in choosed_node)



def gen(s, limit):
	if (limit <= 0) or (s <= 0):
		return None
	if random.randint(0, 50) >= s * s:
		return None
	
	#f0 = dec()
	down()
	x = random.randint(0, limit)
	p = random.randint(0, (s - 1) // 2)
	# p = (s - 1) // 2
	# z = 0
	# for i in range(p):
	# 	f = dec(0)
	# 	if f:
	# 		z += 1
	z = p
	f1 = dec()
	L = gen(z, x)

	f2 = dec()
	R = gen(z, x)

	# if not f0:
	# 	return None
	
	if f1 and f2:
		return (-x, L, R) 
	else:
		if (not f1) and (not f2):
			return None
		else:
			if f1:
				return L
			else:
				return R
	up()

# res = ('/', 1, ('+', 3, -3))
# print(calculator_check.test(res))

tot_size, tot_ti, tot = 0, 0, 0
totmyt, totspeed = 0, 0

def mycheck(res):
	try:
		binheap_check.test(res)
	except Exception as e:
		# print(e)
		return True
	return False

for i in range(11111111111):
	REPLAY = False
	random.seed(i)
	clear_dec()
	res = gen(8, 8)
	# if size_python(res) > 50:
	# 	continue
	if not mycheck(res):
		continue
		# print(e)
		# print(res)
		# print(dec_rec)

	# print("find=", res)
	# binheap_check.test(res)
	s1 = size_python(res)

	l = [x for x in dec_rec]
	ti = 0
	final = None

	import dd
	def f(ls):
		time.sleep(0.001)
		global ti
		ti += 1
		global choosed_node
		choosed_node = set(ls)
		global REPLAY
		REPLAY = True
		random.seed(i)
		clear_dec()
		res = gen(8, 8)
		if mycheck(res):
			global final
			final = res
			return True
		return False

	# t = dd._ddmin(l, f)
	st = time.time()
	t = dd._hddmin(l, f)
	ed = time.time()
	totmyt += ed-st

	# print(t)
	tot_ti += ti
	f(t)
	# print("time=", ti)
	# print(final)
	tot_size += size_python(final)
	tot += 1
	s2 = size_python(final)
	# if s2 > 9:
	# 	print(res)
	# 	print(final)
	totspeed += (s1-s2)/(ed-st)

	print(tot, 1.0 * tot_size / tot)
	if tot >= 1000:
		break

with open('all.txt', 'a') as f:
	print('binheap',file=f)
	print(tot,file=f)
	print(1.0 * tot_size / tot, 1.0 * tot_ti / tot,file=f)
	print(1.0 * totmyt / tot, 1.0 * totspeed / tot,file=f)

