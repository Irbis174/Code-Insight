def partition(unsorted_list, left_index, right_index):
    pivot_value = unsorted_list[right_index]
    pivot_index = left_index
    for j in range(left_index, right_index):
        if unsorted_list[j] <= pivot_value:
            unsorted_list[pivot_index], unsorted_list[j] = unsorted_list[j], unsorted_list[pivot_index]
            pivot_index += 1
    unsorted_list[pivot_index], unsorted_list[right_index] = unsorted_list[right_index], unsorted_list[pivot_index]
    return pivot_index

def quicksort(unsorted_list, left_index=0, right_index=None):
    if right_index is None:
        right_index = len(unsorted_list) - 1
    if left_index < right_index:
        pivot_position = partition(unsorted_list, left_index, right_index)
        quicksort(unsorted_list, left_index, pivot_position - 1)
        quicksort(unsorted_list, pivot_position + 1, right_index)
