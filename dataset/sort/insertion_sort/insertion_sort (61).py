def insertion_sort(lst):
    for i in range(1, len(lst)):
        current_value = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > current_value:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = current_value
    return lst
