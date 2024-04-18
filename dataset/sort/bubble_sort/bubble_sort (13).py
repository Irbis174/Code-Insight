def OrdinaryBubbleSort(array):
    length = len(array)
    for idx1 in range(length):
        for idx2 in range(0, length-idx1-1):
            if array[idx2] > array[idx2+1]:
                array[idx2], array[idx2+1] = array[idx2+1], array[idx2]
    return array