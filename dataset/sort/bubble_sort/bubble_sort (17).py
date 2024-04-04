def bubble_sort(arr, N=None):
    if N is None:
        N = len(arr)

    if N == 1:
        return arr

    for i in range(N - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    return bubble_sort(arr, N - 1)