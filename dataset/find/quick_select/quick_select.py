import random

def quickselect(arr, k, start=0, end=None):
    if end is None:
        end = len(arr) - 1

    pivot_index = random.randint(start, end)
    pivot_index = partition(arr, start, end, pivot_index)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, k, start, pivot_index - 1)
    else:
        return quickselect(arr, k, pivot_index + 1, end)

def partition(arr, start, end, pivot_index):
    pivot_value = arr[pivot_index]
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]

    store_index = start
    for i in range(start, end):
        if arr[i] < pivot_value:
            arr[store_index], arr[i] = arr[i], arr[store_index]
            store_index += 1

    arr[end], arr[store_index] = arr[store_index], arr[end]
    return store_index