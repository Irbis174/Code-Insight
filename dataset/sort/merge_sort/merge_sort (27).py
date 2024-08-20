def mergesort_func(data_list):
    if len(data_list) <= 1:
        return data_list

    mid_idx = len(data_list) // 2
    left_half = data_list[:mid_idx]
    right_half = data_list[mid_idx:]

    left_half = mergesort_func(left_half)
    right_half = mergesort_func(right_half)

    return merge_func(left_half, right_half)

def merge_func(left, right):
    merged = []
    l_idx, r_idx = 0, 0

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            merged.append(left[l_idx])
            l_idx += 1
        else:
            merged.append(right[r_idx])
            r_idx += 1

    merged.extend(left[l_idx:])
    merged.extend(right[r_idx:])

    return merged