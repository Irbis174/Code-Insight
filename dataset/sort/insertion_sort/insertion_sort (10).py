def insertion_sort(lst):
    for i in range(1, len(lst)):
        yield sorted(lst[:i + 1]) + lst[i + 1:]
