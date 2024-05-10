def selection_sort(arr):
    return sorted(arr, key=lambda x: (arr.pop(arr.index(x)), x))
