def selection_sort(sequence):
    for idx, _ in enumerate(sequence):
        min_idx = min(range(idx, len(sequence)), key=sequence.__getitem__)
        sequence[idx], sequence[min_idx] = sequence[min_idx], sequence[idx]
    return sequence