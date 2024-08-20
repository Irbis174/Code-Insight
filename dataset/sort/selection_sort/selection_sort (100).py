def selection_sort(arr):
    min_idx = lambda arr, i: i if i == len(arr) - 1 else min_idx(arr, i + 1) if arr[i] < arr[min_idx(arr, i + 1)] else min_idx(arr, i + 1)
    return [arr.pop(min_idx(arr, 0)) for _ in range(len(arr))]
