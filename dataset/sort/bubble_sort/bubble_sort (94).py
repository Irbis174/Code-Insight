def SinglePassBubbleSort(array):
    length = len(array)
    while True:
        swapped = False
        for idx in range(1, length):
            if array[idx - 1] > array[idx]:
                array[idx - 1], array[idx] = array[idx], array[idx - 1]
                swapped = True
        if not swapped:
            break
        length -= 1
    return array
