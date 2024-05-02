def list_selection_sort(sequence):
    sorted_seq = []
    unsorted_seq = sequence[:]
    for _ in range(len(sequence)):
        min_val = min(unsorted_seq)
        sorted_seq.append(min_val)
        unsorted_seq.remove(min_val)
    return sorted_seq