def hybrid_quicksort(arr):
    if len(arr) <= 10:
        return sorted(arr)  # Switch to Insertion Sort for small arrays
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return hybrid_quicksort(left) + mid + hybrid_quicksort(right)