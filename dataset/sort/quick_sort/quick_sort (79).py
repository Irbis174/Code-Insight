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
    up_index = left
    down_index = right + 1
    while True:
        while True:
            up_index += 1
            if sequence[up_index] >= pivot or up_index == right:
                break
        while True:
            down_index -= 1
            if sequence[down_index] <= pivot or down_index == left:
                break
        if up_index >= down_index:
            break
        sequence[up_index], sequence[down_index] = sequence[down_index], sequence[up_index]
    sequence[left], sequence[down_index] = sequence[down_index], sequence[left]
    return down_index