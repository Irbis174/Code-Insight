def hybrid_quicksort(arr):
    if len(arr) <= 10:
        return sorted(arr)  # Switch to Insertion Sort for small arrays
    else:
        pivot = arr[len(arr) // 2]
        l = [x for x in arr if x < pivot]
        m = [x for x in arr if x == pivot]
        r = [x for x in arr if x > pivot]
        return hybrid_quicksort(l) + m + hybrid_quicksort(r)