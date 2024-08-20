def insertion_sort(array):
    for index in range(1, len(array)):
        current_element = array[index]
        position = index
        while position > 0 and array[position - 1] > current_element:
            array[position] = array[position - 1]
            position -= 1
        array[position] = current_element
        yield array
