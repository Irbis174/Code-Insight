import operator

def selection_sort(arr):
    sorted_arr = arr[:]
    for i in range(len(sorted_arr)):
        min_idx = min(range(i, len(sorted_arr)), key=sorted_arr.__getitem__)
        sorted_arr[i], sorted_arr[min_idx] = sorted_arr[min_idx], sorted_arr[i]
    return sorted_arr
