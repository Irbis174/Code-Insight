import numpy as np

def bubble_sort(array):
    arr = np.array(array)
    is_sorted = False
    while not is_sorted:
        swapped = False
        for i in range(arr.size - 1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                swapped = True
        is_sorted = not swapped
    return arr.tolist()
