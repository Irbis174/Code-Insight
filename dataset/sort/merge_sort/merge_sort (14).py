def merge_sort(unsorted_arr):
    if len(unsorted_arr) <= 1:
        return unsorted_arr

    m = len(unsorted_arr) // 2
    l = unsorted_arr[:m]
    r = unsorted_arr[m:]

    sorted_l = merge_sort(l)
    sorted_r = merge_sort(r)

    return merge_sorted_sublists(sorted_l, sorted_r)

def merge(l, r):
    merged_arr = []
    i, j = 0, 0

    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            merged_arr.append(l[i])
            i += 1
        else:
            merged_arr.append(r[j])
            j += 1

    merged_arr.extend(l[i:])
    merged_arr.extend(r[j:])

    return merged_arr