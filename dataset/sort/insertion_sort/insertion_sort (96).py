import bisect

def insertion_sort(sequence):
    sorted_list = []
    for item in sequence:
        bisect.insort(sorted_list, item)
    return sorted_list
