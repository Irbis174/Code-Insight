import bisect

def insertion_sort(arr):
    sorted_arr = []
    for val in arr:
        bisect.insort(sorted_arr, val)
    return sorted_arr
