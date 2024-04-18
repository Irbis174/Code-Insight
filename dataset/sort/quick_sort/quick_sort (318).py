def quick_sort(arr, ascending=True):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    if ascending:
        return quick_sort(left, ascending) + middle + quick_sort(right, ascending)
    else:
        return quick_sort(right, ascending) + middle + quick_sort(left, ascending)