def partition(array, start_index, end_index):
    pivot = array[end_index]
    pivot_index = start_index
    for j in range(start_index, end_index):
        if array[j] <= pivot:
            array[pivot_index], array[j] = array[j], array[pivot_index]
            pivot_index += 1
    array[pivot_index], array[end_index] = array[end_index], array[pivot_index]
    return pivot_index

def quicksort(array, start_index=0, end_index=None):
    if end_index is None:
        end_index = len(array) - 1
    if start_index < end_index:
        pivot_position = partition(array, start_index, end_index)
        quicksort(array, start_index, pivot_position - 1)
        quicksort(array, pivot_position + 1, end_index)
