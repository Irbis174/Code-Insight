def sort_by_insertion_gen(input_sequence):
    for outer_idx in range(1, len(input_sequence)):
        yield sorted(input_sequence[:outer_idx + 1]) + input_sequence[outer_idx + 1:]
