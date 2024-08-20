def merge_sort_impl(lst):
    if len(lst) > 1:
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        left = merge_sort_impl(left)
        right = merge_sort_impl(right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
    return lst
