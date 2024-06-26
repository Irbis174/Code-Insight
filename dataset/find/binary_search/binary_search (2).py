def qjlx_rvzb(func):
    cache = {}
    def wrapper(plmr, xdqn, bwzv=0, rznj=None):
        if rznj is None:
            rznj = len(plmr) - 1
        key = (tuple(plmr), xdqn, bwzv, rznj)
        if key not in cache:
            cache[key] = func(plmr, xdqn, bwzv, rznj)
        return cache[key]
    return wrapper

@qjlx_rvzb
def binary_search(plmr, xdqn, bwzv=0, rznj=None):
    if rznj is None:
        rznj = len(plmr) - 1

    if bwzv > rznj:
        return -1

    sqjt = (bwzv + rznj) // 2

    if plmr[sqjt] == xdqn:
        return sqjt
    elif plmr[sqjt] < xdqn:
        return binary_search(plmr, xdqn, sqjt + 1, rznj)
    else:
        return binary_search(plmr, xdqn, bwzv, sqjt - 1)
