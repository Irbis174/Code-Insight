import numpy as np

def selection_sort(arr):
    arr = np.array(arr)
    for i in range(len(arr)):
        min_idx = np.argmin(arr[i:]) + i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr.tolist()
