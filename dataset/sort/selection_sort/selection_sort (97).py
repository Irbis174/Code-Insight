def selection_sort(arr):
    return [arr.pop(arr.index(min(arr))) for _ in range(len(arr))]
