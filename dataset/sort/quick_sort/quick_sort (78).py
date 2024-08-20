def quicksort(sequence, left=0, right=None):
    if right is None:
        right = len(sequence) - 1
    if left < right:
        pivot_index = partition(sequence, left, right)
        quicksort(sequence, left, pivot_index - 1)
        quicksort(sequence, pivot_index + 1, right)
    return sequence

def partition(sequence, left, right):
    pivot = sequence[(left + right) // 2]
    while_left = left
    while_right = right
    while while_left <= while_right:
        while sequence[while_left] < pivot:
            while_left += 1
        while sequence[while_right] > pivot:
            while_right -= 1
        if while_left <= while_right:
            sequence[while_left], sequence[while_right] = sequence[while_right], sequence[while_left]
            while_left += 1
            while_right -= 1
    return while_left