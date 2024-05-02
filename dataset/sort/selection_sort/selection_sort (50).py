def ListSelectionSort(data_sequence):
    sorted_seq = []
    unsorted_seq = data_sequence[:]
    for _ in range(len(data_sequence)):
        min_val = min(unsorted_seq)
        sorted_seq.append(min_val)
        unsorted_seq.remove(min_val)
    return sorted_seq