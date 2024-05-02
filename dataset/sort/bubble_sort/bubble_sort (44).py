def bubble_sort(sequence):
    seq_len = len(sequence)
    def sort(idx):
        if idx == seq_len:
            return
        for inner_idx in range(seq_len - idx - 1):
            if sequence[inner_idx] > sequence[inner_idx + 1]:
                sequence[inner_idx], sequence[inner_idx + 1] = sequence[inner_idx + 1], sequence[inner_idx]
        sort(idx + 1)
    sort(1)
    return sequence
