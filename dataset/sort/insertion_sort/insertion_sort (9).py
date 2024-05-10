def insertion_sort(arr):
    for i in range(1, len(arr)):
        yield sorted(arr[:i + 1]) + arr[i + 1:]
