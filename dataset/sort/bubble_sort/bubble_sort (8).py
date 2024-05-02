def bubble_sort(arr):
    n = len(arr)
    
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]
        
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                swap(j, j + 1)
                
    return arr