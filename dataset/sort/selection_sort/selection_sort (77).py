def selection_sort(array_to_sort):
    for i in range(len(array_to_sort)):
        min_idx = i
        for j in range(i + 1, len(array_to_sort)):
            if array_to_sort[j] < array_to_sort[min_idx]:
                min_idx = j
        array_to_sort[i], array_to_sort[min_idx] = array_to_sort[min_idx], array_to_sort[i]
    return array_to_sort
