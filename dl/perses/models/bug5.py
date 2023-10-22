from onnx import helper
input_tensor = []
output_tensor = []
init_tensor = []
node_list = []

node1 = helper.make_tensor_value_info('node1', 1, [1, 4])
node2 = helper.make_tensor_value_info('node2', 1, [1, 4])
op0 = helper.make_node('Mul', inputs=['node1', 'node1'], outputs=['node2'], name='op0')
node_list.append(op0)
node3 = helper.make_tensor_value_info('node3', 1, [1, 4])
op1 = helper.make_node('Flatten', inputs=['node2'], outputs=['node3'], name='op1', axis=1)
node_list.append(op1)
node4 = helper.make_tensor_value_info('node4', 1, [2, 5, 2, 5])
node5 = helper.make_tensor_value_info('node5', 1, [2, 5, 2, 5])
node6 = helper.make_tensor_value_info('node6', 1, [2, 5, 2, 5])
node7 = helper.make_tensor_value_info('node7', 1, [2, 5, 2, 5])
node8 = helper.make_tensor_value_info('node8', 1, [2, 5, 2, 5])
node9 = helper.make_tensor_value_info('node9', 1, [2, 5, 2, 5])
node10 = helper.make_tensor_value_info('node10', 1, [2, 5, 2, 5])
node11 = helper.make_tensor_value_info('node11', 1, [2, 5, 2, 5])
op2 = helper.make_node('Min', inputs=['node4', 'node5', 'node6', 'node7', 'node8', 'node9', 'node10'], outputs=['node11'], name='op2')
node_list.append(op2)
node12 = helper.make_tensor_value_info('node12', 1, [2, 5, 2, 5])
op3 = helper.make_node('Softmax', inputs=['node11'], outputs=['node12'], name='op3', axis=0)
node_list.append(op3)
node13 = helper.make_tensor_value_info('node13', 1, [1, 1, 1, 1])
op4 = helper.make_node('ReduceMean', inputs=['node11'], outputs=['node13'], name='op4', axes=[1, 3, 0, 2])
node_list.append(op4)
node14 = helper.make_tensor_value_info('node14', 7, [4])
init_tensor.append(helper.make_tensor('node14', 7, dims=(4,), vals=[1, 1, 1, 1]))
node15 = helper.make_tensor_value_info('node15', 1, [2, 5, 2, 5])
op5 = helper.make_node('Expand', inputs=['node12', 'node14'], outputs=['node15'], name='op5')
node_list.append(op5)
node16 = helper.make_tensor_value_info('node16', 1, [1, 1, 1, 1])
op6 = helper.make_node('Sin', inputs=['node13'], outputs=['node16'], name='op6')
node_list.append(op6)
node17 = helper.make_tensor_value_info('node17', 1, [1, 1, 1, 1])
op7 = helper.make_node('ReduceL2', inputs=['node16'], outputs=['node17'], name='op7', axes=[3, 1, 2])
node_list.append(op7)
node18 = helper.make_tensor_value_info('node18', 1, [3])
node19 = helper.make_tensor_value_info('node19', 1, [3])
op8 = helper.make_node('Elu', inputs=['node18'], outputs=['node19'], name='op8', alpha=0.5)
node_list.append(op8)
node20 = helper.make_tensor_value_info('node20', 1, [3])
op9 = helper.make_node('Elu', inputs=['node19'], outputs=['node20'], name='op9')
node_list.append(op9)
node21 = helper.make_tensor_value_info('node21', 1, [3])
op10 = helper.make_node('Round', inputs=['node20'], outputs=['node21'], name='op10')
node_list.append(op10)
node22 = helper.make_tensor_value_info('node22', 1, [3])
op11 = helper.make_node('Cos', inputs=['node20'], outputs=['node22'], name='op11')
node_list.append(op11)
node23 = helper.make_tensor_value_info('node23', 1, [3])
op12 = helper.make_node('Identity', inputs=['node21'], outputs=['node23'], name='op12')
node_list.append(op12)
node24 = helper.make_tensor_value_info('node24', 1, [1, 3])
op13 = helper.make_node('Flatten', inputs=['node22'], outputs=['node24'], name='op13', axis=0)
node_list.append(op13)
node25 = helper.make_tensor_value_info('node25', 1, [1, 3])
op14 = helper.make_node('Sqrt', inputs=['node24'], outputs=['node25'], name='op14')
node_list.append(op14)
node26 = helper.make_tensor_value_info('node26', 1, [1, 3])
op15 = helper.make_node('Selu', inputs=['node24'], outputs=['node26'], name='op15')
node_list.append(op15)
node27 = helper.make_tensor_value_info('node27', 7, [5, 5, 5, 1])
init_tensor.append(helper.make_tensor('node27', 7, dims=(5, 5, 5, 1), vals=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
node28 = helper.make_tensor_value_info('node28', 1, [5, 5, 5, 1, 3])
op16 = helper.make_node('Gather', inputs=['node26', 'node27'], outputs=['node28'], name='op16', axis=0)
node_list.append(op16)
node29 = helper.make_tensor_value_info('node29', 1, [5, 5, 5, 1, 3])
op17 = helper.make_node('Reciprocal', inputs=['node28'], outputs=['node29'], name='op17')
node_list.append(op17)
node30 = helper.make_tensor_value_info('node30', 1, [5, 5, 5, 1, 3])
op18 = helper.make_node('Erf', inputs=['node29'], outputs=['node30'], name='op18')
node_list.append(op18)
node31 = helper.make_tensor_value_info('node31', 1, [5, 5, 5, 1, 3])
op19 = helper.make_node('Reciprocal', inputs=['node29'], outputs=['node31'], name='op19')
node_list.append(op19)
node32 = helper.make_tensor_value_info('node32', 1, [5, 5, 2, 1, 1])
op20 = helper.make_node('LpPool', inputs=['node30'], outputs=['node32'], name='op20', kernel_shape=[2, 1, 2], strides=[2, 1, 2], p=2)
node_list.append(op20)
node33 = helper.make_tensor_value_info('node33', 1, [5, 1, 1])
node34 = helper.make_tensor_value_info('node34', 1, [5, 1, 1])
op21 = helper.make_node('Softsign', inputs=['node33'], outputs=['node34'], name='op21')
node_list.append(op21)
node35 = helper.make_tensor_value_info('node35', 1, [5, 1, 1])
op22 = helper.make_node('Identity', inputs=['node34'], outputs=['node35'], name='op22')
node_list.append(op22)
output_tensor.append(node23)
output_tensor.append(node31)
output_tensor.append(node17)
output_tensor.append(node32)
output_tensor.append(node15)
output_tensor.append(node25)
output_tensor.append(node35)
output_tensor.append(node3)
input_tensor.append(node1)
input_tensor.append(node4)
input_tensor.append(node5)
input_tensor.append(node6)
input_tensor.append(node7)
input_tensor.append(node8)
input_tensor.append(node9)
input_tensor.append(node10)
input_tensor.append(node18)
input_tensor.append(node33)
graph_def = helper.make_graph(node_list, 'test-model', input_tensor, output_tensor, init_tensor)
model = helper.make_model(graph_def, producer_name='onnx-example')