def bubble_sort(sequence):
    length = len(sequence)
    
    for outer_idx in range(length):
        sequence = [sequence[inner_idx + 1] if sequence[inner_idx] > sequence[inner_idx + 1] else sequence[inner_idx] for inner_idx in range(length - outer_idx - 1)] + sequence[length - outer_idx:]
        
    return sequence
