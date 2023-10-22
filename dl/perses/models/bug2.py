from onnx import helper
input_tensor = []
output_tensor = []
init_tensor = []
node_list = []

node1 = helper.make_tensor_value_info('node1', 1, [2, 5, 5, 4, 4])
node2 = helper.make_tensor_value_info('node2', 1, [2, 5, 5, 4, 4])
op0 = helper.make_node('Round', inputs=['node1'], outputs=['node2'], name='op0')
node_list.append(op0)
node3 = helper.make_tensor_value_info('node3', 1, [2, 5, 1, 1, 1])
op1 = helper.make_node('GlobalAveragePool', inputs=['node1'], outputs=['node3'], name='op1')
node_list.append(op1)
node4 = helper.make_tensor_value_info('node4', 1, [2, 5, 1, 1, 1])
op2 = helper.make_node('Sqrt', inputs=['node3'], outputs=['node4'], name='op2')
node_list.append(op2)
node5 = helper.make_tensor_value_info('node5', 1, [1, 5, 1, 1, 1])
op3 = helper.make_node('ReduceMin', inputs=['node4'], outputs=['node5'], name='op3', axes=[0])
node_list.append(op3)
node6 = helper.make_tensor_value_info('node6', 1, [1, 5, 1, 1, 1])
op4 = helper.make_node('Abs', inputs=['node5'], outputs=['node6'], name='op4')
node_list.append(op4)
node7 = helper.make_tensor_value_info('node7', 1, [5, 1])
op5 = helper.make_node('Flatten', inputs=['node6'], outputs=['node7'], name='op5', axis=3)
node_list.append(op5)
node8 = helper.make_tensor_value_info('node8', 1, [5, 1])
op6 = helper.make_node('ReduceMin', inputs=['node7'], outputs=['node8'], name='op6', axes=[1])
node_list.append(op6)
node9 = helper.make_tensor_value_info('node9', 1, [5, 1])
op7 = helper.make_node('Round', inputs=['node8'], outputs=['node9'], name='op7')
node_list.append(op7)
node10 = helper.make_tensor_value_info('node10', 1, [5, 1])
op8 = helper.make_node('Sigmoid', inputs=['node9'], outputs=['node10'], name='op8')
node_list.append(op8)
node11 = helper.make_tensor_value_info('node11', 7, [2, 1, 3])
init_tensor.append(helper.make_tensor('node11', 7, dims=(2, 1, 3), vals=[0, 0, 0, 0, 0, 0]))
node12 = helper.make_tensor_value_info('node12', 1, [5, 2, 1, 3])
op9 = helper.make_node('Gather', inputs=['node10', 'node11'], outputs=['node12'], name='op9', axis=1)
node_list.append(op9)
node13 = helper.make_tensor_value_info('node13', 1, [5, 2, 1, 3])
op10 = helper.make_node('Erf', inputs=['node12'], outputs=['node13'], name='op10')
node_list.append(op10)
node14 = helper.make_tensor_value_info('node14', 1, [5, 2, 1, 3])
op11 = helper.make_node('Abs', inputs=['node13'], outputs=['node14'], name='op11')
node_list.append(op11)
node15 = helper.make_tensor_value_info('node15', 1, [5, 2, 1, 3])
op12 = helper.make_node('Identity', inputs=['node14'], outputs=['node15'], name='op12')
node_list.append(op12)
node16 = helper.make_tensor_value_info('node16', 1, [1, 2, 1, 3])
op13 = helper.make_node('ReduceMax', inputs=['node14'], outputs=['node16'], name='op13', axes=[0, 2])
node_list.append(op13)
node17 = helper.make_tensor_value_info('node17', 1, [5, 2, 1, 3])
op14 = helper.make_node('Relu', inputs=['node15'], outputs=['node17'], name='op14')
node_list.append(op14)
node18 = helper.make_tensor_value_info('node18', 1, [3, 3, 4])
node19 = helper.make_tensor_value_info('node19', 1, [3, 3, 2])
op15 = helper.make_node('AveragePool', inputs=['node18'], outputs=['node19'], name='op15', kernel_shape=[1], strides=[3])
node_list.append(op15)
node20 = helper.make_tensor_value_info('node20', 1, [3, 2, 2])
node21 = helper.make_tensor_value_info('node21', 1, [3, 2, 2])
node22 = helper.make_tensor_value_info('node22', 1, [3, 5, 2])
node23 = helper.make_tensor_value_info('node23', 1, [3, 5, 2])
node24 = helper.make_tensor_value_info('node24', 1, [3, 4, 2])
node25 = helper.make_tensor_value_info('node25', 1, [3, 27, 2])
op16 = helper.make_node('Concat', inputs=['node19', 'node20', 'node21', 'node22', 'node19', 'node19', 'node23', 'node24'], outputs=['node25'], name='op16', axis=1)
node_list.append(op16)
node26 = helper.make_tensor_value_info('node26', 1, [3, 27, 2])
op17 = helper.make_node('Dropout', inputs=['node25'], outputs=['node26'], name='op17')
node_list.append(op17)
node27 = helper.make_tensor_value_info('node27', 1, [3, 2, 1])
node28 = helper.make_tensor_value_info('node28', 1, [3, 27, 1])
op18 = helper.make_node('MatMul', inputs=['node26', 'node27'], outputs=['node28'], name='op18')
node_list.append(op18)
node29 = helper.make_tensor_value_info('node29', 1, [27])
node30 = helper.make_tensor_value_info('node30', 1, [27])
node31 = helper.make_tensor_value_info('node31', 1, [27])
node32 = helper.make_tensor_value_info('node32', 1, [27])
node33 = helper.make_tensor_value_info('node33', 1, [3, 27, 2])
op19 = helper.make_node('BatchNormalization', inputs=['node26', 'node29', 'node30', 'node31', 'node32'], outputs=['node33'], name='op19')
node_list.append(op19)
node34 = helper.make_tensor_value_info('node34', 1, [3, 27, 2])
op20 = helper.make_node('Round', inputs=['node33'], outputs=['node34'], name='op20')
node_list.append(op20)
node35 = helper.make_tensor_value_info('node35', 1, [3, 27, 1])
op21 = helper.make_node('ReduceMax', inputs=['node33'], outputs=['node35'], name='op21', axes=[2])
node_list.append(op21)
node36 = helper.make_tensor_value_info('node36', 1, [1, 2, 1, 3])
op22 = helper.make_node('SpaceToDepth', inputs=['node16'], outputs=['node36'], name='op22', blocksize=1)
node_list.append(op22)
node37 = helper.make_tensor_value_info('node37', 1, [3, 27, 1])
op23 = helper.make_node('Erf', inputs=['node35'], outputs=['node37'], name='op23')
node_list.append(op23)
node38 = helper.make_tensor_value_info('node38', 1, [1, 2, 1, 2])
op24 = helper.make_node('LpPool', inputs=['node36'], outputs=['node38'], name='op24', kernel_shape=[1, 2], strides=[1, 1], p=1)
node_list.append(op24)
node39 = helper.make_tensor_value_info('node39', 1, [3, 27, 1])
op25 = helper.make_node('Relu', inputs=['node37'], outputs=['node39'], name='op25')
node_list.append(op25)
node40 = helper.make_tensor_value_info('node40', 1, [1, 2, 1, 1])
op26 = helper.make_node('ReduceLogSumExp', inputs=['node38'], outputs=['node40'], name='op26', axes=[2, 0, 3])
node_list.append(op26)
node41 = helper.make_tensor_value_info('node41', 1, [4])
init_tensor.append(helper.make_tensor('node41', 1, dims=(4,), vals=[1.0, 1.0, 1.0, 1.0]))
node42 = helper.make_tensor_value_info('node42', 1, [8])
init_tensor.append(helper.make_tensor('node42', 1, dims=(1, 8), vals=[0, 0, 0, 0, 1, 1, 1, 1]))
node43 = helper.make_tensor_value_info('node43', 1, [1, 2, 1, 1])
op27 = helper.make_node('Resize', inputs=['node40', 'node42', 'node41'], outputs=['node43'], name='op27', mode='nearest')
node_list.append(op27)
node44 = helper.make_tensor_value_info('node44', 1, [1, 2, 1, 1])
op28 = helper.make_node('Softsign', inputs=['node43'], outputs=['node44'], name='op28')
node_list.append(op28)
node45 = helper.make_tensor_value_info('node45', 7, [4])
init_tensor.append(helper.make_tensor('node45', 7, dims=(4,), vals=[1, 1, 1, 1]))
node46 = helper.make_tensor_value_info('node46', 1, [1, 2, 1, 1])
op29 = helper.make_node('Expand', inputs=['node43', 'node45'], outputs=['node46'], name='op29')
node_list.append(op29)
node47 = helper.make_tensor_value_info('node47', 1, [1, 2, 1, 1])
op30 = helper.make_node('GlobalAveragePool', inputs=['node44'], outputs=['node47'], name='op30')
node_list.append(op30)
node48 = helper.make_tensor_value_info('node48', 1, [1, 2, 1, 1])
op31 = helper.make_node('Reciprocal', inputs=['node47'], outputs=['node48'], name='op31')
node_list.append(op31)
node49 = helper.make_tensor_value_info('node49', 1, [5, 3, 1, 3, 2])
node50 = helper.make_tensor_value_info('node50', 1, [5, 3, 1, 3, 2])
node51 = helper.make_tensor_value_info('node51', 1, [5, 3, 1, 3, 2])
op32 = helper.make_node('Sub', inputs=['node49', 'node50'], outputs=['node51'], name='op32')
node_list.append(op32)
node52 = helper.make_tensor_value_info('node52', 1, [5, 3, 1, 3, 2])
op33 = helper.make_node('Tanh', inputs=['node51'], outputs=['node52'], name='op33')
node_list.append(op33)
node53 = helper.make_tensor_value_info('node53', 1, [5, 3, 1, 3, 2])
op34 = helper.make_node('Exp', inputs=['node51'], outputs=['node53'], name='op34')
node_list.append(op34)
node54 = helper.make_tensor_value_info('node54', 7, [10])
init_tensor.append(helper.make_tensor('node54', 7, dims=(10,), vals=[2, 2, 2, 2, 1, 2, 0, 0, 2, 2]))
node55 = helper.make_tensor_value_info('node55', 1, [9, 5, 3, 7, 5])
op35 = helper.make_node('Pad', inputs=['node53', 'node54'], outputs=['node55'], name='op35', mode='constant')
node_list.append(op35)
node56 = helper.make_tensor_value_info('node56', 7, [1])
init_tensor.append(helper.make_tensor('node56', 7, dims=(1,), vals=[90]))
node57 = helper.make_tensor_value_info('node57', 1, [90])
op36 = helper.make_node('Reshape', inputs=['node53', 'node56'], outputs=['node57'], name='op36')
node_list.append(op36)
node58 = helper.make_tensor_value_info('node58', 1, [5, 2, 1, 3])
op37 = helper.make_node('Floor', inputs=['node12'], outputs=['node58'], name='op37')
node_list.append(op37)
node59 = helper.make_tensor_value_info('node59', 1, [5, 2, 1, 3])
op38 = helper.make_node('ReduceLogSumExp', inputs=['node58'], outputs=['node59'], name='op38', axes=[2])
node_list.append(op38)
output_tensor.append(node2)
output_tensor.append(node55)
output_tensor.append(node46)
output_tensor.append(node57)
output_tensor.append(node17)
output_tensor.append(node48)
output_tensor.append(node39)
output_tensor.append(node59)
output_tensor.append(node52)
output_tensor.append(node28)
output_tensor.append(node34)
input_tensor.append(node1)
input_tensor.append(node18)
input_tensor.append(node20)
input_tensor.append(node21)
input_tensor.append(node22)
input_tensor.append(node23)
input_tensor.append(node24)
input_tensor.append(node27)
input_tensor.append(node29)
input_tensor.append(node30)
input_tensor.append(node31)
input_tensor.append(node32)
input_tensor.append(node49)
input_tensor.append(node50)
graph_def = helper.make_graph(node_list, 'test-model', input_tensor, output_tensor, init_tensor)
model = helper.make_model(graph_def, producer_name='onnx-example')
