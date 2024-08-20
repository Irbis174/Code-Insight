def bubble_sort(arr):
    n = len(arr)
    
    def sort(i):
        if i == n:
            return
        
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        
        sort(i + 1)
        
    sort(1)
    return arr