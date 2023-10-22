seeds = [0, 28725, 99408, 6572, 6750, 109591, 52596, 136141, 110129, 136672, 142490]
def oracle(cases, s):
	if cases == 1:
		return 'INDEX' in s
	if cases == 2:
		return s.count('UNREACH') >= 4
	if cases == 3:
		return s.count('NaN') >= 1
	if cases == 4:
		return s.count('k_4') >= 1
	if cases == 5:
		return s.count('UNREACH') >= 2
	if cases == 6:
		return (s.count('UNREACH') >= 1) and (s.count('NEGATING') >= 1)
	if cases == 7:
		return s.count('undefined') >= 1
	if cases == 8:
		return (s.count('NEGATING') >= 1)
	if cases == 9:
		return s.count('x_7') >= 1
	if cases == 10:
		return s.count('i_26') >= 1

	return False
