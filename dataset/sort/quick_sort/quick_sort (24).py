import random

def partition(array, start_index, end_index):
    pivot_index = random.randrange(start_index, end_index + 1)
    pivot = array[pivot_index]
    array[pivot_index], array[end_index] = array[end_index], array[pivot_index]
    pivot_index = start_index
    for j in range(start_index, end_index):
        if array[j] <= pivot:
            array[pivot_index], array[j] = array[j], array[pivot_index]
            pivot_index += 1
    array[pivot_index], array[end_index] = array[end_index], array[pivot_index]
    return pivot_index
