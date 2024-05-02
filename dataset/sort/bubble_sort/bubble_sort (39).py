def bubble_sort(sequence):
    length = len(sequence)
    for outer_idx in range(length):
        for inner_idx in range(0, length - outer_idx - 1):
            if sequence[inner_idx] > sequence[inner_idx + 1]:
                sequence[inner_idx], sequence[inner_idx + 1] = sequence[inner_idx + 1], sequence[inner_idx]
    return sequence
