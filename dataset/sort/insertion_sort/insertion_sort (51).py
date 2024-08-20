def insertion_sort_generator(unsorted_seq):
    for i, x in enumerate(unsorted_seq):
        j = i
        while j > 0 and unsorted_seq[j - 1] > x:
            unsorted_seq[j] = unsorted_seq[j - 1]
            j -= 1
        unsorted_seq[j] = x
        yield unsorted_seq
