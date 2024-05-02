def mergesort_iter(data_list):
    if len(data_list) <= 1:
 return data_list

    mid_idx = len(data_list) // 2
    left_part = mergesort_iter(data_list[:mid_idx])
    right_part = mergesort_iter(data_list[mid_idx:])

    return list(merge_iter(left_part, right_part))

def merge_iter(left, right):
    l_idx, r_idx = 0, 0
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            yield left[l_idx]
            l_idx += 1
        else:
            yield right[r_idx]
            r_idx += 1

    yield from left[l_idx:]
    yield from right[r_idx:]