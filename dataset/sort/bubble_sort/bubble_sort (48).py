def bubble_sort(sequence):
    seq_len = len(sequence)
    for outer_idx in range(seq_len):
        swapped = False
        for inner_idx in range(seq_len - outer_idx - 1):
            if sequence[inner_idx] > sequence[inner_idx + 1]:
                sequence[inner_idx], sequence[inner_idx + 1] = sequence[inner_idx + 1], sequence[inner_idx]
                swapped = True
        if not swapped:
            break
    return sequence
