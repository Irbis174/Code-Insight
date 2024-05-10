def selection_sort(arr):
    if not arr:
        return []
    min_val = min(arr)
    min_idx = arr.index(min_val)
    return [min_val] + selection_sort(arr[:min_idx] + arr[min_idx + 1:])
