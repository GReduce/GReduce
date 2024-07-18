from evalcommon import support_executable, eval_given
BUG = support_executable('parser', 'Bug')
SIZE = support_executable('parser', 'Size')

from subprocess import Popen, PIPE
import string
import ast

import random
random.seed(1)

import time

CACHE = {}
def size_haskell(output):
    try:
        return CACHE[output]
    except KeyError:
        pass
    proc = Popen([SIZE], stdin=PIPE, stdout=PIPE, encoding='utf-8')
    stdout, _ = proc.communicate(output)
    assert proc.returncode == 0
    return CACHE.setdefault(output, int(stdout.strip()))

def size_python(output):
    return size_haskell(output)

REPLAY = False

choosed_node = set()

dec_cnt = 0
dec_level = 0
dec_father = 0
dec_rec = []

def clear_dec():
    global dec_cnt
    dec_cnt = 0
    global dec_level
    dec_level = 0
    global dec_father
    dec_father = 0
    global dec_rec
    dec_rec = []

def get_choosed_node():
    global choosed_node
    return choosed_node

def get_dec_rec():
    global dec_rec
    return dec_rec

def dec(*args):
    global dec_cnt
    dec_cnt += 1

    global dec_father
    my_father = 0
    if (args[0] == 1):
        my_father = dec_father
    else:
        dec_father = dec_cnt

    # cur_dec_key = dec_cnt # DD
    cur_dec_key = (my_father, dec_cnt) # HDD

    if not REPLAY:
        dec_rec.append(cur_dec_key) 
        return True
    else:
        return (cur_dec_key in choosed_node)


def Var():
    return formatted(
        'Var "%s"',
        random.choice(string.ascii_letters + string.digits)
    )


def Mod():
    return formatted(
        "Mod { imports = %s, exports = %s }",
        string_lists(Var),
        string_lists(Var),
    )


def Func():
    return formatted(
        "Func{ fnName = %s, args = %s , stmts = %s }",
        Var(), string_lists(Exp), string_lists(Stmt)
    )


def formatted(format_string, *args):
    return format_string % args
    # return map(lambda t: format_string % t, args)
    #return st.tuples(*args).map(lambda t: format_string % t)


def string_lists(args):
    l = random.randint(0, 5)
    x = []
    for i in range(l):
        t = str(args())
        if dec(0):
            x.append(t)
    return "[%s]" % (', '.join(x))
    # return st.lists(*args, **kwargs).map(
    #     lambda ls: "[%s]" % (', '.join(ls),))

def one_of(*args):
    t = len(args)
    return args[random.randint(0, t - 1)]

def Stmt():
    return one_of((
        formatted("Return (%s)", Exp()),
        formatted("Assign (%s) (%s)", Var(), Exp()),
        formatted("Alloc (%s) (%s)", Var(), Exp()),
    ))


# class Frequency(SearchStrategy):
#     def __init__(self, children):
#         SearchStrategy.__init__(self)
#         children = tuple(children)
#         self.values = [
#             t for _, t in children
#         ]
#         self.sampler = Sampler([s for s, _ in children])

#     def do_draw(self, data):
#         i = self.sampler.sample(data)
#         return self.values[i]


EXP_PATTERNS = ([
    (10,  "Not (%s)"),
    (100, "And (%s) (%s)"),
    (100, "Or (%s) (%s)"),
    (100, "Add (%s) (%s)"),
    (100, "Sub (%s) (%s)"),
    (100, "Mul (%s) (%s)"),
    (100, "Div (%s) (%s)"),
])


def Exp(depth=None):
    if depth is None:
        depth = random.randint(0, 5)

    if depth <= 0:
        return one_of(
            formatted("Bool %s", random.choice(["True", "False"])),
            formatted("Int %s", str(random.randint(-9, 9))),
        )

    

    pattern = random.choices([x[1] for x in EXP_PATTERNS], weights = [x[0] for x in EXP_PATTERNS])
    pattern = pattern[0]

    if pattern.count("%s") == 1:
        child = Exp(depth=random.randint(0, depth - 1))
        if dec(0):
            return formatted(pattern, child)
        return child
    else:
        child1 = Exp(depth=random.randint(0, depth - 1))
        child2 = Exp(depth=random.randint(0, depth - 1))
        f1 = dec(0)
        f2 = dec(0)
        if f1:
            return formatted(pattern, child1, child2)
        else:
            if f2:
                return child1
            else:
                return child2


def Lang():
    return formatted(
        "Lang {modules=%s, funcs=%s}",
        string_lists(Mod), string_lists(Func),
    )


if __name__ == '__main__':
    def test(value):
        proc = Popen([BUG], stdin=PIPE, stdout=PIPE, encoding='utf-8')
        stdout, _ = proc.communicate(value)
        assert proc.returncode == 0
        #print("stdout=", stdout.strip())
        #assert stdout.strip() == 'True'
        #print(value)
        return stdout.strip() == 'False'
    def mycheck(value):
        try:
            return test(value)
        except:
            return False

    tot_size, tot_ti, tot = 0, 0, 0
    totmyt, totspeed = 0, 0

    for i in range(111111111):
        REPLAY = False
        random.seed(i)
        clear_dec()
        res = Lang()
        if not mycheck(res):
            continue

        l = [x for x in dec_rec]
        ti = 0
        final = None

        import dd
        def f(ls):
            time.sleep(0.05)
            global ti
            ti += 1
            global choosed_node
            choosed_node = set(ls)
            global REPLAY
            REPLAY = True
            random.seed(i)
            clear_dec()
            res = Lang()
            if mycheck(res):
                global final
                final = res
                return True
            return False

        st = time.time()
        t = dd._ddmin(l, f)
        ed = time.time()
        totmyt += ed-st

        # print(t)
        tot_ti += ti
        f(t)
        # print("time=", ti)
        #print(res, "--->")
        #print(final)

        tot_size += size_python(final)
        tot += 1
        s1 = size_python(res)
        s2 = size_python(final)
        totspeed += (s1-s2)/(ed-st)

        print(tot)

        if tot >= 1000:
            break

    print(tot)
    print(1.0 * tot_ti / tot, 1.0 * tot_size / tot)
    print(1.0 * totmyt / tot, 1.0 * totspeed / tot)
    """
    #test(' Lang {modules=[], funcs=[Func{ stmts = Or (Bool True) (Bool False) ] }')
    test(' Lang {modules=[Mod { imports = [], exports = [Var "z", Var "P", Var "Z", Var "W"] }], funcs=[]}')
    """
    # test('Lang {modules=[], funcs=[Func{ fnName = Var "f", args = [] , stmts = [Return (Or (Bool True) (Bool False))] }]}')
