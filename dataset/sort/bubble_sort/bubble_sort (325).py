def GotoBubbleSort(arr):
    length = len(arr)
    start:
    swapped = False
    for i in range(1, length):
        if arr[i - 1] > arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            swapped = True
    if swapped:
        goto start
    return arr