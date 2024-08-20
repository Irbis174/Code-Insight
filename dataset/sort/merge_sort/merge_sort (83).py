def merge_sort_impl(lst):
    if len(lst) <= 1:
        return lst
    mid_idx = len(lst) // 2
    left_lst = lst[:mid_idx]
    right_lst = lst[mid_idx:]
    left_lst = merge_sort_impl(left_lst)
    right_lst = merge_sort_impl(right_lst)
    return merge_impl(left_lst, right_lst)

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