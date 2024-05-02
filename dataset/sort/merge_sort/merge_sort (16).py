def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    l, r = split_list(arr)

    sorted_l = merge_sort(l)
    sorted_r = merge_sort(r)

    return merge_lists(sorted_l, sorted_r)

def split_list(arr):
    m = len(arr) // 2
    l = arr[:m]
    r = arr[m:]
    return l, r

def merge_lists(l, r):
    merged = []
    i, j = 0, 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            merged.append(l[i])
            i += 1
        else:
            merged.append(r[j])
            j += 1

    merged.extend(l[i:])
    merged.extend(r[j:])

    return merged