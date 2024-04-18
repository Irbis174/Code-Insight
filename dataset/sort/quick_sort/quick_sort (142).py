def hybrid_quicksort(arr):
    if len(arr) <= 10:
        return sorted(arr)  # Switch to Insertion Sort for small arrays
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return hybrid_quicksort(left) + middle + hybrid_quicksort(right)
