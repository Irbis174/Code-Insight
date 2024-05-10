def insertion_sort(arr):
    for i, val in enumerate(arr):
        j = i
        while j > 0 and arr[j - 1] > val:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = val
    return arr
