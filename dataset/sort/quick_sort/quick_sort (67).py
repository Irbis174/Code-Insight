def quicksort(lst, start=0, end=None):
    if end is None:
        end = len(lst) - 1
    if start < end:
        p = partition(lst, start, end)
        quicksort(lst, start, p - 1)
        quicksort(lst, p + 1, end)
    return lst

def partition(lst, start, end):
    pivot = lst[end]
    i = start
    for j in range(start, end):
        if lst[j] < pivot:
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
    lst[i], lst[end] = lst[end], lst[i]
    return i