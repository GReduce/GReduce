from onnx import helper
input_tensor = []
output_tensor = []
init_tensor = []
node_list = []

node1 = helper.make_tensor_value_info('node1', 1, [2, 3, 3, 2])
node2 = helper.make_tensor_value_info('node2', 1, [2, 3, 3, 2])
op0 = helper.make_node('Sqrt', inputs=['node1'], outputs=['node2'], name='op0')
node_list.append(op0)
node3 = helper.make_tensor_value_info('node3', 7, [4])
init_tensor.append(helper.make_tensor('node3', 7, dims=(4,), vals=[1, 2, 1, 1]))
node4 = helper.make_tensor_value_info('node4', 7, [4])
init_tensor.append(helper.make_tensor('node4', 7, dims=(4,), vals=[2, 3, 3, 2]))
node5 = helper.make_tensor_value_info('node5', 7, [4])
init_tensor.append(helper.make_tensor('node5', 7, dims=(4,), vals=[0, 1, 2, 3]))
node6 = helper.make_tensor_value_info('node6', 7, [4])
init_tensor.append(helper.make_tensor('node6', 7, dims=(4,), vals=[2, 1, 2, 3]))
node7 = helper.make_tensor_value_info('node7', 1, [1, 1, 1, 1])
op1 = helper.make_node('Slice', inputs=['node1', 'node3', 'node4', 'node5', 'node6'], outputs=['node7'], name='op1')
node_list.append(op1)
node8 = helper.make_tensor_value_info('node8', 1, [2, 3, 3, 2])
op2 = helper.make_node('ThresholdedRelu', inputs=['node2'], outputs=['node8'], name='op2', alpha=1.0)
node_list.append(op2)
node9 = helper.make_tensor_value_info('node9', 7, [4])
init_tensor.append(helper.make_tensor('node9', 7, dims=(4,), vals=[1, 1, 1, 1]))
node10 = helper.make_tensor_value_info('node10', 1, [2, 3, 3, 2])
op3 = helper.make_node('Expand', inputs=['node8', 'node9'], outputs=['node10'], name='op3')
node_list.append(op3)
node11 = helper.make_tensor_value_info('node11', 7, [4])
init_tensor.append(helper.make_tensor('node11', 7, dims=(4,), vals=[0, 1, 1, 1]))
node12 = helper.make_tensor_value_info('node12', 7, [4])
init_tensor.append(helper.make_tensor('node12', 7, dims=(4,), vals=[2, 3, 3, 2]))
node13 = helper.make_tensor_value_info('node13', 7, [4])
init_tensor.append(helper.make_tensor('node13', 7, dims=(4,), vals=[0, 1, 2, 3]))
node14 = helper.make_tensor_value_info('node14', 7, [4])
init_tensor.append(helper.make_tensor('node14', 7, dims=(4,), vals=[1, 2, 2, 1]))
node15 = helper.make_tensor_value_info('node15', 1, [2, 1, 1, 1])
op4 = helper.make_node('Slice', inputs=['node10', 'node11', 'node12', 'node13', 'node14'], outputs=['node15'], name='op4')
node_list.append(op4)
node16 = helper.make_tensor_value_info('node16', 1, [2, 3, 3, 2])
op5 = helper.make_node('PRelu', inputs=['node10', 'node10'], outputs=['node16'], name='op5')
node_list.append(op5)
node17 = helper.make_tensor_value_info('node17', 1, [2, 3, 2, 2])
op6 = helper.make_node('MaxPool', inputs=['node16'], outputs=['node17'], name='op6', kernel_shape=[1, 1], strides=[2, 1])
node_list.append(op6)
node18 = helper.make_tensor_value_info('node18', 7, [1])
init_tensor.append(helper.make_tensor('node18', 7, dims=(1,), vals=[3]))
node19 = helper.make_tensor_value_info('node19', 1, [2, 3, 3, 1, 2])
op7 = helper.make_node('Unsqueeze', inputs=['node16', 'node18'], outputs=['node19'], name='op7')
node_list.append(op7)
node20 = helper.make_tensor_value_info('node20', 1, [2, 1, 2, 2])
node21 = helper.make_tensor_value_info('node21', 1, [2, 1, 2, 2])
node22 = helper.make_tensor_value_info('node22', 1, [2, 1, 2, 2])
node23 = helper.make_tensor_value_info('node23', 7, [3])
init_tensor.append(helper.make_tensor('node23', 7, dims=(3,), vals=[1, 1, 1]))
op8 = helper.make_node('Split', inputs=['node17', 'node23'], outputs=['node20', 'node21', 'node22'], name='op8', axis=1)
node_list.append(op8)
node24 = helper.make_tensor_value_info('node24', 7, [4])
init_tensor.append(helper.make_tensor('node24', 7, dims=(4,), vals=[8, 1, 1, 1]))
node25 = helper.make_tensor_value_info('node25', 1, [8, 1, 1, 1])
op9 = helper.make_node('Reshape', inputs=['node22', 'node24'], outputs=['node25'], name='op9')
node_list.append(op9)
node26 = helper.make_tensor_value_info('node26', 1, [2, 1, 2, 1])
op10 = helper.make_node('ReduceL2', inputs=['node22'], outputs=['node26'], name='op10', axes=[3, 1])
node_list.append(op10)
node27 = helper.make_tensor_value_info('node27', 1, [2, 1, 2, 1])
op11 = helper.make_node('SpaceToDepth', inputs=['node26'], outputs=['node27'], name='op11', blocksize=1)
node_list.append(op11)
node28 = helper.make_tensor_value_info('node28', 1, [2, 1, 2, 1])
op12 = helper.make_node('ThresholdedRelu', inputs=['node27'], outputs=['node28'], name='op12')
node_list.append(op12)
node29 = helper.make_tensor_value_info('node29', 7, [3])
init_tensor.append(helper.make_tensor('node29', 7, dims=(3,), vals=[1, 1, 1]))
node30 = helper.make_tensor_value_info('node30', 1, [3, 1, 2, 1])
op13 = helper.make_node('Gather', inputs=['node27', 'node29'], outputs=['node30'], name='op13', axis=0)
node_list.append(op13)
node31 = helper.make_tensor_value_info('node31', 1, [2, 1, 2, 1])
op14 = helper.make_node('Relu', inputs=['node28'], outputs=['node31'], name='op14')
node_list.append(op14)
node32 = helper.make_tensor_value_info('node32', 1, [2, 1, 2, 1])
op15 = helper.make_node('Round', inputs=['node31'], outputs=['node32'], name='op15')
node_list.append(op15)
node33 = helper.make_tensor_value_info('node33', 1, [2, 1, 2, 1])
op16 = helper.make_node('Add', inputs=['node32', 'node31'], outputs=['node33'], name='op16')
node_list.append(op16)
node34 = helper.make_tensor_value_info('node34', 1, [2, 1, 2, 1])
op17 = helper.make_node('Reciprocal', inputs=['node32'], outputs=['node34'], name='op17')
node_list.append(op17)
node35 = helper.make_tensor_value_info('node35', 7, [4])
init_tensor.append(helper.make_tensor('node35', 7, dims=(4,), vals=[0, 0, 0, 0]))
node36 = helper.make_tensor_value_info('node36', 7, [4])
init_tensor.append(helper.make_tensor('node36', 7, dims=(4,), vals=[1, 1, 1, 1]))
node37 = helper.make_tensor_value_info('node37', 7, [4])
init_tensor.append(helper.make_tensor('node37', 7, dims=(4,), vals=[0, 1, 2, 3]))
node38 = helper.make_tensor_value_info('node38', 7, [4])
init_tensor.append(helper.make_tensor('node38', 7, dims=(4,), vals=[3, 3, 1, 3]))
node39 = helper.make_tensor_value_info('node39', 1, [1, 1, 1, 1])
op18 = helper.make_node('Slice', inputs=['node34', 'node35', 'node36', 'node37', 'node38'], outputs=['node39'], name='op18')
node_list.append(op18)
node40 = helper.make_tensor_value_info('node40', 1, [2, 1, 2, 1])
op19 = helper.make_node('Neg', inputs=['node34'], outputs=['node40'], name='op19')
node_list.append(op19)
node41 = helper.make_tensor_value_info('node41', 1, [4, 3, 3, 4])
node42 = helper.make_tensor_value_info('node42', 1, [3, 1, 3, 2])
node43 = helper.make_tensor_value_info('node43', 1, [4, 1, 9, 14])
op20 = helper.make_node('ConvTranspose', inputs=['node41', 'node42'], outputs=['node43'], name='op20', kernel_shape=[3, 2], strides=[3, 4], pads=[0, 0, 0, 0], group=1)
node_list.append(op20)
node44 = helper.make_tensor_value_info('node44', 1, [2, 1, 2, 1])
op21 = helper.make_node('Relu', inputs=['node40'], outputs=['node44'], name='op21')
node_list.append(op21)
node45 = helper.make_tensor_value_info('node45', 1, [1, 1, 2, 1])
node46 = helper.make_tensor_value_info('node46', 1, [2, 1, 3, 1])
op22 = helper.make_node('ConvTranspose', inputs=['node26', 'node45'], outputs=['node46'], name='op22', kernel_shape=[2, 1], strides=[1, 1], pads=[0, 0, 0, 0], group=1)
node_list.append(op22)
node47 = helper.make_tensor_value_info('node47', 7, [8])
init_tensor.append(helper.make_tensor('node47', 7, dims=(8,), vals=[0, 0, 0, 2, 1, 2, 1, 1]))
node48 = helper.make_tensor_value_info('node48', 1, [3, 3, 4, 4])
op23 = helper.make_node('Pad', inputs=['node46', 'node47'], outputs=['node48'], name='op23', mode='constant')
node_list.append(op23)
node49 = helper.make_tensor_value_info('node49', 1, [2, 1, 1, 1])
op24 = helper.make_node('AveragePool', inputs=['node46'], outputs=['node49'], name='op24', kernel_shape=[2, 1], strides=[2, 1])
node_list.append(op24)
node50 = helper.make_tensor_value_info('node50', 1, [2, 1, 1, 1])
op25 = helper.make_node('Softsign', inputs=['node49'], outputs=['node50'], name='op25')
node_list.append(op25)
node51 = helper.make_tensor_value_info('node51', 1, [2, 1, 1, 1])
op26 = helper.make_node('ThresholdedRelu', inputs=['node50'], outputs=['node51'], name='op26', alpha=2.0)
node_list.append(op26)
node52 = helper.make_tensor_value_info('node52', 1, [2, 1])
op27 = helper.make_node('Flatten', inputs=['node50'], outputs=['node52'], name='op27', axis=2)
node_list.append(op27)
node53 = helper.make_tensor_value_info('node53', 7, [1])
init_tensor.append(helper.make_tensor('node53', 7, dims=(1,), vals=[0]))
node54 = helper.make_tensor_value_info('node54', 1, [1, 1])
op28 = helper.make_node('ReduceSum', inputs=['node52', 'node53'], outputs=['node54'], name='op28')
node_list.append(op28)
node55 = helper.make_tensor_value_info('node55', 1, [4])
init_tensor.append(helper.make_tensor('node55', 1, dims=(4,), vals=[1.0, 1.0, 1.0, 1.0]))
node56 = helper.make_tensor_value_info('node56', 1, [8])
init_tensor.append(helper.make_tensor('node56', 1, dims=(1, 8), vals=[0, 0, 0, 0, 1, 1, 1, 1]))
node57 = helper.make_tensor_value_info('node57', 1, [2, 3, 3, 2])
op29 = helper.make_node('Resize', inputs=['node16', 'node56', 'node55'], outputs=['node57'], name='op29', mode='nearest')
node_list.append(op29)
node58 = helper.make_tensor_value_info('node58', 1, [4])
node59 = helper.make_tensor_value_info('node59', 1, [4])
op30 = helper.make_node('Elu', inputs=['node58'], outputs=['node59'], name='op30', alpha=1.0)
node_list.append(op30)
node60 = helper.make_tensor_value_info('node60', 1, [1])
op31 = helper.make_node('ReduceLogSumExp', inputs=['node59'], outputs=['node60'], name='op31', axes=[0])
node_list.append(op31)
node61 = helper.make_tensor_value_info('node61', 1, [4])
op32 = helper.make_node('ThresholdedRelu', inputs=['node59'], outputs=['node61'], name='op32')
node_list.append(op32)
node62 = helper.make_tensor_value_info('node62', 1, [1])
node63 = helper.make_tensor_value_info('node63', 1, [2])
node64 = helper.make_tensor_value_info('node64', 1, [1])
node65 = helper.make_tensor_value_info('node65', 7, [3])
init_tensor.append(helper.make_tensor('node65', 7, dims=(3,), vals=[1, 2, 1]))
op33 = helper.make_node('Split', inputs=['node61', 'node65'], outputs=['node62', 'node63', 'node64'], name='op33')
node_list.append(op33)
node66 = helper.make_tensor_value_info('node66', 1, [2])
op34 = helper.make_node('Add', inputs=['node63', 'node63'], outputs=['node66'], name='op34')
node_list.append(op34)
node67 = helper.make_tensor_value_info('node67', 1, [1])
op35 = helper.make_node('ReduceLogSumExp', inputs=['node64'], outputs=['node67'], name='op35', axes=[0])
node_list.append(op35)
node68 = helper.make_tensor_value_info('node68', 1, [1])
node69 = helper.make_tensor_value_info('node69', 1, [1])
op36 = helper.make_node('Add', inputs=['node67', 'node68'], outputs=['node69'], name='op36')
node_list.append(op36)
node70 = helper.make_tensor_value_info('node70', 1, [2, 1, 2, 2])
op37 = helper.make_node('ConvTranspose', inputs=['node22', 'node39'], outputs=['node70'], name='op37', kernel_shape=[1, 1], strides=[1, 1], pads=[0, 0, 0, 0])
node_list.append(op37)
node71 = helper.make_tensor_value_info('node71', 1, [1])
op38 = helper.make_node('ReduceSumSquare', inputs=['node69'], outputs=['node71'], name='op38', axes=[0])
node_list.append(op38)
node72 = helper.make_tensor_value_info('node72', 1, [2, 1, 2, 2])
node73 = helper.make_tensor_value_info('node73', 1, [2, 1, 2, 2])
op39 = helper.make_node('Max', inputs=['node70', 'node70', 'node70', 'node72', 'node70', 'node70', 'node70', 'node70', 'node70', 'node70'], outputs=['node73'], name='op39')
node_list.append(op39)
node74 = helper.make_tensor_value_info('node74', 1, [3, 2, 1, 5, 5])
node75 = helper.make_tensor_value_info('node75', 1, [3, 2, 1, 5, 5])
node76 = helper.make_tensor_value_info('node76', 1, [3, 2, 1, 5, 5])
op40 = helper.make_node('Add', inputs=['node74', 'node75'], outputs=['node76'], name='op40')
node_list.append(op40)
node77 = helper.make_tensor_value_info('node77', 1, [3, 2, 1, 5, 5])
op41 = helper.make_node('Selu', inputs=['node76'], outputs=['node77'], name='op41')
node_list.append(op41)
node78 = helper.make_tensor_value_info('node78', 1, [3, 2, 1, 5, 5])
op42 = helper.make_node('Sin', inputs=['node77'], outputs=['node78'], name='op42')
node_list.append(op42)
node79 = helper.make_tensor_value_info('node79', 1, [3, 2, 1, 5, 5])
op43 = helper.make_node('Round', inputs=['node78'], outputs=['node79'], name='op43')
node_list.append(op43)
node80 = helper.make_tensor_value_info('node80', 1, [3, 1, 1, 1, 1])
op44 = helper.make_node('ReduceL1', inputs=['node79'], outputs=['node80'], name='op44', axes=[2, 3, 1, 4])
node_list.append(op44)
node81 = helper.make_tensor_value_info('node81', 1, [3, 1, 1, 1, 1])
op45 = helper.make_node('LpPool', inputs=['node80'], outputs=['node81'], name='op45', kernel_shape=[1, 1, 1], strides=[1, 1, 1])
node_list.append(op45)
node82 = helper.make_tensor_value_info('node82', 7, [5])
init_tensor.append(helper.make_tensor('node82', 7, dims=(5,), vals=[1, 1, 1, 2, 3]))
node83 = helper.make_tensor_value_info('node83', 1, [3, 1, 1, 2, 3])
op46 = helper.make_node('Expand', inputs=['node81', 'node82'], outputs=['node83'], name='op46')
node_list.append(op46)
node84 = helper.make_tensor_value_info('node84', 1, [3, 1, 1, 2, 3])
op47 = helper.make_node('Relu', inputs=['node83'], outputs=['node84'], name='op47')
node_list.append(op47)
node85 = helper.make_tensor_value_info('node85', 1, [1])
op48 = helper.make_node('Elu', inputs=['node71'], outputs=['node85'], name='op48', alpha=0.5)
node_list.append(op48)
node86 = helper.make_tensor_value_info('node86', 1, [1, 1, 1, 2, 1])
op49 = helper.make_node('ReduceMin', inputs=['node84'], outputs=['node86'], name='op49', axes=[4, 0, 1])
node_list.append(op49)
node87 = helper.make_tensor_value_info('node87', 1, [1])
op50 = helper.make_node('Ceil', inputs=['node85'], outputs=['node87'], name='op50')
node_list.append(op50)
node88 = helper.make_tensor_value_info('node88', 1, [1, 1, 1, 2, 1])
op51 = helper.make_node('Floor', inputs=['node86'], outputs=['node88'], name='op51')
node_list.append(op51)
node89 = helper.make_tensor_value_info('node89', 1, [1])
op52 = helper.make_node('Mean', inputs=['node87', 'node87', 'node87', 'node87'], outputs=['node89'], name='op52')
node_list.append(op52)
node90 = helper.make_tensor_value_info('node90', 1, [1, 1])
op53 = helper.make_node('Flatten', inputs=['node89'], outputs=['node90'], name='op53', axis=0)
node_list.append(op53)
node91 = helper.make_tensor_value_info('node91', 1, [1])
op54 = helper.make_node('Sum', inputs=['node85', 'node89', 'node89', 'node89'], outputs=['node91'], name='op54')
node_list.append(op54)
node92 = helper.make_tensor_value_info('node92', 1, [1, 1])
op55 = helper.make_node('ReduceLogSumExp', inputs=['node90'], outputs=['node92'], name='op55', axes=[1])
node_list.append(op55)
node93 = helper.make_tensor_value_info('node93', 7, [2])
init_tensor.append(helper.make_tensor('node93', 7, dims=(2,), vals=[1, 2]))
node94 = helper.make_tensor_value_info('node94', 1, [1, 2])
op56 = helper.make_node('Tile', inputs=['node92', 'node93'], outputs=['node94'], name='op56')
node_list.append(op56)
node95 = helper.make_tensor_value_info('node95', 7, [5])
init_tensor.append(helper.make_tensor('node95', 7, dims=(5,), vals=[1, 1, 1, 1, 1]))
node96 = helper.make_tensor_value_info('node96', 1, [1, 1, 1, 1, 1])
op57 = helper.make_node('Reshape', inputs=['node92', 'node95'], outputs=['node96'], name='op57')
node_list.append(op57)
node97 = helper.make_tensor_value_info('node97', 7, [10])
init_tensor.append(helper.make_tensor('node97', 7, dims=(10,), vals=[0, 0, 1, 0, 1, 0, 1, 1, 1, 0]))
node98 = helper.make_tensor_value_info('node98', 1, [1, 2, 3, 2, 2])
op58 = helper.make_node('Pad', inputs=['node96', 'node97'], outputs=['node98'], name='op58', mode='constant')
node_list.append(op58)
node99 = helper.make_tensor_value_info('node99', 7, [5])
init_tensor.append(helper.make_tensor('node99', 7, dims=(5,), vals=[2, 1, 1, 1, 1]))
node100 = helper.make_tensor_value_info('node100', 1, [2, 2, 3, 2, 2])
op59 = helper.make_node('Expand', inputs=['node98', 'node99'], outputs=['node100'], name='op59')
node_list.append(op59)
node101 = helper.make_tensor_value_info('node101', 1, [2, 2, 3, 2, 2])
op60 = helper.make_node('Identity', inputs=['node100'], outputs=['node101'], name='op60')
node_list.append(op60)
node102 = helper.make_tensor_value_info('node102', 1, [2, 1, 1, 1, 1])
op61 = helper.make_node('ReduceL1', inputs=['node100'], outputs=['node102'], name='op61', axes=[2, 3, 4, 1])
node_list.append(op61)
node103 = helper.make_tensor_value_info('node103', 1, [2, 1, 1, 1, 1])
op62 = helper.make_node('Tanh', inputs=['node102'], outputs=['node103'], name='op62')
node_list.append(op62)
node104 = helper.make_tensor_value_info('node104', 1, [2, 1, 1, 1, 1])
op63 = helper.make_node('Softsign', inputs=['node103'], outputs=['node104'], name='op63')
node_list.append(op63)
node105 = helper.make_tensor_value_info('node105', 1, [2, 1, 1, 1, 1])
op64 = helper.make_node('Sign', inputs=['node104'], outputs=['node105'], name='op64')
node_list.append(op64)
node106 = helper.make_tensor_value_info('node106', 1, [1, 1, 1, 1, 1])
op65 = helper.make_node('ReduceL2', inputs=['node105'], outputs=['node106'], name='op65', axes=[0, 1, 3, 2, 4])
node_list.append(op65)
node107 = helper.make_tensor_value_info('node107', 1, [2, 1, 1, 1, 1])
op66 = helper.make_node('BatchNormalization', inputs=['node105', 'node60', 'node91', 'node85', 'node67'], outputs=['node107'], name='op66')
node_list.append(op66)
node108 = helper.make_tensor_value_info('node108', 1, [2, 1, 1, 1, 1])
op67 = helper.make_node('Tanh', inputs=['node107'], outputs=['node108'], name='op67')
node_list.append(op67)
node109 = helper.make_tensor_value_info('node109', 1, [2, 1, 1, 1, 1])
op68 = helper.make_node('Identity', inputs=['node107'], outputs=['node109'], name='op68')
node_list.append(op68)
node110 = helper.make_tensor_value_info('node110', 7, [1])
init_tensor.append(helper.make_tensor('node110', 7, dims=(1,), vals=[2]))
node111 = helper.make_tensor_value_info('node111', 1, [2])
op69 = helper.make_node('Reshape', inputs=['node108', 'node110'], outputs=['node111'], name='op69')
node_list.append(op69)
node112 = helper.make_tensor_value_info('node112', 1, [1, 3, 2])
node113 = helper.make_tensor_value_info('node113', 1, [1, 3, 2])
node114 = helper.make_tensor_value_info('node114', 1, [1, 1, 1])
op70 = helper.make_node('Conv', inputs=['node112', 'node113'], outputs=['node114'], name='op70', kernel_shape=[2], strides=[1], pads=[0, 0], group=1)
node_list.append(op70)
output_tensor.append(node44)
output_tensor.append(node94)
output_tensor.append(node109)
output_tensor.append(node30)
output_tensor.append(node51)
output_tensor.append(node19)
output_tensor.append(node48)
output_tensor.append(node106)
output_tensor.append(node73)
output_tensor.append(node114)
output_tensor.append(node25)
output_tensor.append(node15)
output_tensor.append(node33)
output_tensor.append(node20)
output_tensor.append(node21)
output_tensor.append(node101)
output_tensor.append(node66)
output_tensor.append(node111)
output_tensor.append(node62)
output_tensor.append(node57)
output_tensor.append(node43)
output_tensor.append(node88)
output_tensor.append(node7)
output_tensor.append(node54)
input_tensor.append(node1)
input_tensor.append(node41)
input_tensor.append(node42)
input_tensor.append(node45)
input_tensor.append(node58)
input_tensor.append(node68)
input_tensor.append(node72)
input_tensor.append(node74)
input_tensor.append(node75)
input_tensor.append(node112)
input_tensor.append(node113)
graph_def = helper.make_graph(node_list, 'test-model', input_tensor, output_tensor, init_tensor)
model = helper.make_model(graph_def, producer_name='onnx-example')
