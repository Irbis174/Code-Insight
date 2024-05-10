def merge_sort_impl(lst):
    if len(lst) > 1:
        mid_idx = len(lst) // 2
        left_half = lst[:mid_idx]
        right_half = lst[mid_idx:]
        left_half = merge_sort_impl(left_half)
        right_half = merge_sort_impl(right_half)
        left_idx, right_idx, lst_idx = 0, 0, 0
        while left_idx < len(left_half) and right_idx < len(right_half):
            if left_half[left_idx] < right_half[right_idx]:
                lst[lst_idx] = left_half[left_idx]
                left_idx += 1
            else:
                lst[lst_idx] = right_half[right_idx]
                right_idx += 1
            lst_idx += 1
        while left_idx < len(left_half):
            lst[lst_idx] = left_half[left_idx]
            left_idx += 1
            lst_idx += 1
        while right_idx < len(right_half):
            lst[lst_idx] = right_half[right_idx]
            right_idx += 1
            lst_idx += 1
    return lst
