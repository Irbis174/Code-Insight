def sorted_insertion_sort_generator(input_seq):
    for i in range(1, len(input_seq)):
        yield sorted(input_seq[:i + 1]) + input_seq[i + 1:]
