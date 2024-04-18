def median_of_three_quicksort(arr):
    if len(arr) <= 1:
        return arr
    first, middle, last = arr[0], arr[len(arr) // 2], arr[-1]
    pivot = sorted([first, middle, last])[1]  # Median of three
    l = [x for x in arr if x < pivot]
    m = [x for x in arr if x == pivot]
    r = [x for x in arr if x > pivot]
    return median_of_three_quicksort(l) + m + median_of_three_quicksort(r)