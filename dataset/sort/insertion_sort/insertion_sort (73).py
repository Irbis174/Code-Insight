def insertion_sort_generator(array):
    for i, value in enumerate(array):
        j = i
        while j > 0 and array[j - 1] > value:
            array[j] = array[j - 1]
            j -= 1
        array[j] = value
        yield array
