def classic_insertion_sort(unsorted_arr):
    for i in range(1, len(unsorted_arr)):
        key_value = unsorted_arr[i]
        j = i - 1
        while j >= 0 and unsorted_arr[j] > key_value:
            unsorted_arr[j + 1] = unsorted_arr[j]
            j -= 1
        unsorted_arr[j + 1] = key_value
    return unsorted_arr
