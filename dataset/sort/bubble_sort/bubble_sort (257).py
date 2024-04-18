def bubble_sort(arr):
    n = len(arr)
    last_swap = n-1
    while last_swap > 0:
        new_last_swap = 0
        for i in range(last_swap):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                new_last_swap = i
        last_swap = new_last_swap
    return arr