def median_of_three_quicksort(arr):
    if len(arr) <= 1:
        return arr
    first, middle, last = arr[0], arr[len(arr) // 2], arr[-1]
    pivot = sorted([first, middle, last])[1]  # Median of three
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return median_of_three_quicksort(left) + mid + median_of_three_quicksort(right)