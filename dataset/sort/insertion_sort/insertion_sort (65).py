def insertion_sort(sequence):
    for idx, elem in enumerate(sequence):
        j = idx
        while j > 0 and sequence[j - 1] > elem:
            sequence[j] = sequence[j - 1]
            j -= 1
        sequence[j] = elem
        yield sequence
