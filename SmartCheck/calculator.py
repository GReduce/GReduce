import random
import calculator_check
import ast
import time


def size_python(value):
    def w(x):
        if isinstance(x, tuple):
            return w(x[1]) + w(x[2]) + 1
        else:
            return 1
    return w(value)


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
	x = random.randint(0, 80)
	y = random.randint(0, 1)
	if x > 1:
		if random.randint(0, 100) < 10:
			return random.randint(-10, 10)
		else:
			return random.randint(-1, 1)
	f2 = dec(0)
	f3 = dec(0)
	a = gen()
	b = gen()
	
	if f2 and f3:
		res = ('+' if y == 0 else '/', a, b)
	else:
		if (not f2) and (not f3):
			res = 0
		elif f2:
			res = a
		else:
			res = b
	return res

# res = ('/', 1, ('+', 3, -3))
# print(calculator_check.test(res))

tot_size, tot_ti, tot = 0, 0, 0
totmyt, totspeed = 0, 0

for i in range(111111111):
	REPLAY = False
	random.seed(i)
	clear_dec()
	res = gen()
	# if size_python(res) > 50:
	# 	continue

	#print(res)
	try:
		calculator_check.test(res)
	except Exception as e:
		# print(e)
		# print(res)
		# print(dec_rec)
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
			res = gen()
			try:
				calculator_check.test(res)
			except Exception as e:
				# print(res, size_python(res))
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
		totspeed += (s1-s2)/(ed-st)
		# if s2 > 5:
		# 	print(l)
		# 	print(t)
		# 	print(res)
		# 	print(final)
		# 	break
		print(tot, 1.0 * tot_size / tot)
		if tot >= 1000:
			break

with open('all.txt', 'a') as f:
	print('calculator',file=f)
	print(tot,file=f)
	print(1.0 * tot_size / tot, 1.0 * tot_ti / tot,file=f)
	print(1.0 * totmyt / tot, 1.0 * totspeed / tot,file=f)
