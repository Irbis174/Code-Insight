def selection_sort(sequence):
    for i, _ in enumerate(sequence):
        min_idx = min(range(i, len(sequence)), key=sequence.__getitem__)
        sequence[i], sequence[min_idx] = sequence[min_idx], sequence[i]
    return sequence
