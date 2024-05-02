def bubble_sort(iterable):
    iter_len = len(iterable)
    for outer_idx in range(iter_len):
        for inner_idx, val in enumerate(iterable[:iter_len - outer_idx]):
            if val > iterable[inner_idx + 1]:
                iterable[inner_idx], iterable[inner_idx + 1] = iterable[inner_idx + 1], val
    return iterable
