def bubble_sort(arr):
    has_swapped = True
    while (has_swapped):
        has_swapped = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                has_swapped = True
    return arr
