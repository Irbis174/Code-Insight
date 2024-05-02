def merge_sort(arr):
    if not arr:
        return []

    if len(arr) == 1:
        return arr

    m = len(arr) // 2
    l = arr[:m]
    r = arr[m:]

    l = merge_sort(l)
    r = merge_sort(r)

    return merge(l, r)

def merge(l, r):
    res = []
    i, j = 0, 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            res.append(l[i])
            i += 1
        else:
            res.append(r[j])
            j += 1

    res.extend(l[i:])
    res.extend(r[j:])

    return res