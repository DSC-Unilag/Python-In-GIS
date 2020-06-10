def unique(filename='unique.txt'):
    with open(filename) as g:
        f = [f[:-2] for f in g.readlines()]
        print(f[-1])# g.readlines()[-1])
    print(f)
    res = []
    for i in f:
        res.extend(f)
    print(res)
unique()