def CustomComparisonBubbleSort(array, comparator):
    length = len(array)
    for idx1 in range(length):
        for idx2 in range(0, length-idx1-1):
            if comparator(array[idx2], array[idx2+1]):
                array[idx2], array[idx2+1] = array[idx2+1], array[idx2]
    return array