def bubble_sort(arr, comparison_key=lambda x: x):
    N = len(arr)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if comparison_key(arr[j]) > comparison_key(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr