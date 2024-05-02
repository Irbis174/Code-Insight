import random

def partition(unsorted_list, left_index, right_index):
    pivot_index = random.randint(left_index, right_index)
    pivot_value = unsorted_list[pivot_index]
    unsorted_list[pivot_index], unsorted_list[right_index] = unsorted_list[right_index], unsorted_list[pivot_index]
    store_index = left_index
    for i in range(left_index, right_index):
        if unsorted_list[i] < pivot_value:
            unsorted_list[i], unsorted_list[store_index] = unsorted_list[store_index], unsorted_list[i]
            store_index += 1
    unsorted_list[right_index], unsorted_list[store_index] = unsorted_list[store_index], unsorted_list[right_index]
    return store_index

def quicksort(unsorted_list, left_index=0, right_index=None):
    if right_index is None:
        right_index = len(unsorted_list) - 1
    if left_index < right_index:
        pivot_index = partition(unsorted_list, left_index, right_index)
        quicksort(unsorted_list, left_index, pivot_index - 1)
        quicksort(unsorted_list, pivot_index + 1, right_index)
