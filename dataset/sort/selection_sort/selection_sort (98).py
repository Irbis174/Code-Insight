def selection_sort(arr):
    def find_min(arr):
        min_val = min(arr)
        min_idx = arr.index(min_val)
        yield min_val
        yield from find_min(arr[:min_idx] + arr[min_idx + 1:])

    return list(find_min(arr))
