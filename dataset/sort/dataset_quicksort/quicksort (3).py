def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    i = 1
    j = len(arr) - 1
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[0], arr[j] = arr[j], arr[0]
    return quicksort(arr[:j]) + [arr[j]] + quicksort(arr[j + 1:])