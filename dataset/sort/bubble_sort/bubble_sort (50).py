def bubble_sort(data_sequence):
    seq_length = len(data_sequence)
    is_sorted = False
    
    while not is_sorted:
        is_sorted = True
        for idx in range(seq_length - 1):
            if data_sequence[idx] > data_sequence[idx + 1]:
                data_sequence[idx], data_sequence[idx + 1] = data_sequence[idx + 1], data_sequence[idx]
                is_sorted = False
                yield data_sequence
                
    return data_sequence
