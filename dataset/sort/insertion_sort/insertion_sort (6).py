def insertion_sort_sorted_generator(arr):
    for i in range(1, len(arr)):
        yield sorted(arr[:i + 1]) + arr[i + 1:]
