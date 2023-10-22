import os
import collections
import time
import numpy as np
import collections
from collections import deque
import json

import onnx
from onnx import helper
from onnx import AttributeProto, TensorProto, GraphProto
import onnxruntime as rt
rt.set_default_logger_severity(3)

# import criterion
from settings import *
import gen_random


error_num = 0
error_config = None
err_message_set = set()
crash_num = 0

graph_num = 0

def work():	
	tensor_list = []
	tensor_map = {}
	tensor_init = {}
	tensor_init_type = {}
	node_list = []
	input_tensor = []
	inputs_feed = {}
	output_tensor = []
	init_tensor = []
	pure_value_tensor = set()
	no_succ = set()

	if PRINT_ONNX:
		with open('./myonnx.py', 'w'):
			pass
		FILE_AS_ONNX_CODE = open('./myonnx.py', 'a')
		print("from onnx import helper\ninput_tensor = []\noutput_tensor = []\ninit_tensor = []\nnode_list = []\n", file=FILE_AS_ONNX_CODE)

	from gen_random import ran, ran_input, ran_ord, dec, ran_ord_b
	gen_random.clear_dec()
	if not gen_random.REPLAY:
		gen_random.clear_rand()

	# print('start G!!!!!!!!!!!!!')
	# print("REPLAY=", gen_random.REPLAY)

	network_node_num = ran(MIN_NODE, MAX_NODE + 1)

	ops_seq = None

	global global_tensor_num
	global_tensor_num = 0

	def rand_shape():
		fixed_dim = ran(MIN_TENSOR_DIM, MAX_TENSOR_DIM + 1)
		fixed_shape = [ran(1, MAX_TENSOR_DIM_LEN + 1) for i in range(fixed_dim)]
		return fixed_shape

	def newOrReuse(shape, withF=None):
		if ran(0, 100000) < 100000 * pickExistRate:
			if withF is None:
				t = match(shape)
			else:
				t = matchWithF(withF)
			if t is not None:
				return t
		if withF is not None:
			lc = list(filter(withF, [i for i in range(MIN_TENSOR_DIM, MAX_TENSOR_DIM + 1)]))
			if len(lc) == 0:
				raise Exception("can not generate shape for this operation %s" % new_node_type)
			l = lc[ran(0, len(lc))]
			shape = [-1 for i in range(l)]

		for i in range(len(shape)):
			if shape[i] == -1:
				shape[i] = ran(1, MAX_TENSOR_DIM_LEN + 1)
		ret = new_tensor(shape)
		pass_value(ret, False)
		return ret

	def new_tensor(shape, data_type=TensorProto.FLOAT, data_value=None):
		global global_tensor_num
		global_tensor_num += 1
		cur_name = 'node' + str(global_tensor_num)
		# print(cur_name, data_type, shape)

		if PRINT_ONNX:
			print("%s = helper.make_tensor_value_info('%s', %s, %s)" % (cur_name, cur_name, data_type, shape), file=FILE_AS_ONNX_CODE)

		cur_tensor = helper.make_tensor_value_info(cur_name, data_type, shape)
		if (data_value is None) and (-1 not in shape):
			if data_type == TensorProto.FLOAT:
				# cur_value = np.random.random(tuple(shape))
				cur_value = ran_input(shape)
				cur_value = cur_value * 2 - 1
				cur_value = cur_value.astype(np.float32)
		else:
			cur_value = data_value
		tensor_list.append(cur_name)
		tensor_map[cur_name] = cur_tensor
		tensor_init[cur_name] = cur_value
		tensor_init_type[cur_name] = data_type
		return cur_name

	def tensor_shape(t_name):
		return list(tensor_init[t_name].shape)

	def pass_value(t, given_value=True):
		pure_value_tensor.add(t)
		t_value = tensor_init[t]
		t_type = tensor_init_type[t]
		t = tensor_map[t]

		if NO_INPUT or given_value:
			if PRINT_ONNX:
				print("init_tensor.append(helper.make_tensor('%s', %s, dims=%s, vals=%s))" % (t.name, t_type, t_value.shape, list(t_value.flatten())), file=FILE_AS_ONNX_CODE)
			init_tensor.append(helper.make_tensor(t.name, t_type, dims=t_value.shape, vals=t_value.flatten()))
		else:
			input_tensor.append(t)
			inputs_feed[t.name] = t_value
			no_succ.add(t.name)

	first_n = new_tensor(rand_shape())
	pass_value(first_n, False)

	dq = []
	dq.append(first_n)

	def match(partial_shape):
		dq_l = len(dq)		
		if ran(0, 30) > 0:
			x_ord = ran_ord_b(dq_l)
		else:
			x_ord = ran_ord(dq_l)
		for x_index in x_ord:
			x = dq[x_index]
			x_shape = tensor_shape(x)
			x_shape_l = len(x_shape)
			if x_shape_l == len(partial_shape):
				matched = True
				for i in range(x_shape_l):
					if (partial_shape[i] > 0) and (partial_shape[i] != x_shape[i]):
						matched = False
						break
				if matched:
					return x
		return None

	def matchWithF(f):
		dq_l = len(dq)
		if ran(0, 30) > 0:
			x_ord = ran_ord_b(dq_l)
		else:
			x_ord = ran_ord(dq_l)
		for x_index in x_ord:
			x = dq[x_index]
			x_shape = tensor_shape(x)
			x_shape_l = len(x_shape)
			if f(x_shape_l):
				return x
		return None

	for step in range(network_node_num):
		this_op_dec = dec(step, 1)

		v = ran(0, len(ops))
		new_node_type = ops[v]

		# new_node_type = unlikely_bug_ops[ran(0, len(unlikely_bug_ops))]
		# if ran(0, 100) == 0:
		# 	new_node_type = tvm_buggy_ops[ran(0, len(tvm_buggy_ops))]


		if ops_seq != None:
			new_node_type = ops_seq[step % len(ops_seq)]
		node_name = 'op' + str(step)
		kwargs = {}

		op_filter = FILTER_DICT[new_node_type]
		n1 = newOrReuse([], op_filter)
		n1_shape = tensor_shape(n1)
		n1_dim = len(n1_shape)				

		out_shape = tensor_shape(n1)

		real_inputs = None
		real_outputs = None

		if new_node_type in ['Softmax', 'LpNormalization', 'Concat', 'Compress', 'Flatten']:
			kwargs['axis'] = ran(0, len(tensor_shape(n1)))
		if new_node_type in reduce_ops:
			if new_node_type != 'ReduceSum':
				kwargs['axes'] = ran_ord(n1_dim)[:ran(1, n1_dim + 1)]

		if new_node_type == 'SpaceToDepth':
			def gcd(a, b):
				return (a if b == 0 else gcd(b, a % b)) 
			t = gcd(n1_shape[2], n1_shape[3])
			# TODO(generate factor of t)
			kwargs['blocksize'] = t
			out_shape[1] = n1_shape[1] * t * t
			out_shape[2] = out_shape[2] // t
			out_shape[3] = out_shape[3] // t

		if new_node_type in ['MaxPool', 'AveragePool', 'LpPool']:
			kwargs['kernel_shape'] = [ran(1, n1_shape[i + 2] + 1) for i in range(n1_dim - 2)]
			kwargs['strides'] = [ran(1, n1_shape[i + 2] + 1) for i in range(n1_dim - 2)]
			for i in range(n1_dim - 2):
				out_shape[i + 2] = (out_shape[i + 2] - kwargs['kernel_shape'][i]) // kwargs['strides'][i] + 1
		
		if new_node_type in ['Conv', 'ConvTranspose']:
			kwargs['kernel_shape'] = [ran(1, n1_shape[i + 2] + 1) for i in range(n1_dim - 2)]	
			kwargs['strides'] = [ran(1, n1_shape[i + 2] + 1) for i in range(n1_dim - 2)]
			kwargs['pads'] = [0 for i in range((n1_dim - 2) * 2)]
			if ran(0, 2) == 0:
				kwargs['group'] = 1
			# kwargs['auto_pad'] = 'SAME_LOWER'
			if new_node_type == 'Conv':
				for i in range(n1_dim - 2):
					out_shape[i + 2] = (n1_shape[i + 2] - kwargs['kernel_shape'][i] + kwargs['pads'][i * 2] + kwargs['pads'][i * 2 + 1]) // kwargs['strides'][i] + 1
			else:
				for i in range(n1_dim - 2):
					out_shape[i + 2] = (n1_shape[i + 2] - 1) * kwargs['strides'][i] + ((kwargs['kernel_shape'][i] - 1) + 1)

		if new_node_type in ['LpPool', 'LpNormalization']:
			if ran(0, 2) == 1:
				p_value = ran(1, 3)
				if dec(step, 2):
					kwargs['p'] = p_value
		if new_node_type in ['LeakyRelu']:
			if ran(0, 2) == 1:
				alpha_value = ran(1, 3) * 0.01
				if dec(step, 2):
					kwargs['alpha'] = alpha_value

		if new_node_type in ['Elu', 'ThresholdedRelu']:
			if ran(0, 2) == 1:
				alpha_value = 1.0 * ran(1, 3) / ran(1, 3)
				if dec(step, 2):
					kwargs['alpha'] = alpha_value
		if new_node_type == 'Transpose':
			x_ord = [(n1_dim - i - 1) for i in range(n1_dim)]
			if ran(0, 5) > 0:
				x_ord = ran_ord(n1_dim)
				kwargs['perm'] = x_ord
			for i in range(n1_dim):
				out_shape[i] = n1_shape[x_ord[i]]

		if new_node_type == 'Split':
			ax = 0
			if ran(0, 2) > 0:
				axis_value = ran(0, n1_dim)
				ax = kwargs['axis'] = axis_value
			split_sum = n1_shape[ax]
			split_t = []

			nums_output = min(split_sum, ran(2, MAX_MULTI_OUTPUTS + 1))
			# if (split_sum % nums_output == 0) and (ran(0, 2) == 0):
			# 	inputs = [n1]
			# 	for i in range(nums_output):
			# 		split_t.append(split_sum // nums_output)
			# else:
			rest_sum = split_sum - nums_output
			rand_split = sorted([ran(0, rest_sum + 1) for i in range(nums_output - 1)])			
			for i in range(nums_output - 1):
				split_t.append((rand_split[0] if i == 0 else (rand_split[i] - rand_split[i - 1])) + 1)
						
			cur_dec = []
			for i in range(nums_output - 1):
				cur_dec.append(dec(step, 2))

			real_output_num = 0
			real_split_t = []

			outputs = []
			real_outputs = []
			for i in range(nums_output):
				out_n_shape = tensor_shape(n1)				
				out_n_shape[ax] = split_t[i] if i < nums_output - 1 else (split_sum - sum(split_t))
				out_n = new_tensor(out_n_shape)
				outputs.append(out_n)
				if i < nums_output - 1:
					if cur_dec[i]:
						real_split_t.append(split_t[i])
						real_outputs.append(out_n)
				else:
					new_out_n_shape_ax = split_sum - sum(real_split_t)
					if (new_out_n_shape_ax != out_n_shape[ax]):
						out_n_shape[ax] = new_out_n_shape_ax
						out_n = new_tensor(out_n_shape)

					real_split_t.append(out_n_shape[ax])
					real_outputs.append(out_n)
			
			n2 = new_tensor([len(real_split_t)], TensorProto.INT64, np.array(real_split_t))
			pass_value(n2)
			inputs = [n1, n2]
		elif new_node_type in ['GlobalMaxPool', 'GlobalAveragePool']:
			inputs = [n1]
			out_shape = n1_shape
			for i in range(2, n1_dim):
				out_shape[i] = 1
		elif new_node_type == 'Size':
			inputs = [n1]
			tot_c = 1
			for i in range(n1_dim):
				tot_c = tot_c * n1_shape[i]
			out_shape = [tot_c]
		elif new_node_type == 'ReduceSum':
			n2_dim = 1
			n2_value = ran_ord(n1_dim)[:ran(1, n1_dim + 1)]
			n2_shape = [len(n2_value)]
			n2 = new_tensor(n2_shape, TensorProto.INT64, np.array(n2_value))
			pass_value(n2)
			out_shape = n1_shape
			for x in n2_value:
				out_shape[x] = 1
			inputs = [n1, n2]
		elif new_node_type == 'Tile':
			n2_dim = 1
			n2_shape = [n1_dim]
			tile_value = [ran(1, 4) for i in range(n1_dim)]
			n2 = new_tensor(n2_shape, TensorProto.INT64, np.array(tile_value))
			pass_value(n2)
			out_shape = [tile_value[i] * n1_shape[i] for i in range(n1_dim)]
			# print('Tile:', n1_shape, tile_value, out_shape)
			inputs = [n1, n2]
		elif new_node_type == 'Gather':
			ax = 0
			if ran(0, 10) > 0:
				ax_value = ran(0, n1_dim)
				ax = kwargs['axis'] = ax_value
			indices_dim = ran(1, MAX_TENSOR_DIM - n1_dim + 2)
			indices_shape = []
			tot_c = 1
			for i in range(indices_dim):
				if ran(0, 2) > 0:
					indices_shape_value = ran(1, MAX_TENSOR_DIM_LEN + 1)
					indices_shape.append(indices_shape_value)
				else:
					indices_shape.append(1)
				tot_c = tot_c * indices_shape[i]
			all_indices = [ran(0, n1_shape[ax]) for i in range(tot_c)]
			# TODO(support with negative indices)
			indices_value = np.array(all_indices).reshape(indices_shape)

			indices = new_tensor(indices_shape, TensorProto.INT64, np.array(indices_value))
			pass_value(indices)

			out_shape = n1_shape[:ax] + indices_shape + n1_shape[ax+1:]
			inputs = [n1, indices]
		elif new_node_type == 'Slice':
			starts_shape = [n1_dim]
			starts_value = [ran(0, n1_shape[i]) for i in range(n1_dim)]
			ends_shape = [n1_dim]
			ends_value = [starts_value[i] + ran(0, n1_shape[i] - starts_value[i]) + 1 for i in range(n1_dim)]
			axes_shape = [n1_dim]
			axes_value = [i for i in range(n1_dim)]
			steps_shape = [n1_dim]
			steps_value = [ran(1, 4) for i in range(n1_dim)]
			# TODO(negtive steps)
			# for i in range(n1_dim):
			# 	if steps_value[i] < 0:
			# 		starts_value[i], ends_value[i] = ends_value[i], starts_value[i]

			starts = new_tensor(starts_shape, TensorProto.INT64, np.array(starts_value))
			pass_value(starts)
			ends = new_tensor(ends_shape, TensorProto.INT64, np.array(ends_value))
			pass_value(ends)
			axes = new_tensor(axes_shape, TensorProto.INT64, np.array(axes_value))
			pass_value(axes)
			steps = new_tensor(steps_shape, TensorProto.INT64, np.array(steps_value))
			pass_value(steps)
			
			out_shape = [((ends_value[i] - starts_value[i] - 1) // steps_value[i] + 1) for i in range(n1_dim)]
			
			inputs = [n1, starts, ends, axes, steps]
			# print(n1_shape, starts_value, ends_value, steps_value, out_shape)
		elif new_node_type == 'Resize':
			scales_dim = 1
			scales_shape = [n1_dim]
			scales = new_tensor(scales_shape, TensorProto.FLOAT, np.array([1.0 for i in range(n1_dim)]))
			pass_value(scales)

			roi_dim = 1
			roi_shape = [2 * n1_dim]
			roi_value = []
			for i in range(n1_dim):
				roi_value.append(0)
			for i in range(n1_dim):
				roi_value.append(1)
			roi = new_tensor(roi_shape, TensorProto.FLOAT, np.array([roi_value]))
			pass_value(roi)

			out_shape = n1_shape

			kwargs['mode'] = 'nearest'
			inputs = [n1, roi, scales]
		elif new_node_type == 'Reshape':
			def gcd(a, b):
				return (a if b == 0 else gcd(b, a % b)) 
			t = 1
			for i in range(n1_dim):
				t = t * n1_shape[i]
			new_dim = ran(1, MAX_TENSOR_DIM + 1)
			reshape_shape = []
			for i in range(new_dim - 1):
				t2 = gcd(t, ran(1, t + 1))
				t = t // t2
				reshape_shape.append(t2)
			reshape_shape.append(t)

			n2_dim = 1
			n2_shape = [new_dim]
			n2 = new_tensor(n2_shape, TensorProto.INT64, np.array(reshape_shape))
			pass_value(n2)
			out_shape = reshape_shape

			inputs = [n1, n2]
		elif new_node_type == 'Unsqueeze':
			expanded_dim = n1_dim + ran(1, MAX_TENSOR_DIM - n1_dim + 1)
			x_ord = ran_ord(expanded_dim)
			n2_dim = 1
			n2_shape = [expanded_dim - n1_dim]
			n2_value = []
			for i in range(expanded_dim - n1_dim):
				n2_value.append(x_ord[i])
			n2_value = sorted(n2_value)
			n2 = new_tensor(n2_shape, TensorProto.INT64, np.array(n2_value))
			pass_value(n2)

			out_shape = []
			ori_cnt = 0
			for i in range(expanded_dim):
				if i in n2_value:
					out_shape.append(1)
				else:
					out_shape.append(n1_shape[ori_cnt])
					ori_cnt += 1

			inputs = [n1, n2]
		elif new_node_type == 'Expand':
			n2_dim = 1
			new_dim = n1_dim + ran(0, MAX_TENSOR_DIM - n1_dim + 1)
			new_dim = n1_dim 
			n2_shape = [new_dim]
			expand_shape = [n1_shape[i] for i in range(n1_dim)]
			for i in range(new_dim - n1_dim):
				expand_shape = [1] + expand_shape
			saved_shape = [expand_shape[i] for i in range(new_dim)]
			for i in range(new_dim):
				if expand_shape[i] == 1:
					if ran(0, 2) == 0:
						expand_shape[i] = ran(2, 5)
				else:
					expand_shape[i] = 1

			n2 = new_tensor(n2_shape, TensorProto.INT64, np.array(expand_shape))
			pass_value(n2)
			out_shape = [max(saved_shape[i], expand_shape[i]) for i in range(new_dim)]
			inputs = [n1, n2]
		elif new_node_type == 'Pad':
			pads_value = []
			kwargs['mode'] = 'constant'
			# if ran(0, 2) > 0:
			# 	kwargs['constant_value'] = ran(0, 10) 
			for i in range(n1_dim):
				pad_n = ran(0, 3)
				pads_value += [pad_n]
				out_shape[i] += pad_n
			for i in range(n1_dim):
				pad_n = ran(0, 3)
				pads_value += [pad_n]
				out_shape[i] += pad_n
			pads = new_tensor([2 * n1_dim], TensorProto.INT64, np.array(pads_value))
			pass_value(pads)

			inputs = [n1, pads]
		elif new_node_type == 'BatchNormalization':
			c_dim_len = n1_shape[1]
			s = newOrReuse([c_dim_len])
			bias = newOrReuse([c_dim_len])
			mean = newOrReuse([c_dim_len])
			var = newOrReuse([c_dim_len])
			inputs = [n1, s, bias, mean, var]
		elif new_node_type == 'Compress':
			l = n1_shape[kwargs['axis']]
			n2_dim = 1
			n2_shape = [l]

			compress_shape = [ran(0, 2) for i in range(l)]
			compress_sum = int(sum(compress_shape))
			if compress_sum == 0:
				compress_shape[ran(0, l)] = 1
				compress_sum = 1
				
			n2 = new_tensor(n2_shape, TensorProto.BOOL, np.array(compress_shape))
			pass_value(n2)
			out_shape[kwargs['axis']] = compress_sum
			inputs = [n1, n2]
		elif new_node_type in extra_t_ops:
			n2_shape = tensor_shape(n1)
			n2_dim = len(n2_shape)

			if new_node_type == 'Conv':
				# TODO(change n2_shape[0, 1])
				n2_shape[0] = n1_shape[0]
				group = 1
				if 'group' in kwargs:
					group = kwargs['group']
				n2_shape[1] = n1_shape[1] // group
				for i in range(n1_dim - 2):
					n2_shape[2 + i] = kwargs['kernel_shape'][i]
				out_shape[1] = n2_shape[0]

			if new_node_type == 'ConvTranspose':
				n2_shape[0] = n1_shape[1]
				group = 1
				if 'group' in kwargs:
					group = kwargs['group']
				n2_shape[1] = 1
				for i in range(n1_dim - 2):
					n2_shape[2 + i] = kwargs['kernel_shape'][i]
				out_shape[0] = n1_shape[0]
				out_shape[1] = n2_shape[1]

			if new_node_type in ['MatMul', 'Gemm']:
				n2_shape[n2_dim - 2] = n2_shape[n2_dim - 1]
				n2_shape[n2_dim - 1] = -1

			if new_node_type == 'Concat':
				n2_shape[kwargs['axis']] = ran(1, MAX_TENSOR_DIM_LEN + 1)
				out_shape[kwargs['axis']] = n1_shape[kwargs['axis']] + n2_shape[kwargs['axis']]

			n2 = newOrReuse(n2_shape)
			inputs = [n1, n2]

			# if new_node_type == 'Gemm':
			# 	n2_2 = newOrReuse(out_shape)
			# 	if ran(0, 2) == 0:
			# 		inputs.append(n2_2)
		else:
			if new_node_type in reduce_ops:
				if new_node_type != 'ReduceSum':
					for x in kwargs['axes']:
						out_shape[x] = 1
			if new_node_type == 'Flatten':
				# kwargs['axis'] = 0
				d = kwargs['axis']
				p1 = 1
				p2 = 1
				out_shape = []
				for i in range(n1_dim):
					if i < d:
						p1 = p1 * n1_shape[i]
					else:
						p2 = p2 * n1_shape[i]
				out_shape = [p1, p2]
			inputs = [n1]

		if new_node_type in multi_extra_t_ops:
			extra_num = ran(0, MAX_MULTI_INPUTS - 1)
			real_inputs = [x for x in inputs]
			for t in range(extra_num):
				n_another = newOrReuse(tensor_shape(n1))	
				inputs.append(n_another)
				if dec(step, 2):
					real_inputs.append(n_another)

		if new_node_type == "Concat":
			extra_num = ran(0, MAX_MULTI_INPUTS - 1)
			real_inputs = [x for x in inputs]
			real_output_shape = [int(x) for x in out_shape]
			for t in range(extra_num):
				n_another_shape = tensor_shape(n1)
				# print(n1, "another=", n_another_shape)
				n_another_shape[kwargs['axis']] = ran(1, MAX_TENSOR_DIM_LEN + 1)
				n_another = newOrReuse(n_another_shape)
				inputs.append(n_another)
				out_shape[kwargs['axis']] += n_another_shape[kwargs['axis']]
				if dec(step, 2):
					real_inputs.append(n_another)
					real_output_shape[kwargs['axis']] += n_another_shape[kwargs['axis']]

			out_tensor = new_tensor(out_shape)
			outputs = [out_tensor]
			if out_shape != real_output_shape:
				out_tensor = new_tensor(real_output_shape)
			real_outputs = [out_tensor]
			# print("out_tensor=", tensor_shape(out_tensor))

		if new_node_type in ['MatMul', 'Gemm']:
			out_shape[n2_dim - 1] = tensor_shape(n2)[n2_dim - 1]

		if new_node_type not in ['Split', 'Concat']:
			out_tensor = new_tensor(out_shape)
			outputs = [out_tensor]



		myinputs = inputs if (real_inputs == None) else real_inputs
		myoutputs = outputs if (real_outputs == None) else real_outputs


		def on_demand_reduce():
			for x in outputs:
				pass_value(x, False)
				dq.append(x)
			for x in myoutputs:
				if x not in pure_value_tensor:
					pass_value(x, False)
				no_succ.add(x)
		if not this_op_dec:
			on_demand_reduce()
			continue

		# print(myinputs)
		# print(myoutputs)
		# new_node = helper.make_node(new_node_type, inputs=inputs, outputs=outputs, name=node_name, **kwargs)
		if PRINT_ONNX:
			def tostr(x):
				if str(type(x)) == "<class 'numpy.ndarray'>":
					return str(list(x))
				if type(x) == type("1"):
					return "'%s'" % x
				return str(x)

			mykw = ", ".join(["%s=%s" % (v[0], tostr(v[1])) for v in kwargs.items()])
			if len(mykw) > 0:
				mykw = ", " + mykw
			print("%s = helper.make_node('%s', inputs=%s, outputs=%s, name='%s'%s)" % (node_name, new_node_type, myinputs, myoutputs, node_name, mykw), file=FILE_AS_ONNX_CODE) 

		new_node = helper.make_node(new_node_type, 
			inputs=myinputs, 
			outputs=myoutputs, name=node_name, **kwargs)
		
		if PRINT_ONNX:
			print("node_list.append(%s)" % node_name, file=FILE_AS_ONNX_CODE)
		
		node_list.append(new_node)

		for x in outputs:
			dq.append(x)
		for x in myoutputs:
			no_succ.add(x)

		for t in myinputs:
			if t in no_succ:
				no_succ.remove(t)


	"""
	def totElement(x):
		ans = 1
		for i in tensor_shape(x):
			ans = ans * i
		return ans

	output_ts = []
	tot_output_element = 0
	for x in no_succ:
		if x in pure_value_tensor:
			continue
		x2 = new_tensor([1, totElement(x)])
		output_ts.append(x2)
		n = helper.make_node('Flatten', inputs=[x], outputs=[x2], name='flatten_%s' % x, axis=0)
		node_list.append(n)
		tot_output_element += totElement(x)

	# print(output_ts)
	final_tensor = new_tensor([1, tot_output_element])	
	n = helper.make_node('Concat', inputs=output_ts, outputs=[final_tensor], name='concat_outputs', axis=-1)
	node_list.append(n)
	output_tensor.append(tensor_map[final_tensor])
	"""

	output_tensor = []
	for x in no_succ:
		if x in pure_value_tensor:
			continue
		if PRINT_ONNX:
			print("output_tensor.append(%s)" % x, file=FILE_AS_ONNX_CODE)
		output_tensor.append(tensor_map[x])

	input_tensor_have_succ = []
	for x in input_tensor:
		if x.name in no_succ:
			inputs_feed.pop(x.name)
		else:
			if PRINT_ONNX:
				print("input_tensor.append(%s)" % x.name, file=FILE_AS_ONNX_CODE)
			input_tensor_have_succ.append(x)

	graph_def = helper.make_graph(node_list, "test-model", input_tensor_have_succ, output_tensor, init_tensor)
	model = helper.make_model(graph_def, producer_name='onnx-example')

	if PRINT_ONNX:
		print("graph_def = helper.make_graph(node_list, 'test-model', input_tensor, output_tensor, init_tensor)", file=FILE_AS_ONNX_CODE)
		print("model = helper.make_model(graph_def, producer_name='onnx-example')", file=FILE_AS_ONNX_CODE)

	
	return model, inputs_feed, network_node_num


def test(model_data, model_saved_file="tmp.onnx"):
	print("test for ", model_saved_file)

	model, inputs_feed, network_node_num = model_data
	# print('The graph in model:\n{}'.format(model.graph))
	if len(model.graph.output) == 0:
		raise Exception("model without output!")

	filename = model_saved_file
	onnx.save(model, filename)


	global graph_num
	graph_num += 1
	"""
	saved_file = gen_model_saved_folder + "/g"+str(graph_num)+".onnx"
	print("saved:" + saved_file)
	onnx.save(model, saved_file)
	np.save(gen_model_saved_folder + "/g%d_inputs.npy" % graph_num, inputs_feed)
	"""

	# TEST_ONNXRT:
	np.save("inputs.npy", inputs_feed)
	sess = rt.InferenceSession(filename)
	output_name = sess.get_outputs()[0].name
	onnxrt_out = sess.run([output_name], inputs_feed)
	print('onnx runtime finish normally!')

	# print('out=', onnxrt_out)

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
			print("out=", out)
			print("tvm_out=", out_deploy)
			raise Exception("differential_testing: different results on onnxrt and %s!" % tvm_ver)


from difflib import SequenceMatcher
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

def find_bugs():
	global error_num
	global err_message_set
	global crash_num

	for iter in range(ITER_NUM):
		print("ITER=", iter)

		try:
			test(work())
			if DEBUG and (iter % 10 == 0):
				print("iter=", iter)
				print("OK!")
			# throw("1")
		except Exception as err:
			err_m = str(err)
			if 'ONNXRuntimeError' in err_m:
				continue
			# if not ('indices_or_sections' in err_m):
			# 	continue
			# if not ('data_.size()' in err_m):
			# 	continue
			# if not ("TypedPackedFunc" in err_m):
			# 	continue
			# # if ("Gemm" in err_m) or ("axes" in err_m):
			# 	continue
			# if not ("differential_testing" in err_m):
			# 	continue

			err_pd = err_m
			PROG_MES = 'Error(s) have occurred. The program has been annotated with them:'
			if PROG_MES in err_pd:
				err_pd = err_pd[:err_pd.find(PROG_MES)]
			if err_pd in err_message_set:
				print('............\n............\nsame error message!')
				continue
			dup = 0
			for err_m2 in err_message_set:
				if similarity(err_m2, err_pd) >= 0.8:
					dup = 1
					break
			dup = 0
			if dup:
				print('............\n............\nprobably duplicated error message!')
				continue

			if not ('differential_testing' in err_pd):
				crash_num += 1
				err_message_set.add(err_pd)

			print(err_m)

			error_num += 1
			print("Find Bugs! Number %d" % error_num)
			print("............\n............\n............\n............\n")
			# print("error=", err_m)
			model = onnx.load("tmp.onnx")
			onnx.save(model, "output/bug%d.onnx" % error_num)
			inputs_feed = np.load("inputs.npy", allow_pickle=True)
			np.save("output/bug%d_inputs.npy" % error_num, inputs_feed)
			with open("output/bug%d_log.txt" % error_num, "w") as f:
				# print("tvm_params =", error_config, file=f)
				# print("graph_num = ", graph_num)
				print(err, file=f)
			with open('output/bug%d.onnx_rec.txt' % error_num, 'w') as f:
				f.write(json.dumps(gen_random.get_rand_record()))
			with open('output/bug%d.dec_rec.txt' % error_num, 'w') as f:
				f.write(json.dumps(gen_random.get_dec_rec()))
			os.system("mv myonnx.py output/bug%d.py" % error_num)


			if DEBUG:
				break

	print('iter=%d, all=%d, crash=%d' % (ITER_NUM, error_num, crash_num))

if __name__ == '__main__':
	# test(work())
	test(work())
	
	# find_bugs()
	
	# with open('output/tmp.onnx_rec.txt', 'w') as f:
	# 	f.write(json.dumps(rand_record))
	# debug()


	# for test_case in range(300):
	# 	print(test_case)
	# 	model, inputs_feed, _ = work()
	# 	import run_o2m
	# 	onnx.save(model, "tmp-o2m.onnx")
	# 	try:
	# 		run_o2m.test_o2m("tmp-o2m.onnx")
	# 	except Exception as err:
	# 		if 'unhandled option' not in str(err):
	# 			print("find bug: " + str(test_case))
	# 			onnx.save(model, "ff-output/g%d.onnx" % test_case)
	# 			np.save("ff-output/g%d_inputs.npy" % test_case, inputs_feed)
	# 			with open('ff-output/g%d.onnx_rec.txt' % test_case, 'w') as f:
	# 				f.write(json.dumps(get_rand_record()))

	"""
	for test_case in range(300):
		print(test_case)
		try:
			work()
			test(work())
			# fpectl.turnon_sigfpe()
			# test(work())
		except Exception as err:
			err_m = str(err)
			print("err=", err_m)
			pass
	"""


	