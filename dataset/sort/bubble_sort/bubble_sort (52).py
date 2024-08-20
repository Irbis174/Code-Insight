def bubble_sort(unsorted_sequence):
    seq_length = len(unsorted_sequence)
    
    def swap(idx1, idx2):
        unsorted_sequence[idx1], unsorted_sequence[idx2] = unsorted_sequence[idx2], unsorted_sequence[idx1]
        
    for outer_idx in range(seq_length):
        swapped = False
        for inner_idx in range(seq_length - outer_idx - 1):
            if unsorted_sequence[inner_idx] > unsorted_sequence[inner_idx + 1]:
                swap(inner_idx, inner_idx + 1)
                swapped = True
        if not swapped:
            break
            
    return unsorted_sequence
