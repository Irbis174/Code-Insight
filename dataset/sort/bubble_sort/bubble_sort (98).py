def BubbleSortWithLastSwap(array):
    length = len(array)
    new_length = 0
    while length > 0:
        new_length = 0
        for idx in range(1, length):
            if array[idx - 1] > array[idx]:
                array[idx - 1], array[idx] = array[idx], array[idx - 1]
                new_length = idx
        length = new_length
    return array