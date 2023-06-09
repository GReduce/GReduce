from onnx import helper
input_tensor = []
output_tensor = []
init_tensor = []
node_list = []

node1 = helper.make_tensor_value_info('node1', 1, [1])
node2 = helper.make_tensor_value_info('node2', 1, [4])
node3 = helper.make_tensor_value_info('node3', 1, [5])
op0 = helper.make_node('Concat', inputs=['node1', 'node2'], outputs=['node3'], name='op0', axis=0)
node_list.append(op0)
node4 = helper.make_tensor_value_info('node4', 1, [5])
op1 = helper.make_node('Softmax', inputs=['node3'], outputs=['node4'], name='op1', axis=0)
node_list.append(op1)
node5 = helper.make_tensor_value_info('node5', 1, [5])
op2 = helper.make_node('Mean', inputs=['node3', 'node3', 'node3', 'node4', 'node4', 'node3', 'node4', 'node4', 'node3', 'node4'], outputs=['node5'], name='op2')
node_list.append(op2)
node6 = helper.make_tensor_value_info('node6', 1, [5])
op3 = helper.make_node('Sub', inputs=['node4', 'node4'], outputs=['node6'], name='op3')
node_list.append(op3)
node7 = helper.make_tensor_value_info('node7', 1, [5])
op4 = helper.make_node('Erf', inputs=['node5'], outputs=['node7'], name='op4')
node_list.append(op4)
node8 = helper.make_tensor_value_info('node8', 1, [5])
op5 = helper.make_node('Floor', inputs=['node7'], outputs=['node8'], name='op5')
node_list.append(op5)
node9 = helper.make_tensor_value_info('node9', 1, [5])
op6 = helper.make_node('Transpose', inputs=['node7'], outputs=['node9'], name='op6', perm=[0])
node_list.append(op6)
node10 = helper.make_tensor_value_info('node10', 7, [1])
init_tensor.append(helper.make_tensor('node10', 7, dims=(1,), vals=[1]))
node11 = helper.make_tensor_value_info('node11', 1, [5])
op7 = helper.make_node('Tile', inputs=['node9', 'node10'], outputs=['node11'], name='op7')
node_list.append(op7)
node12 = helper.make_tensor_value_info('node12', 1, [1, 1, 5])
node13 = helper.make_tensor_value_info('node13', 1, [1, 1, 5])
op8 = helper.make_node('BatchNormalization', inputs=['node12', 'node1', 'node1', 'node1', 'node1'], outputs=['node13'], name='op8')
node_list.append(op8)
node14 = helper.make_tensor_value_info('node14', 1, [5])
op9 = helper.make_node('Erf', inputs=['node11'], outputs=['node14'], name='op9')
node_list.append(op9)
node15 = helper.make_tensor_value_info('node15', 1, [1, 1, 5])
op10 = helper.make_node('Mean', inputs=['node13', 'node13', 'node13', 'node13', 'node13', 'node13', 'node13', 'node13', 'node13'], outputs=['node15'], name='op10')
node_list.append(op10)
node16 = helper.make_tensor_value_info('node16', 1, [1, 1, 5])
op11 = helper.make_node('Mul', inputs=['node15', 'node15'], outputs=['node16'], name='op11')
node_list.append(op11)
node17 = helper.make_tensor_value_info('node17', 7, [1])
init_tensor.append(helper.make_tensor('node17', 7, dims=(1,), vals=[2]))
node18 = helper.make_tensor_value_info('node18', 7, [1])
init_tensor.append(helper.make_tensor('node18', 7, dims=(1,), vals=[4]))
node19 = helper.make_tensor_value_info('node19', 7, [1])
init_tensor.append(helper.make_tensor('node19', 7, dims=(1,), vals=[0]))
node20 = helper.make_tensor_value_info('node20', 7, [1])
init_tensor.append(helper.make_tensor('node20', 7, dims=(1,), vals=[3]))
node21 = helper.make_tensor_value_info('node21', 1, [1])
op12 = helper.make_node('Slice', inputs=['node11', 'node17', 'node18', 'node19', 'node20'], outputs=['node21'], name='op12')
node_list.append(op12)
node22 = helper.make_tensor_value_info('node22', 1, [1])
op13 = helper.make_node('Cos', inputs=['node21'], outputs=['node22'], name='op13')
node_list.append(op13)
node23 = helper.make_tensor_value_info('node23', 1, [1])
op14 = helper.make_node('Cos', inputs=['node22'], outputs=['node23'], name='op14')
node_list.append(op14)
node24 = helper.make_tensor_value_info('node24', 1, [1])
op15 = helper.make_node('Dropout', inputs=['node23'], outputs=['node24'], name='op15')
node_list.append(op15)
node25 = helper.make_tensor_value_info('node25', 1, [1])
op16 = helper.make_node('ReduceMean', inputs=['node24'], outputs=['node25'], name='op16', axes=[0])
node_list.append(op16)
node26 = helper.make_tensor_value_info('node26', 1, [1])
op17 = helper.make_node('Add', inputs=['node25', 'node25'], outputs=['node26'], name='op17')
node_list.append(op17)
node27 = helper.make_tensor_value_info('node27', 1, [1])
op18 = helper.make_node('Sin', inputs=['node26'], outputs=['node27'], name='op18')
node_list.append(op18)
node28 = helper.make_tensor_value_info('node28', 1, [5, 2, 1, 3, 4])
node29 = helper.make_tensor_value_info('node29', 1, [5, 2, 1, 1, 1])
op19 = helper.make_node('GlobalMaxPool', inputs=['node28'], outputs=['node29'], name='op19')
node_list.append(op19)
node30 = helper.make_tensor_value_info('node30', 1, [1])
op20 = helper.make_node('Transpose', inputs=['node27'], outputs=['node30'], name='op20', perm=[0])
node_list.append(op20)
node31 = helper.make_tensor_value_info('node31', 1, [1])
op21 = helper.make_node('Selu', inputs=['node30'], outputs=['node31'], name='op21')
node_list.append(op21)
node32 = helper.make_tensor_value_info('node32', 1, [1])
op22 = helper.make_node('Tanh', inputs=['node31'], outputs=['node32'], name='op22')
node_list.append(op22)
node33 = helper.make_tensor_value_info('node33', 1, [5, 2, 1, 1, 1])
op23 = helper.make_node('LpPool', inputs=['node29'], outputs=['node33'], name='op23', kernel_shape=[1, 1, 1], strides=[1, 1, 1], p=2)
node_list.append(op23)
node34 = helper.make_tensor_value_info('node34', 1, [5, 2, 1, 1, 1])
op24 = helper.make_node('Neg', inputs=['node33'], outputs=['node34'], name='op24')
node_list.append(op24)
node35 = helper.make_tensor_value_info('node35', 1, [5, 5, 1, 1, 1])
op25 = helper.make_node('Conv', inputs=['node34', 'node33'], outputs=['node35'], name='op25', kernel_shape=[1, 1, 1], strides=[1, 1, 1], pads=[0, 0, 0, 0, 0, 0])
node_list.append(op25)
node36 = helper.make_tensor_value_info('node36', 1, [5, 2, 1, 1, 1])
op26 = helper.make_node('Neg', inputs=['node34'], outputs=['node36'], name='op26')
node_list.append(op26)
node37 = helper.make_tensor_value_info('node37', 1, [5, 5, 1, 1, 1])
op27 = helper.make_node('Div', inputs=['node35', 'node35'], outputs=['node37'], name='op27')
node_list.append(op27)
node38 = helper.make_tensor_value_info('node38', 1, [5, 5, 1, 1, 1])
node39 = helper.make_tensor_value_info('node39', 1, [5, 5, 1, 1, 1])
op28 = helper.make_node('Sum', inputs=['node37', 'node37', 'node37', 'node38', 'node37', 'node37', 'node37', 'node37', 'node37'], outputs=['node39'], name='op28')
node_list.append(op28)
node40 = helper.make_tensor_value_info('node40', 1, [5, 5, 1, 1, 1])
op29 = helper.make_node('Exp', inputs=['node39'], outputs=['node40'], name='op29')
node_list.append(op29)
node41 = helper.make_tensor_value_info('node41', 1, [1, 1, 1, 1, 1])
op30 = helper.make_node('ReduceSumSquare', inputs=['node39'], outputs=['node41'], name='op30', axes=[1, 3, 0])
node_list.append(op30)
node42 = helper.make_tensor_value_info('node42', 1, [1, 1, 1, 1, 1])
op31 = helper.make_node('Tanh', inputs=['node41'], outputs=['node42'], name='op31')
node_list.append(op31)
node43 = helper.make_tensor_value_info('node43', 1, [1, 1, 1, 1, 1])
op32 = helper.make_node('AveragePool', inputs=['node41'], outputs=['node43'], name='op32', kernel_shape=[1, 1, 1], strides=[1, 1, 1])
node_list.append(op32)
node44 = helper.make_tensor_value_info('node44', 1, [1, 1, 1, 1, 1])
op33 = helper.make_node('Round', inputs=['node43'], outputs=['node44'], name='op33')
node_list.append(op33)
node45 = helper.make_tensor_value_info('node45', 1, [1, 1, 1, 1, 1])
op34 = helper.make_node('MatMul', inputs=['node44', 'node44'], outputs=['node45'], name='op34')
node_list.append(op34)
node46 = helper.make_tensor_value_info('node46', 1, [1])
node47 = helper.make_tensor_value_info('node47', 1, [1])
op35 = helper.make_node('Mul', inputs=['node46', 'node1'], outputs=['node47'], name='op35')
node_list.append(op35)
node48 = helper.make_tensor_value_info('node48', 1, [1, 1, 1, 1, 1])
op36 = helper.make_node('GlobalMaxPool', inputs=['node45'], outputs=['node48'], name='op36')
node_list.append(op36)
node49 = helper.make_tensor_value_info('node49', 1, [1, 1, 4, 1, 1])
node50 = helper.make_tensor_value_info('node50', 1, [1, 1, 5, 1, 1])
op37 = helper.make_node('Concat', inputs=['node48', 'node49'], outputs=['node50'], name='op37', axis=2)
node_list.append(op37)
node51 = helper.make_tensor_value_info('node51', 1, [1, 1, 5, 1, 1])
op38 = helper.make_node('Neg', inputs=['node50'], outputs=['node51'], name='op38')
node_list.append(op38)
node52 = helper.make_tensor_value_info('node52', 1, [1, 1, 1, 1, 1])
op39 = helper.make_node('AveragePool', inputs=['node50'], outputs=['node52'], name='op39', kernel_shape=[5, 1, 1], strides=[2, 1, 1])
node_list.append(op39)
node53 = helper.make_tensor_value_info('node53', 1, [1])
op40 = helper.make_node('Elu', inputs=['node21'], outputs=['node53'], name='op40', alpha=1.0)
node_list.append(op40)
node54 = helper.make_tensor_value_info('node54', 1, [1])
op41 = helper.make_node('Cos', inputs=['node53'], outputs=['node54'], name='op41')
node_list.append(op41)
node55 = helper.make_tensor_value_info('node55', 1, [1])
op42 = helper.make_node('Sum', inputs=['node54', 'node54', 'node53', 'node54'], outputs=['node55'], name='op42')
node_list.append(op42)
node56 = helper.make_tensor_value_info('node56', 1, [5])
init_tensor.append(helper.make_tensor('node56', 1, dims=(5,), vals=[1.0, 1.0, 1.0, 1.0, 1.0]))
node57 = helper.make_tensor_value_info('node57', 1, [10])
init_tensor.append(helper.make_tensor('node57', 1, dims=(1, 10), vals=[0, 0, 0, 0, 0, 1, 1, 1, 1, 1]))
node58 = helper.make_tensor_value_info('node58', 1, [1, 1, 5, 1, 1])
op43 = helper.make_node('Resize', inputs=['node51', 'node57', 'node56'], outputs=['node58'], name='op43', mode='nearest')
node_list.append(op43)
node59 = helper.make_tensor_value_info('node59', 1, [1])
op44 = helper.make_node('Exp', inputs=['node55'], outputs=['node59'], name='op44')
node_list.append(op44)
node60 = helper.make_tensor_value_info('node60', 1, [1])
op45 = helper.make_node('Identity', inputs=['node59'], outputs=['node60'], name='op45')
node_list.append(op45)
node61 = helper.make_tensor_value_info('node61', 1, [4])
node62 = helper.make_tensor_value_info('node62', 1, [2])
node63 = helper.make_tensor_value_info('node63', 1, [18])
op46 = helper.make_node('Concat', inputs=['node59', 'node6', 'node61', 'node62', 'node5', 'node59'], outputs=['node63'], name='op46', axis=0)
node_list.append(op46)
node64 = helper.make_tensor_value_info('node64', 1, [4])
node65 = helper.make_tensor_value_info('node65', 1, [3])
node66 = helper.make_tensor_value_info('node66', 1, [4])
node67 = helper.make_tensor_value_info('node67', 1, [4])
node68 = helper.make_tensor_value_info('node68', 1, [4])
node69 = helper.make_tensor_value_info('node69', 1, [43])
op47 = helper.make_node('Concat', inputs=['node63', 'node6', 'node64', 'node60', 'node65', 'node66', 'node67', 'node68'], outputs=['node69'], name='op47', axis=0)
node_list.append(op47)
node70 = helper.make_tensor_value_info('node70', 1, [18])
op48 = helper.make_node('ThresholdedRelu', inputs=['node63'], outputs=['node70'], name='op48')
node_list.append(op48)
node71 = helper.make_tensor_value_info('node71', 1, [5, 2, 4])
node72 = helper.make_tensor_value_info('node72', 1, [1, 1, 1])
op49 = helper.make_node('ReduceSumSquare', inputs=['node71'], outputs=['node72'], name='op49', axes=[1, 0, 2])
node_list.append(op49)
node73 = helper.make_tensor_value_info('node73', 1, [1, 1, 1])
node74 = helper.make_tensor_value_info('node74', 1, [1, 1, 1])
op50 = helper.make_node('Min', inputs=['node72', 'node72', 'node73', 'node72', 'node72', 'node72', 'node72', 'node72', 'node72', 'node72'], outputs=['node74'], name='op50')
node_list.append(op50)
node75 = helper.make_tensor_value_info('node75', 1, [1, 1, 1])
op51 = helper.make_node('ReduceL2', inputs=['node74'], outputs=['node75'], name='op51', axes=[0, 1, 2])
node_list.append(op51)
node76 = helper.make_tensor_value_info('node76', 7, [5])
init_tensor.append(helper.make_tensor('node76', 7, dims=(5,), vals=[1, 1, 1, 1, 1]))
node77 = helper.make_tensor_value_info('node77', 1, [1, 1, 1, 1, 1])
op52 = helper.make_node('Reshape', inputs=['node74', 'node76'], outputs=['node77'], name='op52')
node_list.append(op52)
node78 = helper.make_tensor_value_info('node78', 1, [1, 1, 1])
op53 = helper.make_node('Tanh', inputs=['node75'], outputs=['node78'], name='op53')
node_list.append(op53)
node79 = helper.make_tensor_value_info('node79', 7, [4])
init_tensor.append(helper.make_tensor('node79', 7, dims=(4,), vals=[2, 4, 1, 0]))
node80 = helper.make_tensor_value_info('node80', 1, [1, 1, 1, 1, 1])
op54 = helper.make_node('ReduceSum', inputs=['node77', 'node79'], outputs=['node80'], name='op54')
node_list.append(op54)
node81 = helper.make_tensor_value_info('node81', 1, [1, 1, 1, 1, 1])
op55 = helper.make_node('Transpose', inputs=['node80'], outputs=['node81'], name='op55', perm=[0, 4, 2, 1, 3])
node_list.append(op55)
node82 = helper.make_tensor_value_info('node82', 1, [1, 1, 1, 1, 1])
op56 = helper.make_node('ReduceMin', inputs=['node80'], outputs=['node82'], name='op56', axes=[4, 3, 1, 0])
node_list.append(op56)
node83 = helper.make_tensor_value_info('node83', 1, [1, 1, 1, 1, 1])
op57 = helper.make_node('Floor', inputs=['node82'], outputs=['node83'], name='op57')
node_list.append(op57)
node84 = helper.make_tensor_value_info('node84', 1, [1, 1, 1, 1, 1])
op58 = helper.make_node('GlobalAveragePool', inputs=['node83'], outputs=['node84'], name='op58')
node_list.append(op58)
node85 = helper.make_tensor_value_info('node85', 1, [1, 1, 1, 1, 1])
op59 = helper.make_node('MatMul', inputs=['node83', 'node84'], outputs=['node85'], name='op59')
node_list.append(op59)
node86 = helper.make_tensor_value_info('node86', 1, [1, 1, 1, 1, 1])
op60 = helper.make_node('MaxPool', inputs=['node77'], outputs=['node86'], name='op60', kernel_shape=[1, 1, 1], strides=[1, 1, 1])
node_list.append(op60)
node87 = helper.make_tensor_value_info('node87', 1, [5, 5, 1, 1, 1])
op61 = helper.make_node('Conv', inputs=['node35', 'node35'], outputs=['node87'], name='op61', kernel_shape=[1, 1, 1], strides=[1, 1, 1], pads=[0, 0, 0, 0, 0, 0], group=1)
node_list.append(op61)
node88 = helper.make_tensor_value_info('node88', 1, [1, 1, 1, 1, 1])
op62 = helper.make_node('Erf', inputs=['node86'], outputs=['node88'], name='op62')
node_list.append(op62)
node89 = helper.make_tensor_value_info('node89', 1, [1, 1, 1, 1, 1])
op63 = helper.make_node('ReduceLogSumExp', inputs=['node88'], outputs=['node89'], name='op63', axes=[2])
node_list.append(op63)
node90 = helper.make_tensor_value_info('node90', 1, [1, 1, 1, 1, 1])
op64 = helper.make_node('AveragePool', inputs=['node88'], outputs=['node90'], name='op64', kernel_shape=[1, 1, 1], strides=[1, 1, 1])
node_list.append(op64)
node91 = helper.make_tensor_value_info('node91', 1, [1])
op65 = helper.make_node('Elu', inputs=['node54'], outputs=['node91'], name='op65')
node_list.append(op65)
node92 = helper.make_tensor_value_info('node92', 1, [1])
op66 = helper.make_node('Exp', inputs=['node91'], outputs=['node92'], name='op66')
node_list.append(op66)
node93 = helper.make_tensor_value_info('node93', 1, [1])
op67 = helper.make_node('Selu', inputs=['node91'], outputs=['node93'], name='op67')
node_list.append(op67)
node94 = helper.make_tensor_value_info('node94', 1, [1])
op68 = helper.make_node('Cos', inputs=['node93'], outputs=['node94'], name='op68')
node_list.append(op68)
node95 = helper.make_tensor_value_info('node95', 1, [5])
init_tensor.append(helper.make_tensor('node95', 1, dims=(5,), vals=[1.0, 1.0, 1.0, 1.0, 1.0]))
node96 = helper.make_tensor_value_info('node96', 1, [10])
init_tensor.append(helper.make_tensor('node96', 1, dims=(1, 10), vals=[0, 0, 0, 0, 0, 1, 1, 1, 1, 1]))
node97 = helper.make_tensor_value_info('node97', 1, [1, 1, 1, 1, 1])
op69 = helper.make_node('Resize', inputs=['node81', 'node96', 'node95'], outputs=['node97'], name='op69', mode='nearest')
node_list.append(op69)
node98 = helper.make_tensor_value_info('node98', 1, [5])
init_tensor.append(helper.make_tensor('node98', 1, dims=(5,), vals=[1.0, 1.0, 1.0, 1.0, 1.0]))
node99 = helper.make_tensor_value_info('node99', 1, [10])
init_tensor.append(helper.make_tensor('node99', 1, dims=(1, 10), vals=[0, 0, 0, 0, 0, 1, 1, 1, 1, 1]))
node100 = helper.make_tensor_value_info('node100', 1, [1, 1, 1, 1, 1])
op70 = helper.make_node('Resize', inputs=['node97', 'node99', 'node98'], outputs=['node100'], name='op70', mode='nearest')
node_list.append(op70)
node101 = helper.make_tensor_value_info('node101', 1, [1, 1, 1, 1, 1])
op71 = helper.make_node('Sign', inputs=['node100'], outputs=['node101'], name='op71')
node_list.append(op71)
node102 = helper.make_tensor_value_info('node102', 1, [1, 1, 1, 1, 1])
op72 = helper.make_node('ReduceMax', inputs=['node101'], outputs=['node102'], name='op72', axes=[3, 2, 0, 1])
node_list.append(op72)
node103 = helper.make_tensor_value_info('node103', 1, [1, 1, 1, 1, 1])
op73 = helper.make_node('GlobalMaxPool', inputs=['node101'], outputs=['node103'], name='op73')
node_list.append(op73)
node104 = helper.make_tensor_value_info('node104', 7, [1])
init_tensor.append(helper.make_tensor('node104', 7, dims=(1,), vals=[2]))
node105 = helper.make_tensor_value_info('node105', 1, [1, 1, 1, 1, 1])
op74 = helper.make_node('ReduceSum', inputs=['node102', 'node104'], outputs=['node105'], name='op74')
node_list.append(op74)
node106 = helper.make_tensor_value_info('node106', 7, [4])
init_tensor.append(helper.make_tensor('node106', 7, dims=(4,), vals=[1, 1, 1, 1]))
node107 = helper.make_tensor_value_info('node107', 1, [1, 1, 1, 1])
op75 = helper.make_node('Reshape', inputs=['node103', 'node106'], outputs=['node107'], name='op75')
node_list.append(op75)
node108 = helper.make_tensor_value_info('node108', 1, [4, 1, 1, 1])
node109 = helper.make_tensor_value_info('node109', 1, [3, 1, 1, 1])
node110 = helper.make_tensor_value_info('node110', 1, [4, 1, 1, 1])
node111 = helper.make_tensor_value_info('node111', 1, [12, 1, 1, 1])
op76 = helper.make_node('Concat', inputs=['node107', 'node108', 'node109', 'node110'], outputs=['node111'], name='op76', axis=0)
node_list.append(op76)
node112 = helper.make_tensor_value_info('node112', 1, [1, 1, 1, 1])
op77 = helper.make_node('Max', inputs=['node107', 'node107', 'node107', 'node107', 'node107', 'node107', 'node107', 'node107', 'node107'], outputs=['node112'], name='op77')
node_list.append(op77)
node113 = helper.make_tensor_value_info('node113', 7, [4])
init_tensor.append(helper.make_tensor('node113', 7, dims=(4,), vals=[1, 0, 2, 3]))
node114 = helper.make_tensor_value_info('node114', 1, [1, 1, 1, 1])
op78 = helper.make_node('ReduceSum', inputs=['node112', 'node113'], outputs=['node114'], name='op78')
node_list.append(op78)
node115 = helper.make_tensor_value_info('node115', 1, [1, 1, 1, 1])
op79 = helper.make_node('GlobalAveragePool', inputs=['node112'], outputs=['node115'], name='op79')
node_list.append(op79)
node116 = helper.make_tensor_value_info('node116', 1, [1, 1, 1, 1])
op80 = helper.make_node('MaxPool', inputs=['node114'], outputs=['node116'], name='op80', kernel_shape=[1, 1], strides=[1, 1])
node_list.append(op80)
node117 = helper.make_tensor_value_info('node117', 1, [1, 1, 1, 1])
op81 = helper.make_node('Selu', inputs=['node115'], outputs=['node117'], name='op81')
node_list.append(op81)
output_tensor.append(node8)
output_tensor.append(node111)
output_tensor.append(node94)
output_tensor.append(node87)
output_tensor.append(node42)
output_tensor.append(node105)
output_tensor.append(node40)
output_tensor.append(node70)
output_tensor.append(node117)
output_tensor.append(node69)
output_tensor.append(node90)
output_tensor.append(node47)
output_tensor.append(node14)
output_tensor.append(node52)
output_tensor.append(node89)
output_tensor.append(node78)
output_tensor.append(node116)
output_tensor.append(node92)
output_tensor.append(node36)
output_tensor.append(node58)
output_tensor.append(node16)
output_tensor.append(node32)
output_tensor.append(node85)
input_tensor.append(node1)
input_tensor.append(node2)
input_tensor.append(node12)
input_tensor.append(node28)
input_tensor.append(node38)
input_tensor.append(node46)
input_tensor.append(node49)
input_tensor.append(node61)
input_tensor.append(node62)
input_tensor.append(node64)
input_tensor.append(node65)
input_tensor.append(node66)
input_tensor.append(node67)
input_tensor.append(node68)
input_tensor.append(node71)
input_tensor.append(node73)
input_tensor.append(node108)
input_tensor.append(node109)
input_tensor.append(node110)
graph_def = helper.make_graph(node_list, 'test-model', input_tensor, output_tensor, init_tensor)
model = helper.make_model(graph_def, producer_name='onnx-example')
