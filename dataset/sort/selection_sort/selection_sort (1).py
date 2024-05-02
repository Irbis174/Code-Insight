def selection_sort(arr):
    for i, _ in enumerate(arr):
        min_idx = min(range(i, len(arr)), key=arr.__getitem__)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
