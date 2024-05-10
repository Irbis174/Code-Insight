def selection_sort(list_data):
    n = len(list_data)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if list_data[j] < list_data[min_idx]:
                min_idx = j
        list_data[i], list_data[min_idx] = list_data[min_idx], list_data[i]
    return list_data
