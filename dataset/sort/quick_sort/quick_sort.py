def quicksort(arr):
    if not arr:
        return []
    pivot = arr[0]
    left = quicksort([x for x in arr[1:] if x < pivot])
    right = quicksort([x for x in arr[1:] if x >= pivot])
    return left + [pivot] + right
