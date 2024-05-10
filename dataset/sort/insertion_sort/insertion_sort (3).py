def sort_by_insertion_gen(sequence):
    for i in range(1, len(sequence)):
        yield sorted(sequence[:i + 1]) + sequence[i + 1:]
