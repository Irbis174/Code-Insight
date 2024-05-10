def quicksort(sequence, left=0, right=None):
    if right is None:
        right = len(sequence) - 1
    if left < right:
        pivot_index = partition(sequence, left, right)
        quicksort(sequence, left, pivot_index - 1)
        quicksort(sequence, pivot_index + 1, right)
    return sequence

def partition(sequence, left, right):
    pivot = sequence[left]
    up_index = left + 1
    down_index = right
    while True:
        while up_index <= down_index and sequence[up_index] <= pivot:
            up_index += 1
        while down_index >= up_index and sequence[down_index] > pivot:
            down_index -= 1
        if up_index <= down_index:
            sequence[up_index], sequence[down_index] = sequence[down_index], sequence[up_index]
        else:
            break
    sequence[left], sequence[down_index] = sequence[down_index], sequence[left]
    return down_index
