def ReverseBubbleSort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr
