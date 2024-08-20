def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    return list(merge(left, right))

def merge(left, right):
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            yield left[i]
            i += 1
        else:
            yield right[j]
            j += 1

    yield from left[i:]
    yield from right[j:]