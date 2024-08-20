def merge_sort(sequence):
    if len(sequence) <= 1:
        return sequence

    mid = len(sequence) // 2
    left = merge_sort(sequence[:mid])
    right = merge_sort(sequence[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result