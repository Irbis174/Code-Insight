def BubbleSortWithRange(array, start, end):
    for idx1 in range(start, end):
        for idx2 in range(start, end-idx1-1):
            if array[idx2] > array[idx2+1]:
                array[idx2], array[idx2+1] = array[idx2+1], array[idx2]
    return array