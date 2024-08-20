def classic_insertion_sort(lst):
    for i in range(1, len(lst)):
        key_value = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key_value:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key_value
    return lst
