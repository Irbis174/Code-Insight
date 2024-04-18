def BubbleSortWithRange(arr, start, end):
    for i in range(start, end):
        for j in range(start, end-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr