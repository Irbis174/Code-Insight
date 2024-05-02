def bubble_sort(arr):
    n = len(arr)
    swap = lambda i, j: (arr[j], arr[i]) if arr[i] > arr[j] else (arr[i], arr[j])
    
    for i in range(n):
        for j in range(n - i - 1):
            arr[j], arr[j + 1] = swap(j, j + 1)
            
    return arr