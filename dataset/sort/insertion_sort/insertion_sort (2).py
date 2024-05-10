def insertion_sort(sequence):
    for index in range(1, len(sequence)):
        yield sorted(sequence[:index + 1]) + sequence[index + 1:]
