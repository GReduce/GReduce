from onnx import helper
input_tensor = []
output_tensor = []
init_tensor = []
node_list = []

node1 = helper.make_tensor_value_info('node1', 1, [1, 4, 3, 3])
node2 = helper.make_tensor_value_info('node2', 1, [1, 4, 3, 3])
op0 = helper.make_node('Dropout', inputs=['node1'], outputs=['node2'], name='op0')
node_list.append(op0)
node3 = helper.make_tensor_value_info('node3', 1, [1, 1, 1, 1])
op1 = helper.make_node('ReduceMax', inputs=['node2'], outputs=['node3'], name='op1', axes=[0, 3, 1, 2])
node_list.append(op1)
node4 = helper.make_tensor_value_info('node4', 1, [1, 1, 1, 1])
node5 = helper.make_tensor_value_info('node5', 1, [1, 1, 1, 1])
op2 = helper.make_node('Min', inputs=['node3', 'node3', 'node3', 'node4', 'node3', 'node3', 'node3'], outputs=['node5'], name='op2')
node_list.append(op2)
node6 = helper.make_tensor_value_info('node6', 1, [1, 1, 1, 1])
op3 = helper.make_node('MaxPool', inputs=['node5'], outputs=['node6'], name='op3', kernel_shape=[1, 1], strides=[1, 1])
node_list.append(op3)
node7 = helper.make_tensor_value_info('node7', 7, [4])
init_tensor.append(helper.make_tensor('node7', 7, dims=(4,), vals=[0, 0, 0, 0]))
node8 = helper.make_tensor_value_info('node8', 7, [4])
init_tensor.append(helper.make_tensor('node8', 7, dims=(4,), vals=[1, 1, 1, 1]))
node9 = helper.make_tensor_value_info('node9', 7, [4])
init_tensor.append(helper.make_tensor('node9', 7, dims=(4,), vals=[0, 1, 2, 3]))
node10 = helper.make_tensor_value_info('node10', 7, [4])
init_tensor.append(helper.make_tensor('node10', 7, dims=(4,), vals=[2, 2, 1, 3]))
node11 = helper.make_tensor_value_info('node11', 1, [1, 1, 1, 1])
op4 = helper.make_node('Slice', inputs=['node5', 'node7', 'node8', 'node9', 'node10'], outputs=['node11'], name='op4')
node_list.append(op4)
node12 = helper.make_tensor_value_info('node12', 1, [1, 1, 1, 1])
op5 = helper.make_node('Neg', inputs=['node6'], outputs=['node12'], name='op5')
node_list.append(op5)
node13 = helper.make_tensor_value_info('node13', 1, [1, 1, 1, 4])
node14 = helper.make_tensor_value_info('node14', 1, [1, 1, 1, 3])
node15 = helper.make_tensor_value_info('node15', 1, [1, 1, 1, 5])
node16 = helper.make_tensor_value_info('node16', 1, [1, 1, 1, 2])
node17 = helper.make_tensor_value_info('node17', 1, [1, 1, 1, 4])
node18 = helper.make_tensor_value_info('node18', 1, [1, 1, 1, 20])
op6 = helper.make_node('Concat', inputs=['node12', 'node12', 'node13', 'node14', 'node15', 'node16', 'node17'], outputs=['node18'], name='op6', axis=3)
node_list.append(op6)
node19 = helper.make_tensor_value_info('node19', 1, [1, 1, 1, 20])
op7 = helper.make_node('Mean', inputs=['node18', 'node18'], outputs=['node19'], name='op7')
node_list.append(op7)
node20 = helper.make_tensor_value_info('node20', 1, [1, 1, 1, 20])
op8 = helper.make_node('Sin', inputs=['node18'], outputs=['node20'], name='op8')
node_list.append(op8)
node21 = helper.make_tensor_value_info('node21', 1, [1, 1, 1, 20])
op9 = helper.make_node('Sigmoid', inputs=['node20'], outputs=['node21'], name='op9')
node_list.append(op9)
node22 = helper.make_tensor_value_info('node22', 1, [1, 1, 1, 20])
op10 = helper.make_node('ThresholdedRelu', inputs=['node20'], outputs=['node22'], name='op10', alpha=1.0)
node_list.append(op10)
node23 = helper.make_tensor_value_info('node23', 1, [1, 1, 1, 4])
op11 = helper.make_node('MaxPool', inputs=['node22'], outputs=['node23'], name='op11', kernel_shape=[1, 6], strides=[1, 4])
node_list.append(op11)
node24 = helper.make_tensor_value_info('node24', 1, [1, 1, 1, 20])
op12 = helper.make_node('Mul', inputs=['node22', 'node22'], outputs=['node24'], name='op12')
node_list.append(op12)
node25 = helper.make_tensor_value_info('node25', 1, [1, 1, 1, 4])
op13 = helper.make_node('Abs', inputs=['node23'], outputs=['node25'], name='op13')
node_list.append(op13)
node26 = helper.make_tensor_value_info('node26', 1, [1, 4])
op14 = helper.make_node('Flatten', inputs=['node25'], outputs=['node26'], name='op14', axis=0)
node_list.append(op14)
node27 = helper.make_tensor_value_info('node27', 1, [1, 3])
node28 = helper.make_tensor_value_info('node28', 7, [3, 1, 5, 1])
init_tensor.append(helper.make_tensor('node28', 7, dims=(3, 1, 5, 1), vals=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
node29 = helper.make_tensor_value_info('node29', 1, [3, 1, 5, 1, 3])
op15 = helper.make_node('Gather', inputs=['node27', 'node28'], outputs=['node29'], name='op15')
node_list.append(op15)
node30 = helper.make_tensor_value_info('node30', 1, [3, 1, 5, 1, 3])
op16 = helper.make_node('Max', inputs=['node29', 'node29'], outputs=['node30'], name='op16')
node_list.append(op16)
node31 = helper.make_tensor_value_info('node31', 1, [3, 1, 5, 1, 3])
op17 = helper.make_node('Sqrt', inputs=['node30'], outputs=['node31'], name='op17')
node_list.append(op17)
node32 = helper.make_tensor_value_info('node32', 1, [1, 4, 1, 1, 4])
node33 = helper.make_tensor_value_info('node33', 1, [1, 4, 1, 1, 1])
op18 = helper.make_node('GlobalAveragePool', inputs=['node32'], outputs=['node33'], name='op18')
node_list.append(op18)
node34 = helper.make_tensor_value_info('node34', 1, [3, 1, 5, 1, 3])
node35 = helper.make_tensor_value_info('node35', 1, [3, 1, 5, 1, 3])
op19 = helper.make_node('Min', inputs=['node31', 'node31', 'node31', 'node31', 'node31', 'node34', 'node31', 'node31', 'node31'], outputs=['node35'], name='op19')
node_list.append(op19)
node36 = helper.make_tensor_value_info('node36', 1, [1, 4, 1, 1, 1])
op20 = helper.make_node('Floor', inputs=['node33'], outputs=['node36'], name='op20')
node_list.append(op20)
node37 = helper.make_tensor_value_info('node37', 1, [3, 1, 5, 1, 3])
op21 = helper.make_node('Exp', inputs=['node35'], outputs=['node37'], name='op21')
node_list.append(op21)
node38 = helper.make_tensor_value_info('node38', 1, [1, 4, 1, 1, 1])
op22 = helper.make_node('Selu', inputs=['node36'], outputs=['node38'], name='op22')
node_list.append(op22)
node39 = helper.make_tensor_value_info('node39', 1, [1, 4, 1, 1, 1])
op23 = helper.make_node('Erf', inputs=['node38'], outputs=['node39'], name='op23')
node_list.append(op23)
node40 = helper.make_tensor_value_info('node40', 7, [4])
init_tensor.append(helper.make_tensor('node40', 7, dims=(4,), vals=[1, 4, 1, 1]))
node41 = helper.make_tensor_value_info('node41', 1, [1, 4, 1, 1])
op24 = helper.make_node('Reshape', inputs=['node38', 'node40'], outputs=['node41'], name='op24')
node_list.append(op24)
node42 = helper.make_tensor_value_info('node42', 1, [1, 4, 1, 1])
op25 = helper.make_node('Softmax', inputs=['node41'], outputs=['node42'], name='op25', axis=0)
node_list.append(op25)
node43 = helper.make_tensor_value_info('node43', 1, [1, 4, 1, 1])
op26 = helper.make_node('HardSigmoid', inputs=['node42'], outputs=['node43'], name='op26')
node_list.append(op26)
node44 = helper.make_tensor_value_info('node44', 1, [1, 4, 1, 1])
op27 = helper.make_node('Relu', inputs=['node43'], outputs=['node44'], name='op27')
node_list.append(op27)
node45 = helper.make_tensor_value_info('node45', 1, [1, 4, 1, 1])
op28 = helper.make_node('Tanh', inputs=['node44'], outputs=['node45'], name='op28')
node_list.append(op28)
node46 = helper.make_tensor_value_info('node46', 1, [1, 4, 1, 1])
node47 = helper.make_tensor_value_info('node47', 1, [1, 4, 1, 1])
node48 = helper.make_tensor_value_info('node48', 1, [1, 4, 1, 1])
op29 = helper.make_node('Min', inputs=['node45', 'node44', 'node46', 'node47', 'node44', 'node45', 'node45', 'node45'], outputs=['node48'], name='op29')
node_list.append(op29)
node49 = helper.make_tensor_value_info('node49', 1, [1, 4, 1, 1])
op30 = helper.make_node('Cos', inputs=['node48'], outputs=['node49'], name='op30')
node_list.append(op30)
node50 = helper.make_tensor_value_info('node50', 7, [4])
init_tensor.append(helper.make_tensor('node50', 7, dims=(4,), vals=[2, 1, 1, 3]))
node51 = helper.make_tensor_value_info('node51', 1, [2, 4, 1, 3])
op31 = helper.make_node('Expand', inputs=['node48', 'node50'], outputs=['node51'], name='op31')
node_list.append(op31)
node52 = helper.make_tensor_value_info('node52', 7, [1])
init_tensor.append(helper.make_tensor('node52', 7, dims=(1,), vals=[0]))
node53 = helper.make_tensor_value_info('node53', 1, [2, 4, 1, 3])
op32 = helper.make_node('Gather', inputs=['node51', 'node52'], outputs=['node53'], name='op32', axis=2)
node_list.append(op32)
node54 = helper.make_tensor_value_info('node54', 1, [4])
node55 = helper.make_tensor_value_info('node55', 1, [4])
node56 = helper.make_tensor_value_info('node56', 1, [4])
node57 = helper.make_tensor_value_info('node57', 1, [4])
node58 = helper.make_tensor_value_info('node58', 1, [2, 4, 1, 3])
op33 = helper.make_node('BatchNormalization', inputs=['node53', 'node54', 'node55', 'node56', 'node57'], outputs=['node58'], name='op33')
node_list.append(op33)
node59 = helper.make_tensor_value_info('node59', 1, [4, 1, 1, 2])
node60 = helper.make_tensor_value_info('node60', 1, [2, 1, 1, 8])
op34 = helper.make_node('ConvTranspose', inputs=['node58', 'node59'], outputs=['node60'], name='op34', kernel_shape=[1, 2], strides=[1, 3], pads=[0, 0, 0, 0], group=1)
node_list.append(op34)
node61 = helper.make_tensor_value_info('node61', 1, [2, 4, 1, 3])
op35 = helper.make_node('Erf', inputs=['node58'], outputs=['node61'], name='op35')
node_list.append(op35)
node62 = helper.make_tensor_value_info('node62', 1, [2, 1, 1, 8])
op36 = helper.make_node('Dropout', inputs=['node60'], outputs=['node62'], name='op36')
node_list.append(op36)
node63 = helper.make_tensor_value_info('node63', 1, [2, 3])
node64 = helper.make_tensor_value_info('node64', 1, [2, 3])
node65 = helper.make_tensor_value_info('node65', 1, [2, 3])
op37 = helper.make_node('PRelu', inputs=['node63', 'node64'], outputs=['node65'], name='op37')
node_list.append(op37)
node66 = helper.make_tensor_value_info('node66', 1, [2, 3])
op38 = helper.make_node('PRelu', inputs=['node65', 'node65'], outputs=['node66'], name='op38')
node_list.append(op38)
node67 = helper.make_tensor_value_info('node67', 1, [1, 3])
op39 = helper.make_node('ReduceL2', inputs=['node65'], outputs=['node67'], name='op39', axes=[0])
node_list.append(op39)
node68 = helper.make_tensor_value_info('node68', 1, [2, 3])
op40 = helper.make_node('Sign', inputs=['node66'], outputs=['node68'], name='op40')
node_list.append(op40)
node69 = helper.make_tensor_value_info('node69', 7, [2])
init_tensor.append(helper.make_tensor('node69', 7, dims=(2,), vals=[1, 1]))
node70 = helper.make_tensor_value_info('node70', 1, [1, 3])
op41 = helper.make_node('Expand', inputs=['node67', 'node69'], outputs=['node70'], name='op41')
node_list.append(op41)
node71 = helper.make_tensor_value_info('node71', 1, [1, 3, 1])
node72 = helper.make_tensor_value_info('node72', 1, [1, 3, 1])
op42 = helper.make_node('ReduceL1', inputs=['node71'], outputs=['node72'], name='op42', axes=[0, 2])
node_list.append(op42)
node73 = helper.make_tensor_value_info('node73', 1, [3, 1, 1, 1, 1])
op43 = helper.make_node('AveragePool', inputs=['node31'], outputs=['node73'], name='op43', kernel_shape=[5, 1, 3], strides=[1, 1, 3])
node_list.append(op43)
node74 = helper.make_tensor_value_info('node74', 1, [3, 1, 1, 1, 1])
op44 = helper.make_node('Softsign', inputs=['node73'], outputs=['node74'], name='op44')
node_list.append(op44)
node75 = helper.make_tensor_value_info('node75', 1, [3, 1, 1, 1, 1])
op45 = helper.make_node('Cos', inputs=['node73'], outputs=['node75'], name='op45')
node_list.append(op45)
node76 = helper.make_tensor_value_info('node76', 1, [4, 3, 2, 3, 2])
node77 = helper.make_tensor_value_info('node77', 1, [12, 12])
op46 = helper.make_node('Flatten', inputs=['node76'], outputs=['node77'], name='op46', axis=2)
node_list.append(op46)
node78 = helper.make_tensor_value_info('node78', 1, [1, 1, 1, 1, 1])
node79 = helper.make_tensor_value_info('node79', 1, [3, 1, 1, 1, 1])
op47 = helper.make_node('ConvTranspose', inputs=['node75', 'node78'], outputs=['node79'], name='op47', kernel_shape=[1, 1, 1], strides=[1, 1, 1], pads=[0, 0, 0, 0, 0, 0])
node_list.append(op47)
node80 = helper.make_tensor_value_info('node80', 1, [1, 12])
op48 = helper.make_node('ReduceProd', inputs=['node77'], outputs=['node80'], name='op48', axes=[0])
node_list.append(op48)
node81 = helper.make_tensor_value_info('node81', 1, [3, 1, 1, 1, 1])
node82 = helper.make_tensor_value_info('node82', 1, [3, 1, 1, 1, 1])
node83 = helper.make_tensor_value_info('node83', 1, [3, 1, 1, 1, 1])
op49 = helper.make_node('Mean', inputs=['node79', 'node79', 'node79', 'node79', 'node79', 'node79', 'node81', 'node79', 'node82'], outputs=['node83'], name='op49')
node_list.append(op49)
node84 = helper.make_tensor_value_info('node84', 1, [5])
init_tensor.append(helper.make_tensor('node84', 1, dims=(5,), vals=[1.0, 1.0, 1.0, 1.0, 1.0]))
node85 = helper.make_tensor_value_info('node85', 1, [10])
init_tensor.append(helper.make_tensor('node85', 1, dims=(1, 10), vals=[0, 0, 0, 0, 0, 1, 1, 1, 1, 1]))
node86 = helper.make_tensor_value_info('node86', 1, [3, 1, 1, 1, 1])
op50 = helper.make_node('Resize', inputs=['node75', 'node85', 'node84'], outputs=['node86'], name='op50', mode='nearest')
node_list.append(op50)
node87 = helper.make_tensor_value_info('node87', 1, [3, 1, 1, 1, 1])
op51 = helper.make_node('Div', inputs=['node79', 'node83'], outputs=['node87'], name='op51')
node_list.append(op51)
node88 = helper.make_tensor_value_info('node88', 1, [3, 1, 1, 1, 1])
op52 = helper.make_node('Max', inputs=['node86', 'node86'], outputs=['node88'], name='op52')
node_list.append(op52)
node89 = helper.make_tensor_value_info('node89', 7, [5])
init_tensor.append(helper.make_tensor('node89', 7, dims=(5,), vals=[1, 4, 1, 1, 1]))
node90 = helper.make_tensor_value_info('node90', 1, [3, 4, 1, 1, 1])
op53 = helper.make_node('Expand', inputs=['node87', 'node89'], outputs=['node90'], name='op53')
node_list.append(op53)
node91 = helper.make_tensor_value_info('node91', 1, [3, 4, 1, 1, 1])
op54 = helper.make_node('Erf', inputs=['node90'], outputs=['node91'], name='op54')
node_list.append(op54)
node92 = helper.make_tensor_value_info('node92', 1, [4])
node93 = helper.make_tensor_value_info('node93', 1, [4])
node94 = helper.make_tensor_value_info('node94', 1, [4])
node95 = helper.make_tensor_value_info('node95', 1, [4])
node96 = helper.make_tensor_value_info('node96', 1, [3, 4, 1, 1, 1])
op55 = helper.make_node('BatchNormalization', inputs=['node90', 'node92', 'node93', 'node94', 'node95'], outputs=['node96'], name='op55')
node_list.append(op55)
node97 = helper.make_tensor_value_info('node97', 1, [3, 4, 1, 1, 1])
op56 = helper.make_node('PRelu', inputs=['node91', 'node91'], outputs=['node97'], name='op56')
node_list.append(op56)
node98 = helper.make_tensor_value_info('node98', 1, [5])
init_tensor.append(helper.make_tensor('node98', 1, dims=(5,), vals=[1.0, 1.0, 1.0, 1.0, 1.0]))
node99 = helper.make_tensor_value_info('node99', 1, [10])
init_tensor.append(helper.make_tensor('node99', 1, dims=(1, 10), vals=[0, 0, 0, 0, 0, 1, 1, 1, 1, 1]))
node100 = helper.make_tensor_value_info('node100', 1, [3, 4, 1, 1, 1])
op57 = helper.make_node('Resize', inputs=['node97', 'node99', 'node98'], outputs=['node100'], name='op57', mode='nearest')
node_list.append(op57)
node101 = helper.make_tensor_value_info('node101', 1, [1, 1, 1, 1, 1])
op58 = helper.make_node('ReduceMin', inputs=['node100'], outputs=['node101'], name='op58', axes=[0, 1, 4, 2, 3])
node_list.append(op58)
output_tensor.append(node49)
output_tensor.append(node37)
output_tensor.append(node61)
output_tensor.append(node21)
output_tensor.append(node80)
output_tensor.append(node68)
output_tensor.append(node70)
output_tensor.append(node74)
output_tensor.append(node96)
output_tensor.append(node24)
output_tensor.append(node88)
output_tensor.append(node26)
output_tensor.append(node62)
output_tensor.append(node72)
output_tensor.append(node39)
output_tensor.append(node19)
output_tensor.append(node101)
output_tensor.append(node11)
input_tensor.append(node1)
input_tensor.append(node4)
input_tensor.append(node13)
input_tensor.append(node14)
input_tensor.append(node15)
input_tensor.append(node16)
input_tensor.append(node17)
input_tensor.append(node27)
input_tensor.append(node32)
input_tensor.append(node34)
input_tensor.append(node46)
input_tensor.append(node47)
input_tensor.append(node54)
input_tensor.append(node55)
input_tensor.append(node56)
input_tensor.append(node57)
input_tensor.append(node59)
input_tensor.append(node63)
input_tensor.append(node64)
input_tensor.append(node71)
input_tensor.append(node76)
input_tensor.append(node78)
input_tensor.append(node81)
input_tensor.append(node82)
input_tensor.append(node92)
input_tensor.append(node93)
input_tensor.append(node94)
input_tensor.append(node95)
graph_def = helper.make_graph(node_list, 'test-model', input_tensor, output_tensor, init_tensor)
model = helper.make_model(graph_def, producer_name='onnx-example')
