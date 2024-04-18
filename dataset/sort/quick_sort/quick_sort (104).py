def dual_pivot_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot1 = arr[len(arr) // 3]
    pivot2 = arr[2 * len(arr) // 3]
    l = [x for x in arr if x < pivot1]
    m = [x for x in arr if pivot1 <= x <= pivot2]
    r = [x for x in arr if x > pivot2]
    return dual_pivot_quicksort(l) + m + dual_pivot_quicksort(r)