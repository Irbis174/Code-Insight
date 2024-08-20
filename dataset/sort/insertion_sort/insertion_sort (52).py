def insertion_sort_recursive(seq, n):
    if n <= 1:
        return

    insertion_sort_recursive(seq, n - 1)

    last = seq[n - 1]
    j = n - 2

    while j >= 0 and seq[j] > last:
        seq[j + 1] = seq[j]
        j -= 1

    seq[j + 1] = last
    return seq
