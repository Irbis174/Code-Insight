def merge_sort_impl(data_list):
    if len(data_list) > 1:
        mid_idx = len(data_list) // 2
        left_half = merge_sort_impl(data_list[:mid_idx])
        right_half = merge_sort_impl(data_list[mid_idx:])
        data_list = merge_impl(left_half, right_half)
    return data_list

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
