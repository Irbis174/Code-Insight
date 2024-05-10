def quicksort(lst, start=0, end=None):
    if end is None:
        end = len(lst) - 1
    if start < end:
        p = partition(lst, start, end)
        quicksort(lst, start, p - 1)
        quicksort(lst, p + 1, end)
    return lst

def partition(lst, start, end):
    pivot = lst[(start + end) // 2]
    i = start - 1
    j = end + 1
    while True:
        i += 1
        while lst[i] < pivot:
            i += 1
        j -= 1
        while lst[j] > pivot:
            j -= 1
        if i >= j:
            return j
        lst[i], lst[j] = lst[j], lst[i]