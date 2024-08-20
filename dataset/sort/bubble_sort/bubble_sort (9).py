def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        for j, value in enumerate(arr[:n - i]):
            if value > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], value
                
    return arr