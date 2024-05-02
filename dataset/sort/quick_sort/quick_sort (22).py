def quicksort(array):
    stack = [(0, len(array) - 1)]
    while stack:
        start_index, end_index = stack.pop()
        if start_index >= end_index:
            continue
        pivot = array[end_index]
        pivot_index = start_index - 1
        for j in range(start_index, end_index):
            if array[j] <= pivot:
                pivot_index += 1
                array[pivot_index], array[j] = array[j], array[pivot_index]
        array[pivot_index + 1], array[end_index] = array[end_index], array[pivot_index + 1]
        stack.append((start_index, pivot_index - 1))
        stack.append((pivot_index + 2, end_index))
