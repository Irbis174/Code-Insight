def insertion_sort_enumerate(sequence):
    for idx, val in enumerate(sequence):
        pos = idx
        while pos > 0 and sequence[pos - 1] > val:
            sequence[pos] = sequence[pos - 1]
            pos -= 1
        sequence[pos] = val
    return sequence
