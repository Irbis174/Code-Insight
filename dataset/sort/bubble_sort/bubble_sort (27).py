def bubble_sort(sequence):
    length = len(sequence)
    
    def swap(i, j):
        sequence[i], sequence[j] = sequence[j], sequence[i]
        
    for outer_idx in range(length):
        for inner_idx in range(length - outer_idx - 1):
            if sequence[inner_idx] > sequence[inner_idx + 1]:
                swap(inner_idx, inner_idx + 1)
                
    return sequence
