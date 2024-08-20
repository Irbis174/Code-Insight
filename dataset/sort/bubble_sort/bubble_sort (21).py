def bubble_sort(sequence):
    length = len(sequence)
    swapped = True
    
    while swapped:
        swapped = False
        for idx in range(length - 1):
            if sequence[idx] > sequence[idx + 1]:
                sequence[idx], sequence[idx + 1] = sequence[idx + 1], sequence[idx]
                swapped = True
                
    return sequence
