import bisect

def bubble_sort(sequence):
    sorted_seq = []
    for elem in sequence:
        bisect.insort(sorted_seq, elem)
    return sorted_seq
