def selection_sort(list_to_sort):
    n = len(list_to_sort)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if list_to_sort[j] < list_to_sort[min_idx]:
                min_idx = j
        list_to_sort[i], list_to_sort[min_idx] = list_to_sort[min_idx], list_to_sort[i]
    return list_to_sort
