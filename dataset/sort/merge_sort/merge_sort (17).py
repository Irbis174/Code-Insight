from concurrent.futures import ThreadPoolExecutor

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    m = len(arr) // 2
    l = arr[:m]
    r = arr[m:]

    with ThreadPoolExecutor() as executor:
        sorted_l = executor.submit(merge_sort, l)
        sorted_r = executor.submit(merge_sort, r)

    return merge(sorted_l.result(), sorted_r.result())

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