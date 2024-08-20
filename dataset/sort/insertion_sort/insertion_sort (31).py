def insertion_sort(sequence, n):
    if n <= 1:
        return

    insertion_sort(sequence, n - 1)

    last_item = sequence[n - 1]
    j = n - 2

    while j >= 0 and sequence[j] > last_item:
        sequence[j + 1] = sequence[j]
        j -= 1

    sequence[j + 1] = last_item
    return sequence
