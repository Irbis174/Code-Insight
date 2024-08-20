def insertion_sort(sequence):
    for idx, item in enumerate(sequence):
        j = idx
        while j > 0 and sequence[j - 1] > item:
            sequence[j] = sequence[j - 1]
            j -= 1
        sequence[j] = item
    return sequence
