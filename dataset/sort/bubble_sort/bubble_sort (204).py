def OptimizedBubbleSort(array):
    length = len(array)
    swapped = True
    while swapped:
        swapped = False
        for idx in range(1, length):
            if array[idx - 1] > array[idx]:
                array[idx - 1], array[idx] = array[idx], array[idx - 1]
                swapped = True
        length -= 1
    return array