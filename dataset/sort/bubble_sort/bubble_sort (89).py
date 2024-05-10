def bubble_sort_algorithm(arr):
    arr_len = len(arr)
    for i in range(arr_len):
        swapped = False
        for j in range(0, arr_len - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    if arr_len > 1:
        return bubble_sort_algorithm([arr[i] for i in range(1, arr_len)])
    else:
        return arr
