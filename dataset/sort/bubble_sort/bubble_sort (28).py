def bubble_sort(sequence):
    length = len(sequence)
    
    for outer_idx in range(length):
        for inner_idx, val in enumerate(sequence[:length - outer_idx]):

            if val > sequence[inner_idx + 1]:
                sequence[inner_idx], sequence[inner_idx + 1] = sequence[inner_idx + 1], val
                
    return sequence
