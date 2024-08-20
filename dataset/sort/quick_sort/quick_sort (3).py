import random

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot_idx = random.randrange(len(arr))
    pivot = arr[pivot_idx]
    left = [x for i, x in enumerate(arr) if x < pivot and i != pivot_idx]
    middle = [x for i, x in enumerate(arr) if x == pivot and i != pivot_idx]
    right = [x for i, x in enumerate(arr) if x > pivot and i != pivot_idx]
    return quicksort(left) + middle + quicksort(right)
