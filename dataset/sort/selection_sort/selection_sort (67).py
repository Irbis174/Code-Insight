def selection_sort(sequence):
    for i in range(len(sequence)):
        min_idx = i
        for j in range(i + 1, len(sequence)):
            if sequence[j] < sequence[min_idx]:
                min_idx = j
        sequence[i], sequence[min_idx] = sequence[min_idx], sequence[i]
    return sequence
