def insertion_sort_classic(unsorted):
    for i in range(1, len(unsorted)):
        key = unsorted[i]
        j = i - 1
        while j >= 0 and unsorted[j] > key:
            unsorted[j + 1] = unsorted[j]
            j -= 1
        unsorted[j + 1] = key
    return unsorted
