from onnx import helper
input_tensor = []
output_tensor = []
init_tensor = []
node_list = []

node1 = helper.make_tensor_value_info('node1', 1, [5, 3, 1])
node2 = helper.make_tensor_value_info('node2', 1, [3])
init_tensor.append(helper.make_tensor('node2', 1, dims=(3,), vals=[1.0, 1.0, 1.0]))
node3 = helper.make_tensor_value_info('node3', 1, [6])
init_tensor.append(helper.make_tensor('node3', 1, dims=(1, 6), vals=[0, 0, 0, 1, 1, 1]))
node4 = helper.make_tensor_value_info('node4', 1, [5, 3, 1])
op0 = helper.make_node('Resize', inputs=['node1', 'node3', 'node2'], outputs=['node4'], name='op0', mode='nearest')
node_list.append(op0)
node5 = helper.make_tensor_value_info('node5', 1, [2, 3, 4])
node6 = helper.make_tensor_value_info('node6', 1, [2, 3, 4])
node7 = helper.make_tensor_value_info('node7', 1, [2, 3, 4])
node8 = helper.make_tensor_value_info('node8', 1, [2, 3, 4])
node9 = helper.make_tensor_value_info('node9', 1, [2, 3, 4])
op1 = helper.make_node('Min', inputs=['node5', 'node6', 'node7', 'node8'], outputs=['node9'], name='op1')
node_list.append(op1)
node10 = helper.make_tensor_value_info('node10', 1, [4, 2, 3])
op2 = helper.make_node('Transpose', inputs=['node9'], outputs=['node10'], name='op2', perm=[2, 0, 1])
node_list.append(op2)
node11 = helper.make_tensor_value_info('node11', 1, [2, 3, 4])
op3 = helper.make_node('Sin', inputs=['node9'], outputs=['node11'], name='op3')
node_list.append(op3)
node12 = helper.make_tensor_value_info('node12', 1, [4, 2, 3])
op4 = helper.make_node('Cos', inputs=['node10'], outputs=['node12'], name='op4')
node_list.append(op4)
node13 = helper.make_tensor_value_info('node13', 1, [4, 2, 3])
op5 = helper.make_node('HardSigmoid', inputs=['node12'], outputs=['node13'], name='op5')
node_list.append(op5)
node14 = helper.make_tensor_value_info('node14', 1, [4, 2, 3])
op6 = helper.make_node('Mul', inputs=['node13', 'node13'], outputs=['node14'], name='op6')
node_list.append(op6)
node15 = helper.make_tensor_value_info('node15', 1, [4, 1, 3])
op7 = helper.make_node('ReduceMin', inputs=['node13'], outputs=['node15'], name='op7', axes=[1])
node_list.append(op7)
node16 = helper.make_tensor_value_info('node16', 7, [3])
init_tensor.append(helper.make_tensor('node16', 7, dims=(3,), vals=[1, 1, 1]))
node17 = helper.make_tensor_value_info('node17', 1, [4, 2, 3])
op8 = helper.make_node('Expand', inputs=['node14', 'node16'], outputs=['node17'], name='op8')
node_list.append(op8)
node18 = helper.make_tensor_value_info('node18', 1, [1])
node19 = helper.make_tensor_value_info('node19', 1, [1])
op9 = helper.make_node('Elu', inputs=['node18'], outputs=['node19'], name='op9', alpha=2.0)
node_list.append(op9)
node20 = helper.make_tensor_value_info('node20', 1, [1, 3])
node21 = helper.make_tensor_value_info('node21', 1, [1, 3])
node22 = helper.make_tensor_value_info('node22', 1, [1, 3])
op10 = helper.make_node('PRelu', inputs=['node20', 'node21'], outputs=['node22'], name='op10')
node_list.append(op10)
node23 = helper.make_tensor_value_info('node23', 1, [1])
op11 = helper.make_node('Sub', inputs=['node19', 'node19'], outputs=['node23'], name='op11')
node_list.append(op11)
node24 = helper.make_tensor_value_info('node24', 1, [4, 2, 3])
op12 = helper.make_node('Softsign', inputs=['node12'], outputs=['node24'], name='op12')
node_list.append(op12)
node25 = helper.make_tensor_value_info('node25', 1, [1, 24])
op13 = helper.make_node('Flatten', inputs=['node24'], outputs=['node25'], name='op13', axis=0)
node_list.append(op13)
node26 = helper.make_tensor_value_info('node26', 1, [1, 24])
op14 = helper.make_node('ReduceSumSquare', inputs=['node25'], outputs=['node26'], name='op14', axes=[0])
node_list.append(op14)
node27 = helper.make_tensor_value_info('node27', 1, [1, 24])
op15 = helper.make_node('Min', inputs=['node25', 'node26', 'node25'], outputs=['node27'], name='op15')
node_list.append(op15)
node28 = helper.make_tensor_value_info('node28', 1, [1, 24])
op16 = helper.make_node('Transpose', inputs=['node27'], outputs=['node28'], name='op16', perm=[0, 1])
node_list.append(op16)
node29 = helper.make_tensor_value_info('node29', 1, [1, 1])
op17 = helper.make_node('ReduceLogSumExp', inputs=['node27'], outputs=['node29'], name='op17', axes=[1])
node_list.append(op17)
node30 = helper.make_tensor_value_info('node30', 1, [1, 24])
op18 = helper.make_node('Add', inputs=['node28', 'node28'], outputs=['node30'], name='op18')
node_list.append(op18)
node31 = helper.make_tensor_value_info('node31', 1, [1, 24])
op19 = helper.make_node('ThresholdedRelu', inputs=['node30'], outputs=['node31'], name='op19')
node_list.append(op19)
node32 = helper.make_tensor_value_info('node32', 7, [2])
init_tensor.append(helper.make_tensor('node32', 7, dims=(2,), vals=[0, 0]))
node33 = helper.make_tensor_value_info('node33', 7, [2])
init_tensor.append(helper.make_tensor('node33', 7, dims=(2,), vals=[1, 17]))
node34 = helper.make_tensor_value_info('node34', 7, [2])
init_tensor.append(helper.make_tensor('node34', 7, dims=(2,), vals=[0, 1]))
node35 = helper.make_tensor_value_info('node35', 7, [2])
init_tensor.append(helper.make_tensor('node35', 7, dims=(2,), vals=[2, 2]))
node36 = helper.make_tensor_value_info('node36', 1, [1, 9])
op20 = helper.make_node('Slice', inputs=['node31', 'node32', 'node33', 'node34', 'node35'], outputs=['node36'], name='op20')
node_list.append(op20)
node37 = helper.make_tensor_value_info('node37', 1, [1, 9])
op21 = helper.make_node('HardSigmoid', inputs=['node36'], outputs=['node37'], name='op21')
node_list.append(op21)
node38 = helper.make_tensor_value_info('node38', 1, [1, 9])
op22 = helper.make_node('Softsign', inputs=['node37'], outputs=['node38'], name='op22')
node_list.append(op22)
node39 = helper.make_tensor_value_info('node39', 1, [1, 5])
node40 = helper.make_tensor_value_info('node40', 1, [1, 1])
op23 = helper.make_node('ReduceSumSquare', inputs=['node39'], outputs=['node40'], name='op23', axes=[0, 1])
node_list.append(op23)
node41 = helper.make_tensor_value_info('node41', 1, [1, 9])
op24 = helper.make_node('Exp', inputs=['node38'], outputs=['node41'], name='op24')
node_list.append(op24)
node42 = helper.make_tensor_value_info('node42', 1, [1, 1])
op25 = helper.make_node('ReduceL2', inputs=['node41'], outputs=['node42'], name='op25', axes=[1])
node_list.append(op25)
node43 = helper.make_tensor_value_info('node43', 1, [1, 9])
op26 = helper.make_node('Sin', inputs=['node41'], outputs=['node43'], name='op26')
node_list.append(op26)
node44 = helper.make_tensor_value_info('node44', 7, [2])
init_tensor.append(helper.make_tensor('node44', 7, dims=(2,), vals=[2, 1]))
node45 = helper.make_tensor_value_info('node45', 1, [2, 9])
op27 = helper.make_node('Expand', inputs=['node43', 'node44'], outputs=['node45'], name='op27')
node_list.append(op27)
node46 = helper.make_tensor_value_info('node46', 1, [9, 4])
node47 = helper.make_tensor_value_info('node47', 1, [2, 4])
op28 = helper.make_node('MatMul', inputs=['node45', 'node46'], outputs=['node47'], name='op28')
node_list.append(op28)
node48 = helper.make_tensor_value_info('node48', 1, [2, 1])
op29 = helper.make_node('ReduceSumSquare', inputs=['node47'], outputs=['node48'], name='op29', axes=[1])
node_list.append(op29)
node49 = helper.make_tensor_value_info('node49', 1, [3, 1, 1])
node50 = helper.make_tensor_value_info('node50', 1, [5, 1, 1])
op30 = helper.make_node('ConvTranspose', inputs=['node4', 'node49'], outputs=['node50'], name='op30', kernel_shape=[1], strides=[1], pads=[0, 0])
node_list.append(op30)
node51 = helper.make_tensor_value_info('node51', 1, [1, 1])
op31 = helper.make_node('ReduceL2', inputs=['node48'], outputs=['node51'], name='op31', axes=[0, 1])
node_list.append(op31)
node52 = helper.make_tensor_value_info('node52', 1, [1, 1, 1])
op32 = helper.make_node('ReduceL1', inputs=['node50'], outputs=['node52'], name='op32', axes=[0, 1, 2])
node_list.append(op32)
node53 = helper.make_tensor_value_info('node53', 1, [1, 1])
op33 = helper.make_node('Ceil', inputs=['node51'], outputs=['node53'], name='op33')
node_list.append(op33)
node54 = helper.make_tensor_value_info('node54', 1, [1, 1])
op34 = helper.make_node('Tanh', inputs=['node53'], outputs=['node54'], name='op34')
node_list.append(op34)
output_tensor.append(node29)
output_tensor.append(node15)
output_tensor.append(node23)
output_tensor.append(node52)
output_tensor.append(node22)
output_tensor.append(node42)
output_tensor.append(node54)
output_tensor.append(node11)
output_tensor.append(node40)
output_tensor.append(node17)
input_tensor.append(node1)
input_tensor.append(node5)
input_tensor.append(node6)
input_tensor.append(node7)
input_tensor.append(node8)
input_tensor.append(node18)
input_tensor.append(node20)
input_tensor.append(node21)
input_tensor.append(node39)
input_tensor.append(node46)
input_tensor.append(node49)
graph_def = helper.make_graph(node_list, 'test-model', input_tensor, output_tensor, init_tensor)
model = helper.make_model(graph_def, producer_name='onnx-example')
