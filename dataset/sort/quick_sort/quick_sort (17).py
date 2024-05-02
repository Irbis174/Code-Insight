import itertools

def qs(arr):
    if len(arr) <= 1:
        return arr
    p = arr[len(arr) // 2]
    l = [x for x in arr if x < p]
    m = [x for x in arr if x == p]
    r = [x for x in arr if x > p]
    return list(itertools.chain(qs(l), m, qs(r)))
