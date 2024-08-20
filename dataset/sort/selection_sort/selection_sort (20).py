def generator_selection_sort(arr):
    for i in range(len(arr)):
        min_idx = min((j for j in range(i, len(arr))), key=lambda j: arr[j])
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr