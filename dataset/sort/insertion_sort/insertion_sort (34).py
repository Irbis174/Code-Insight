def recursive_insertion_sort(lst, n):
    if n <= 1:
        return

    recursive_insertion_sort(lst, n - 1)

    last_element = lst[n - 1]
    j = n - 2

    while j >= 0 and lst[j] > last_element:
        lst[j + 1] = lst[j]
        j -= 1

    lst[j + 1] = last_element
    return lst
