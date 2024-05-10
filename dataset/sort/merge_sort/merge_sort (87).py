def merge_sort_impl(lst):
    if len(lst) > 1:
        mid_idx = len(lst) // 2
        left_part = lst[:mid_idx]
        right_part = lst[mid_idx:]
        left_part = merge_sort_impl(left_part)
        right_part = merge_sort_impl(right_part)
        left_idx, right_idx, lst_idx = 0, 0, 0
        while left_idx < len(left_part) and right_idx < len(right_part):
            if left_part[left_idx] < right_part[right_idx]:
                lst[lst_idx] = left_part[left_idx]
                left_idx += 1
            else:
                lst[lst_idx] = right_part[right_idx]
                right_idx += 1
            lst_idx += 1
        while left_idx < len(left_part):
            lst[lst_idx] = left_part[left_idx]
            left_idx += 1
            lst_idx += 1
        while right_idx < len(right_part):
            lst[lst_idx] = right_part[right_idx]
            right_idx += 1
            lst_idx += 1
    return lst