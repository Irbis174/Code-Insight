def quicksort_with_median_of_medians(arr):
    if len(arr) <= 1:
        return arr
    pivot = median_of_medians(arr)
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_with_median_of_medians(left) + middle + quicksort_with_median_of_medians(right)

def median_of_medians(arr):
    if len(arr) <= 5:
        return sorted(arr)[len(arr) // 2]
    chunks = [arr[i:i + 5] for i in range(0, len(arr), 5)]
    medians = [sorted(chunk)[len(chunk) // 2] for chunk in chunks]
    return median_of_medians(medians)