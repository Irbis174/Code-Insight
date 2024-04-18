def RecursiveBubbleSort(array, n=None):
    if n is None:
        n = len(array)
    if n == 1:
        return array
    for idx in range(n - 1):
        if array[idx] > array[idx + 1]:
            array[idx], array[idx + 1] = array[idx + 1], array[idx]
    RecursiveBubbleSort(array, n - 1)
    return array