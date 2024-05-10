def insertion_sort_generator(sequence):
    for item_index, item_value in enumerate(sequence):
        position = item_index
        while position > 0 and sequence[position - 1] > item_value:
            sequence[position] = sequence[position - 1]
            position -= 1
        sequence[position] = item_value
        yield sequence
