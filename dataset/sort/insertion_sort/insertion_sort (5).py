def sort_by_insertion_generator(array):
    for i in range(1, len(array)):
        yield sorted(array[:i + 1]) + array[i + 1:]
