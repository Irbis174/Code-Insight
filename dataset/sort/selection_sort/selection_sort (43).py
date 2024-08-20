import operator

def OperatorSelectionSort(sequence)
    sorted_seq = sequence[]
    for i in range(len(sorted_seq))
        min_idx = min(range(i, len(sorted_seq)), key=sorted_seq.__getitem__)
        sorted_seq[i], sorted_seq[min_idx] = sorted_seq[min_idx], sorted_seq[i]
    return sorted_seq
