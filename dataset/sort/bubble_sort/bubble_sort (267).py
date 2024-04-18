def bubble_sort(arr):
    N = len(arr)
    for i in range(N - 1):
        is_swapped = False
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swapped = True
        if not is_swapped:
            break
    return arr