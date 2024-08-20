def selection_sort(arr):
    if not arr:
        return []
    min_val = min(arr)
    min_idx = arr.index(min_val)
    return [min_val] + selection_sort([x for i, x in enumerate(arr) if i != min_idx])