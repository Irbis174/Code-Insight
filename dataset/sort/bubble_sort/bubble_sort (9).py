def bubble_sort(array):
    size = len(array)
    for i in range(size - 1):
        for j in range(size - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array