def insertion_sort(sequence):
    for idx in range(1, len(sequence)):
        temp_value = sequence[idx]
        j = idx - 1
        while j >= 0 and sequence[j] > temp_value:
            sequence[j + 1] = sequence[j]
            j -= 1
        sequence[j + 1] = temp_value
    return sequence
