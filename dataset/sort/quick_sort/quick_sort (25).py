
def quicksort(array, start_index=0, end_index=None):
    if end_index is None:
        end_index = len(array) - 1
    if start_index < end_index:
        pivot_position = partition(array, start_index, end_index)
        quicksort(array, start_index, pivot_position - 1)
        quicksort(array, pivot_position + 1, end_index)
