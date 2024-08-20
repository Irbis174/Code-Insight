def qs(arr):
    if not arr:
        return []
    p = arr[0]
    l = qs([x for x in arr[1:] if x < p])
    r = qs([x for x in arr[1:] if x >= p])
    return l + [p] + r
