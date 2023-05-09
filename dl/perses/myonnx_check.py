import os
import numpy as np
import mytest as g

DENUM = 1
bug_file = './bug%d' % DENUM
inputs_feed = np.load("%s_inputs.npy" % bug_file, allow_pickle=True)
inputs_feed = inputs_feed.item()
with open(bug_file + '_log.txt') as f:
	error_message = f.read()
	
def check():
	try:
		import myonnx
		model_data = (myonnx.model, inputs_feed, None)
		g.test(model_data, "reduce-test.onnx")
	except Exception as err:
		err_m = str(err)
		# print("sim=", g.similarity(error_message, err_m))
		# print("err=", err_m)
		if 'ONNXRuntimeError' in err_m:
			return False
		if g.similarity(error_message, err_m) >= 0.8:
			os.system("cp reduce-test.onnx %s/ok.onnx" % (os.getcwd()))
			return True
	return False

if check():
	print('0', end="")
else:
	print('1', end="")

