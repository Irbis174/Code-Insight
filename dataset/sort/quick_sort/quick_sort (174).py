def dual_pivot_quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot1 = arr[len(arr) // 3]
    pivot2 = arr[2 * len(arr) // 3]
    left = [x for x in arr if x < pivot1]
    mid = [x for x in arr if pivot1 <= x <= pivot2]
    right = [x for x in arr if x > pivot2]
    return dual_pivot_quicksort(left) + mid + dual_pivot_quicksort(right)