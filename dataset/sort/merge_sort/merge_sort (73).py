def merge_sort_impl(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]
    left_half = merge_sort_impl(left_half)
    right_half = merge_sort_impl(right_half)
    return merge_impl(left_half, right_half)

def merge_impl(left, right):
    result = []
    l_idx, r_idx = 0, 0
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1
    result += left[l_idx:]
    result += right[r_idx:]
    return result