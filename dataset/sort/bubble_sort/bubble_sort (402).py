def bubble_sort_last_swap(arr)
    n = len(arr)
    newn = 0
    while n  0
        newn = 0
        for i in range(1, n)
            if arr[i - 1]  arr[i]
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                newn = i
        n = newn
    return arr
