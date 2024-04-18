def bubble_sort(arr):
    n = len(arr)
    boundary = n-1
    while boundary > 0:
        new_boundary = 0
        for i in range(boundary):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                new_boundary = i
        boundary = new_boundary
    return arr