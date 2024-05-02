def selection_sort(arr):
    sorted_arr = []
    unsorted_arr = arr[:]
    for _ in range(len(arr)):
        min_val = min(unsorted_arr)
        sorted_arr.append(min_val)
        unsorted_arr.remove(min_val)
    return sorted_arr