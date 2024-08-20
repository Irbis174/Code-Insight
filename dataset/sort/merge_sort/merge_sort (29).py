def mergesort_rec(data_seq):
    if not data_seq:
        return []

    if len(data_seq) == 1:
        return data_seq

    mid_idx = len(data_seq) // 2
    left_half = data_seq[:mid_idx]
    right_half = data_seq[mid_idx:]

    left_half = mergesort_rec(left_half)
    right_half = mergesort_rec(right_half)

    return merge_rec(left_half, right_half)

def merge_rec(left, right):
    result = []
    l_idx, r_idx = 0, 0

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1

    result.extend(left[l_idx:])
    result.extend(right[r_idx:])

    return result