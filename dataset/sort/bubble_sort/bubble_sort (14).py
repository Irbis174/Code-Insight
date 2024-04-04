def bubble_sort(arr, max_passes):
    n = len(arr)
    for i in range(min(max_passes, n-1)):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr