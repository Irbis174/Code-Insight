def bubble_sort(arr):
    N = len(arr)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                buff = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = buff
