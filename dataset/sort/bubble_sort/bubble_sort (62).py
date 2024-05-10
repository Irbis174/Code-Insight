def BubbleSort(array):
    array_length = len(array)
    for i in range(array_length):
        for j in range(0, array_length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array
