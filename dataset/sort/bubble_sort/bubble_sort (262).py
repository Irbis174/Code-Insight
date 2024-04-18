def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        swaps = 0
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swaps += 1
        if swaps == 0:
            break
    return arr