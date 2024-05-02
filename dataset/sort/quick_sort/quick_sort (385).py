def updated_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    l = [x for x in arr if x < pivot]
    m = [x for x in arr if x == pivot]
    r = [x for x in arr if x > pivot]
    return updated_quicksort(l) + m + updated_quicksort(r)