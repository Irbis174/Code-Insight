def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    l = merge_sort(arr[:m])
    r = merge_sort(arr[m:])

    return list(merge(l, r))

def merge(l, r):
    i, j = 0, 0
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            yield l[i]
            i += 1
        else:
            yield r[j]
            j += 1

    yield from l[i:]
    yield from r[j:]