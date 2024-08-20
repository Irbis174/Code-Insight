def insertion_sort_enumerate(data_sequence):
    for outer_index, element_value in enumerate(data_sequence):
        inner_index = outer_index
        while inner_index > 0 and data_sequence[inner_index - 1] > element_value:
            data_sequence[inner_index] = data_sequence[inner_index - 1]
            inner_index -= 1
        data_sequence[inner_index] = element_value
    return data_sequence
