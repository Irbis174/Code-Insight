def quicksort(sequence, left=0, right=None):
    if right is None:
        right = len(sequence) - 1
    if left < right:
        pivot_index = partition(sequence, left, right)
        quicksort(sequence, left, pivot_index - 1)
        quicksort(sequence, pivot_index + 1, right)
    return sequence

def partition(sequence, left, right):
    pivot = sequence[right]
    store_index = left - 1
    for iterator in range(left, right):
        if sequence[iterator] <= pivot:
            store_index += 1
            sequence[store_index], sequence[iterator] = sequence[iterator], sequence[store_index]
    sequence[store_index + 1], sequence[right] = sequence[right], sequence[store_index + 1]
    return store_index + 1