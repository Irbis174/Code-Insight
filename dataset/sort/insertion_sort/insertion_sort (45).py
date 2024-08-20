def sort_with_insertion(sequence):
    for idx in range(1, len(sequence)):
        val = sequence[idx]
        j = idx - 1
        while j >= 0 and sequence[j] > val:
            sequence[j + 1] = sequence[j]
            j -= 1
        sequence[j + 1] = val
    return sequence
