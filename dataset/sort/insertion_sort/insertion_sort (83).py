def insertion_sort(arr):
    for i, value in enumerate(arr):
        j = i
        while j > 0 and arr[j - 1] > value:
            arr[j] = arr[j - 1]
            j -= 1
        arr[j] = value
        yield arr
