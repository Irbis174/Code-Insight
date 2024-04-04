def bubble(arr,N):
    i = 0
    while i < N - 1:
        j = 0
        while j < N - 1 - i:
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            j += 1
        i += 1
