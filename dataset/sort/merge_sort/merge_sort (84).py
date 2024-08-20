def merge_sort_impl(sequence):
    if len(sequence) <= 1:
        return sequence
    mid_idx = len(sequence) // 2
    left_half = merge_sort_impl(sequence[:mid_idx])
    right_half = merge_sort_impl(sequence[mid_idx:])
    return merge_impl(left_half, right_half)

def merge_impl(left, right):
    merged = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] <= right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    merged += left[left_idx:]
    merged += right[right_idx:]
    return merged