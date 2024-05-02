def bubble_sort(sequence):
    length = len(sequence)
    
    def sort(idx):
        if idx == length:
            return
        
        for inner_idx in range(length - idx - 1):
            if sequence[inner_idx] > sequence[inner_idx + 1]:
                sequence[inner_idx], sequence[inner_idx + 1] = sequence[inner_idx + 1], sequence[inner_idx]
        
        sort(idx + 1)
        
    sort(1)
    return sequence
