def bubble_sort(sequence):
    seq_len = len(sequence)
    def swap(i, j):
        sequence[i], sequence[j] = sequence[j], sequence[i]
    for outer_idx in range(seq_len):
        for inner_idx in range(seq_len - outer_idx - 1):
            if sequence[inner_idx] > sequence[inner_idx + 1]:
                swap(inner_idx, inner_idx + 1)
    return sequence
