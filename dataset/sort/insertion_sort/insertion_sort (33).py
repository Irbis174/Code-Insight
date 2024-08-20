def insertion_sort(sequence):
    for index, value in enumerate(sequence):
        position = index
        while position > 0 and sequence[position - 1] > value:
            sequence[position] = sequence[position - 1]
            position -= 1
        sequence[position] = value
    return sequence
