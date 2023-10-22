def _ddmin(ls, criterion):
    if not criterion(ls):
        raise ValueError('Initial example does not satisfy condition')

    n = 2     # Initial granularity
    while len(ls) >= 2:
        start = 0.0
        subset_length = len(ls) / n
        some_complement_is_failing = False

        while start < len(ls):
            complement = ls[:int(start)] + \
                ls[int(start + subset_length):]

            if criterion(complement):
                ls = complement
                n = max(n - 1, 2)
                some_complement_is_failing = True
                break

            start += subset_length

        if not some_complement_is_failing:
            if n == len(ls):
                break
            n = min(n * 2, len(ls))
    return ls

ITERATIVE = True

def _hddmin(ls, criterion):
    if type(ls[0]) == type("1"):
        ls = [x.split('-') for x in ls]
        ls = [(int(x[0]), int(x[1])) for x in ls]

    depmap = {}
    depmap[0] = 0
    for x in ls:
        depmap[x[1]] = depmap[x[0]] + 1
    maxd = max(depmap.values())

    depth = 0
    while True:
        stls = [x for x in ls]
        for depth in range(1, maxd + 1):
            ddls = []
            for x in ls:
                if depmap[x[1]] == depth:
                    ddls.append(x)

            def hdd_filter(all_ls, curd_ls):
                myls = set([x[1] for x in curd_ls])
                totls = []
                for x in all_ls:
                    intotls = True
                    if (depmap[x[1]] == depth):
                        intotls = (x[1] in myls)
                    else:
                        intotls = ((depmap[x[1]] < depth) or (x[0] in myls))
                    if intotls:
                        myls.add(x[1])
                        totls.append(x)
                # print("all=", all_ls, "curd=", curd_ls, ":", totls)
                return totls         

            def hdd_criterion(currentls):
                return criterion(hdd_filter(ls, currentls))

            reduced_ddls = _ddmin(ddls, hdd_criterion) if len(ddls) > 1 else ddls
            # reduced_ddls = _ddmin(ddls, hdd_criterion)

            ls = hdd_filter(ls, reduced_ddls)
        if not ITERATIVE:
            break
        if ls == stls:
            break

    return ls


if __name__=='__main__':
    ls = ['a', 'b', 'e', 'f', 'g', 'c', 'd']

    def f0(s):
        return ('a' in s) and ('c' in s)

    print(_ddmin(ls, f0))

    def f(s):
        return ((6,8) in s) and ((0,1) in s) and ((0,5) in s) and ((12,13) in s)

    ls = ['0-1', '0-2', '0-3', '0-4', '0-5', '2-6', '6-7', '6-8', '4-9', '4-10', '10-11', '11-12', '12-13', '13-14']

    print(_hddmin(ls, f))



