def bubble_sort_goto(arr):
    n = len(arr)
    start:
    swapped = False
    for i in range(1, n):
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            swapped = True
    if swapped:
        goto start
    return arr
