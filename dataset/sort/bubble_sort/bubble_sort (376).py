def BubbleSortWithLastSwap(arr):
    length = len(arr)
    new_length = 0
    while length > 0:
        new_length = 0
        for i in range(1, length):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                new_length = i
        length = new_length
    return arr
