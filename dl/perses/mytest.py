import numpy as np
import onnx
import onnxruntime as rt
rt.set_default_logger_severity(3)

TEST_TVM = True

def test(model_data, model_saved_file="tmp.onnx"):
	# print("test for ", model_saved_file)

	model, inputs_feed, network_node_num = model_data
	# # print('The graph in model:\n{}'.format(model.graph))
	if len(model.graph.output) == 0:
		raise Exception("model without output!")

	filename = model_saved_file
	onnx.save(model, filename)

	# TEST_ONNXRT:
	np.save("inputs.npy", inputs_feed)
	sess = rt.InferenceSession(filename)
	output_name = sess.get_outputs()[0].name
	onnxrt_out = sess.run([output_name], inputs_feed)
	# print('onnx runtime finish normally!')

	# # print('out=', out)

	tvm_out = {}
	from run_tvm import run_tvm
	if TEST_TVM:
		# i = 3
		# tvm_out[i] = run_tvm(model, inputs_feed, i)
		for i in range(0, 4):
			tvm_out[i] = run_tvm(model, inputs_feed, i)

	# differential testing
	fix_dec = 1
	out = np.around(onnxrt_out, decimals=fix_dec)

	for i in tvm_out.keys():
		tvm_ver = 'tvm_with_opt_%d' % i
		out_deploy = np.around(tvm_out[i], decimals=fix_dec)

		if np.isnan(out).any() or np.isnan(out_deploy).any():
			return
		
		# assert((out == out_deploy).all())
		res = (out == out_deploy)
		# assert(np.sum(res==False) < 10)
		res = np.array(res)

		if not (np.sum(res==True) >= res.size * 0.9):
			# print("out=", out)
			# print("tvm_out=", out_deploy)
			raise Exception("differential_testing: different results on onnxrt and %s!" % tvm_ver)


from difflib import SequenceMatcher
def similarity(a, b):
	return SequenceMatcher(None, a, b).ratio()
