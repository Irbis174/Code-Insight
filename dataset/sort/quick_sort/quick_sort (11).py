def qs(arr):
    if len(arr) <= 1:
        return arr
    s, e, l = [], [], []
    p = arr[len(arr) // 2]
    for x in arr:
        if x < p:
            s.append(x)
        elif x == p:
            e.append(x)
        else:
            l.append(x)
    return qs(s) + e + qs(l)
