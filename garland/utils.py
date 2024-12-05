def is_ordered(l: list, desc=False):
    if desc:
        return all(l[i] >= l[i+1] for i in range(len(l) - 1))
    else:
        return all(l[i] <= l[i+1] for i in range(len(l) - 1))
