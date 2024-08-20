def selection_sort(arr):
    sorted_arr = []
    for _ in range(len(arr)):
        min_val = min(arr)
        sorted_arr.append(min_val)
        arr.remove(min_val)
    return sorted_arr
