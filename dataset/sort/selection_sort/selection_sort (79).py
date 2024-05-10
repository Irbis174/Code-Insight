def selection_sort(sequence_to_sort):
    for i, _ in enumerate(sequence_to_sort):
        min_idx = min(range(i, len(sequence_to_sort)), key=sequence_to_sort.__getitem__)
        sequence_to_sort[i], sequence_to_sort[min_idx] = sequence_to_sort[min_idx], sequence_to_sort[i]
    return sequence_to_sort
