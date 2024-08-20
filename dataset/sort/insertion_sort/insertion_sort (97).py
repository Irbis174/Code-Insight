import bisect

def insertion_sort(array):
    sorted_array = []
    for val in array:
        bisect.insort(sorted_array, val)
    return sorted_array
