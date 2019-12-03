def file2list(fname):
    with open(fname) as f:
        return list(map(int, f))
