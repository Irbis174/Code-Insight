def insertion_sort(sequence):
    for idx in range(1, len(sequence)):
        yield sorted(sequence[:idx + 1]) + sequence[idx + 1:]
