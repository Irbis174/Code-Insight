def insertion_sort_list(unsorted_array):
    for idx in range(1, len(unsorted_array)):
        current_value = unsorted_array[idx]
        j = idx - 1
        while j >= 0 and unsorted_array[j] > current_value:
            unsorted_array[j + 1] = unsorted_array[j]
            j -= 1
        unsorted_array[j + 1] = current_value
    return unsorted_array
