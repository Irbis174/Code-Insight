def mergesort_opt(data_seq):
    if len(data_seq) <= 1:
        return data_seq

    mid_idx = len(data_seq) // 2
    left_half = data_seq[:mid_idx]
    right_half = data_seq[mid_idx:]

    left_half = mergesort_opt(left_half)
    right_half = mergesort_opt(right_half)

    return merge_inplace(left_half, right_half, data_seq)

def merge_inplace(left, right, result):
    l_idx, r_idx, res_idx = 0, 0, 0

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            result[res_idx] = left[l_idx]
            l_idx += 1
        else:
            result[res_idx] = right[r_idx]
            r_idx += 1
        res_idx += 1

    while l_idx < len(left):
        result[res_idx] = left[l_idx]
        l_idx += 1
        res_idx += 1

    while r_idx < len(right):
        result[res_idx] = right[r_idx]
        r_idx += 1
        res_idx += 1

    return result