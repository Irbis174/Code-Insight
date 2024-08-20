def insertion_sort_list(lst):
    for idx in range(1, len(lst)):
        val = lst[idx]
        j = idx - 1
        while j >= 0 and lst[j] > val:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = val
    return lst
