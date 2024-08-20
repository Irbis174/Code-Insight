def insertion_sort(array):
    for i in range(1, len(array)):
        yield sorted(array[:i + 1]) + array[i + 1:]
