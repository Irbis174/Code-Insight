def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left, right = [], []
    for x in arr:
        if x < pivot:
            left.append(x)
        elif x > pivot:
            right.append(x)
    return quicksort(left) + [pivot] + quicksort(right)
