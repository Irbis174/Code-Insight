def insertion_sort(sequence):
    for idx in range(1, len(sequence)):
        item = sequence[idx]
        j = idx - 1
        while j >= 0 and sequence[j] > item:
            sequence[j + 1] = sequence[j]
            j -= 1
        sequence[j + 1] = item
    return sequence
