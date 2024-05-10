def insertion_sort_list(array):
    for idx in range(1, len(array)):
        current_val = array[idx]
        j = idx - 1
        while j >= 0 and array[j] > current_val:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = current_val
    return array
