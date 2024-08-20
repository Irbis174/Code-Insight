def insertion_sort_enumerate(input_sequence):
    for idx, val in enumerate(input_sequence):
        pos = idx
        while pos > 0 and input_sequence[pos - 1] > val:
            input_sequence[pos] = input_sequence[pos - 1]
            pos -= 1
        input_sequence[pos] = val
    return input_sequence
