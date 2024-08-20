def selection_sort(input_array):
    n = len(input_array)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if input_array[j] < input_array[min_idx]:
                min_idx = j
        input_array[i], input_array[min_idx] = input_array[min_idx], input_array[i]
    return input_array
