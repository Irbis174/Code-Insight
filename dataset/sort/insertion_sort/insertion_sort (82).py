def enumerated_insertion_sort(lst):
    for i, val in enumerate(lst):
        j = i
        while j > 0 and lst[j - 1] > val:
            lst[j] = lst[j - 1]
            j -= 1
        lst[j] = val
    return lst
