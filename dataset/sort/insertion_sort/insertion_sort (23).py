def insertion_sort(array):
    for index in range(1, len(array)):
        key_element = array[index]
        position = index - 1
        while position >= 0 and array[position] > key_element:
            array[position + 1] = array[position]
            position -= 1
        array[position + 1] = key_element
    return array
