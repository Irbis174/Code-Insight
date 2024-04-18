def SinglePassBubbleSort(arr):
    length = len(arr)
    while True:
        swapped = False
        for i in range(1, length):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        if not swapped:
            break
        length -= 1
    return arr