def insertion_sort(sequence):
    for idx in range(1, len(sequence)):
        item = sequence[idx]
        j = idx
        while j > 0 and sequence[j - 1] > item:
            sequence[j] = sequence[j - 1]
            j -= 1
        sequence[j] = item
        yield sequence
