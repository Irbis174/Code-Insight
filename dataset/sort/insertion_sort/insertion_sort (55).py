def insertion_sort(array):
    for i in range(1, len(array)):
        current_value = array[i]
        j = i
        while j > 0 and array[j - 1] > current_value:
            array[j] = array[j - 1]
            j -= 1
        array[j] = current_value
        yield array
