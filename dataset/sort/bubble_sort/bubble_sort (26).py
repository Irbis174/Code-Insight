def bubble_sort(sequence):
    length = len(sequence)
    swap = lambda i, j: (sequence[j], sequence[i]) if sequence[i] > sequence[j] else (sequence[i], sequence[j])
    
    for outer_idx in range(length):
        for inner_idx in range(length - outer_idx - 1):
            sequence[inner_idx], sequence[inner_idx + 1] = swap(inner_idx, inner_idx + 1)
            
    return sequence
