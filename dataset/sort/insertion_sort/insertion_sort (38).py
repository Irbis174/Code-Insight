def insertion_sort_classic(sequence):
    for i in range(1, len(sequence)):
        key_value = sequence[i]
        j = i - 1
        while j >= 0 and sequence[j] > key_value:
            sequence[j + 1] = sequence[j]
            j -= 1
        sequence[j + 1] = key_value
    return sequence
