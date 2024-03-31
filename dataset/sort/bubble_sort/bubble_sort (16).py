def bubble_sort_optimized(lst):
    length = len(lst)
    for i in range(length - 1):
        is_swapped = False
        for j in range(length - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                is_swapped = True
        if not is_swapped:
            break
    return lst