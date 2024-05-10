def bubble_sort_algorithm(arr, reverse=False):
    arr_len = len(arr)
    for i in range(arr_len):
        swapped = False
        for j in range(0, arr_len - i - 1):
            if (arr[j] > arr[j + 1] and not reverse) or (arr[j] < arr[j + 1] and reverse):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
