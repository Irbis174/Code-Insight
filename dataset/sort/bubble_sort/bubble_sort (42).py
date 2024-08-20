def bubble_sort(array):
    arr_len = len(array)
    for outer_idx in range(arr_len):
        array = [array[inner_idx + 1] if array[inner_idx] > array[inner_idx + 1] else array[inner_idx] for inner_idx in range(arr_len - outer_idx - 1)] + array[arr_len - outer_idx:]
    return array
