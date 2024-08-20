from collections import deque

def bubble_sort(sequence):
    seq = deque(sequence)
    seq_len = len(seq)
    for i in range(seq_len):
        for j in range(seq_len - i - 1):
            if seq[j] > seq[j+1]:
                seq[j], seq[j+1] = seq[j+1], seq[j]
    return list(seq)
