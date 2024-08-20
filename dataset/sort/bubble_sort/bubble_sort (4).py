def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        arr = [arr[j + 1] if arr[j] > arr[j + 1] else arr[j] for j in range(n - i - 1)] + arr[n - i:]
        
    return arr