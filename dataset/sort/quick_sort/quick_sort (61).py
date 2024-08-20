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
    i = start + 1
    j = end
    while True:
        while i <= j and lst[i] <= pivot:
            i += 1
        while j >= i and lst[j] > pivot:
            j -= 1
        if i <= j:
            lst[i], lst[j] = lst[j], lst[i]
        else:
            break
    lst[start], lst[j] = lst[j], lst[start]
    return j