def qs(arr):
    if len(arr) <= 1:
        return arr
    p = arr[len(arr) // 2]
    l, r = [], []
    for x in arr:
        if x < p:
            l.append(x)
        elif x > p:
            r.append(x)
    return qs(l) + [p] + qs(r)
