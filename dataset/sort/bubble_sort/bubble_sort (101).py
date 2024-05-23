
    def bubble_sort(array):
        len = len(array)
        for n in range(len):
            for k in range(0, len - n - 1):
                if array[k] > array[k + 1]:
                    array[k], array[k + 1] = array[k + 1], array[k]
            