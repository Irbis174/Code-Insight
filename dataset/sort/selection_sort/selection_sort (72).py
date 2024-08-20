def selection_sort(unsorted):
    n = len(unsorted)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if unsorted[j] < unsorted[min_idx]:
                min_idx = j
        unsorted[i], unsorted[min_idx] = unsorted[min_idx], unsorted[i]
    return unsorted
