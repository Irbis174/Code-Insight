def bubble_sort(arr):
    has_swapped = True

    total_iteration = 0

    while (has_swapped):
        has_swapped = False
        for i in range(len(arr) - total_iteration - 1):
            if arr[i] > arr[i + 1]:
                # Swap
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                has_swapped = True
        total_iteration += 1
    print("The number of iteraton: ", total_iteration)
    return arr

