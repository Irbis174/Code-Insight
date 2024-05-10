def merge_sort_impl(lst):
    if len(lst) <= 1:
        return lst
    mid_idx = len(lst) // 2
    left_part = merge_sort_impl(lst[:mid_idx])
    right_part = merge_sort_impl(lst[mid_idx:])
    return merge_impl(left_part, right_part)

def merge_impl(left, right):
    merged = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    merged += left[left_idx:]
    merged += right[right_idx:]
    return merged
