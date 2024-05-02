def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    l = arr[:m]
    r = arr[m:]

    l = merge_sort(l)
    r = merge_sort(r)

    return merge(l, r, arr)

def merge(l, r, arr):
    i, j, k = 0, 0, 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            arr[k] = l[i]
            i += 1
        else:
            arr[k] = r[j]
            j += 1
        k += 1

    while i < len(l):
        arr[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        arr[k] = r[j]
        j += 1
        k += 1

    return arr