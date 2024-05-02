import random

def qs(arr):
    if len(arr) <= 1:
        return arr
    p_idx = random.randrange(len(arr))
    p = arr[p_idx]
    l = [x for i, x in enumerate(arr) if x < p and i != p_idx]
    m = [x for i, x in enumerate(arr) if x == p and i != p_idx]
    r = [x for i, x in enumerate(arr) if x > p and i != p_idx]
    return qs(l) + m + qs(r)
