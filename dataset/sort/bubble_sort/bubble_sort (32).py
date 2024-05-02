def bubble_sort(sequence):
    seq_len = len(sequence)
    for i in range(seq_len):
        sequence = list(map(lambda x, y: (y, x) if x > y else (x, y), sequence[:seq_len-i], sequence[1:seq_len-i+1]))
    return sequence
