def bubble_sort(sequence):
    length = len(sequence)
    
    for outer_idx in range(length):
        swapped = False
        for inner_idx in range(length - outer_idx - 1):
            if sequence[inner_idx] > sequence[inner_idx + 1]:
                sequence[inner_idx], sequence[inner_idx + 1] = sequence[inner_idx + 1], sequence[inner_idx]
                swapped = True
        if not swapped:
            break
            
    return sequence
