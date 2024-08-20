def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    l = merge_sort(arr[:m])
    r = merge_sort(arr[m:])

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