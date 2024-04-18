def CustomComparisonBubbleSort(arr, comparator):
    length = len(arr)
    for i in range(length):
        for j in range(0, length-i-1):
            if comparator(arr[j], arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
