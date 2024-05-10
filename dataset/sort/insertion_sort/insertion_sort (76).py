def insertion_sort_enumerate(array):
    for i, val in enumerate(array):
        j = i
        while j > 0 and array[j - 1] > val:
            array[j] = array[j - 1]
            j -= 1
        array[j] = val
    return array
