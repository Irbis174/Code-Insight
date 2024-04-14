def bubble_sort(arr):
    n = len(arr)
    stack = [(0, n)]
    while stack:
        i, j = stack.pop()
        if i < j - 1:
            pivot = i
            for k in range(i, j-1):
                if arr[k] > arr[k+1]:
                    arr[k], arr[k+1] = arr[k+1], arr[k]
                    pivot = k + 1
            stack.extend([(i, pivot), (pivot, j)])
    return arr