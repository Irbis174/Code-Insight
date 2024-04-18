def ReverseBubbleSort(array):
    length = len(array)
    for idx1 in range(length):
        for idx2 in range(length-1, idx1, -1):
            if array[idx2] < array[idx2-1]:
                array[idx2], array[idx2-1] = array[idx2-1], array[idx2]
    return array