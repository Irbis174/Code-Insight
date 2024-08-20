def insertion_sort_list_generator(sequence):
    for i in range(1, len(sequence)):
        val = sequence[i]
        j = i
        while j > 0 and sequence[j - 1] > val:
            sequence[j] = sequence[j - 1]
            j -= 1
        sequence[j] = val
        yield sequence
