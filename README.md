# GReduce

This repository contains evaluations of **Generator-based Test Input Reduction**.

The evaluations consist of 40 subjects from three application domains: Graphs, DL Models, and JavaScript Programs, including 10 subjects on Graphs, 20 subjects on DL Models, and 10 subjects on JavaScript Programs. 37 of 40 are unexpected exceptions or crashes, and 3 of 40 are wrong-result cases.

The details of the subjects are listed in `Subjects.xlsx`.

# Results

## Graphs

Original Graphs: Check  `graph/GReduce/original/*`

Results of GReduce (Tree-based + alter) : Check  `graph/GReduce/results/*`

Results of Perses: Check `graph/perses/reduced_graphs.txt`



## DL Models

Original DL Models: Check `dl/GReduce/models/bug*.onnx`

Results of GReduce (Tree-based + alter) : Check `dl/GReduce/models/bug*.reduceTa.onnx`

Results of Perses: Check `dl/perses/models/bug*.perses.reduce.onnx`



## JS Programs

Original JS Programs: Check `js/perses/njs/n*.js`

Results of GReduce (Tree-based + alter) :  Check `js/GReduce/results/ok_n*.js`

Results of Perses:  Check `js/perses/results/ok_n*.js`

Results of JSDelta: Check `js/jsdelta/results/ok_n*.js`





# How to Reproduce

## Environment

Our experiment runs on macOS, probably also works for Linux.

Dependencies:

Java 11

Python 3.6 (packages are listed in `environment.yml`, you could directly import with [conda](https://docs.conda.io/en/latest/))

TVM of this [version](https://github.com/apache/tvm/commit/c31e338d5f98a8e8c97286c5b93b20caee8be602), check [here](https://tvm.apache.org/docs/install/from_source.html#developers-get-source-from-github) for details (it is used for property testing on DL models.)

Node.js (it is used for JSDelta on JS Programs, check [here](https://github.com/wala/jsdelta) for details)

Due to the limitation of Github file size, we upload following files on Google Drive.
```
./js/perses/testjs-n.jar
./js/jsdelta/testjs-n.jar
./js/GReduce/g_js_r.jar
./js/GReduce/g_js_a.jar
./js/GReduce/g_js_b.jar
```
Please download [here](https://drive.google.com/drive/folders/1Won9OdE15ykLDoM09KENmqk5Hq5wS1cV?usp=sharing), and add them into corresponding folders.

## Graphs

### GReduce

```bash
cd graph/GReduce/run
# usage: python debugger.py --GMD $decompose_way --GMC $compose_way --GN $case
# $decompose_way: T, S
# $compose_way: r, b, a
# for case 2, 4, 9, replace debugger.py by debuggerc.py for differential testing.

# run all of cases, default mode: T a (change the mode by editing runall.py) 
python run_all.py
#  for results, check all.txt, and graphX.txt
```



## Perses

```bash
cd graph/perses
# run G-1 as an example
cd graph-g1
python run.py
# ...
```



## DL Models

### GReduce

```bash
cd dl/GReduce
# usage: python debugger.py --GMD $decompose_way --GMC $compose_way --GN $case
# $decompose_way: T, S
# $compose_way: r, b, a
# As an example:
python debugger.py --GMD T --GMC a --GN 1 
# after then, check all.txt, for reduction candidates, check models/bug1.reduceTa.onnx

# run all of cases, default mode: T a (change the mode by editing runall.py) 
python run_all.py
#  for results, check all.txt, and models/bugX.reduceYZ.onnx
```

### Perses

```bash
cd dl/perses
python run_all.py
python count.py
# for results, check all.txt, models/bugX.perses.reduce.onnx
```



## JS Programs

### GReduce

```bash
cd js/GReduce
# usage: python debugger.py $decompose_way $compose_way $case
# $decompose_way: T, S
# $compose_way: r, b, a
# As an example:
python debugger.py T a 1
# after then, check all.txt, for reduction candidates, check testres.txt

# run all of cases, default mode: T a (change the mode by editing runall.py) 
python run_all.py
# check all.txt
```

### Perses

```bash
cd js/perses
# run all of cases
python run_all.py
# check all.txt
# for each case, check res_n*.js.txt and ok_n*.js
```

### JSDelta

```bash
cd js/jsdelta
# run all of cases
python run_all.py
# check all.txt
# for each case, check res_n*.js.txt and ok_n*.js
```

