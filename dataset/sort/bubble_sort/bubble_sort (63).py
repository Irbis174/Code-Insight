def BubbleSort(array):
    array_length = len(array)
    for i in range(array_length):
        swap_occurred = False
        for j in range(0, array_length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swap_occurred = True
        if not swap_occurred:
            break
    return array
