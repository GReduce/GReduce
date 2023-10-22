import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--minnode', type=int,  help="MIN_NODE", default=20)
parser.add_argument('--maxnode', type=int,  help="MAX_NODE", default=100)
parser.add_argument('--pickrate', type=float,  help="pickExistRate", default=0.95) # 0.95
parser.add_argument('--file', type=str, help='res_file', default='./res_dice_time.txt')
parser.add_argument('--seed', type=int, help='res_file', default=175)
parser.add_argument('--GMD', type=str, help='Decompose Mode', default='T')
parser.add_argument('--GMC', type=str, help='Compose Mode', default='a')
parser.add_argument('--GN', type=int, help='Reduce Case Number', default=1)

args = parser.parse_args()

ITER_NUM = 1000
SEED = args.seed

# SEED = hash(args.file) % 10000
# import time
# SEED = int(time.time())

MIN_NODE = args.minnode
MAX_NODE = args.maxnode

pickExistRate = args.pickrate

DEBUG = True
NO_INPUT = False
TEST_TVM = True
TEST_GLOW = False
TEST_ONNX2MLIR = False
TEST_ONNXRT = False

PRINT_ONNX = False
FILE_AS_ONNX_CODE = None

# TEST_TVM = True
# TEST_GLOW = True
# TEST_ONNX2MLIR = False
# TEST_ONNXRT = True

global_tensor_num = 0

MIN_TENSOR_DIM = 1
MAX_TENSOR_DIM = 5
MAX_TENSOR_DIM_LEN = 5
MAX_MULTI_INPUTS = 10
MAX_MULTI_OUTPUTS = 10

id_ops = ['Identity', 'Abs', 'Neg', 'Reciprocal', 'Floor', 'Ceil', 'Softsign',\
		  'Sigmoid', 'HardSigmoid', 'Relu', 'LeakyRelu', 'Elu', 'ThresholdedRelu', \
		  'Sin', 'Cos', 'Tanh', \
		  'Transpose', 'Softplus', \
		  'Softmax', 'MaxPool', 'AveragePool', \
		  'LpPool',\
		  'SpaceToDepth', 'Erf', 'Sign', \
		  'Flatten', \
		  'Round', \
		  'Exp', 'Selu', 'Sqrt',\
		  'Dropout'
		  ]

extra_t_ops = ['MatMul', 'Add', 'Sub', 'Mul', 'Div', 'Concat']
extra_t_ops += ['Pad']
extra_t_ops += ['BatchNormalization']
extra_t_ops += ['Expand']
extra_t_ops += ['PRelu']
extra_t_ops += ['Gemm']
extra_t_ops += ['Conv']
extra_t_ops += ['ConvTranspose']

multi_extra_t_ops = ['Sum', 'Max', 'Min', 'Mean']

extra_t_ops += multi_extra_t_ops

reduce_ops = ["ReduceMax", "ReduceMean", "ReduceMin", "ReduceProd", "ReduceSumSquare", \
              "ReduceL1", "ReduceL2", "ReduceLogSumExp",]

multi_out_ops = ['Split']

other_ops = []

ops = []
ops += id_ops
ops += extra_t_ops
ops += reduce_ops
ops += other_ops
ops += multi_out_ops
ops += ['Resize', 'Reshape', 'Unsqueeze', 'Slice', 'Tile', 'Gather']
ops += ['GlobalAveragePool', 'GlobalMaxPool']
ops += ['Compress']
ops += ['ReduceSum']

tvm_unsupported_ops = ['Softplus', 'Compress'] # v0.7 is not supported

o2m_unsupported_ops = ['LpPool', 'ThresholdedRelu', 'Pad']

glow_unsupported_ops = ['Compress', 'Elu', 'GlobalMaxPool', 'LpPool', 'ReduceL1' , 'ReduceLogSumExp', 'Round', 'Selu', 'Softplus', 'Softsign', 'ThresholdedRelu']

if TEST_TVM:
	ops = list(set(ops) - set(tvm_unsupported_ops))

if TEST_ONNX2MLIR:
	ops = list(set(ops) - set(o2m_unsupported_ops))

if TEST_GLOW:
	ops = list(set(ops) - set(glow_unsupported_ops))


ops = sorted(ops)
print("Total gen OPs = %d" % len(ops))

def get_filter(get_op):
	filter_f = lambda x: True
	if get_op == 'SpaceToDepth':
		filter_f = lambda x: x == 4
	if get_op in ['MaxPool', 'AveragePool', 'LpPool', 'GlobalMaxPool', 'GlobalAveragePool']:
		filter_f = lambda x: (x >= 3) and (x <= 5) # unsupprt on ONNXRuntime/TVM
	if get_op == 'Conv':
		filter_f = lambda x: (x >= 3) and (x <= 5) # TVM only supports with 1d, 2d, 3d kernel.
	if get_op == 'ConvTranspose':
		filter_f = lambda x: (x >= 3) and (x <= 5) # TVM only supports with 1d, 2d, 3d kernel.
		# filter_f = lambda x: x == 4
	if get_op in ['MatMul']:
		filter_f = lambda x: x >= 2
	if get_op == 'Gemm':
		filter_f = lambda x: x == 2
	if get_op == 'BatchNormalization':
		filter_f = lambda x: (x >= 3) and (x <= 5) # unsupprt on ONNXRuntime/TVM
	if get_op == 'Unsqueeze':
		filter_f = lambda x: x < MAX_TENSOR_DIM
	if get_op == 'Resize':
		filter_f = lambda x: (x >= 3) and (x <= 5) # unsupprt on ONNXRuntime/TVM
	if get_op in ['Elu', 'Softplus', 'ConstantOfShape']:
		filter_f = lambda x: x == 1
	return filter_f

FILTER_DICT = {}
for op in ops:
	FILTER_DICT[op] = get_filter(op)


