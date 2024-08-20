def merge_sort_impl(arr):
    if len(arr) > 1:
        mid_idx = len(arr) // 2
        left_part = arr[:mid_idx]
        right_part = arr[mid_idx:]
        left_part = merge_sort_impl(left_part)
        right_part = merge_sort_impl(right_part)
        arr = merge_impl(left_part, right_part)
    return arr

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