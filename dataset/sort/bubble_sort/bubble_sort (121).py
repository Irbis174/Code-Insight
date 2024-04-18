def OptimizedBubbleSort(arr):
    length = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, length):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        length -= 1
    return arr