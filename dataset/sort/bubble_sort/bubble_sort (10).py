def bubble_sort(arr):
    N = len(arr)
    swapped = True
    while swapped:
        swapped = False
        for i in range(N-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
    return arr