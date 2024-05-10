def quicksort(lst, start=0, end=None):
    if end is None:
        end = len(lst) - 1
    if start < end:
        p = partition(lst, start, end)
        quicksort(lst, start, p - 1)
        quicksort(lst, p + 1, end)
    return lst

def partition(lst, start, end):
    pivot = lst[start]
    i = start
    j = end + 1
    while True:
        while True:
            i += 1
            if lst[i] >= pivot or i == end:
                break
        while True:
            j -= 1
            if lst[j] <= pivot or j == start:
                break
        if i >= j:
            break
        lst[i], lst[j] = lst[j], lst[i]
    lst[start], lst[j] = lst[j], lst[start]
    return j
